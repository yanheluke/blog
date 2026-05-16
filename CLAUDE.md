# Blog Project

Static blog generated from Obsidian notes. Spotify dark theme per DESIGN.md.

## Setup

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Update workflow

```
# Incremental (Obsidian vault, for daily use):
source venv/bin/activate
python3 export_obsidian.py                 # New notes since last sync
python3 export_obsidian.py --section writing  # Only writing section
python3 export_obsidian.py --full          # Full export (ignore .last_sync)
python3 build.py

# Legacy Bear export (kept for reference, not daily use):
python3 export.py --section writing --limit 1
python3 export_full.py   # SQLite read-only, Bear only
```

- `export_obsidian.py` — reads `.md` from Obsidian vault `~/Research Hub/`, copies images from `_assets/`. Supports `--section`, `--full`, `--limit`
- `export.py` — legacy Bear export via `bearcli` CLI (kept for reference)
- `export_full.py` — legacy Bear bulk export via SQLite (kept for reference)
- `.last_sync` file tracks last export date for incremental sync
- Image prefix uses `obsidian_id` (MD5 first 8 chars of vault-relative path)

## Architecture

- `export_obsidian.py` — reads Obsidian vault `.md` files, parses YAML frontmatter, copies images from `_assets/{note-name}/`
- `build.py` — reads local `.md`, generates `index.html` using `template.html`
- `css/style.css` — all styles (Spotify dark, DESIGN.md-aligned)
- `js/app.js` — all interactivity (section switching, hero swap, scroll restore, gallery lightbox)
- `DEVELOPMENT.md` — pitfalls and lessons learned (read before major changes)
- `DESIGN.md` — design system spec

## Obsidian vault structure

```
~/Research Hub/
  4. Writing/          → content/writing/ (filter: YAML tags include "Writing")
  About Me.md          → content/about/
  _assets/{note-name}/ → per-note images (subdirectory named after note)
```

## Obsidian YAML frontmatter

```yaml
---
title: 文章标题              # Falls back to filename if absent
subtitle: 副标题             # Optional, from YAML (NOT from blockquote)
create_date: 2015-06-07      # YYYY-MM-DD, falls back to file mtime (UTC+8)
modify_date: 2026-05-16      # Not used for blog, Obsidian tracking only
tags:                        # YAML list; "Writing" tag = blog writing section
  - 北京
  - 杂谈
---
```

## Key rules — data (Obsidian)

- Date source: YAML `create_date` → file mtime (Beijing time UTC+8). Never use `modify_date`
- Image storage: `_assets/{note-name}/{image.jpg}` — one subdirectory per note
- Image references: standard `![](image.jpg)` in Markdown. OSS URLs used directly
- `export_obsidian.py` auto-creates `covers/` and `images/` dirs, no manual cleanup needed
- Never modify Obsidian vault files during export — read only

## Key rules — build

- OSS image URLs must be protected with negative lookahead: `(?!https?://)` in regexes. Otherwise they get turned into broken local `images/` paths
- Cover detection: first non-empty content after H1 title → if image, remove from body + use as cover. Otherwise first image in body → keep in body + use as cover
- Strip duplicate `<h3>Title</h3>` from body before extracting summary. Use regex with `\s*` to tolerate whitespace variance (e.g. `#  Title` → `<h3> Title</h3>`)
- `covers/` is for cover images (may be removed from body); `images/` is for inline body images
- Gallery images are served directly from `gallery/` directory — no export step needed
- Lightbox photo data MUST use `json.dumps()` for valid JS, never Python `str(list)`
- Build template uses `str.replace()` with `__PLACEHOLDER__` tokens — never embed CSS/JS with `{}` in Python f-strings

## Key rules — frontend

- **Inline `style.display` overrides ALL CSS classes.** When hiding sections in `openArticle()`, `closeArticle()` must clear inline styles on ALL sections with `c.style.display = ''`, not just restore the current one
- **Save hero style before modifying it.** `openArticle()` appends article cover to hero's inline style; `closeArticle()` must restore the original `style` attribute via `savedHeroStyle`, not just toggle display
- Section switching must close any open article first, then show the new section's list
- Browser back/forward: `popstate` handler must restore both section AND article state, and handle hero style save/restore
- KaTeX config in template: `$$` for display math, `$` for inline. No special preprocessing needed

## Layout

- Content-adaptive in `build.py`: no hardcoded cycle
  - Articles with cover images → featured (spaced by ≥2 non-featured rows)
  - Default → 2-col rows
  - Last remaining article → 1-col full-width
  - No 3-col rows (removed per user preference)
- Featured rows: full-width, 420px tall, cover image background with gradient overlay
- Gallery: album cards (full-width, 340px, cover image + gradient text overlay), CSS `columns: 2` for photo grid inside albums

## Homepage hero covers

- Place `covers/home-writing.jpg` and `covers/home-academic.jpg` for section hero backgrounds
- Falls back to first article's cover image if home-* files don't exist
