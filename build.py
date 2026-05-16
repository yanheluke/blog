#!/usr/bin/env python3
"""
Build index.html from local content/ markdown files.
Run: python3 build.py
"""

import re, os, glob, json, time
from PIL import Image

ROOT = os.path.dirname(__file__)
COVER_CACHE = {}  # path → (brightness, gradient_css, title_color, preview_color)

def cover_adaptive(cover):
    """Analyze cover image brightness, return (gradient_css, title_color, preview_color)."""
    if not cover:
        return 'var(--feat-overlay)', 'var(--text-bright)', 'var(--feat-p-color)'
    if cover in COVER_CACHE:
        return COVER_CACHE[cover]
    try:
        path = os.path.join(ROOT, cover)
        img = Image.open(path).resize((20, 20), Image.LANCZOS).convert('RGB')
        px = list(img.getdata())
        r = sum(p[0] for p in px) / len(px)
        g = sum(p[1] for p in px) / len(px)
        b = sum(p[2] for p in px) / len(px)
        bright = 0.299 * r + 0.587 * g + 0.114 * b
    except Exception:
        bright = 128
    # Dark gradient overlay, opacity inversely proportional to brightness:
    # darker image → lighter overlay (so image shows through)
    # brighter image → heavier overlay (to dampen brightness for text readability)
    a = round(max(0.45, min(0.92, bright / 200 * 0.7)), 2)
    grad = (f'linear-gradient(to top,'
            f'rgba(18,18,18,{a:.2f}) 0%,'
            f'rgba(18,18,18,{a*0.55:.2f}) 30%,'
            f'rgba(18,18,18,{a*0.18:.2f}) 60%,'
            f'transparent 100%)')
    result = (grad, '#fff', 'rgba(255,255,255,.8)')
    COVER_CACHE[cover] = result
    return result
CONTENT_DIR = os.path.join(ROOT, 'content')

# ═══════════════════════════════════════════════════════
# MARKDOWN → HTML
# ═══════════════════════════════════════════════════════

def md_to_html(text, strip_fm=True):
    if not text: return ''
    lines = text.split('\n')
    out, in_code, in_list, in_bq, lt = [], False, False, False, 'ul'

    def flush_bq():
        nonlocal in_bq
        if in_bq: out.append('</blockquote>'); in_bq = False

    for line in lines:
        line = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',
            lambda m: f'<img src="{m.group(2).strip(chr(126))}" alt="{m.group(1)}" loading="lazy">', line)
        s = line.strip()

        if s.startswith('```'):
            if in_code: out.append('</code></pre>'); in_code = False
            else: out.append('<pre><code>'); in_code = True
            continue
        if in_code: out.append(line); continue
        if not s:
            if in_list: out.append(f'</{lt}>'); in_list = False
            flush_bq()
            continue

        if s.startswith('#### '): flush_bq(); out.append(f'<h5>{s[5:]}</h5>')
        elif s.startswith('### '): flush_bq(); out.append(f'<h4>{s[4:]}</h4>')
        elif s.startswith('## '): flush_bq(); out.append(f'<h3>{s[3:]}</h3>')
        elif s.startswith('# '): flush_bq(); out.append(f'<h3>{s[2:]}</h3>')
        elif s.startswith('> '):
            if not in_bq: out.append('<blockquote>'); in_bq = True
            out.append(f'{_inl(s[2:])}<br>')
        elif s == '>':
            if not in_bq: out.append('<blockquote>'); in_bq = True
            out.append('<br>')
        elif s in ('---','- - -','***'): flush_bq(); out.append('<hr>')
        elif re.match(r'[-*+]\s', s):
            flush_bq()
            if not in_list or lt != 'ul':
                if in_list: out.append(f'</{lt}>')
                out.append('<ul>'); in_list, lt = True, 'ul'
            out.append(f'<li>{_inl(s[2:])}</li>')
        elif re.match(r'\d+[.)]\s', s):
            flush_bq()
            if not in_list or lt != 'ol':
                if in_list: out.append(f'</{lt}>')
                out.append('<ol>'); in_list, lt = True, 'ol'
            c2 = re.sub(r'^\d+[.)]\s', '', s)
            out.append(f'<li>{_inl(c2)}</li>')
        else:
            if in_list: out.append(f'</{lt}>'); in_list = False
            flush_bq()
            out.append(f'<p>{_inl(s)}</p>')

    if in_list: out.append(f'</{lt}>')
    flush_bq()
    if in_code: out.append('</code></pre>')
    return '\n'.join(out)

def _inl(t):
    t = re.sub(r'~~(.+?)~~', r'<s>\1</s>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t

# ═══════════════════════════════════════════════════════
# ARTICLE LOADING
# ═══════════════════════════════════════════════════════

def parse_frontmatter(text):
    """Parse YAML-like frontmatter at the start of a .md file."""
    meta = {}
    if text.startswith('---'):
        idx = text.find('---', 3)
        if idx > 0:
            fm = text[3:idx]
            for line in fm.split('\n'):
                m = re.match(r'(\w+):\s*"?(.*?)"?$', line.strip())
                if m: meta[m.group(1)] = m.group(2).strip().rstrip('"')
            text = text[idx+3:].strip()
    return meta, text

def load_articles(section):
    """Load all articles for a section from content/{section}/*.md"""
    md_dir = os.path.join(CONTENT_DIR, section)
    if not os.path.isdir(md_dir): return []

    articles = []
    for md_path in sorted(glob.glob(os.path.join(md_dir, '*.md'))):
        with open(md_path, 'r', encoding='utf-8') as f:
            raw = f.read()

        meta, body = parse_frontmatter(raw)
        title = meta.get('title', os.path.basename(md_path)[:-3])
        pub_date = meta.get('date', None)
        course_id = meta.get('course', None)
        cover_file = meta.get('cover', None)
        cover_oss = meta.get('cover_oss', None)
        subtitle = meta.get('subtitle', None)

        html_body = md_to_html(body)

        # Strip duplicate <h3>Title</h3> before extracting summary
        # Handle optional whitespace inside <h3> (e.g. "#  Title" → "<h3> Title</h3>")
        title_pattern = re.compile(
            r'<h3>\s*' + re.escape(title) + r'\s*</h3>',
            re.IGNORECASE
        )
        html_body_for_summary = title_pattern.sub('', html_body, count=1).lstrip()

        # Build cover URL (prefer local covers/ over OSS URL)
        cover = None
        if cover_file:
            cover = f'covers/{cover_file}'
        elif cover_oss:
            cover = cover_oss
        if not cover:
            # Fallback: extract first image from body
            cv = extract_cover(html_body)
            if cv:
                if cv.startswith('http'): cover = cv
                else: cover = f'images/{cv}'

        summary = extract_summary(html_body_for_summary)

        oid = meta.get('obsidian_id', meta.get('bear_pk', '0'))
        # obsidian_id is already 8 chars; bear_pk needs shortening
        if '-' in oid and len(oid) > 8:
            oid = oid[:8]
        aid = f'a{oid}'

        articles.append({
            'id': aid, 'title': title, 'date': pub_date,
            'subtitle': subtitle,
            'summary': summary, 'cover': cover,
            'course': course_id, 'section': section,
            'body': html_body,
            'cover_file': cover_file,
            'cover_oss': cover_oss,
        })

    articles.sort(key=lambda a: a['date'] or '2000-01-01', reverse=True)
    return articles

def extract_summary(html, n=160):
    p = re.sub(r'<[^>]+>', '', html)
    p = re.sub(r'(layout|title|subtitle|date|autor|header-img|header-mask|catalog|tags):\s*\S*', '', p)
    p = re.sub(r'\s+', ' ', p).strip()
    return (p[:n].rsplit(' ', 1)[0] + '...') if len(p) > n else (p or '')

def extract_cover(html):
    m = re.search(r'<img src="([^"]+)"', html)
    return m.group(1) if m else None

# ═══════════════════════════════════════════════════════
# LAYOUT — content-adaptive (no hardcoded cycle)
# ═══════════════════════════════════════════════════════

def build_rows(articles):
    """Content-adaptive layout: spaced featured for covers, 2-col with periodic 1-col breathing room."""
    rows, cy, i = [], None, 0
    rows_since_featured = 0
    cols2_since_cols1 = 0   # insert 1-col after every 2 consecutive 2-col rows

    while i < len(articles):
        a = articles[i]
        y = a['date'][:4] if a['date'] else 'Other'
        if y != cy:
            cy = y
            rows.append(('year', y, None))

        rem = articles[i:]

        # 1-col breathing room: after every 2 consecutive 2-col rows
        if cols2_since_cols1 >= 2:
            rows.append(('cols1', y, [rem[0]]))
            i += 1
            rows_since_featured += 1
            cols2_since_cols1 = 0
            continue

        # Featured: current article has cover AND spaced by ≥2 non-featured rows
        if rem[0]['cover'] and rows_since_featured >= 2:
            rows.append(('featured', y, [rem[0]]))
            i += 1
            rows_since_featured = 0
            cols2_since_cols1 = 0
            continue

        # Default: 2-col, but don't group articles from different years
        if len(rem) >= 2:
            y_next = rem[1]['date'][:4] if rem[1]['date'] else 'Other'
            if y != y_next:
                rows.append(('cols1', y, [rem[0]]))
                i += 1
                rows_since_featured += 1
            else:
                rows.append(('cols2', y, rem[:2]))
                i += 2
                rows_since_featured += 1
                cols2_since_cols1 += 1
        else:
            rows.append(('cols1', y, [rem[0]]))
            i += 1
            rows_since_featured += 1

    return rows

def render_rows(rows_data):
    h = ''
    for row in rows_data:
        rtype, year, items = row
        if rtype == 'year':
            h += '<div class="year-divider"><span>%s</span></div>\n' % year; continue
        if rtype == 'featured':
            a = items[0]
            badge = ('<span class="badge">%s</span>' % a['course']) if a.get('course') else ''
            sub = ('<p class="feat-subtitle">%s</p>' % a['subtitle']) if a.get('subtitle') else ''
            grad, tc, pc = cover_adaptive(a.get('cover'))
            h += '<section class="row row-featured" onclick="openArticle(\'%s\')"><div class="feat-cover"><img src="%s" alt=""><div class="feat-gradient" style="background:%s"></div><div class="feat-text">%s<time>%s</time><h2 style="color:%s">%s</h2>%s<p style="color:%s">%s</p></div></div></section>\n' % (a['id'], a['cover'] or '', grad, badge, a['date'] or '', tc, a['title'], sub, pc, a['summary'])
        elif rtype == 'cols3':
            h += '<section class="row row-3col">\n'
            for a in items:
                cv = '<div class="card-img"><img src="%s" alt=""></div>' % a['cover'] if a['cover'] else ''
                badge = '<span class="badge">%s</span>' % a['course'] if a.get('course') else ''
                sub = ('<p class="card-subtitle">%s</p>' % a['subtitle']) if a.get('subtitle') else ''
                h += '<article class="card" onclick="openArticle(\'%s\')">%s<div class="card-body">%s<time>%s</time><h2>%s</h2>%s<p>%s</p></div></article>\n' % (a['id'], cv, badge, a['date'] or '', a['title'], sub, a['summary'])
            h += '</section>\n'
        elif rtype == 'cols2':
            h += '<section class="row row-2col">\n'
            for a in items:
                badge = '<span class="badge">%s</span>' % a['course'] if a.get('course') else ''
                sub = ('<p class="card-subtitle">%s</p>' % a['subtitle']) if a.get('subtitle') else ''
                cover = a.get('cover')
                if cover:
                    grad, tc, pc = cover_adaptive(cover)
                    h += '<article class="card card-cover" style="background-image:url(%s)" onclick="openArticle(\'%s\')"><div class="card-gradient" style="background:%s"></div><div class="card-body">%s<time>%s</time><h2 style="color:%s">%s</h2>%s<p style="color:%s">%s</p></div></article>\n' % (cover, a['id'], grad, badge, a['date'] or '', tc, a['title'], sub, pc, a['summary'])
                else:
                    h += '<article class="card" onclick="openArticle(\'%s\')"><div class="card-body">%s<time>%s</time><h2>%s</h2>%s<p>%s</p></div></article>\n' % (a['id'], badge, a['date'] or '', a['title'], sub, a['summary'])
            h += '</section>\n'
        elif rtype == 'cols1':
            a = items[0]
            badge = '<span class="badge">%s</span>' % a['course'] if a.get('course') else ''
            sub = ('<p class="card-subtitle">%s</p>' % a['subtitle']) if a.get('subtitle') else ''
            cover = a.get('cover')
            if cover:
                grad, tc, pc = cover_adaptive(cover)
                h += '<article class="row row-full-cover" style="background-image:url(%s)" onclick="openArticle(\'%s\')"><div class="full-gradient" style="background:%s"></div><div class="full-body">%s<time>%s</time><h2 style="color:%s">%s</h2>%s<p style="color:%s">%s</p></div></article>\n' % (cover, a['id'], grad, badge, a['date'] or '', tc, a['title'], sub, pc, a['summary'])
            else:
                h += '<article class="row row-full" onclick="openArticle(\'%s\')"><div class="full-body">%s<time>%s</time><h2>%s</h2>%s<p>%s</p></div></article>\n' % (a['id'], badge, a['date'] or '', a['title'], sub, a['summary'])
    return h

# ═══════════════════════════════════════════════════════
# IMAGE PATH FIXING (for article bodies)
# ═══════════════════════════════════════════════════════

def fix_image_paths(html):
    """Normalize image paths: ../images/ → images/, protect OSS URLs, fix bare filenames."""
    html = re.sub(r'src="\.\./images/', 'src="images/', html)
    html = re.sub(r'src="(?!https?://)([^"]*/([^/"]+\.(?:jpe?g|png|gif|JPG|PNG|JPEG|webp)))"',
                  lambda m: f'src="images/{m.group(2)}"', html)
    html = re.sub(r'src="(?!https?://|images/)([^/"]+\.(?:jpe?g|png|gif|JPG|PNG|JPEG|webp))"',
                  r'src="images/\1"', html)
    return html

# ═══════════════════════════════════════════════════════
# BUILD
# ═══════════════════════════════════════════════════════

print("Loading articles...")
writing_arts = load_articles('writing')
mitx_arts = load_articles('academic')
about_arts = load_articles('about')
print(f"  Writing: {len(writing_arts)}, Academic: {len(mitx_arts)}, About: {len(about_arts)}")

print("Rendering rows...")
WRITING_ROWS = render_rows(build_rows(writing_arts))
MITX_ROWS = render_rows(build_rows(mitx_arts))

print("Rendering article pages...")
ARTICLES_HTML = ''
for a in writing_arts + mitx_arts + about_arts:
    badge = '<span class="badge">%s</span>' % a['course'] if a.get('course') else ''
    body = fix_image_paths(a['body'])

    # Remove duplicate title: the first <h3>Title</h3> from md_to_html
    # duplicates the <h1>Title</h1> in the article header. Strip it.
    # Use regex to handle optional whitespace inside <h3> (e.g. "#  Title")
    body = re.sub(
        r'<h3>\s*' + re.escape(a['title']) + r'\s*</h3>',
        '', body, count=1
    ).lstrip()

    # Cover URL and subtitle for hero banner swap
    cover_attr = ' data-cover="%s"' % a['cover'] if a['cover'] else ''
    sub_attr = ' data-subtitle="%s"' % a['subtitle'].replace('"', '&quot;') if a.get('subtitle') else ''

    ARTICLES_HTML += '<div class="article-page" id="%s"%s%s><article class="prose"><a href="javascript:void(0)" class="back" onclick="closeArticle()"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>Back</a><header>%s<time>%s</time><h1>%s</h1></header>%s</article></div>\n' % (a['id'], cover_attr, sub_attr, badge, a['date'] or '', a['title'], body)

# ═══════════════════════════════════════════════════════
# GALLERY
# ═══════════════════════════════════════════════════════

GALLERY_DIR = os.path.join(ROOT, 'gallery')
ALBUMS = []
if os.path.isdir(GALLERY_DIR):
    for album_name in sorted(os.listdir(GALLERY_DIR)):
        album_path = os.path.join(GALLERY_DIR, album_name)
        if not os.path.isdir(album_path): continue
        photos = sorted([
            f for f in os.listdir(album_path)
            if f.lower().endswith(('.jpg','.jpeg','.png','.gif','.webp'))
        ])
        if not photos: continue
        cover = 'gallery/%s/%s' % (album_name, photos[0])
        ALBUMS.append({
            'id': 'gal-' + album_name.replace(' ', '-'),
            'name': album_name,
            'cover': cover,
            'count': len(photos),
            'photos': ['gallery/%s/%s' % (album_name, p) for p in photos],
        })

GALLERY_ALBUM_LIST = ''
for a in ALBUMS:
    agrad, atc, apc = cover_adaptive(a['cover'])
    GALLERY_ALBUM_LIST += '''
    <article class="album-card" onclick="openAlbum('%s')">
      <div class="album-cover"><img src="%s" alt="" loading="lazy"></div>
      <div class="album-body" style="background:%s">
        <h2 style="color:%s">%s</h2>
        <p style="color:%s">%d photos</p>
      </div>
    </article>''' % (a['id'], a['cover'], agrad, atc, a['name'], apc, a['count'])

GALLERY_ALBUM_PAGES = ''
for a in ALBUMS:
    imgs = '\n'.join('<img src="%s" alt="" loading="lazy" onclick="openLightbox(%d)">' % (p, i)
                     for i, p in enumerate(a['photos']))
    GALLERY_ALBUM_PAGES += '''
    <div class="gallery-album" id="%s">
      <a href="javascript:void(0)" class="back" onclick="showGalleryList()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>Gallery
      </a>
      <header><h1>%s</h1><p>%d photos</p></header>
      <div class="gallery-grid">%s</div>
    </div>''' % (a['id'], a['name'], a['count'], imgs)

# Lightbox data — use json.dumps for valid JS
LIGHTBOX_DATA = '<script>var lightboxData=' + json.dumps({a['id']: a['photos'] for a in ALBUMS}) + ';</script>'

# Hero cover images — prefer hand-picked covers/home-* files, fallback to article covers
HOME_W = os.path.join(ROOT, 'covers', 'home-writing.jpg')
HOME_A = os.path.join(ROOT, 'covers', 'home-academic.jpg')
who_bg = ''
aho_bg = ''
if os.path.exists(HOME_W):
    who_bg = 'style="background:linear-gradient(rgba(0,0,0,.45),rgba(0,0,0,.45)),url(covers/home-writing.jpg) center/cover"'
else:
    print('WARNING: covers/home-writing.jpg not found — using fallback cover')
    wcov = next((a['cover'] for a in writing_arts if a['cover']), None)
    if wcov: who_bg = 'style="background:linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,.55)),url(%s) center/cover"' % wcov

if os.path.exists(HOME_A):
    aho_bg = 'style="background:linear-gradient(rgba(0,0,0,.45),rgba(0,0,0,.45)),url(covers/home-academic.jpg) center/cover;display:none"'
else:
    print('WARNING: covers/home-academic.jpg not found — using fallback cover')
    acov = next((a['cover'] for a in mitx_arts if a['cover']), None)
    if acov: aho_bg = 'style="background:linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,.55)),url(%s) center/cover;display:none"' % acov

# About hero — find home-about with any extension
HOME_ABOUT = None
for ext in ('.jpg', '.jpeg', '.png', '.webp'):
    p = os.path.join(ROOT, 'covers', f'home-about{ext}')
    if os.path.exists(p):
        HOME_ABOUT = f'covers/home-about{ext}'
        break
abo_bg = ''
if HOME_ABOUT:
    abo_bg = f'style="background:linear-gradient(rgba(0,0,0,.45),rgba(0,0,0,.45)),url({HOME_ABOUT}) center/cover;display:none"'
else:
    print('WARNING: covers/home-about.* not found — using fallback cover')
    acov = next((a['cover'] for a in about_arts if a['cover']), None)
    if acov: abo_bg = f'style="background:linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,.55)),url({acov}) center/cover;display:none"'

# About page content — render the first about article as a prose block
ABOUT_CONTENT = ''
if about_arts:
    a = about_arts[0]
    body = fix_image_paths(a['body'])
    body = re.sub(
        r'<h3>\s*' + re.escape(a['title']) + r'\s*</h3>',
        '', body, count=1
    ).lstrip()
    ABOUT_CONTENT = '<article class="prose about-prose">%s</article>' % body

# ═══════════════════════════════════════════════════════
# GENERATE HTML
# ═══════════════════════════════════════════════════════

# Read the HTML template
template_path = os.path.join(ROOT, 'template.html')
if os.path.exists(template_path):
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
else:
    print("ERROR: template.html not found!")
    exit(1)

# Gallery hero — use home-writing.jpg as background
gho_bg = 'style="background:linear-gradient(rgba(0,0,0,.45),rgba(0,0,0,.45)),url(covers/home-writing.jpg) center/cover;display:none"'

html = template.replace('__WCNT__', str(len(writing_arts)))
html = html.replace('__ACNT__', str(len(mitx_arts)))
html = html.replace('__GCNT__', str(len(ALBUMS)))
html = html.replace('__ABTCNT__', str(len(about_arts)))
html = html.replace('__WHO_BG__', who_bg)
# Cache-busting version
ver = str(int(time.time()))

html = html.replace('__AHO_BG__', aho_bg)
html = html.replace('__GHO_BG__', gho_bg)
html = html.replace('__ABO_BG__', abo_bg)
html = html.replace('css/style.css', f'css/style.css?v={ver}')
html = html.replace('js/app.js', f'js/app.js?v={ver}')
html = html.replace('__WROWS__', WRITING_ROWS)
html = html.replace('__AROWS__', MITX_ROWS)
html = html.replace('__ABROWS__', ABOUT_CONTENT)
html = html.replace('__GALBUMS__', GALLERY_ALBUM_LIST)
html = html.replace('__GALPAGES__', GALLERY_ALBUM_PAGES)
html = html.replace('__ARTICLES__', ARTICLES_HTML)
html = html.replace('__LBDATA__', LIGHTBOX_DATA)

out_path = os.path.join(ROOT, 'index.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Generated {out_path} ({os.path.getsize(out_path):,} bytes)')
