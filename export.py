#!/usr/bin/env python3
"""
Export Bear notes to local markdown files via bearcli CLI.
No SQLite, no MCP — uses Bear's official CLI.

Usage:
  python3 export.py                          # Incremental: new notes not in content/
  python3 export.py --section academic       # Only academic section
  python3 export.py --limit 3                # Latest 3 notes from each section
  python3 export.py --since 2026-05-13       # Notes created after date
  python3 export.py --since last             # Notes since last sync (.last_sync)
  python3 export.py --full                   # Full re-export (clear + rebuild)
"""

import subprocess, json, re, os, shutil, datetime, urllib.parse, sys, argparse

BEARCLI = '/Applications/Bear.app/Contents/MacOS/bearcli'
ROOT = os.path.dirname(__file__)
CONTENT_DIR = os.path.join(ROOT, 'content')
IMG_DIR = os.path.join(ROOT, 'images')
COVER_DIR = os.path.join(ROOT, 'covers')
LAST_SYNC = os.path.join(ROOT, '.last_sync')

os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(COVER_DIR, exist_ok=True)

# Tag → content folder mapping
SECTIONS = {
    'writing': 'Writing',
    'academic': 'Courses/MITx',
    'about': 'Writing/About',
}


def bearcli(*args, stdin=None):
    """Run bearcli, return stdout text. Raises on non-zero exit."""
    cmd = [BEARCLI] + list(args)
    r = subprocess.run(cmd, capture_output=True, text=True, input=stdin)
    if r.returncode != 0:
        msg = r.stderr.strip() or r.stdout.strip() or 'unknown error'
        raise RuntimeError(f'bearcli {" ".join(args[:2])}... failed: {msg}')
    return r.stdout.strip()


def bearcli_json(*args):
    """Run bearcli with --format json, return parsed JSON."""
    out = bearcli(*args, '--format', 'json')
    return json.loads(out) if out else []


def search_notes(section, limit=None, since_date=None):
    """Search Bear notes for a section. Returns list of note dicts."""
    tag = SECTIONS[section]
    query = f'#{tag}'
    # Exclude about notes from writing section
    if section == 'writing':
        query += ' -#Writing/About'
    if since_date:
        query += f' @cdate(>{since_date})'

    args = ['search', query, '--fields', 'all,content', '--sort', 'created:desc']
    if limit:
        args += ['--limit', str(limit)]

    return bearcli_json(*args)


def save_attachment(note_id, filename, dest_dir, dest_name=None):
    """Save an attachment to a directory via bearcli. Returns saved filename or None."""
    fname = dest_name or filename
    dst = os.path.join(dest_dir, fname)
    if os.path.exists(dst):
        return fname
    try:
        cmd = [BEARCLI, 'attachments', 'save', note_id, '--filename', filename]
        with open(dst, 'wb') as f:
            subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, check=True)
        return fname
    except subprocess.CalledProcessError:
        return None


def extract_cover_info(text, note_id, skip_subtitle=False):
    """
    Analyze note body to determine cover image and subtitle.
    Returns (cover_filename, cover_oss_url, subtitle, modified_text).

    subtitle: concatenated blockquote lines right after title (or None).
    """
    if not text:
        return None, None, None, text

    id_prefix = note_id[:8] if '-' in note_id else note_id
    lines = text.split('\n')

    # ── Step 1: Extract subtitle (consecutive > lines right after title) ──
    subtitle = None
    if not skip_subtitle:
        past_title = False
        subtitle_lines = []
        subtitle_indices = []
        for i, line in enumerate(lines):
            s = line.strip()
            if s.startswith('# ') and not past_title:
                past_title = True
                continue
            if past_title and s == '':
                continue
            if past_title and s.startswith('>'):
                subtitle_indices.append(i)
                content = re.sub(r'^>\s?', '', s)
                subtitle_lines.append(content)
                if i + 1 < len(lines) and lines[i + 1].strip().startswith('>'):
                    continue
                subtitle = ' '.join(subtitle_lines)
                for idx in reversed(subtitle_indices):
                    lines.pop(idx)
                break
            if past_title and s:
                break

    # ── Step 2: Find images ──
    all_images = []
    for i, line in enumerate(lines):
        m = re.search(r'!\[([^\]]*)\]\(([^)]+)\)', line)
        if m:
            all_images.append((i, m.group(2).strip('~'), m.group(0)))

    if not all_images:
        return None, None, subtitle, '\n'.join(lines)

    # Find first non-empty content line after the H1 title
    first_content_line = None
    past_title = False
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith('# ') and not past_title:
            past_title = True
            continue
        if past_title and s == '':
            continue
        if past_title and s:
            first_content_line = i
            break

    # Rule 1: cover-at-start
    if first_content_line is not None:
        first_img = next((img for img in all_images if img[0] == first_content_line), None)
        if first_img:
            li, src, full_match = first_img
            resolved = False
            cover_filename = None
            cover_oss = None

            if src.startswith('http'):
                cover_oss = src
                resolved = True
            else:
                decoded = urllib.parse.unquote(src)
                fname = os.path.basename(decoded)
                unique_fn = f'{id_prefix}_{fname}'
                saved = save_attachment(note_id, fname, COVER_DIR, unique_fn)
                if saved:
                    cover_filename = saved
                    resolved = True

            if resolved:
                lines.pop(li)
                if li < len(lines) and lines[li].strip() == '':
                    lines.pop(li)
                return cover_filename, cover_oss, subtitle, '\n'.join(lines)

    # Rule 2: fallback — first real image as cover
    for li, src, full_match in all_images:
        if src.startswith('http'):
            return None, src, subtitle, text

        decoded = urllib.parse.unquote(src)
        fname = os.path.basename(decoded)
        unique_fn = f'{id_prefix}_{fname}'
        saved = save_attachment(note_id, fname, COVER_DIR, unique_fn)
        if saved:
            return saved, None, subtitle, text

    return None, None, subtitle, '\n'.join(lines)


def process_note(note, section, skip_subtitle=False):
    """Export one note: save images, detect cover, write .md file. Returns True on success."""
    note_id = note['id']
    title = note.get('title', 'Untitled')
    created = note.get('created', '')
    text = note.get('content', '')
    tags = note.get('tags', [])
    attachment_names = note.get('attachments', [])

    if not text or len(text) < 30:
        return False

    pub_date = ''
    if created:
        try:
            dt = datetime.datetime.fromisoformat(created.replace('Z', '+00:00'))
            pub_date = dt.strftime('%Y-%m-%d')
        except Exception:
            pass

    # Course ID for academic section
    course_id = None
    if section == 'academic':
        for tag in tags:
            t = tag.lstrip('#')
            if t.startswith('Courses/MITx/'):
                course_id = t.split('/')[-1]
                break

    # Detect cover
    cover_filename, cover_oss_url, subtitle, modified_text = extract_cover_info(text, note_id, skip_subtitle=skip_subtitle)

    id_prefix = note_id[:8] if '-' in note_id else note_id

    # Save inline images with unique prefix
    for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', modified_text):
        src = m.group(2).strip('~')
        if src.startswith('http'):
            continue
        decoded = urllib.parse.unquote(src)
        fname = os.path.basename(decoded)
        unique_fn = f'{id_prefix}_{fname}'
        if save_attachment(note_id, fname, IMG_DIR, unique_fn):
            modified_text = re.sub(
                r'\(' + re.escape(src) + r'\)',
                r'(../images/' + unique_fn + r')', modified_text)

    # Strip Jekyll frontmatter
    body_clean = modified_text.replace('\r\n', '\n')
    for open_sep in ('\n---\n', '\n----\n'):
        start = body_clean.find(open_sep)
        if start < 0:
            continue
        for close_sep in ('\n---\n', '\n----\n'):
            end = body_clean.find(close_sep, start + len(open_sep))
            if end > 0:
                body_clean = body_clean[:start] + body_clean[end + len(close_sep):]
                break
        if end > 0:
            break

    # Write .md file
    out_dir = os.path.join(CONTENT_DIR, section)
    os.makedirs(out_dir, exist_ok=True)
    safe_t = re.sub(r'[<>:"/|?*]', '_', title)[:80]
    md_path = os.path.join(out_dir, f'{safe_t}.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(f'title: "{title}"\n')
        if subtitle:
            f.write(f'subtitle: "{subtitle}"\n')
        f.write(f'date: {pub_date}\n')
        if course_id:
            f.write(f'course: {course_id}\n')
        if cover_filename:
            f.write(f'cover: "{cover_filename}"\n')
        if cover_oss_url:
            f.write(f'cover_oss: "{cover_oss_url}"\n')
        f.write(f'bear_pk: {note_id}\n')
        f.write('---\n\n')
        f.write(body_clean)

    return True


def existing_note_ids(section):
    """Return set of bear_pk values already in content/{section}/."""
    ids = set()
    out_dir = os.path.join(CONTENT_DIR, section)
    if not os.path.isdir(out_dir):
        return ids
    for fname in os.listdir(out_dir):
        if not fname.endswith('.md'):
            continue
        with open(os.path.join(out_dir, fname), 'r', encoding='utf-8') as f:
            m = re.search(r'bear_pk:\s*(\S+)', f.read())
            if m:
                ids.add(m.group(1))
    return ids


def export_section(section, limit=None, since_date=None, full=False):
    """Export notes for a section. Returns (new_count, skipped_count)."""
    out_dir = os.path.join(CONTENT_DIR, section)

    if full and os.path.exists(CONTENT_DIR):
        shutil.rmtree(CONTENT_DIR)
        if os.path.exists(COVER_DIR):
            for f in os.listdir(COVER_DIR):
                if not f.startswith('home-'):
                    os.remove(os.path.join(COVER_DIR, f))
        if os.path.exists(IMG_DIR):
            for f in os.listdir(IMG_DIR):
                os.remove(os.path.join(IMG_DIR, f))

    notes = search_notes(section, limit=limit, since_date=since_date)
    existing = set() if full else existing_note_ids(section)

    count, skipped = 0, 0
    for note in notes:
        nid = note.get('id', '')
        if nid in existing:
            skipped += 1
            continue
        if process_note(note, section, skip_subtitle=(section == 'about')):
            count += 1

    return count, skipped


def update_last_sync():
    """Write current UTC timestamp to .last_sync."""
    now = datetime.datetime.utcnow().strftime('%Y-%m-%d')
    with open(LAST_SYNC, 'w') as f:
        f.write(now)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Export Bear notes via bearcli CLI')
    parser.add_argument('--section', type=str, choices=['writing', 'academic'],
                        help='Export only this section (default: both)')
    parser.add_argument('--limit', type=int, help='Export only the N most recent notes')
    parser.add_argument('--since', type=str,
                        help='Export notes created after DATE (YYYY-MM-DD), or "last" for .last_sync')
    parser.add_argument('--full', action='store_true',
                        help='Full re-export: clear content/ and rebuild')
    args = parser.parse_args()

    sections = [args.section] if args.section else ['writing', 'academic', 'about']

    since_date = None
    if args.since:
        if args.since == 'last':
            if os.path.exists(LAST_SYNC):
                with open(LAST_SYNC) as f:
                    since_date = f.read().strip()
                print(f'Last sync: {since_date}')
            else:
                print('No .last_sync file found (run without --since first)')
                sys.exit(1)
        else:
            since_date = args.since

    if args.full:
        pass  # Full export

    total_new, total_skipped = 0, 0
    for sec in sections:
        cnt, sk = export_section(sec, limit=args.limit, since_date=since_date,
                                 full=args.full)
        total_new += cnt
        total_skipped += sk

    # Update .last_sync after successful export
    update_last_sync()

    img_count = len([f for f in os.listdir(IMG_DIR) if os.path.isfile(os.path.join(IMG_DIR, f))])
    cover_count = len([f for f in os.listdir(COVER_DIR) if os.path.isfile(os.path.join(COVER_DIR, f))])
    sections_str = ', '.join(sections)
    print(f'Exported: {total_new} new + {total_skipped} skipped in {sections_str}')
    print(f'Images: {img_count} in images/')
    print(f'Covers: {cover_count} in covers/')
