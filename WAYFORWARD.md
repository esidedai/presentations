# Way Forward: Slide Generation Improvements

## 1. SVG → PNG Pipeline (from esided.com)

**What:** Build slide backgrounds as SVG templates, inject content programmatically, render to PNG via `@resvg/resvg-js`.

**Why it earns a spot:**
- Bypasses html2canvas entirely — no gray background issue
- Pixel-perfect output: fonts embedded as base64, exact colors, no browser rendering quirks
- Proven in production (esided.com blog/case-study banner pipeline)
- Works server-side (Node.js), no browser dependency

**How it could fit:**
- Create branded 1280×720 SVG slide backgrounds (decorative shapes, logos, patterns)
- Layer content (titles, text, images) into SVG programmatically
- Render final PNG with `@resvg/resvg-js`
- Insert PNGs into PowerPoint as before

**Limitations:**
- SVG text layout is more rigid than CSS (no flexbox/grid)
- Complex layouts (multi-column, charts) may still need the HTML approach
- Best suited for backgrounds + simple text overlays, not full slide composition

**Reference:** `c:\Dev\esided.com\scripts\generate-covers.js` — 299-line working implementation
**Assets copied:** `assets/templates/backgrounds/bg.svg` and `bg-with-logo.svg`

## 2. Tetris Layout Reasoning for Slides

**What:** A 6-step framework for solving layout problems by rearranging pieces instead of shrinking fonts. Already codified and proven for resumes (portrait + landscape) and case studies.

**The 6 steps:**
1. Measure pieces (height category + width hunger)
2. Identify culprits (height mismatches, cramped width-hungry content)
3. Classify content type (narrative, reference, anchor, hero, conclusion)
4. Pair by height (tall+tall, short+short, stack tiny pieces)
4b. Assign by width (width-hungry content gets wider columns)
5. Apply patterns (full-width anchors, stacked columns, 2-col flows, hero framing)

**Key insight for slides:** 1280×720 is a fixed canvas like landscape resumes. Same rules apply — measure, pair, assign, never shrink below font floors (24pt minimum for slides viewed at distance).

**Reference:** `.ai/reference/LAYOUT-REASONING.md` — full spec with decision tree and worked examples

## 3. Single-File HTML as Slide Canvas (proven at both ratios)

**What:** Build each slide as a self-contained HTML file with inline CSS, CSS Grid/Flexbox layout, and Google Fonts via CDN. The Tetris layout patterns render directly in the browser as a validation layer.

**Proven examples:**
- **Portrait (816×1056):** `.ai/reference/S2-lead-follow-up-enforcer.html` — AI worker resume with hero row (`250px 1fr`), trust row (`290px 1fr`), 2-col responsibilities, stacked pills, full-width anchors
- **Landscape (1280×720):** `.ai/reference/invoice-processing-agent.html` — 3-column grid (`280px 380px 1fr`), fixed height, 2×2 value cards, html2canvas export button

**Why this matters:**
- CSS Grid/Flexbox gives layout power that SVG can't (multi-column, wrapping, auto-sizing)
- Browser preview = exact validation of what the slide looks like
- Data-driven: content as JS objects → template literals → CSS Grid sections (see Gatewood case studies in `c:\Dev\aidemohub.com\gW7dT4kP2m\`)
- Single file = zero dependencies, version-controllable, portable

**The one broken link:** html2canvas export produces gray backgrounds instead of white. This is the only thing that doesn't work.

## 4. The Combined Strategy (connecting the dots)

**HTML for layout + SVG/resvg for export** — use each tool where it's strongest:

1. **Design slides in HTML** using Tetris layout reasoning (item #2) — full CSS Grid/Flexbox power, browser preview as validation
2. **Export backgrounds via SVG → resvg** (item #1) — pixel-perfect, no gray background
3. **For complex slides:** explore replacing html2canvas with resvg-based rendering, or use SVG backgrounds with HTML content overlaid before export
4. **For simple slides (title, divider, quote):** SVG pipeline may handle the entire slide

**Open questions:**
- Can we convert full HTML slides to SVG for resvg rendering? (would solve everything)
- Is there a headless browser approach (Puppeteer) that avoids html2canvas limitations?
- Can we composite SVG background + HTML content in a two-pass export?

---

## Scar Tissue (Don't Repeat These)

1. **SVG "e" centering trap:** Hand-approximating SVG paths produces off-center results. Always use the exact original path data from source SVGs, wrap in `translate(-originX -originY)` to zero-out, then position with outer `translate()` and `scale()`.
2. **Perfectionism on backgrounds before content:** The objective is a final in-person presentation deck. Backgrounds are foundation, not the deliverable. Don't over-iterate on decorative elements — get to content slides fast.
3. **html2canvas gray background:** Known limitation, documented in RETROSPECTIVE.md. Don't retry the same library expecting different results.
4. **SVG→PNG visual validation:** Claude can't see SVGs but CAN see PNGs. If visual validation is needed without user, use `npx @resvg/resvg-cli` to convert SVG→PNG, read the image, then delete the temp file.
5. **Content vs. logo zone conflict:** Top-left corner (0-120px top, 0-350px left) is the logo zone. Never place content (headings, act labels) with `padding: 80px 120px` — it lands right on the logo. Use `justify-content: center` to vertically center content, or pad top 160px+ to clear the logo.
6. **No solid-color highlight cards:** Full `background: var(--brand-blue)` cards are aggressive on-screen. Use subtle differentiation instead: `border-top` color accent on the lead card, keep all card backgrounds white. Blue should be an accent, never a fill.
7. **Transition slides = centered, no illustration:** Slides like "What if?" reframes are dramatic pauses. Don't split 50/50 with an illustration — center the text, use a divider, let whitespace do the work. Less is more on transition slides.
8. **Tables don't work on slides:** HTML `<table>` elements look messy at presentation scale. Use side-by-side card columns instead — each column is a rounded card with its own header + stacked label/value rows. Much more readable from the back of a room.
9. **Purple is not a brand color for content:** Only use `--brand-blue` (#0078d4) for accents. Purple (#8764b8) was only ever in the old accent-bar gradient. Don't let it creep into borders, text, or fills.

---

## Progress Log

### 2026-02-14 — Session 1: Foundation & Templates

**Dots gathered:**
1. Read RETROSPECTIVE.md — understood proven workflow + html2canvas blocker
2. Explored esided.com SVG→PNG banner pipeline (`generate-covers.js`, `@resvg/resvg-js`)
3. Read LAYOUT-REASONING.md — Tetris 6-step framework for any canvas shape
4. Read S2-lead-follow-up-enforcer.html — portrait (816×1056) Tetris layout in action
5. Read invoice-processing-agent.html — landscape (1280×720) same pattern, has html2canvas export

**Actions completed:**
1. Created WAYFORWARD.md (this file)
2. Copied `bg.svg` + `bg-with-logo.svg` to `assets/templates/backgrounds/`
3. Updated WAYFORWARD.md with all dots
4. Created 3 SVG slide backgrounds (initially 1280×720, now 1920×1080):
   - `b-clean/slide-bg.svg` — no logo, subtle hex+dot patterns ✓ validated
   - `c-branded/slide-bg.svg` — same + "e" badge (80px, bottom-right) ✓ fixed centering
   - `d-bold/slide-bg.svg` — bolder wash, left accent bar, second dot grid, larger "e" badge, bottom accent line ✓ validated
5. **Locked resolution at 1920×1080** (PowerPoint native Full HD)
6. Restructured folders: `backgrounds/a-title, b-clean, c-branded, d-bold` + `slides/`
7. Created `a-title/slide-bg.svg` — gradient blobs (blue top-left, purple bottom-right) + accent bar
8. Built `slides/01-title.html` — first artifact for final deck (1920×1080, gradient bg, logo, illustration, title text)

**Scar tissue added:** Resolution was 1280×720 in retrospective — wasted time on wrong size. Locked at 1920×1080 going forward.

9. Created 3 title slide variants (v1/v2/v3) using b-clean, c-branded, d-bold backgrounds — no accent bar
10. Discovered Figma asset goldmine in `assets/From-Figma/`

**Figma Assets Inventory (key files for slides):**
| File | What | Use |
|------|------|-----|
| `eSided-Original-Logo.svg` | Full eSided logo (SVG) | Title slides, branding — replaces PNG |
| `eSided-e-only-of-logo.svg` | "e" mark (SVG) | Badge on content slides — replaces hand-coded path |
| `PowerPoint-Slides-Background-Final.svg` | Slide background from Figma | Likely THE production background — check first |
| `light-background-with-shapes.svg` | Alternative light bg | Content slides |
| `Portrait-Background.svg` | Portrait bg | If needed for portrait formats |
| `esided-Title-Slide-Illustration.svg` | Title illustration (SVG) | Color-changeable version of the PNG |
| `Zak-Ali-SVG-Gray-Scale.svg` + 3 others | Team headshots (SVG) | Team slide |
| `Banner-Example-*.svg` | Reference banner designs | Design inspiration |

**Key insight:** SVG versions of logo, illustration, and backgrounds mean we can change colors programmatically. No more hand-approximating paths — use these source files.

**Status:** Title slide variants ready for validation. Figma assets available for production slides.

11. Built `01-title-figma.html` using all Figma source assets (SVG bg, SVG logo, SVG illustration)
12. Added diffuse radial-gradient logo backing to mask dot pattern behind logo — still tuning

---

## 5. DECK BUILD PLAN — "Building Your AI Workforce" (28 slides)

**Source of truth:** `presentations/2026-02-live-event/content/outline.md`
**Resolution:** 1920×1080 | **Fonts:** Inter + Playfair Display (Google CDN)
**Brand colors:** `#0078d4` (blue), `#8764b8` (purple), `#323130` (dark), `#0886C8` (esided blue)

### Slide Types & Templates Needed

| Type | Slides | Layout Pattern |
|------|--------|---------------|
| **Title** | 1, 28 | Hero title left, illustration right, logo top-left, Figma bg |
| **Photo + Text** | 2, 3, 4, 5 | Full-bleed image left/right, text overlay with semi-transparent backing |
| **Icon/Illustration + Text** | 6, 8, 9, 11, 15, 17, 19, 21, 23, 24, 25, 27 | undraw illustration + text (60/40 or 50/50 split) |
| **Data/Chart** | 7, 13, 18 | QuickChart or CSS chart + key numbers callout |
| **Comparison/Table** | 10, 22 | 2-col or table layout, full-width |
| **Diagram** | 14, 16, 20, 26 | Mermaid-rendered diagram as image + caption |
| **List/Bullets** | 12, 27 | Numbered cards or icon list |

### Asset Map (all local, no fetching needed)

| Asset | Path | Used On |
|-------|------|---------|
| Figma background SVG | `assets/From-Figma/PowerPoint-Slides-Background-Final.svg` | All slides (or light variant) |
| Light background SVG | `assets/From-Figma/light-background-with-shapes.svg` | Content slides alternative |
| eSided logo SVG | `assets/From-Figma/eSided-Original-Logo.svg` | Every slide (top-left) |
| eSided "e" mark SVG | `assets/From-Figma/eSided-e-only-of-logo.svg` | Subtle badge on content slides |
| Title illustration SVG | `assets/From-Figma/esided-Title-Slide-Illustration.svg` | Slides 1, 28 |
| Team headshots (SVG) | `assets/From-Figma/Zak-Ali-SVG-Gray-Scale.svg`, `Dr-Kamran-Malik-SVG.svg`, `Humaira-Waqas.svg`, `Olga-Skeen.svg` | Team slide |
| undraw illustrations (PNG) | `assets/illustrations/concepts/undraw_*.png` | 13 content slides (see outline for mapping) |
| Historical images | Generate via Ideogram or source from Unsplash | Slides 2-5 (harvest, combine, switchboard, phone) |

### CDN Libraries (for HTML validation UI + charts)

```
Chart.js      — https://cdn.jsdelivr.net/npm/chart.js (slides 7, 13, 18)
Mermaid       — https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js (slides 14, 16, 20, 26)
html2canvas   — https://cdn.jsdelivr.net/npm/html2canvas (export, if needed)
Google Fonts  — Inter + Playfair Display
```

### Build Workflow (for new Claude session)

**Step 0 — Read this file + outline.md. That's all the context you need.**

**Step 1 — Create `index.html` validation UI**
- Grid of slide thumbnails (scaled-down iframes or img tags)
- Click to open full 1920×1080 in new tab
- Shows 3 slides per row, all slides on one page
- No build tools — single HTML file with inline CSS/JS

**Step 2 — Build slides in batches of 3**
- Create each slide as `NN-slug.html` in `presentations/2026-02-live-event/html-slides/`
- Each file: self-contained, 1920×1080, Google Fonts CDN, Figma bg via relative path
- Follow Tetris layout reasoning for complex slides
- Use `object-fit: cover` for photo slides, CSS Grid for multi-section slides
- Font floor: 24pt body text minimum (viewed at distance)
- Present batch to user for validation before next batch

**Step 3 — Iterate per user feedback**
- Fix individual slides as directed
- Never batch more than 3 at a time
- Mark validated slides in this progress log

**Step 4 — Export to PNG (after all slides validated)**
- Use Puppeteer or playwright to screenshot each HTML at 1920×1080
- Alternative: `npx @resvg/resvg-cli` for SVG-only slides
- Output to `presentations/2026-02-live-event/output/`

**Step 5 — Assemble PowerPoint**
- Insert PNGs as full-slide images via PptxGenJS or manual
- Add speaker notes from outline.md

### Slide-by-Slide Checklist

| # | Slug | Type | Key Visual | Status |
|---|------|------|-----------|--------|
| 1 | title | Title | Figma illustration | **DONE** |
| 2 | harvest-1800s | Photo+Text | Sepia gradient placeholder | **DONE** (needs real photo) |
| 3 | combine-harvester | Photo+Text | Green gradient placeholder | **DONE** (needs real photo) |
| 4 | switchboard-operators | Photo+Text | Indigo gradient placeholder | **DONE** (needs real photo) |
| 5 | direct-dial | Photo+Text | Steel-blue gradient placeholder | **DONE** (needs real photo) |
| 6 | todays-reality | Illust+Text | undraw_in_the_office | **DONE** |
| 7 | million-dollar-bottleneck | Stat Cards | 3 white cards, border-top accent | **DONE** |
| 8 | tool-trap | Illust+Text | undraw_creative_woman | **DONE** |
| 9 | what-if-reframe | Centered Transition | No illustration, centered text | **DONE** |
| 10 | workers-vs-tools | Card Columns | Side-by-side cards (not table) | **DONE** |
| 11 | meet-meridian | Illust+Text | undraw_team_collaboration | **DONE** |
| 12 | five-ai-workers | Numbered Cards | 5 worker cards, vertically centered | **DONE** |
| 13 | the-numbers | Stat Cards | 3 metric cards + payback bar | **DONE** |
| 14 | invoice-processor | Workflow+Stats | CSS dot-line workflow + stat cards | **DONE** |
| 15 | what-really-changed | Illust+Text | undraw_our_solution | **DONE** |
| 16 | three-autonomy-modes | Mode Cards | 3 color-coded cards | **DONE** |
| 17 | what-happened-humans | Illust+Text | undraw_startup_life | **DONE** |
| 18 | compounding-effect | Period Cards | 3 cards with CSS bar charts | **DONE** |
| 19 | real-asset | Illust+Text | undraw_building_blocks | **DONE** |
| 20 | capital-lens | Card Spectrum | Two-card centered layout | **DONE** |
| 21 | scar-tissue-test | Illust+Text | undraw_interview | **DONE** |
| 22 | meridian-examples | Numbered Cards | 3 example cards with $ values | **DONE** |
| 23 | ai-changing-fast | Illust+Text | undraw_swipe_options | **DONE** |
| 24 | asset-isnt-model | Illust+Text | undraw_live_collaboration | **DONE** |
| 25 | like-hiring | Illust+Text | undraw_team_spirit | **DONE** |
| 26 | two-paths | Card Columns | Two path cards | **DONE** |
| 27 | getting-started | Numbered Cards | 4 step cards + illustration | **DONE** |
| 28 | closing-question | Closing | Logo top-center, contact info | **DONE** |

### Historical Images Still Needed (Slides 2-5)
These are NOT in the asset folders yet. Options:
- Generate via Ideogram (user has access)
- Source from Unsplash/Pexels (free, high-res)
- Use placeholder text-heavy layouts until images sourced

### Key Rules for Future Claude Session
1. **Read WAYFORWARD.md + outline.md first** — all context is here
2. **3 slides at a time max** — user validates each batch
3. **SVG-first** — always use `assets/From-Figma/` SVGs (logo, illustration, backgrounds, headshots). Never use old PNGs from `assets-local/` — those are pre-Figma exports and superseded
4. **Font floor 24pt** for body text (in-person viewing)
5. **No html2canvas** — use Playwright for PNG export (solved the gray background issue)
6. **Tetris layout** for complex slides — measure, pair, assign, don't shrink
7. **index.html validation UI first** — user needs to see all slides at a glance
8. **All paths relative** from html-slides/ folder
9. **Slide toolbar** — `shared/slide-toolbar.js` auto-injects nav (prev/next/index) + PNG export. Skips in iframes. Add `<script src="../shared/slide-toolbar.js"></script>` to every slide.
10. **Speaker notes format** — WHY this slide / SAY what / DELIVER how. Not just script. Coaching notes for rehearsal.

---

### 2026-02-14 — Session 2: Full Deck Build + PowerPoint Export

**All 28 slides built and validated in batches of 3-6.**

**Key decisions:**
- Used `light-background-with-shapes.svg` as standard content slide bg
- Title slide has NO background SVG (logo conflict with hex patterns)
- Closing slide uses logo top-center instead of top-left
- All slides use `brand.css` shared stylesheet + per-slide `<style>` overrides
- Accent bar hidden on all new slides (`.accent-bar { display: none; }`)
- Historical images (slides 2-5) use gradient placeholders pending real photos

**Validation UI:**
- `index.html` — 3-per-row centered grid, click to navigate (same tab)
- `shared/slide-toolbar.js` — prev/next/index nav + PNG export on every slide
- Python HTTP server on port 8080 for local preview

**Export pipeline (SOLVED — no more html2canvas):**
1. `render_slides.py` — Playwright, single browser instance, 1920x1080 @ 1x scale
   - Removes toolbar before screenshot: `page.evaluate("document.getElementById('slide-toolbar')?.remove()")`
   - Output: `html-slides/output/*.png`
2. `assemble_pptx.py` — python-pptx, 13.333" x 7.5" (16:9), speaker notes from dict
   - Output: `output/AI-Workforce-Deck.pptx`
   - Speaker notes format: WHY / SAY / DELIVER coaching structure

**Scar tissue added (#5-9):**
- Logo zone conflict (top-left 120x350px)
- No solid-color highlight cards (use border-top accent)
- Transition slides = centered, no illustration
- Tables don't work on slides (use card columns)
- Purple is not a brand color for content

**Remaining work:**
- Historical images for slides 2-5 (gradient placeholders currently)
- Remove old `02-team.png` and `03-chart.png` from output (pre-existing slides)
- Final visual QA pass in PowerPoint Presenter View
- Background swap exploration (one-line change per slide if needed)
