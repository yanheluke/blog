# Blog Project

Static blog generated from Bear notes. Spotify dark theme per DESIGN.md.

## Update workflow

```
# Incremental (bearcli CLI, for daily use):
python3 export.py                     # New notes since last sync
python3 export.py --limit 3           # Latest 3 from each section
python3 export.py --since 2026-05-13  # Notes created after date
python3 export.py --since last        # Notes since .last_sync
python3 export.py --section writing   # Only writing section
python3 build.py

# Full export (SQLite read-only, for init/disaster recovery):
python3 export_full.py   # reads Bear SQLite (mode=ro), copies images from disk
python3 build.py
```

- `export.py` — incremental via `bearcli` CLI. No SQLite, no MCP. Supports `--limit`, `--since`, `--section`
- `export_full.py` — SQLite **read-only** bulk export. Opens DB with `mode=ro`
- Both use `{note_uuid[:8]}_{filename}` naming to prevent image collisions across notes
- `.last_sync` file tracks last export date for `--since last` mode
- `bear_pk` is the Bear note UUID (consistent between both scripts)

**Always use Bear MCP tools / bearcli, never modify Bear SQLite DB directly.** SQLite read-only is acceptable for bulk export. If an operation requires writing to SQLite (e.g., changing creation timestamps), ask for explicit permission first.

**Never modify Bear DB during this process — read only.**

## Architecture

- `export.py` — incremental via `bearcli` CLI. Uses `bearcli search --format json` + `attachments save`. No SQLite, no MCP
- `export_full.py` — bulk via SQLite read-only (`mode=ro`), copies images from Bear's file storage
- `build.py` — reads local `.md`, generates `index.html` using `template.html`
- `css/style.css` — all styles (Spotify dark, DESIGN.md-aligned)
- `js/app.js` — all interactivity (section switching, hero swap, scroll restore, gallery lightbox)
- `DEVELOPMENT.md` — pitfalls and lessons learned (read before major changes)
- `DESIGN.md` — design system spec

## Key rules — data

- Use `ZCREATIONDATE` for dates, NEVER `ZMODIFICATIONDATE`
- CoreData timestamps: `datetime.utcfromtimestamp(ts - 978307200)` (subtract, not add)
- Image resolution: use `ZSFNOTEFILE.ZUNIQUEIDENTIFIER` (file UUID) to find directories, NOT note UUID. Query: `SELECT ZFILENAME, ZUNIQUEIDENTIFIER FROM ZSFNOTEFILE WHERE ZNOTE=?`
- Image references in note text are URL-encoded — MUST `urllib.parse.unquote()` before matching against filesystem filenames
- Always use `re.sub()` for global replacement of image references; `str.replace()` only replaces the first occurrence

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

## Key rules — Bear DB

- **Close Bear before modifying its SQLite DB.** Bear re-parses tags on restart and will undo direct DB changes
- Tag format: `#simpleword` for no-space tags, `#multi word#` for tags with spaces, `#parent/child` for nesting
- When modifying tags, update ALL THREE: inline `#tag` in ZTEXT, ZSFNOTETAG.ZTITLE, and Z_5TAGS associations
- `ZISROOT=1` only for true root tags; compound tags (with `/`) should always have `ZISROOT=0`

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
- **CRITICAL: `export.py` clears `covers/` on each run.** Files named `home-*` are now preserved (skip in the cleanup loop). When adding new hand-picked covers with special names, follow the `home-*` prefix convention or add an exception in `export.py` — otherwise they will be deleted on the next export.
