#!/usr/bin/env python3
"""
Full export from Bear SQLite (READ-ONLY).
For bulk/initial export. Incremental updates use export.py via MCP.

Run: python3 export_full.py
"""

import sqlite3, re, os, shutil, datetime, urllib.parse

ROOT = os.path.dirname(__file__)
CONTENT_DIR = os.path.join(ROOT, 'content')
IMG_DIR = os.path.join(ROOT, 'images')
COVER_DIR = os.path.join(ROOT, 'covers')
DB = '/Users/yanhe/Library/Group Containers/9K33E3U3T4.net.shinyfrog.bear/Application Data/database.sqlite'
BEAR_IMG = os.path.expanduser(
    "~/Library/Group Containers/9K33E3U3T4.net.shinyfrog.bear/Application Data/Local Files/Note Images")

os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(COVER_DIR, exist_ok=True)


def copy_image(src_path, dst_dir, dst_name=None):
    """Copy an image to dst_dir. Return the destination filename."""
    fname = dst_name or os.path.basename(src_path)
    dst = os.path.join(dst_dir, fname)
    if not os.path.exists(dst):
        shutil.copy2(src_path, dst)
    return fname


def extract_cover_info(text, resolve_image, img_prefix, skip_subtitle=False):
    """
    Returns (cover_filename, cover_oss_url, subtitle, modified_text).
    subtitle: concatenated blockquote lines after title (or None).
    """
    if not text:
        return None, None, None, text

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

    # Find first non-empty content after H1 title
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

    # Rule 1: first content is an image → cover, remove from body
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
                disk_path, disk_fn = resolve_image(src)
                if disk_path:
                    unique_fn = f'{img_prefix}_{disk_fn}'
                    copy_image(disk_path, COVER_DIR, unique_fn)
                    cover_filename = unique_fn
                    resolved = True

            if resolved:
                lines.pop(li)
                if li < len(lines) and lines[li].strip() == '':
                    lines.pop(li)
                return cover_filename, cover_oss, subtitle, '\n'.join(lines)

    # Rule 2: use first real image as cover (keep in body)
    for li, src, full_match in all_images:
        if src.startswith('http'):
            return None, src, subtitle, text

        disk_path, disk_fn = resolve_image(src)
        if disk_path:
            unique_fn = f'{img_prefix}_{disk_fn}'
            copy_image(disk_path, COVER_DIR, unique_fn)
            return unique_fn, None, subtitle, text

    return None, None, subtitle, '\n'.join(lines)


def export_section(tag_name, folder_name, exclude_tag=None, skip_subtitle=False):
    """Export notes for a given tag to content/{folder_name}/"""
    out_dir = os.path.join(CONTENT_DIR, folder_name)
    os.makedirs(out_dir, exist_ok=True)

    conn = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
    c = conn.cursor()
    tag_pk = c.execute("SELECT Z_PK FROM ZSFNOTETAG WHERE ZTITLE=?", (tag_name,)).fetchone()
    if not tag_pk:
        conn.close()
        return 0

    if exclude_tag:
        rows = c.execute("""
            SELECT n.Z_PK, n.ZTITLE, n.ZTEXT, n.ZCREATIONDATE, n.ZUNIQUEIDENTIFIER
            FROM ZSFNOTE n JOIN Z_5TAGS j ON n.Z_PK=j.Z_5NOTES
            WHERE j.Z_13TAGS=? AND n.ZTRASHED=0
            AND NOT EXISTS (
                SELECT 1 FROM Z_5TAGS j2
                WHERE j2.Z_5NOTES=n.Z_PK
                AND j2.Z_13TAGS=(SELECT Z_PK FROM ZSFNOTETAG WHERE ZTITLE=?)
            )
            ORDER BY n.ZCREATIONDATE DESC
        """, (tag_pk[0], exclude_tag)).fetchall()
    else:
        rows = c.execute("""
            SELECT n.Z_PK, n.ZTITLE, n.ZTEXT, n.ZCREATIONDATE, n.ZUNIQUEIDENTIFIER
            FROM ZSFNOTE n JOIN Z_5TAGS j ON n.Z_PK=j.Z_5NOTES
            WHERE j.Z_13TAGS=? AND n.ZTRASHED=0 ORDER BY n.ZCREATIONDATE DESC
        """, (tag_pk[0],)).fetchall()

    count = 0
    for pk, title, text, create_date, note_uuid in rows:
        if not text or len(text) < 30:
            continue

        pub_date = None
        if create_date:
            pub_date = datetime.datetime.utcfromtimestamp(
                create_date + 978307200).strftime('%Y-%m-%d')

        # Course ID for academic
        course_id = None
        if tag_name == 'Courses/MITx':
            ct = c.execute("""SELECT t.ZTITLE FROM ZSFNOTETAG t
                JOIN Z_5TAGS j ON t.Z_PK=j.Z_13TAGS
                WHERE j.Z_5NOTES=? AND t.ZTITLE LIKE 'Courses/MITx/%'
            """, (pk,)).fetchall()
            if ct:
                course_id = ct[0][0].split('/')[-1]

        # Build image mapping: filename → (file_uuid, actual_name)
        img_map = {}
        for fn, fid in c.execute(
            "SELECT ZFILENAME, ZUNIQUEIDENTIFIER FROM ZSFNOTEFILE WHERE ZNOTE=?", (pk,)
        ).fetchall():
            img_map[fn.lower()] = (fid, fn)

        # Image prefix for unique names (first 8 chars of note UUID)
        img_prefix = note_uuid[:8] if note_uuid else str(pk)

        def resolve_image_to_disk(src):
            if src.startswith('http'):
                return None, None
            decoded = urllib.parse.unquote(src)
            fname = os.path.basename(decoded)
            key = fname.lower()
            if key in img_map:
                fid, disk_fn = img_map[key]
                for d in os.listdir(BEAR_IMG):
                    if fid.upper() in d.upper():
                        img_dir = os.path.join(BEAR_IMG, d)
                        disk_path = os.path.join(img_dir, disk_fn)
                        if os.path.exists(disk_path):
                            return disk_path, disk_fn
                        for f in os.listdir(img_dir):
                            if f.lower() == fname.lower():
                                return os.path.join(img_dir, f), f
                        break
            return None, None

        # Extract cover + subtitle
        cover_filename, cover_oss_url, subtitle, modified_text = extract_cover_info(
            text, resolve_image_to_disk, img_prefix, skip_subtitle=skip_subtitle)

        # Copy inline images with unique names
        for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', modified_text):
            src = m.group(2).strip('~')
            disk_path, disk_fn = resolve_image_to_disk(src)
            if disk_path:
                unique_fn = f'{img_prefix}_{disk_fn}'
                copy_image(disk_path, IMG_DIR, unique_fn)
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
        safe_t = re.sub(r'[<>:"/|?*]', '_', title)[:80]
        md_path = os.path.join(out_dir, f'{safe_t}.md')
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write('---\n')
            f.write(f'title: "{title}"\n')
            if subtitle:
                f.write(f'subtitle: "{subtitle}"\n')
            f.write(f'date: {pub_date or ""}\n')
            if course_id:
                f.write(f'course: {course_id}\n')
            if cover_filename:
                f.write(f'cover: "{cover_filename}"\n')
            if cover_oss_url:
                f.write(f'cover_oss: "{cover_oss_url}"\n')
            f.write(f'bear_pk: {note_uuid}\n')
            f.write('---\n\n')
            f.write(body_clean)
        count += 1

    conn.close()
    return count


if __name__ == '__main__':
    # Clear and rebuild
    if os.path.exists(CONTENT_DIR):
        shutil.rmtree(CONTENT_DIR)

    # Clear covers (preserve home-*)
    if os.path.exists(COVER_DIR):
        for f in os.listdir(COVER_DIR):
            if f.startswith('home-'):
                continue
            os.remove(os.path.join(COVER_DIR, f))

    # Clear images
    if os.path.exists(IMG_DIR):
        for f in os.listdir(IMG_DIR):
            os.remove(os.path.join(IMG_DIR, f))

    w = export_section('Writing', 'writing', exclude_tag='Writing/About')
    a = export_section('Courses/MITx', 'academic')
    abt = export_section('Writing/About', 'about', skip_subtitle=True)

    img_count = len([f for f in os.listdir(IMG_DIR) if os.path.isfile(os.path.join(IMG_DIR, f))])
    cover_count = len([f for f in os.listdir(COVER_DIR) if os.path.isfile(os.path.join(COVER_DIR, f))])
    print(f'Exported: {w} writing + {a} academic + {abt} about = {w+a+abt} .md files')
    print(f'Images: {img_count} in images/')
    print(f'Covers: {cover_count} in covers/')
