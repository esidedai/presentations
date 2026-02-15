# Quick Reference

**Last updated:** 2026-02-15

## Current State

- **35 slides** — v3 deck ("Building Your AI Workforce: What's Actually Working")
- **Event:** Kehr Technologies, 5360 Legacy Dr, Feb 19 2026, 9:30-11:00am CST
- **Slides 2-4** use gradient placeholders (need real historical photos)
- **Output:** `presentations/2026-02-live-event/output/AI-Workforce-Deck.pptx`

## Content Sources

| File | What |
|------|------|
| `.scratch/Content-Files/slide-content-v3.md` | 35-slide content (source of truth) |
| `.scratch/Content-Files/presentation-script-v3.md` | Full verbatim speaking script |
| `.scratch/Content-Files/demo-narration-v3.md` | Live demo walkthrough (9-12 min) |
| `presentations/2026-02-live-event/content/outline.md` | OLD v2 outline (28 slides, superseded) |

## Key Paths

```
presentations/2026-02-live-event/html-slides/
├── slides/              # 35 HTML slide files (01-title.html ... 35-qa.html)
├── styles/brand.css     # Shared CSS variables + layout utilities
├── shared/slide-toolbar.js  # Nav + PNG export toolbar
├── index.html           # 3-per-row validation grid
├── render_slides.py     # Playwright → PNGs
├── assemble_pptx.py     # PNGs + speaker notes → .pptx
└── output/              # Rendered PNGs

assets/From-Figma/       # SVG source assets (logo, bg, illustration, badge)
```

## Brand

- **Fonts:** Inter + Playfair Display (Google CDN)
- **Colors:** `--brand-blue: #0078d4` | `--dark-gray: #323130` | `--success-green: #107c10`
- **Logo:** `assets/From-Figma/eSided-Original-Logo.svg`
- **Background:** `assets/From-Figma/light-background-with-shapes.svg` (content slides)
- **Badge:** `assets/From-Figma/eSided-e-only-of-logo.svg` (bottom-right, 8% opacity)
- **24pt minimum** body text

## Export Pipeline

```bash
cd presentations/2026-02-live-event/html-slides
python render_slides.py     # Playwright → PNGs (35/35)
python assemble_pptx.py     # PNGs + speaker notes → .pptx (35 with notes)
```

Dependencies: `pip install playwright python-pptx Pillow && playwright install chromium`

## Slide Template Types

| Type | Example Slides | Pattern |
|------|---------------|---------|
| Title | 01, 35 | No bg SVG, logo top-left, illustration right |
| Photo+Text | 02, 03, 04 | 55/45 grid, gradient image panel, era label |
| Centered transition | 05-08, 10-11, 14, 16, 32-34 | Flexbox center, whitespace is the design |
| Text+list | 09, 15, 19, 23, 31 | Left-aligned with structured points |
| Two-column | 12, 18 | Card columns side-by-side |
| Three-card | 20, 26, 30 | 3-col grid with border-top accents |
| Numbered cards | 17, 29 | Vertical stack with number+content |
| Custom visual | 21, 22, 24, 27, 28 | One-off layouts (spectrum, timeline, bars, grid) |

## Git

- **main** branch only, push directly
- `git push origin main`
