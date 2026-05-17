#!/usr/bin/env python3
"""
Export Obsidian vault notes to blog content/.
Replaces export.py (Bear-based).

Usage:
  python3 export_obsidian.py                  # All sections, incremental
  python3 export_obsidian.py --full           # Full export, ignore .last_sync
  python3 export_obsidian.py --section writing # Only writing section
"""

import re, os, shutil, datetime, hashlib, sys, argparse

ROOT = os.path.dirname(__file__)
VAULT = os.path.expanduser("~/Research Hub")
CONTENT_DIR = os.path.join(ROOT, 'content')
COVER_DIR = os.path.join(ROOT, 'covers')
IMAGE_DIR = os.path.join(ROOT, 'images')
LAST_SYNC = os.path.join(ROOT, '.last_sync')

BEIJING_TZ = datetime.timezone(datetime.timedelta(hours=8))

SECTIONS = {
    'writing': {
        'vault_dir': '4. Writing',
        'output_dir': 'writing',
    },
    'about': {
        'vault_dir': '.',
        'output_dir': 'about',
        'files': ['About Me.md'],
    },
}


def parse_yaml_frontmatter(text):
    """Parse simple YAML frontmatter between --- delimiters.
    Handles: key: value, key: "value", and lists (key:\n  - item).
    Returns (meta_dict, body_text)."""
    meta = {}
    body = text
    if not text.startswith('---'):
        return meta, body

    idx = text.find('---', 3)
    if idx < 0:
        return meta, body

    fm = text[3:idx]
    body = text[idx + 3:].strip()

    current_key = None
    for line in fm.split('\n'):
        s = line.strip()
        if not s:
            continue
        list_m = re.match(r'-\s+(.*)', s)
        if list_m and current_key:
            if current_key not in meta:
                meta[current_key] = []
            meta[current_key].append(list_m.group(1).strip().strip('"'))
            continue
        kv = re.match(r'(\w+):\s*"?(.*?)"?$', s)
        if kv:
            key = kv.group(1)
            val = kv.group(2).strip().rstrip('"')
            if val:
                meta[key] = val
            current_key = key
        else:
            current_key = None

    return meta, body


def file_id(vault_rel_path):
    """Stable 8-char ID from vault-relative path."""
    return hashlib.md5(vault_rel_path.encode()).hexdigest()[:8]


def normalize_wiki_images(text):
    """Convert Obsidian wiki-link images ![[filename|size]] to standard ![](filename)."""
    return re.sub(
        r'!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]',
        r'![](\1)',
        text
    )


def extract_cover_info(text, note_dir, prefix):
    """
    Analyze note body for cover image.
    Returns (cover_filename, cover_oss_url, modified_text).

    Rules (unchanged):
    1. First non-empty content after H1 that is an image → cover, removed from body
    2. Else first image anywhere → cover, kept in body
    """
    if not text:
        return None, None, text

    lines = text.split('\n')

    all_images = []
    for i, line in enumerate(lines):
        m = re.search(r'!\[([^\]]*)\]\(([^)]+)\)', line)
        if m:
            all_images.append((i, m.group(2).strip('~'), m.group(0)))

    if not all_images:
        return None, None, text

    # Find first non-empty content line after the H1 title (or first content if no H1)
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
    # If no H1 found, first non-empty line is the candidate for Rule 1
    if first_content_line is None:
        for i, line in enumerate(lines):
            if line.strip():
                first_content_line = i
                break

    # Rule 1: cover-at-start
    if first_content_line is not None:
        first_img = next((img for img in all_images if img[0] == first_content_line), None)
        if first_img:
            li, src, full_match = first_img
            if src.startswith('http'):
                lines.pop(li)
                if li < len(lines) and lines[li].strip() == '':
                    lines.pop(li)
                return None, src, '\n'.join(lines)
            else:
                fname = os.path.basename(src).replace(' ', '_')
                unique_fn = f'{prefix}_{fname}'
                asset_path = os.path.join(note_dir, fname)
                if os.path.isfile(asset_path):
                    shutil.copy2(asset_path, os.path.join(COVER_DIR, unique_fn))
                    lines.pop(li)
                    if li < len(lines) and lines[li].strip() == '':
                        lines.pop(li)
                    return unique_fn, None, '\n'.join(lines)

    # Rule 2: fallback — first image as cover, stays in body
    for li, src, full_match in all_images:
        if src.startswith('http'):
            return None, src, text
        fname = os.path.basename(src).replace(' ', '_')
        unique_fn = f'{prefix}_{fname}'
        asset_path = os.path.join(note_dir, fname)
        if os.path.isfile(asset_path):
            shutil.copy2(asset_path, os.path.join(COVER_DIR, unique_fn))
            return unique_fn, None, text

    return None, None, text


def copy_inline_images(text, note_dir, prefix):
    """Copy inline images from _assets/{note-dir}/ to images/, rewrite references.
    Skips OSS URLs. Returns modified text."""
    lines = text.split('\n')
    out = []
    for line in lines:
        out.append(re.sub(
            r'!\[([^\]]*)\]\(((?!https?://)[^)]+)\)',
            lambda m: _copy_image_ref(m, note_dir, prefix),
            line
        ))
    return '\n'.join(out)


def _copy_image_ref(m, note_dir, prefix):
    alt = m.group(1)
    src = m.group(2)
    fname = os.path.basename(src).replace(' ', '_')
    unique_fn = f'{prefix}_{fname}'

    dest = os.path.join(IMAGE_DIR, unique_fn)
    if not os.path.exists(dest):
        asset_path = os.path.join(note_dir, fname)
        if os.path.isfile(asset_path):
            shutil.copy2(asset_path, dest)

    return f'![{alt}](images/{unique_fn})'


def process_note(filepath, prefix):
    """Process a single Obsidian note into a blog .md file.
    Returns (safe_title, output_text) or None if skipped."""
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()

    meta, body = parse_yaml_frontmatter(raw)

    # Normalize Obsidian wiki-link images ![[file]] → ![](file)
    body = normalize_wiki_images(body)

    # Title: YAML title > filename without .md
    title = meta.get('title') or os.path.basename(filepath)[:-3]

    # Date: YAML create_date > file mtime (Beijing time)
    date_str = meta.get('create_date')
    if date_str:
        # Accept YYYY-MM-DD, YYYY-M-D, YYYY-MM-D, YYYY-M-DD
        m = re.match(r'(\d{4})-(\d{1,2})-(\d{1,2})$', str(date_str))
        if m:
            date_str = f'{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}'
        else:
            date_str = None
    if not date_str:
        mtime = os.path.getmtime(filepath)
        dt = datetime.datetime.fromtimestamp(mtime, tz=BEIJING_TZ)
        date_str = dt.strftime('%Y-%m-%d')

    # Subtitle: from YAML, only if non-empty
    subtitle = meta.get('subtitle')
    if subtitle and subtitle.strip():
        subtitle = subtitle.strip()
    else:
        subtitle = None

    # Tags: from YAML tags list
    tags = meta.get('tags', [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(',')]

    # Determine note's _assets directory
    note_name = os.path.basename(filepath)[:-3]
    note_assets_dir = os.path.join(VAULT, '_assets', note_name)
    if not os.path.isdir(note_assets_dir):
        note_assets_dir = None

    # Extract cover (modifies body text)
    cover_file, cover_oss, body = extract_cover_info(body, note_assets_dir or '', prefix)

    # Copy inline images and rewrite references
    if note_assets_dir:
        body = copy_inline_images(body, note_assets_dir, prefix)

    # Sanitize title for filename
    safe_title = re.sub(r'[\\/:*?"<>|]', '', title).strip()
    safe_title = safe_title.replace('/', ' ')

    # Build output frontmatter
    fm_lines = [
        '---',
        f'title: "{title}"',
        f'date: {date_str}',
    ]
    if subtitle:
        fm_lines.append(f'subtitle: "{subtitle}"')
    if cover_file:
        fm_lines.append(f'cover: "{cover_file}"')
    if cover_oss:
        fm_lines.append(f'cover_oss: "{cover_oss}"')
    if tags:
        fm_lines.append(f'tags: {", ".join(tags)}')
    fm_lines.append(f'obsidian_id: {prefix}')
    fm_lines.append('---')

    output = '\n'.join(fm_lines) + '\n\n' + body.lstrip()
    return safe_title, output


def existing_obsidian_ids(section_dir):
    """Return set of obsidian_id values already exported."""
    ids = set()
    if not os.path.isdir(section_dir):
        return ids
    for md_path in os.listdir(section_dir):
        if not md_path.endswith('.md'):
            continue
        with open(os.path.join(section_dir, md_path), 'r', encoding='utf-8') as f:
            raw = f.read()
        meta, _ = parse_yaml_frontmatter(raw)
        oid = meta.get('obsidian_id', '')
        if oid:
            ids.add(oid)
    return ids


def export_section(section_key, full=False, limit=None):
    """Export one section from Obsidian vault to content/."""
    cfg = SECTIONS[section_key]
    output_dir = os.path.join(CONTENT_DIR, cfg['output_dir'])
    os.makedirs(output_dir, exist_ok=True)

    # Get list of files to process
    if 'files' in cfg:
        files = [os.path.join(VAULT, f) for f in cfg['files'] if os.path.isfile(os.path.join(VAULT, f))]
    else:
        vault_dir = os.path.join(VAULT, cfg['vault_dir'])
        if not os.path.isdir(vault_dir):
            print(f"  Vault directory not found: {vault_dir}")
            return 0, 0
        files = sorted([
            os.path.join(vault_dir, f)
            for f in os.listdir(vault_dir)
            if f.endswith('.md')
        ])

    # Read last sync date
    last_sync_date = None
    if not full and os.path.isfile(LAST_SYNC):
        with open(LAST_SYNC, 'r') as f:
            last_sync_date = f.read().strip()

    # Check existing exports
    existing_ids = existing_obsidian_ids(output_dir)

    # Clear output dir on full export
    if full:
        for f in os.listdir(output_dir):
            if f.endswith('.md'):
                os.remove(os.path.join(output_dir, f))

    new_count, skipped_count = 0, 0

    for filepath in files:
        oid = file_id(os.path.relpath(filepath, VAULT))

        # Incremental: skip if already exported and not modified since last sync
        if not full and oid in existing_ids:
            mtime = os.path.getmtime(filepath)
            mtime_date = datetime.datetime.fromtimestamp(mtime, tz=BEIJING_TZ).strftime('%Y-%m-%d')
            if last_sync_date and mtime_date <= last_sync_date:
                skipped_count += 1
                continue

        result = process_note(filepath, oid)
        if result is None:
            continue
        safe_title, output = result
        out_path = os.path.join(output_dir, f'{safe_title}.md')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(output)
        new_count += 1

        if limit and new_count >= limit:
            break

    return new_count, skipped_count


def update_last_sync():
    """Write today's Beijing date to .last_sync."""
    today = datetime.datetime.now(tz=BEIJING_TZ).strftime('%Y-%m-%d')
    with open(LAST_SYNC, 'w') as f:
        f.write(today)


def main():
    parser = argparse.ArgumentParser(description='Export Obsidian notes to blog content/')
    parser.add_argument('--full', action='store_true', help='Full export, ignore .last_sync')
    parser.add_argument('--section', type=str, help='Export only one section (writing, about)')
    parser.add_argument('--limit', type=int, default=0, help='Limit number of new notes per section')
    args = parser.parse_args()

    os.makedirs(COVER_DIR, exist_ok=True)
    os.makedirs(IMAGE_DIR, exist_ok=True)
    os.makedirs(CONTENT_DIR, exist_ok=True)

    sections_to_export = [args.section] if args.section else list(SECTIONS.keys())

    total_new, total_skip = 0, 0
    for sk in sections_to_export:
        new, skipped = export_section(sk, full=args.full, limit=args.limit)
        print(f'  {sk}: {new} new + {skipped} skipped')
        total_new += new
        total_skip += skipped

    if total_new > 0:
        update_last_sync()
        print(f'\nExported: {total_new} new + {total_skip} skipped')
        print(f'Updated .last_sync')
    else:
        print(f'\nNo new notes ({total_skip} skipped)')


if __name__ == '__main__':
    main()
