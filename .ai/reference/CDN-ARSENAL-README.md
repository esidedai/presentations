# CDN Arsenal — README

## What This Is

**`CDN-ARSENAL-KB.md`** is the single, definitive reference for every design asset available in this project. It replaces three previous files that had overlapping content:

| Old File | Status | What Happened |
|----------|--------|---------------|
| `CDN-and-Librarries-Arsemal-KB.md` | **Retired** | Foundation of the merge — its depth, gotchas, recipes, and DiceBear section are all preserved |
| `CDN-ARSENAL-GOLD-STANDARD.md` | **Retired** | Its 21 additional libraries, Creative Concepts, Combination Stacks, and Teaching Goal matrix were merged in |
| `CDN-ASSETS-README.md` | **Retired** | Was a strict subset — added nothing unique. Fully covered by the merged file |

**Keep only `CDN-ARSENAL-KB.md`.** Delete the other three.

---

## What's In It

The KB covers **35+ CDN libraries and tools** across these categories:

| Category | Libraries |
|----------|-----------|
| **Icons** (5) | Font Awesome, Bootstrap Icons, Lucide, Unicons, LineIcons |
| **Typography** (6 fonts) | Inter, Poppins, Playfair Display, Caveat, Fira Code, Roboto Mono |
| **Animation** | Animate.css, Hover.css, GSAP + ScrollTrigger, AOS, Vivus.js |
| **Graphics** | Rough.js, Lottie, DiceBear Avatars, Inline SVG Patterns |
| **Illustrations** | unDraw, Open Doodles |
| **Data Viz** | Chart.js, D3.js, Mermaid, Plotly |
| **STEM/Code** | KaTeX, Prism.js, Highlight.js |
| **Physics/Simulation** | Matter.js, P5.js |
| **Canvas** | Fabric.js, Konva.js |
| **Micro-Interactions** | Typed.js, CountUp.js, tsParticles |
| **Presentation** | Reveal.js, ScrollMagic |
| **Audio** | Howler.js, Tone.js |
| **3D** | Three.js |
| **Export** | html2canvas, PptxGenJS, Marked.js |

Plus:
- **12 Creative Concepts** for teaching AI agent collaboration (with tool mappings and wireframes)
- **5 Named Combination Stacks** (Explainer, Dashboard, Interactive Demo, Story, Technical Tutorial)
- **Teaching Goal → Tool matrix** for pedagogical content
- **6 complete HTML recipes** (hero sections, stat cards, social banners, diagrams)
- **Lessons Learned** (performance tips, CDN reliability, library gotchas)
- **Color palette** with light and dark mode variables

---

## How to Use It

**For LLMs / AI agents:** Point the agent at `CDN-ARSENAL-KB.md` as context. It contains every CDN link, usage example, and decision guide needed to build visually rich HTML pages without any build tooling.

**For humans:** Use the Quick Decision Guide (Section 1) to find the right tool, then jump to that section for CDN links and copy-paste code.

**For Claude Code / programmatic PowerPoint:** This KB covers the HTML/CSS/JS side. For the python-pptx and PptxGenJS programmatic pipeline, see the separate Perplexity research document.

---

## Philosophy

> Never install, never build, never bundle. Every visual asset loads from a URL or lives as a local file. If an `<img>` tag or `<script>` tag can do it, that's how we do it.

---

*Last updated: February 2026*
