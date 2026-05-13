# Development Notes & Lessons Learned

This document captures all pitfalls, non-obvious behaviors, and design decisions encountered while building this static blog generator from Bear notes. Read this before rebuilding the project from scratch.

---

## 1. Bear Data Extraction

### 1.1 CoreData Timestamps

Bear uses Apple CoreData internally. All timestamps (`ZCREATIONDATE`, `ZMODIFICATIONDATE`) are **seconds since 2001-01-01**, not Unix epoch (1970-01-01).

```python
# WRONG
unix_ts = timestamp + 978307200  # DO NOT ADD

# CORRECT
unix_ts = timestamp - 978307200  # SUBTRACT
datetime.utcfromtimestamp(timestamp - 978307200)
```

**Never use `ZMODIFICATIONDATE` for article dates.** Always use `ZCREATIONDATE`. Modification dates get overwritten by any edit (including tag migrations), making them useless for chronological ordering.

### 1.2 Image Storage in Bear

Bear stores attached images in two layers:

**Layer 1 — Database (`ZSFNOTEFILE` table)**
- `ZNOTE` → FK to `ZSFNOTE.Z_PK`
- `ZFILENAME` → original filename as stored on disk (e.g., `"image 2.png"`)
- `ZUNIQUEIDENTIFIER` → file UUID

**Layer 2 — Filesystem**
```
~/Library/Group Containers/9K33E3U3T4.net.shinyfrog.bear/
  Application Data/Local Files/Note Images/
    {note-UUID}-{suffix}/     ← directory per note
      image.png
      image 2.png
      ...
```

The mapping from text reference → actual file:

```
Note text:   ![](image%202.png)
             ↓ URL decode
             image 2.png
             ↓ match against ZSFNOTEFILE.ZFILENAME or filesystem
             {note-img-dir}/image 2.png
```

**Critical:** The text reference uses URL-encoding (`%20` for space). You MUST `urllib.parse.unquote()` before matching against filesystem filenames.

### 1.3 Tag Format in Bear

Tags are stored as inline `#` references in note text (`ZTEXT`). Two formats exist:

| Type | Text Format | Example |
|------|-------------|---------|
| Simple word (no space) | `#tagname` | `#Writing`, `#python` |
| Multi-word or CJK | `#tag name#` (wrapped) | `#3. 美团#`, `#中文标签#` |
| Sub-tag (no space) | `#parent/child` | `#Work/Meituan` |
| Sub-tag (with space) | `#parent/child name#` | `#3. 美团/骑手险#` |

**Rule:** If a tag name contains a space, Bear wraps it in `#...#`. If no space, just a leading `#` suffices. The `/` character creates nesting hierarchy.

**When modifying tags, you MUST update BOTH:**
- `ZSFNOTETAG.ZTITLE` (tag definition)
- `Z_5TAGS` (note-tag associations)
- The inline `#tag` references in `ZTEXT` (note body)

Failing to update the inline text means Bear will **recreate the old tags** on next restart when it re-parses the notes.

### 1.4 ZISROOT Controls Sidebar Visibility

`ZSFNOTETAG.ZISROOT` determines whether a tag appears as a root (top-level) item in the sidebar:

- `ZISROOT = 1` → shown as root tag (single-segment names like `Writing`, `Work`)
- `ZISROOT = 0` → only shown as child under parent (e.g., `Work/Meituan`, `Finance/CFA`)

Setting `ZISROOT=1` on a compound tag like `Finance/CPA` will cause `CPA` to appear as a standalone top-level tag in addition to appearing under `Finance`. This is almost always wrong.

---

## 2. Image Handling Pipeline

### 2.1 Three Types of Images

1. **OSS URLs** — hosted on external CDN (e.g., `https://yanheluke.oss-cn-beijing.aliyuncs.com/photo.jpeg`). Keep as-is.
2. **Bear-local images** — stored in Bear's `Note Images/` directory. Must be extracted and copied.
3. **Jekyll header images** — paths like `img/in-post/tokyo.jpg` from frontmatter. These do NOT exist locally.

### 2.2 Bear-Local Image Extraction

```python
def copy_bear_images(note_pk, note_uuid, text, output_img_dir):
    # 1. Find note's image directory
    note_img_dir = None
    for root, dirs, files in os.walk(BEAR_IMG_BASE):
        for d in dirs:
            if note_uuid.upper() in d.upper():
                note_img_dir = os.path.join(root, d)
                break

    # 2. For each image reference in text
    for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', text):
        src = m.group(2).strip('~')
        if src.startswith('http'):
            continue  # OSS URL, skip

        # 3. URL-decode and match against filesystem
        decoded = urllib.parse.unquote(src)
        fname = os.path.basename(decoded)

        if note_img_dir:
            for disk_file in os.listdir(note_img_dir):
                if disk_file.lower() == fname.lower():
                    shutil.copy2(src=..., dst=output_img_dir / disk_file)
                    break

    # 4. Update text references — use re.sub, NOT str.replace!
    # str.replace only replaces FIRST occurrence!
    modified_text = re.sub(
        r'\(' + re.escape(src) + r'\)',
        r'(../images/' + disk_file + r')',
        modified_text
    )
```

### 2.3 Why `str.replace` Fails for Image References

If a note has the same image referenced twice:
```markdown
![](image.png)
...text...
![](image.png)
```

`text.replace('(image.png)', '(../images/image.png)')` only replaces the **first** occurrence.

**Always use `re.sub()` for global replacement.**

### 2.4 OSS URL Protection in Phase 2

When normalizing image paths during HTML generation, never let regexes touch OSS URLs:

```python
# WRONG — this will turn https://... URLs into local images/ paths
body = re.sub(r'src="([^"]+\.(?:jpe?g|png|gif))"',
              r'src="images/\1"', body)

# CORRECT — use negative lookahead to skip http(s) URLs
body = re.sub(r'src="(?!https?://)([^/"]+\.(?:jpe?g|png|gif))"',
              r'src="images/\1"', body)
```

---

## 3. LaTeX / KaTeX

### 3.1 Display Math Format

Bear stores display math as `$$` on **separate lines**:

```latex
$$
\int_a^b f(x) dx
$$
```

KaTeX renders this as a display block by default because `$$` → `{display: true}`. However, the `$$` delimiters must be at the start/end of the line, and KaTeX's auto-render needs to see them as separate tokens. The `$$` at line start/end is handled by KaTeX's built-in `splitAtDelimiters` logic — no special preprocessing needed IF KaTeX is configured with:

```javascript
renderMathInElement(document.body, {
  delimiters: [
    {left: "$$", right: "$$", display: true},
    {left: "$", right: "$", display: false}
  ]
});
```

### 3.2 Inline Math

Inline math uses single `$...$` on the same line. Works out of the box with the config above.

---

## 4. Python/Build Pitfalls

### 4.1 f-string Curly Braces

**Never embed CSS or JS with bare `{` `}` inside Python f-strings.** Python interprets `{...}` as f-string expressions, causing `SyntaxError` for CSS rules like `.card{display:flex}`.

**Solution:** Use template strings with `str.replace()`:

```python
# WRONG
html = f'''<style>{CSS}</style>'''  # CSS has { } → SyntaxError

# CORRECT
TEMPLATE = '''<style>__CSS__</style>'''
html = TEMPLATE.replace('__CSS__', CSS)
```

### 4.2 f-string Backslash in Expressions

```python
# WRONG — backslash not allowed in f-string expression
f'{re.sub(r"\d+", "", s)}'

# CORRECT — extract to variable first
v = re.sub(r'\d+', '', s)
f'{v}'
```

---

## 5. Frontend Pitfalls

### 5.1 Inline Style vs CSS Class Priority

**Inline `element.style.display = 'none'` overrides ALL CSS classes**, including `.active { display: flex }`.

Bug pattern:
```javascript
// openArticle: hide all sections
document.querySelectorAll('.section-content')
  .forEach(c => c.style.display = 'none');  // ← sets inline style

// closeArticle (BUGGY): only restore current section
var sc = document.getElementById('section-' + currentSection);
sc.style.display = 'flex';  // OLD section still has inline display:none!

// switchSection: adds CSS class
section.classList.add('active');  // CSS says display:flex
// BUT inline display:none from openArticle overrides → HIDDEN!
```

**Fix:** `closeArticle()` must clear inline styles on ALL sections:
```javascript
document.querySelectorAll('.section-content')
  .forEach(c => c.style.display = '');  // Remove inline, let CSS control
```

### 5.2 DOMContentLoaded for Initial State

Don't rely on HTML `style` attributes alone for initial visibility on page load. Browser refresh may restore previous scroll/display state. Always run an explicit initialization:

```javascript
document.addEventListener('DOMContentLoaded', function() {
  setHero('writing');  // Ensure correct hero on page load/refresh
});
```

### 5.3 Section Switching Architecture

When building a sidebar-tabbed interface with article detail views:

```
State machine:
  List View → click article → Article View
  List View → click sidebar tab → switch list
  Article View → click Back → List View
  Article View → click sidebar tab → switch list (CLOSE article first)
```

Key invariants:
- **Only one section's list** is visible at a time (`.section-content.active`)
- **Only one article** is visible at a time (`.article-page.active`)
- When switching tabs, **always close any open article first**
- Browser back/forward must restore the correct section + article state

---

## 6. Layout Design

### 6.1 Layout Cycle Must Be Short Enough

If your layout cycle length exceeds the number of articles, some layout types will **never be reached**:

```python
# Problem: 27 articles, 8-pattern cycle → position 7 never reached
LAYOUT = [3, 2, 'F', 3, 3, 'F', 2, 1]  # '1' at pos 7, cycle len 8
# After 3 full cycles (24 articles), 3 remaining → positions 0,1,2 only

# Fix: duplicate '1' at multiple positions
LAYOUT = [3, 2, 'F', 1, 3, 'F', 2, 1]  # '1' at pos 3 and 7, cycle len 8
```

### 6.2 Featured Rows Require Cover Images

The `'F'` pattern looks for an article with a cover image in the next 4 articles. If none found, falls back to `cols3`. This means:
- Sections without many cover images will have fewer featured rows
- MITx notes (screenshots as images) vs Writing (photos as images) have different cover density
- The `extract_cover()` function picks the FIRST `<img>` in the article body

---

## 7. Data Pipeline Architecture

### Recommended: Two-Phase Export

```
Phase 1: Bear DB → local .md files + images/
  - Runs once after Bear content changes
  - Decouples from Bear database
  - Images copied to local directory

Phase 2: .md files → index.html (static site generator)
  - Runs whenever presentation changes
  - No Bear dependency at runtime
  - Pure file-in, file-out
```

This separation means you can iterate on frontend design without repeatedly querying the Bear database.

### 7.1 Why Decoupling Matters

- Bear's database format can change across app versions
- SQLite queries on a live Bear DB may conflict with Bear's own writes
- iCloud sync can modify the DB at any time
- Exporting to local files creates a stable snapshot for version control

---

## 8. Tag Migration Checklist

When restructuring Bear tags across many notes:

1. [ ] Backup the database: `cp database.sqlite backup.sqlite`
2. [ ] **Close Bear** — it will re-parse tags on restart and undo DB changes
3. [ ] Replace inline `#oldtag` → `#newtag` in ZTEXT (use `re.sub`, not `str.replace`)
4. [ ] Rename/merge tags in ZSFNOTETAG
5. [ ] Redirect Z_5TAGS associations
6. [ ] Handle sub-tag duplicates: notes with both `#parent` and `#parent/child` → both become `#newparent` → use DELETE + UPDATE, not UPDATE OR IGNORE
7. [ ] Set ZISROOT=0 for all compound tags (with `/`)
8. [ ] Delete empty/zombie tags
9. [ ] Open Bear and verify sidebar
10. [ ] Check for text/DB consistency (count mismatches)

---

---

## 9. Cover Image System

### 9.1 Detection Rules

Cover images are determined at export time (`export.py`) with two rules:

1. **Cover at start**: If the first non-empty content after the H1 title is an image → it's the cover. The image is **removed from the body** (it was placed there solely to indicate the cover).
2. **Fallback**: Otherwise, the first image found anywhere in the article is used as the cover. It **stays in the body** at its original position.

```python
# Simplified logic
lines = text.split('\n')
first_content_after_title = find_first_nonempty_after_h1(lines)

if is_image_line(first_content_after_title):
    cover = extract_and_remove(first_content_after_title)
else:
    cover = find_first_image_anywhere(text)  # keep in body
```

### 9.2 File Storage

- **`covers/`** directory stores one copy of each cover image
- **`images/`** directory stores inline images (used within article bodies)
- Covers are referenced as `covers/filename.jpg` in HTML
- OSS URLs used as covers are referenced directly (no local copy)

### 9.3 Where Covers Appear

- **Article list cards**: `card-img` shows the cover
- **Featured rows**: background image
- **Article detail page**: `.prose-hero` section at the top, before the title

### 9.4 Why Separate `covers/` from `images/`

- Covers may be removed from the article body (rule 1), so they're not in `images/`
- Covers have different display requirements (hero sizing vs inline sizing)
- Clean separation makes it easy to replace covers without touching inline images

### 9.5 Writing Convention

When writing in Bear, place the cover image as the **first line after the title** to indicate it's the cover (not body content):

```markdown
# My Travel Blog
![](cover-photo.jpg)       ← This is the cover, won't appear in body
                           ← (blank line)
Content starts here...
```

If you don't place an image at the start, the first image in the body will be used as the cover but will still appear inline.

---

### 9.6 Image File Resolution (ZSFNOTEFILE)

**Critical:** Bear stores each attached image in its own directory named after the **file's UUID** (from `ZSFNOTEFILE.ZUNIQUEIDENTIFIER`), NOT the note's UUID.

```
ZSFNOTE.ZUNIQUEIDENTIFIER       → Note UUID (e.g., "00B15142-...")
ZSFNOTEFILE.ZUNIQUEIDENTIFIER   → File UUID (e.g., "1E02CAA4-...")
                                   ↑ This is the directory name in Note Images/
```

The correct resolution pipeline:
1. Note text has `![](image%202.png)`
2. URL-decode → `image 2.png`
3. `SELECT ZFILENAME, ZUNIQUEIDENTIFIER FROM ZSFNOTEFILE WHERE ZNOTE = {note_pk}`
4. Match `ZFILENAME` (case-insensitive) against the decoded reference
5. Get `ZUNIQUEIDENTIFIER` — this is the directory name in `Note Images/`
6. Copy the file from `Note Images/{file-UUID}/{filename}`

**Do NOT** use the note UUID to find image directories — it will never match.


*Last updated: 2026-05-12*
