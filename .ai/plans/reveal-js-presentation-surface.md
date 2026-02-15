# Reveal.js Presentation Surface — Plan

## Goal

Add a reveal.js-based presentation mode alongside the existing PPTX export pipeline. Author once in HTML, present live from browser (with clicker), export to PPTX when needed.

## Current State

- 35 individual HTML slide files in `presentations/2026-02-live-event/html-slides/slides/`
- Each slide is self-contained HTML with shared `styles/brand.css`
- `index.html` is a 3-per-row validation grid (QA only, not presentable)
- PPTX pipeline: Playwright → PNGs → python-pptx assembly

## Tasks

### 1. Add reveal.js to the pipeline

- Add reveal.js as a dependency (CDN or vendored into the project)
- Create `present.html` alongside `index.html` — same slide folder, different surface
- `index.html` stays as the QA grid, `present.html` is the live presentation

### 2. Adapt slide HTML to reveal.js sections

- Each of the 35 `.html` slide files needs to be embedded as `<section>` blocks inside reveal.js
- Options:
  - **Build script** that reads `slides/*.html` and assembles `present.html` (keeps single-file authoring)
  - **Iframes** — reveal.js sections loading each slide via iframe (preserves isolation, may have sizing quirks)
  - **Inline** — concatenate slide content directly into sections (simplest, may need CSS scoping)
- Recommend: **build script** — Claude Code generates `present.html` from the slide folder, same as it generates the PPTX

### 3. Map speaker notes

- Speaker notes already exist in `slide-content-v3.md` and are used by `assemble_pptx.py`
- Reveal.js supports `<aside class="notes">` inside each `<section>`
- Build script should inject notes into each section from the same source
- Presenter view: `present.html?presenter` shows notes on speaker screen

### 4. Clicker + keyboard nav

- Reveal.js handles this natively (arrow keys, Page Up/Down, spacebar)
- Standard clickers send these key events — zero config needed
- Test with actual clicker before the event

### 5. Preserve the PPTX pipeline

- Nothing changes: `render_slides.py` + `assemble_pptx.py` still work from individual slide files
- Two outputs from one source: `present.html` (live) + `.pptx` (handout/fallback)

### 6. Offline capability

- Vendor reveal.js locally (don't rely on CDN at live events)
- Ensure `file://` works or use `python -m http.server` as fallback
- Test: airplane mode, open present.html, click through all 35 slides

## Architecture After

```
slides/*.html (source of truth — 35 files)
    ├─→ index.html        (QA validation grid, unchanged)
    ├─→ present.html      (reveal.js live presentation, NEW)
    │     ├── clicker/keyboard nav
    │     ├── speaker notes (presenter view)
    │     └── offline-capable
    └─→ output/*.pptx     (PPTX export, unchanged)
```

## Not In Scope

- Replacing the slide authoring format (stays as individual HTML files)
- Changing the brand CSS or slide designs
- Migrating away from PPTX (keep as parallel output)

## When to Execute

- Open Presentations in its own VS Code session
- Claude Code reads this plan + `.ai/INDEX.md` and executes
