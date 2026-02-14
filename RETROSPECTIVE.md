# Retrospective: HTML → PNG → PowerPoint Workflow

## The Proven Workflow

**HTML (1920×1080) → Playwright screenshot → python-pptx assembly with speaker notes**

> **UPDATE 2026-02-14:** Resolution upgraded to 1920×1080 (Full HD native). Export solved via Playwright (no more html2canvas gray background). Full 28-slide deck built and exported.

This workflow works because:
- ✅ Full CSS/Grid/Flexbox control for layouts
- ✅ All CDN tools available (Chart.js, Mermaid, Google Fonts, icons)
- ✅ Edit in VS Code (version control, find/replace, multi-cursor)
- ✅ Browser preview = validation layer (what you see is what you get)
- ✅ Professional-grade output with full design control

---

## What We Built Successfully

### 1. **CDN Arsenal** (Reference: `.ai/reference/CDN-ARSENAL-KB.md`)
**Available and READY to use:**
- **Chart.js (via QuickChart.io)** - Advanced chart configurations
- **Mermaid.js** - Text-to-diagram for flowcharts, sequences, Gantt charts
- **Font Awesome / Bootstrap Icons / Remix Icons** - 2000+ professional icons
- **Google Fonts** - Inter, Poppins, Playfair Display, Fira Code, Roboto Mono, Caveat
- **Ideogram API** - AI-generated images for custom needs
- **Unsplash / Pexels APIs** - Professional curated photos
- **QuickChart** - Chart.js configs → instant PNG charts
- **DiceBear API** - Consistent avatar generation

### 2. **Professional Illustrations** (Downloaded via Figma)
**Located in `assets/illustrations/concepts/`:**
- 29 unDraw illustrations (professional, brand-colorable SVGs)
- DrawKit creativity/design illustrations
- Clean, modern aesthetic
- **Use these FIRST before generating new images**

### 3. **Team Assets** (`assets/team/headshots/` and `assets-local/Team-Pictures/`)
- Professional headshots: Zak Ali, Olga Skeen, Dr. Kamran Malik, Dr. Humaira Waqas
- Title slide illustration (`Title-Slide-Illustration.png`)
- Global team theme with world map, brand colors

### 4. **Design System**
**Established in `design-system.css`:**
- Typography hierarchy (Inter + Playfair Display)
- Brand color palette (#0078d4 blue, #8764b8 purple)
- Spacing system (8px base)
- Reusable layout utilities

---

## PNG Export: SOLVED (Playwright)

### The Old Problem (html2canvas — now abandoned)
html2canvas rendered gray backgrounds instead of white. Tried 6 fixes, all failed. Root cause: html2canvas composites against default canvas color instead of capturing actual CSS backgrounds.

### The Solution: Playwright Screenshots
**`pip install playwright && playwright install chromium`**

Playwright launches a real Chromium browser, navigates to each HTML file, and takes a pixel-perfect screenshot. No CSS rendering quirks, no gray backgrounds, no library issues.

**Key implementation details:**
- Single browser instance for all slides (fast — ~30 slides in seconds)
- `page.wait_for_load_state("networkidle")` ensures fonts/images load
- `page.evaluate("document.getElementById('slide-toolbar')?.remove()")` strips dev toolbar before capture
- `device_scale_factor=1` for native 1920×1080 (not 2x — keeps file sizes reasonable for pptx)
- `full_page=False` captures viewport only (exactly 1920×1080)

**Files:**
- `html-slides/render_slides.py` — Playwright renderer
- `html-slides/assemble_pptx.py` — python-pptx assembler with speaker notes

### Dependencies
```
pip install playwright python-pptx Pillow
playwright install chromium
```

---

## What Works Perfectly

### ✅ HTML Slide Design (PROVEN)
- **1280×720px fixed canvas** - perfect 16:9 ratio
- **CSS Grid/Flexbox layouts** - modern, flexible, Tetris-based
- **Google Fonts integration** - Inter, Playfair Display loaded via CDN
- **Decorative shapes** - Blue/purple ovals with blur/opacity for visual interest
- **Brand consistency** - Logo, footer, colors all correct
- **Professional typography** - Proper hierarchy (72pt titles, 24pt+ body)

### ✅ Content Integration (PROVEN)
- **Team photos** - Professional headshots load correctly
- **Illustrations** - SVG/PNG illustrations render beautifully
- **Icons** - Font Awesome, Bootstrap Icons, Remix Icons all work
- **Layout principles** - Tetris layout (rearrange pieces, don't shrink fonts)

### ✅ Browser Preview (PROVEN)
- **Live editing** - Change HTML/CSS, refresh browser, see changes
- **Validation layer** - What you see in browser IS the final design
- **Black background** - Slide stands out clearly against black body
- **Box shadow** - Visual boundary shows exact 1280×720 dimensions
- **Export button** - One-click PNG export works

---

## Professional Design Principles (VALIDATED)

### Typography Hierarchy
```
Hero/Title:   Playfair Display Bold 72pt (#323130 dark gray)
Subtitle:     Inter SemiBold 36pt (#0078d4 brand blue)
Section Head: Inter Bold 32pt (#323130)
Body:         Inter Regular 24pt (#323130) ← MINIMUM for slides
Caption:      Inter Regular 18pt (#8e8e93)
Code/Data:    Fira Code Regular 20-24pt
```

**Critical insight:** 24pt minimum for body text on slides (viewed from distance), NOT 12-16pt like resumes (viewed at arm's length).

### Brand Color Palette
```css
Primary Blue:    #0078d4  /* Headings, CTAs, brand elements */
Accent Purple:   #8764b8  /* Decorative shapes, highlights */
Dark Gray:       #323130  /* Body text */
Light Gray:      #f3f2f1  /* Backgrounds, subtle accents */
Success Green:   #107c10  /* Positive data, growth */
White:           #ffffff  /* Slide background */
```

### Layout Principles (Tetris, Not Shrinking)
**Core principle:** When content doesn't fit, REARRANGE pieces (match by height, assign by width). NEVER shrink fonts below minimums.

**Two-dimension rule:**
- **Height (vertical):** Match pieces by height to avoid dead space
  - Tall + Tall = ✓ Balanced
  - Short + Short = ✓ Balanced
  - Tall + Short = ✗ Dead space
- **Width (horizontal):** Match width-hungry content to wider columns
  - Pills/tags = width-hungry → wider column
  - Text lines = width-indifferent → narrower column

**Reference:** `.ai/lessons-from-other-resources.md` (comprehensive Tetris layout guide)

### Chart Design (QuickChart.io)
**CRITICAL: Charts must be READABLE at distance**
- Data labels: 28pt minimum, bold, high contrast
- Axis labels: 22pt minimum
- Chart title: 32pt minimum
- Add generous padding: `layout.padding: {top: 40, left/right/bottom: 20}`
- Use annotations for insights: `plugins.annotation`
- Format values: `formatter: (value) => '$' + value + 'K'`
- Custom colors: Use brand palette, not defaults
- Gallery: https://quickchart.io/gallery/

### Mermaid Diagrams
- Keep simple (max 10 nodes per diagram)
- Use custom colors via `style` directives
- Export at 1200px width minimum for clarity
- Descriptive labels (no abbreviations)
- Types: flowchart, sequence, gantt, class, ER

---

## Asset Management (PROVEN)

### Critical Rule: Assets First, Generation Second
**ALWAYS check existing assets before generating new ones:**
1. `assets/illustrations/concepts/` - 29 unDraw + DrawKit illustrations
2. `assets/brand/logos/` - eSided logo + 200+ Remix Icons brand logos
3. `assets/team/headshots/` - Team photos
4. `presentations/*/assets-local/` - Project-specific professional assets
5. Previous presentations for style consistency

**Never generate from scratch what already exists professionally.**

### File Structure (PROVEN)
```
assets/
├── brand/logos/           # Company logo + partner brand logos
├── team/headshots/        # Professional team photos
├── illustrations/
│   └── concepts/          # unDraw + DrawKit (29 illustrations)
└── templates/backgrounds/ # Branded slide backgrounds

presentations/YYYY-MM-event/
├── assets-local/          # PROJECT-SPECIFIC professional assets
│   ├── Team-Pictures/     # Event-specific team photos
│   └── Title-Slide-Illustration.png  # Professional hero images
├── content/outline.md     # Slide-by-slide content plan
├── slides/                # HTML slide files
│   ├── design-system.css  # Design tokens
│   ├── 01-title.html      # Individual HTML slides
│   ├── 02-problem.html
│   └── ...
├── output/                # PNG exports + final .pptx
│   ├── 01-title.png       # PNG exports
│   ├── 02-problem.png
│   └── final.pptx         # PowerPoint with PNGs inserted
```

---

## Lessons Learned

### What Works
1. **HTML → PNG → PowerPoint workflow is proven** (just PNG export color issue to solve)
2. **CSS Grid/Flexbox for layouts** - modern, flexible, professional
3. **CDN arsenal** - All tools work perfectly (fonts, icons, charts, diagrams)
4. **Browser preview as validation** - What you see IS what you get
5. **Design-system.css** - Reusable tokens for consistency
6. **Tetris layout principle** - Rearrange pieces, don't shrink fonts
7. **Professional assets first** - Use existing illustrations/photos before generating
8. **Typography hierarchy** - 24pt minimum body text for slides

### What Needs Work
1. ~~**PNG export background color**~~ — **SOLVED** via Playwright (Session 2)
2. ~~**Batch export workflow**~~ — **SOLVED** via render_slides.py + assemble_pptx.py (Session 2)
3. **Historical images for slides 2-5** — using gradient placeholders, need real photos (Ideogram or Unsplash)

### Critical Insights
1. **Slides ≠ Resumes** - Different viewing distance = different font size minimums
2. **Library choice matters** - html2canvas works but has limitations, need alternatives
3. **ES modules in browser** - modern-screenshot failed due to import issues
4. **Traditional script loading** - More reliable than ES modules for now
5. **Validation layer is key** - HTML preview must match PNG export EXACTLY

---

## Next Steps (For Future Work)

### Immediate Priorities
1. ~~**Solve PNG export background**~~ — DONE (Playwright)
2. ~~**Batch export script**~~ — DONE (render_slides.py + assemble_pptx.py)
3. **Historical photos for slides 2-5** — Ideogram or Unsplash, replace gradient placeholders
4. **Background swap exploration** — one-line change per slide if a better bg is chosen
5. **Final QA pass** — open .pptx in Presenter View, check all 28 speaker notes

### Future Enhancements
1. **Animation workflow** — Add transitions via PowerPoint XML injection
2. **Template library** — Reusable slide templates for common card/column patterns
3. **Background variants** — swap `light-background-with-shapes.svg` for alternatives per-slide or globally
4. **Slide toolbar enhancements** — slide timer, rehearsal mode, annotation overlay

---

## Key Takeaway

**The HTML → Playwright → PowerPoint workflow is PROVEN and COMPLETE.**

Full pipeline, end to end:
1. Design slides as self-contained HTML (1920×1080, CSS Grid/Flexbox, Google Fonts CDN)
2. Preview in browser via `index.html` validation UI + `shared/slide-toolbar.js`
3. Iterate per user feedback (3 slides at a time)
4. `python render_slides.py` — Playwright screenshots all slides to PNG
5. `python assemble_pptx.py` — python-pptx assembles PNGs + speaker notes into .pptx
6. Open in PowerPoint Presenter View to rehearse with coaching notes

**No gray backgrounds. No html2canvas. No build tools. No dependencies beyond Python + Playwright.**

---

## Session 2 Learnings (2026-02-14)

### What Worked
- **Batches of 3-6 slides** with user feedback between — caught issues early
- **Shared brand.css + per-slide overrides** — consistency without rigidity
- **Scar tissue documentation** — writing down what broke prevented repeating it
- **Card-based layouts over tables** — more readable at presentation distance
- **Centered transitions over split layouts** — whitespace is the design on pivot slides
- **Single Playwright instance** — fast rendering (30 slides in seconds vs per-slide browsers)
- **WHY/SAY/DELIVER speaker notes** — much more useful than just a script

### What to Improve
- **Start with scar tissue list** — read it BEFORE designing, not after making the same mistake
- **Test real PowerPoint export earlier** — don't wait until all 28 slides are done
- **Historical images** — should have sourced these in parallel while building slides
- **Old slides in output** — `02-team.html` and `03-chart.html` from Session 1 slipped into the PNG output; clean these up before final delivery
