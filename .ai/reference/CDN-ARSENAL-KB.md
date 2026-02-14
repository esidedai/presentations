# CDN Design Assets Arsenal — Complete Reference

> **Purpose:** This is the project's design asset library and living reference. Use it to build visually rich demos, blog posts, social media banners, landing pages, interactive explainers, educational content, and scroll-stopping visuals — all zero-build, CDN-only.
>
> **Live demo:** `/cD2nS4hW9k/` (no password)
>
> **Philosophy:** Never install, never build, never bundle. Every visual asset loads from a URL or lives as a local file. If an `<img>` tag or `<script>` tag can do it, that's how we do it.

---

## Table of Contents

1. [Quick Decision Guide](#quick-decision-guide)
2. [Quick Start — Copy-Paste Head Block](#quick-start)
3. [Icon Libraries (5)](#icon-libraries)
4. [Typography (6 Google Fonts)](#typography)
5. [Animation Libraries (CSS + JS)](#animation-libraries)
6. [DiceBear Avatars (URL-based, no JS)](#dicebear-avatars)
7. [Lottie Animations (JSON-based)](#lottie-animations)
8. [SVG Illustration Libraries](#svg-illustration-libraries)
9. [Inline SVG Patterns (zero CDN)](#inline-svg-patterns)
10. [Stock Photography](#stock-photography)
11. [Data Visualization](#data-visualization)
12. [STEM & Code Rendering](#stem-and-code-rendering)
13. [Physics & Simulation](#physics-and-simulation)
14. [Interactive Canvas](#interactive-canvas)
15. [Presentation & Scroll](#presentation-and-scroll)
16. [Micro-Interactions](#micro-interactions)
17. [Audio](#audio)
18. [3D & WebGL](#3d-and-webgl)
19. [Export Tools](#export-tools)
20. [Creative Concept Library: AI Agents as Coworkers](#creative-concepts)
21. [Combination Patterns (Named Stacks)](#combination-patterns)
22. [Asset Selection by Teaching Goal](#asset-selection-by-teaching-goal)
23. [Recipes — Common Visual Patterns](#recipes)
24. [Lessons Learned](#lessons-learned)
25. [Complete CDN Reference](#complete-cdn-reference)
26. [File Structure](#file-structure)

---

<a name="quick-decision-guide"></a>
## 1. Quick Decision Guide

| Need | Recommended Asset |
|------|-------------------|
| Professional icons | Font Awesome 6 or Bootstrap Icons |
| Modern line icons (React-friendly) | Lucide Icons |
| Animated feedback (success, loading) | Lottie animations |
| Friendly illustrations (people) | Open Doodles SVGs |
| Tech/business illustrations | unDraw SVGs |
| Hero typography | Playfair Display + Inter |
| Handwriting / casual feel | Caveat font |
| Code/monospace text | Fira Code or Roboto Mono |
| Entrance animations | Animate.css |
| Complex sequenced animation | GSAP + ScrollTrigger |
| Scroll-triggered reveals | AOS |
| Hover effects | Hover.css |
| Hand-drawn aesthetic | Rough.js |
| SVG line-drawing animation | Vivus.js |
| Stock photography | Local Unsplash/Pexels files |
| Data dashboards | Chart.js |
| Process flows / diagrams | Mermaid |
| Custom data visualizations | D3.js |
| Scientific / 3D plots | Plotly |
| Math equations | KaTeX |
| Code syntax highlighting | Prism.js |
| Typewriter / AI typing effect | Typed.js |
| Animated number counters | CountUp.js |
| Physics simulations | Matter.js |
| Creative coding / generative art | P5.js |
| Interactive whiteboard / drag-drop | Fabric.js or Konva.js |
| Particle backgrounds | tsParticles |
| Browser slide decks | Reveal.js |
| Scroll-driven storytelling | ScrollMagic |
| Sound effects / audio feedback | Howler.js |
| 3D experiences | Three.js |
| Screenshot DOM to PNG | html2canvas |
| Generate PowerPoint in browser | PptxGenJS |

---

<a name="quick-start"></a>
## 2. Quick Start — Copy-Paste Head Block

Paste this into any `<head>` to get every design asset available:

```html
<!-- Fonts (Inter, Poppins, Playfair Display, Fira Code, Roboto Mono, Caveat) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=Fira+Code:wght@400;600&family=Playfair+Display:wght@700;900&family=Roboto+Mono:wght@400;700&family=Poppins:wght@400;600;800&family=Caveat:wght@500;700&display=swap" rel="stylesheet">

<!-- Icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@iconscout/unicons@4.0.8/css/line.css">
<link href="https://cdn.lineicons.com/4.0/lineicons.css" rel="stylesheet">
<script src="https://unpkg.com/lucide@latest"></script>

<!-- CSS Animations -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/hover.css/2.3.1/css/hover-min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css">

<!-- JS Animation Engines -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/vivus/0.4.6/vivus.min.js"></script>

<!-- Graphics & Animation -->
<script src="https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.min.js"></script>
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>

<!-- Data Visualization -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<!-- STEM & Code -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>

<!-- Physics & Canvas -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/matter-js/0.19.0/matter.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.7.0/p5.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.3.1/fabric.min.js"></script>

<!-- Micro-Interactions -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/typed.js/2.0.16/typed.umd.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/countup.js/2.8.0/countUp.umd.js"></script>
<script src="https://cdn.jsdelivr.net/npm/tsparticles@2.12.0/tsparticles.bundle.min.js"></script>

<!-- Audio -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/howler/2.2.3/howler.min.js"></script>

<!-- 3D -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<!-- Presentation -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.js"></script>

<!-- Export Tools -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/pptxgenjs"></script>

<!-- Markdown Rendering -->
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
```

**Pick only what you need.** Don't load everything for a simple blog post. The sections below tell you which CDN tag to grab for each use case.

---

<a name="icon-libraries"></a>
## 3. Icon Libraries (5)

### Font Awesome 6.4 — The Default
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
```
- **2,000+ icons** in solid (`fas`), regular (`far`), and brand (`fab`) styles
- Usage: `<i class="fas fa-robot"></i>`, `<i class="far fa-envelope"></i>`, `<i class="fab fa-linkedin"></i>`
- Best for: General UI, social media icons, brand logos, navigation
- Browse: [fontawesome.com/icons](https://fontawesome.com/icons)

### Bootstrap Icons — Clean Alternative
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
```
- **2,000+ icons**, all line-style, consistent stroke width
- Usage: `<i class="bi bi-graph-up"></i>`, `<i class="bi bi-person-circle"></i>`
- Best for: Clean minimal UI, dashboards, data-heavy layouts
- Browse: [icons.getbootstrap.com](https://icons.getbootstrap.com)

### Lucide Icons — Modern & React-Friendly
```html
<script src="https://unpkg.com/lucide@latest"></script>
```
- **1,000+ icons**, consistent modern line style
- Usage: `<i data-lucide="check"></i>` then `<script>lucide.createIcons();</script>`
- Best for: Modern apps, React projects, consistent stroke-width aesthetic
- Browse: [lucide.dev](https://lucide.dev)

### Unicons — Thin & Modern
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@iconscout/unicons@4.0.8/css/line.css">
```
- **1,100+ icons**, thin line style
- Usage: `<i class="uil uil-chart-line"></i>`, `<i class="uil uil-envelope-alt"></i>`
- Best for: Modern SaaS feel, lightweight interfaces
- Browse: [iconscout.com/unicons](https://iconscout.com/unicons)

### LineIcons — Geometric & Elegant
```html
<link href="https://cdn.lineicons.com/4.0/lineicons.css" rel="stylesheet">
```
- **500+ icons**, geometric line style
- Usage: `<i class="lni lni-dashboard"></i>`, `<i class="lni lni-users"></i>`
- Best for: Elegant layouts, geometric design systems
- Browse: [lineicons.com](https://lineicons.com)

### When to Use Which

| Scenario | Pick This |
|----------|-----------|
| General-purpose, most variety | Font Awesome |
| Clean dashboard, data tables | Bootstrap Icons |
| Modern app, React codebase | Lucide |
| Modern SaaS marketing page | Unicons |
| Minimal elegant design | LineIcons |
| Need brand logos (LinkedIn, GitHub, etc.) | Font Awesome (only one with brands) |

---

<a name="typography"></a>
## 4. Typography (6 Google Fonts)

One tag loads all six:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=Fira+Code:wght@400;600&family=Playfair+Display:wght@700;900&family=Roboto+Mono:wght@400;700&family=Poppins:wght@400;600;800&family=Caveat:wght@500;700&display=swap" rel="stylesheet">
```

| Font | CSS | Personality | Use For |
|------|-----|-------------|---------|
| **Inter** | `font-family: 'Inter', sans-serif` | Clean, professional, neutral | Body text, UI labels, dashboards, forms |
| **Poppins** | `font-family: 'Poppins', sans-serif` | Friendly, geometric, modern | Headlines, marketing copy, CTAs, social banners |
| **Playfair Display** | `font-family: 'Playfair Display', serif` | Elegant, editorial, authoritative | Blog titles, hero headlines, pull quotes, luxury feel |
| **Caveat** | `font-family: 'Caveat', cursive` | Handwritten, casual, human | Annotations, sketchy labels, friendly callouts, "napkin" aesthetic |
| **Fira Code** | `font-family: 'Fira Code', monospace` | Technical, developer-oriented | Code snippets, data labels, metric values, terminal output |
| **Roboto Mono** | `font-family: 'Roboto Mono', monospace` | Clean monospace, dashboard feel | Timestamps, IDs, tabular numbers, status codes |

### Font Pairing Recipes

| Content Type | Headline | Body | Accent |
|-------------|----------|------|--------|
| Blog post | Playfair Display 700 | Inter 400 | Fira Code for inline code |
| SaaS landing page | Poppins 800 | Inter 400 | Poppins 600 for subheads |
| Dashboard | Inter 700 | Inter 400 | Roboto Mono for numbers |
| Social media banner | Poppins 800 | Poppins 600 | — |
| Technical article | Inter 700 | Inter 400 | Fira Code for everything code |
| Friendly / casual | Caveat 700 | Inter 400 | — |
| Educational explainer | Poppins 600 | Inter 400 | Fira Code + Caveat for annotations |

---

<a name="animation-libraries"></a>
## 5. Animation Libraries

### Animate.css — Drop-in CSS Animations
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
```

Add a class, get an animation. That's it.

**Usage:** `<div class="animate__animated animate__fadeInUp">Content</div>`

**Key entrance classes:**
- `animate__fadeIn` — Simple fade
- `animate__fadeInUp` — Fade + slide up (most versatile)
- `animate__fadeInLeft` / `animate__fadeInRight` — Slide from sides
- `animate__bounceIn` — Bouncy entrance
- `animate__zoomIn` — Scale up from small

**Key attention classes:**
- `animate__pulse` — Gentle pulse
- `animate__bounce` — Bouncing
- `animate__headShake` — Shake "no"
- `animate__heartBeat` — Heart beat effect

**Modifiers:**
- `animate__infinite` — Loop forever
- `animate__delay-1s` through `animate__delay-5s` — Built-in delays
- `style="animation-delay: 0.2s;"` — Custom delay for staggering

**Stagger pattern** (cards appearing one by one):
```html
<div class="animate__animated animate__fadeInUp" style="animation-delay: 0.1s;">Card 1</div>
<div class="animate__animated animate__fadeInUp" style="animation-delay: 0.2s;">Card 2</div>
<div class="animate__animated animate__fadeInUp" style="animation-delay: 0.3s;">Card 3</div>
```

### Hover.css — CSS Hover Effects
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/hover.css/2.3.1/css/hover-min.css">
```

Add a class, get a hover effect.

**Usage:** `<button class="hvr-grow">Hover me</button>`

**Key classes:**
- `hvr-grow` — Scale up slightly
- `hvr-shrink` — Scale down slightly
- `hvr-float` — Float upward
- `hvr-bob` — Gentle bobbing
- `hvr-pulse` — Pulsing glow
- `hvr-buzz` — Vibrate
- `hvr-sweep-to-right` — Background sweep
- `hvr-underline-from-left` — Underline animates in

### GSAP — Professional Timeline Animation
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
```

Industry-standard animation engine. Pixar-level control over timing, easing, sequencing.

**Basic usage:**
```javascript
gsap.to(".box", { x: 100, duration: 1, ease: "power2.out" });

// Timeline for sequencing
const tl = gsap.timeline();
tl.to(".step1", { opacity: 1, duration: 0.5 })
  .to(".step2", { opacity: 1, duration: 0.5 })
  .to(".step3", { opacity: 1, duration: 0.5 });

// Scroll-triggered
gsap.to(".hero", {
  scrollTrigger: { trigger: ".hero", start: "top center" },
  opacity: 1, y: 0, duration: 1
});
```

**Best for:** Complex sequenced animations, scroll-driven storytelling, professional motion, anything Animate.css can't handle
**When to use over Animate.css:** Multiple elements that need coordinated timing, scrubbing, or scroll-binding

### AOS — Animate on Scroll
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
```

Dead-simple scroll-triggered animations. One attribute per element.

**Usage:**
```html
<div data-aos="fade-up" data-aos-duration="1000">Animates when scrolled into view</div>
<div data-aos="fade-right" data-aos-delay="200">Staggered entrance</div>
<script>AOS.init();</script>
```

**Best for:** Landing pages, storytelling, progressive reveal
**When to use over GSAP:** Simpler pages where you just need "show on scroll" without timeline control

### Vivus.js — SVG Line Drawing
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/vivus/0.4.6/vivus.min.js"></script>
```

Makes SVGs "draw themselves" stroke by stroke.

**Usage:**
```javascript
new Vivus('my-svg', { duration: 200, type: 'oneByOne' });
```

**Best for:** Logo reveals, diagram "drawing itself", architectural blueprints, process flows that build visually

### Rough.js — Hand-Drawn Canvas Graphics
```html
<script src="https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.min.js"></script>
```

Draws shapes that look hand-sketched. ~9 KB. Great for humanizing technical content.

**Basic usage:**
```javascript
const canvas = document.getElementById('myCanvas');
const rc = rough.canvas(canvas);

rc.rectangle(10, 10, 200, 100, {
  roughness: 2,
  fill: '#ffd5c8',
  fillStyle: 'hachure',
  stroke: '#333',
  strokeWidth: 2
});

rc.circle(150, 60, 50, { roughness: 1.5, fill: '#e8f4fd' });
rc.line(10, 130, 200, 130, { roughness: 1, strokeWidth: 2 });
```

**Shapes:** `rectangle`, `circle`, `ellipse`, `line`, `polygon`, `arc`, `path`

**Fill styles:** `hachure` (sketch lines — default), `solid`, `zigzag`, `cross-hatch`, `dots`

**Key parameters:**
- `roughness` — 0 = perfectly clean, 1 = subtle sketch, 2+ = very rough
- `bowing` — How much lines curve (0 = straight, higher = more bowed)
- `fill` — Fill color hex
- `fillStyle` — How fill is drawn (hachure, solid, zigzag, cross-hatch, dots)
- `stroke` — Outline color
- `strokeWidth` — Outline thickness

**Pro tip:** Use `rc.path()` for complex shapes (SVG path syntax). Combine with standard canvas `ctx.fillText()` for labels.

**Pro tip 2:** Use **svg2roughjs** to convert any existing SVG into sketchy Rough.js style automatically.

**Best for:** "AI + human" visual metaphors, whiteboard-style diagrams, informal infographics, blog illustrations, explainer content

---

<a name="dicebear-avatars"></a>
## 6. DiceBear Avatars (URL-based, no JS needed)

Generate unique avatars with just an `<img>` tag. No library, no JavaScript, no API key.

**Base URL:** `https://api.dicebear.com/7.x/{style}/svg?seed={name}`

Change the seed, get a different avatar. Same seed always returns the same avatar (deterministic).

### Minimal / Abstract Styles

| Style | URL | Look |
|-------|-----|------|
| **Initials** | `initials/svg?seed=JD&backgroundColor=667eea` | Letters in colored circle |
| **Shapes** | `shapes/svg?seed=Alex` | Geometric patterns |
| **Identicon** | `identicon/svg?seed=Sam` | GitHub-style pixel grid |
| **Rings** | `rings/svg?seed=Taylor` | Concentric ring pattern |
| **Thumbs** | `thumbs/svg?seed=Jordan` | Simple cartoon face |

### Character Styles

| Style | URL | Look |
|-------|-----|------|
| **Bottts** | `bottts/svg?seed=Robot1` | Friendly robots |
| **Pixel Art** | `pixel-art/svg?seed=Gamer` | Retro 8-bit characters |
| **Fun Emoji** | `fun-emoji/svg?seed=Happy` | Expressive emoji faces |
| **Adventurer** | `adventurer/svg?seed=Hero` | RPG-style characters |
| **Croodles** | `croodles/svg?seed=Doodle` | Sketchy hand-drawn faces |

### Professional / Detailed Styles

| Style | URL | Look |
|-------|-----|------|
| **Avataaars** | `avataaars/svg?seed=Professional` | Full character with accessories |
| **Lorelei** | `lorelei/svg?seed=Artist` | Artistic line portraits |
| **Open Peeps** | `open-peeps/svg?seed=Creative` | Hand-drawn diverse characters |
| **Personas** | `personas/svg?seed=Designer` | Colorful diverse characters |
| **Notionists** | `notionists/svg?seed=Thinker` | Abstract head illustrations |

### Usage Examples

```html
<!-- Basic avatar -->
<img src="https://api.dicebear.com/7.x/avataaars/svg?seed=John" width="80" height="80">

<!-- With background color -->
<img src="https://api.dicebear.com/7.x/initials/svg?seed=JD&backgroundColor=667eea" width="80" height="80" style="border-radius: 50%;">

<!-- Rounded square -->
<img src="https://api.dicebear.com/7.x/bottts/svg?seed=MyBot" width="60" height="60" style="border-radius: 12px;">
```

**URL parameters:**
- `seed=Name` — Determines the unique avatar (required)
- `backgroundColor=hex` — Background color without `#` (e.g., `b6e3f4`)
- `radius=50` — Border radius (0-50, where 50 = circle)
- `size=200` — Output size in pixels

**Best for:** User profiles, team pages, comment avatars, placeholder people in demos, notification senders, AI worker personas

---

<a name="lottie-animations"></a>
## 7. Lottie Animations (JSON-based)

```html
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
```

Lightweight vector animations stored as JSON. 10x smaller than GIFs, infinitely scalable, customizable speed.

### Local Animations (in `assets/lottie/`)

| File | Size | What It Shows | Use For |
|------|------|---------------|---------|
| `success-check.json` | 25 KB | Animated green checkmark | Form submissions, approvals, task completion |
| `loading-spinner.json` | 11 KB | Smooth loading circle | Chat loading, data fetch, processing |
| `heart-pulse.json` | 60 KB | Pulsing heart | Engagement metrics, likes, health indicators |
| `rocket-launch.json` | 186 KB | Rocket lifting off | Launch announcements, growth, hero sections |
| `data-analytics.json` | 205 KB | Charts/graphs animating | Dashboards, analytics, data sections |
| `working-person.json` | 84 KB | Person at desk | About pages, "AI at work" visuals, team sections |

### Usage

```html
<!-- Basic: autoplay + loop -->
<lottie-player
  src="assets/lottie/success-check.json"
  background="transparent"
  speed="1"
  style="width: 80px; height: 80px;"
  loop autoplay>
</lottie-player>

<!-- From LottieFiles CDN (browse lottiefiles.com for URLs) -->
<lottie-player
  src="https://lottie.host/xxxxx/animation.json"
  background="transparent"
  speed="0.5"
  style="width: 200px; height: 200px;"
  loop autoplay>
</lottie-player>

<!-- Play only on hover -->
<lottie-player
  src="assets/lottie/rocket-launch.json"
  background="transparent"
  speed="1"
  style="width: 120px; height: 120px;"
  hover>
</lottie-player>
```

**Attributes:**
- `loop` — Repeat animation
- `autoplay` — Start immediately
- `hover` — Play only on hover
- `speed="0.5"` — Half speed (great for subtle background animations)
- `speed="2"` — Double speed
- `direction="-1"` — Play in reverse

**Finding more:** Browse **lottiefiles.com** — 100K+ free animations. Search by keyword, filter by category/color. Copy the JSON URL directly into `src`.

### Free Lottie Sources
- [LottieFiles](https://lottiefiles.com/) — Thousands of free animations
- [IconScout](https://iconscout.com/lottie-animations) — Curated collections

---

<a name="svg-illustration-libraries"></a>
## 8. SVG Illustration Libraries

### unDraw-Style Illustrations (in `assets/undraw/`)

Professional flat vector illustrations. Colors are editable — open the SVG, change `fill="#6c5ce7"` to any hex.

| File | Subject | Mood | Use For |
|------|---------|------|---------|
| `team-collaboration.svg` | Two people working together | Cooperative | Team pages, collaboration features |
| `programming.svg` | Person coding | Technical | Developer sections, tech content |
| `data-trends.svg` | Chart/graph visual | Analytical | Analytics, reporting, dashboards |
| `mobile-app.svg` | Phone screen | Modern | Mobile features, app showcase |
| `secure-files.svg` | Lock + documents | Trustworthy | Security, compliance, privacy |
| `website-builder.svg` | Browser mockup | Creative | Web dev, builder tools |

**Usage:**
```html
<img src="assets/undraw/team-collaboration.svg" alt="Team collaboration" style="width: 200px;">
```

**Customizing colors:** Open the SVG file, find `fill="#6c5ce7"` (or whatever the accent color is), and replace with your brand color. All unDraw illustrations use a single accent color that's easy to swap.

**Finding more:** Visit **undraw.co**, use the color picker to set your brand color, search by keyword, download SVG. Every illustration updates to your chosen color instantly.

### Open Doodles (in `assets/doodles/`)

Hand-drawn character illustrations. Black outlines with skin-tone fills. CC0 license — use anywhere, no attribution.

| File | Character Pose | Mood | Use For |
|------|---------------|------|---------|
| `sitting.svg` | Casual sitting | Relaxed | Landing pages, about sections |
| `reading.svg` | Reading a book | Thoughtful | Education, learning, blog posts |
| `coffee.svg` | Holding coffee | Friendly | Work/productivity, "about us" |
| `dancing.svg` | Dancing | Celebratory | Success states, celebrations |
| `meditating.svg` | Meditation | Calm | Wellness, mindfulness, focus |
| `loving.svg` | Heart gesture | Warm | Thank you pages, appreciation |

**Usage:**
```html
<img src="assets/doodles/coffee.svg" alt="Coffee break" style="width: 140px; height: 140px;">
```

**Style note:** These pair perfectly with Rough.js for a consistent hand-drawn aesthetic across your entire page.

**Finding more:** Visit **opendoodles.com** for the full collection.

---

<a name="inline-svg-patterns"></a>
## 9. Inline SVG Patterns (Zero CDN)

Write SVG directly in HTML. No CDN, no network request, no blocked assets. These patterns are demonstrated in the live demo.

### Status Indicators
```html
<!-- Success (green check) -->
<svg width="44" height="44" viewBox="0 0 48 48">
  <circle cx="24" cy="24" r="22" fill="#107c10"/>
  <path d="M14 24 L21 31 L34 18" stroke="white" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</svg>

<!-- Warning (amber exclamation) -->
<svg width="44" height="44" viewBox="0 0 48 48">
  <circle cx="24" cy="24" r="22" fill="#f7630c"/>
  <rect x="22" y="14" width="4" height="14" rx="2" fill="white"/>
  <circle cx="24" cy="33" r="2.5" fill="white"/>
</svg>

<!-- Error (red X) -->
<svg width="44" height="44" viewBox="0 0 48 48">
  <circle cx="24" cy="24" r="22" fill="#d13438"/>
  <path d="M16 16 L32 32 M32 16 L16 32" stroke="white" stroke-width="4" stroke-linecap="round"/>
</svg>

<!-- Info (blue i) -->
<svg width="44" height="44" viewBox="0 0 48 48">
  <circle cx="24" cy="24" r="22" fill="#0078d4"/>
  <circle cx="24" cy="15" r="2.5" fill="white"/>
  <rect x="22" y="20" width="4" height="14" rx="2" fill="white"/>
</svg>
```

### Circular Progress Gauge
```html
<svg width="70" height="70" viewBox="0 0 80 80">
  <circle cx="40" cy="40" r="32" fill="none" stroke="#e0e0e0" stroke-width="8"/>
  <circle cx="40" cy="40" r="32" fill="none" stroke="#0078d4" stroke-width="8"
    stroke-dasharray="201" stroke-dashoffset="50" stroke-linecap="round"
    transform="rotate(-90 40 40)"/>
  <text x="40" y="45" text-anchor="middle" font-family="Inter, sans-serif"
    font-size="14" font-weight="700" fill="#323130">75%</text>
</svg>
```
**Math:** `stroke-dasharray` = circumference (2 × π × r). `stroke-dashoffset` = unfilled portion. For 75%: offset = circumference × 0.25.

### AI Badge with Gradient
```html
<svg width="90" height="90" viewBox="0 0 90 90">
  <defs>
    <linearGradient id="aiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0078d4"/>
      <stop offset="100%" style="stop-color:#8764b8"/>
    </linearGradient>
  </defs>
  <circle cx="45" cy="45" r="38" fill="url(#aiGrad)"/>
  <circle cx="45" cy="45" r="30" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2"/>
  <text x="45" y="52" text-anchor="middle" font-family="Inter, sans-serif"
    font-size="22" font-weight="700" fill="white">AI</text>
</svg>
```

**Why inline SVG?**
- Never blocked by ad blockers or corporate firewalls
- Zero network round-trip — instant render
- Fully CSS/JS controllable (hover effects, color changes, animations)
- Scales perfectly at any resolution

---

<a name="stock-photography"></a>
## 10. Stock Photography

Curated photos in `assets/stock/` with full attribution in `metadata.json`.

### Unsplash (in `assets/stock/unsplash/`)

| File | Subject | Photographer | License |
|------|---------|-------------|---------|
| `business.jpg` | Group meeting | Mario Gogh | Free commercial use |
| `technology.jpg` | Calculator/tech | Bernd Dittrich | Free commercial use |
| `office.jpg` | Team with laptops | SEO Galaxy | Free commercial use |
| `nature.jpg` | Rock formation, water | Allyson Beaucourt | Free commercial use |
| `abstract.jpg` | Blue striped textile | Debora Pilati | Free commercial use |

### Pexels (in `assets/stock/pexels/`)

| File | Subject | Photographer | License |
|------|---------|-------------|---------|
| `business.jpg` | People handshaking | fauxels | Free commercial use |
| `technology.jpg` | Photography equipment | Caleb Oquendo | Free commercial use |
| `office.jpg` | Team overhead view | fauxels | Free commercial use |
| `nature.jpg` | Green field panoramic | Akos Szabo | Free commercial use |
| `abstract.jpg` | Minimalist curves | gdtography | Free commercial use |

**Attribution:** Always credit when possible. Full metadata (photographer name, URL, original link) in `assets/stock/metadata.json`.

**Finding more:** Search [unsplash.com](https://unsplash.com) or [pexels.com](https://www.pexels.com). Both are free for commercial use.

---

<a name="data-visualization"></a>
## 11. Data Visualization

### Chart.js — Standard Charts
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

**Usage:**
```javascript
new Chart(ctx, {
  type: 'bar', // line, pie, doughnut, radar, scatter, polar
  data: {
    labels: ['Jan', 'Feb', 'Mar'],
    datasets: [{ label: 'Sales', data: [12, 19, 3] }]
  }
});
```

**Best for:** Dashboards, reports, simple data stories
**Effort:** Lowest — just pass config object
**Docs:** [chartjs.org](https://www.chartjs.org/docs/)

### Mermaid.js — Diagrams from Text
```html
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
```

Write diagrams in plain text, Mermaid renders them as SVG.

```html
<pre class="mermaid">
graph LR
    A[User Request] --> B{AI Worker}
    B --> C[Autonomous Action]
    B --> D[Human Review]
    D --> E[Approved]
</pre>
<script>mermaid.initialize({ startOnLoad: true });</script>
```

**Diagram types:** flowcharts, sequence diagrams, Gantt charts, class diagrams, state diagrams, ER diagrams, mindmaps, user journeys, pie charts
**Best for:** Process documentation, architecture diagrams, workflows
**Effort:** Zero drawing — just describe relationships in text

### D3.js v7 — Custom SVG Visualizations
```html
<script src="https://d3js.org/d3.v7.min.js"></script>
```
Full control over SVG. Build funnels, treemaps, force-directed graphs, custom animated transitions.
**Best for:** Novel visualizations, data journalism, anything bindable to data
**Effort:** High — full control means full responsibility
**When to use:** When Chart.js or Mermaid can't do what you need

### Plotly — Scientific & 3D Charts
```html
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
```

**Usage:**
```javascript
Plotly.newPlot('chart', [{
  x: [1, 2, 3],
  y: [2, 6, 3],
  type: 'scatter'
}]);
```

**Best for:** 3D plots, scientific data, hover interactivity, export-friendly charts
**Effort:** Medium — more config than Chart.js, less than D3

---

<a name="stem-and-code-rendering"></a>
## 12. STEM & Code Rendering

### KaTeX — Math Equations
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
```

**Usage:**
```html
<p>The quadratic formula: $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$</p>
<script>renderMathInElement(document.body);</script>
```

**Best for:** Any STEM content — math, physics, chemistry, ML formulas
**Essential for:** AI/ML explainers (loss functions, gradients, attention formulas)

### Prism.js — Syntax Highlighting
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
```

**Usage:**
```html
<pre><code class="language-python">
def hello():
    print("Hello, World!")
</code></pre>
```

**Best for:** Code tutorials, documentation, technical blogs
**Themes:** `prism`, `prism-dark`, `prism-tomorrow`, `prism-okaidia`

### Highlight.js — Alternative Syntax Highlighting
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/github-dark.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
```

**Best for:** Auto-detection of language, broader language support
**When to use over Prism:** You don't know what language the code is, or need more obscure language support

---

<a name="physics-and-simulation"></a>
## 13. Physics & Simulation

### Matter.js — 2D Physics Engine
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/matter-js/0.19.0/matter.min.js"></script>
```

**Usage:**
```javascript
const engine = Matter.Engine.create();
const box = Matter.Bodies.rectangle(400, 200, 80, 80);
const ground = Matter.Bodies.rectangle(400, 610, 810, 60, { isStatic: true });
Matter.World.add(engine.world, [box, ground]);
Matter.Engine.run(engine);
```

**Best for:** Gravity simulations, collision demos, "tasks falling like Tetris" metaphors, capacity/overflow visualizations
**Teaching power:** Show abstract concepts physically (workload piling up, systems breaking under pressure)

### P5.js — Creative Coding
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.7.0/p5.min.js"></script>
```

**Usage:**
```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  ellipse(mouseX, mouseY, 50, 50);
}
```

**Best for:** Generative art, interactive simulations, creative visualizations
**Teaching power:** Neural network visualizations, particle systems, data art

---

<a name="interactive-canvas"></a>
## 14. Interactive Canvas

### Fabric.js — Object Manipulation
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.3.1/fabric.min.js"></script>
```

**Usage:**
```javascript
const canvas = new fabric.Canvas('c');
const rect = new fabric.Rect({ left: 100, top: 100, width: 50, height: 50, fill: 'red' });
canvas.add(rect);
// User can now drag, resize, rotate the rectangle
```

**Best for:** Whiteboard tools, drag-and-drop interfaces, image editors
**Teaching power:** "Drag tasks to the agent" interactions

### Konva.js — High-Performance Canvas
```html
<script src="https://cdn.jsdelivr.net/npm/konva@9.2.0/konva.min.js"></script>
```

**Best for:** High-performance canvas apps, games, complex layered graphics
**When to use over Fabric:** Need higher performance with many objects, or building game-like interfaces

---

<a name="presentation-and-scroll"></a>
## 15. Presentation & Scroll

### Reveal.js — Browser Slide Decks
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.js"></script>
```

**Best for:** Browser-based presentations, interactive slides, conference talks

### ScrollMagic — Scroll-Driven Scenes
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/ScrollMagic/2.0.8/ScrollMagic.min.js"></script>
```

**Best for:** Scroll-driven storytelling, pinned sections, progress indicators
**Pairs with:** GSAP for animation within scroll scenes

---

<a name="micro-interactions"></a>
## 16. Micro-Interactions

### Typed.js — Typewriter Effect
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/typed.js/2.0.16/typed.umd.js"></script>
```

**Usage:**
```javascript
new Typed('#element', {
  strings: ['First sentence.', 'Second sentence.'],
  typeSpeed: 50,
  backSpeed: 30,
  loop: true
});
```

**Best for:** Hero sections, "AI typing" effect, terminal simulations
**Teaching power:** Perfect for showing agent "thinking" then responding

### CountUp.js — Animated Numbers
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/countup.js/2.8.0/countUp.umd.js"></script>
```

**Usage:**
```javascript
const countUp = new countUp.CountUp('target', 5000);
countUp.start();
```

**Best for:** Statistics, metrics, KPI dashboards, "X invoices processed" counters

### tsParticles — Particle Backgrounds
```html
<script src="https://cdn.jsdelivr.net/npm/tsparticles@2.12.0/tsparticles.bundle.min.js"></script>
```

**Best for:** Hero backgrounds, network visualizations, ambient motion, "neural network" aesthetics

---

<a name="audio"></a>
## 17. Audio

### Howler.js — Simple Audio Playback
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/howler/2.2.3/howler.min.js"></script>
```

**Best for:** Sound effects, notification sounds, background audio, simple playback
**When to use:** UI feedback sounds, demo interactions

### Tone.js — Web Audio Synthesis
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>
```

**Best for:** Sound synthesis, audio tutorials, music apps, generative audio

---

<a name="3d-and-webgl"></a>
## 18. 3D & WebGL

### Three.js
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
```

**Best for:** 3D product viewers, immersive experiences, data sculptures, "wow factor" hero sections

---

<a name="export-tools"></a>
## 19. Export Tools

### html2canvas — Screenshot DOM to PNG
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
```
```javascript
html2canvas(document.querySelector('#my-element')).then(canvas => {
  const link = document.createElement('a');
  link.download = 'screenshot.png';
  link.href = canvas.toDataURL();
  link.click();
});
```
**Best for:** "Download this card as image" buttons, social sharing previews, report generation, capturing HTML visuals as PowerPoint slide images

### PptxGenJS — Generate PowerPoint in Browser
```html
<script src="https://cdn.jsdelivr.net/npm/pptxgenjs"></script>
```
```javascript
const pptx = new PptxGenJS();
const slide = pptx.addSlide();
slide.addText('Hello World', { x: 1, y: 1, fontSize: 24 });
pptx.writeFile({ fileName: 'Presentation.pptx' });
```
**Best for:** "Download as PowerPoint" from dashboard data, automated report generation, programmatic slide decks

### Marked.js — Markdown Rendering
```html
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
```
**Best for:** Rendering markdown content as HTML in demos, blog previews, CMS-like interfaces

---

<a name="creative-concepts"></a>
## 20. Creative Concept Library: AI Agents as Coworkers

These concepts are designed to teach AI agent collaboration through interactive, visual experiences. Each maps to specific tools from this arsenal.

---

### Concept 1: The Parallel Workday

**What it teaches:** Capacity difference between human and agent

**Visualization:** Split-screen animated timeline
- Left: Your 8-hour day (meetings, lunch, end of day)
- Right: Agent's 24-hour day (continuous processing)

**Key moments:**
- You go to lunch → agent keeps working
- You leave at 5pm → agent processes evening requests
- You sleep → agent clears overnight queue
- You arrive → inbox already handled

**Tools:** GSAP (timeline animation), Canvas or SVG

**Emotional impact:** "I'm limited. It's not."

```
HUMAN:    |====WORK====|lunch|===WORK===|----sleep----|
AGENT:    |=WORK=WORK=WORK=WORK=WORK=WORK=WORK=WORK=|
                                         ↑
                              "47 invoices processed
                               while you slept"
```

---

### Concept 2: The Escalation Moment

**What it teaches:** Supervised autonomy — agent knows when to stop

**Visualization:**
1. Agent typing a response confidently (Typed.js)
2. Cursor stops... blinks...
3. Lottie "thinking" animation
4. Message: "I'm not sure about this one. Handing to you."
5. Human input box appears

**Tools:** Typed.js, Lottie, CSS transitions

**Emotional impact:** "It knows its limits. I'm still in control."

```
Agent: "Processing refund request..."
Agent: "Customer has valid receipt..."
Agent: "Amount is $4,500 which exceeds..."
       [cursor blinks]
       [thinking animation]
Agent: "This is above my approval limit.
        Your call, boss."
       [APPROVE] [DENY] [MODIFY]
```

---

### Concept 3: The Delegation Inbox

**What it teaches:** The accumulation problem — your pile grows, theirs clears

**Visualization:** Interactive drag-and-drop
- Tasks fall from top of screen
- Two buckets: "Give to Agent" and "Do Myself"
- Agent bucket: items auto-process with progress bars, then disappear
- Human bucket: items just... sit there. Pile grows.

**Tools:** Fabric.js or native drag-drop, GSAP for animations

**Emotional impact:** "Oh. I'm the bottleneck."

---

### Concept 4: The Trust Meter

**What it teaches:** Trust is earned over time, not assumed

**Visualization:** Animated line chart from Day 1 to Month 3
- Y-axis: Oversight level (100% = review everything, 0% = full autonomy)
- Line starts high, gradually drops
- Milestone markers: "First week without errors", "Handled edge case correctly", "Caught something you missed"

**Tools:** Chart.js or D3, GSAP for milestone animations

**Emotional impact:** "Trust is a journey, not a switch."

```
100% |●─────────────────────────────────────
     |  ╲
 75% |    ╲___●
     |         ╲    "First week: no errors"
 50% |           ╲____●
     |                  ╲  "Handled exception"
 25% |                    ╲____●
     |                          ╲___●  "Spot-check only"
  0% |──────────────────────────────────────
     Day 1    Week 2    Month 1    Month 3
```

---

### Concept 5: The Org Chart That Breathes

**What it teaches:** Agents are nodes in your workflow, not separate tools

**Visualization:** Living org chart where work pulses through connections
- Task enters at top (customer request)
- Flows to agent node (processes, enriches)
- Branches: routine → auto-complete, exception → escalate
- Human approves → flows back down

**Tools:** Mermaid (structure) + GSAP (pulse animation) or D3 (full custom)

**Emotional impact:** "We're a system. Agent is part of it."

---

### Concept 6: The Night Shift

**What it teaches:** Agents work while you don't

**Visualization:** Atmospheric, almost cinematic
- Office scene goes dark (CSS transition)
- Single desk glows with screen light
- Counter ticks up: "Processing... 12... 23... 47 invoices"
- Dawn gradient appears
- You "arrive" → see cleared queue with summary

**Tools:** CSS animations, CountUp.js, Lottie (working-person)

**Emotional impact:** "Someone was working while I rested."

---

### Concept 7: The Handoff Sequence

**What it teaches:** The shape of human-agent collaboration

**Visualization:** Mermaid sequence diagram, animated step by step

```
sequenceDiagram
    participant Human
    participant Agent
    participant CRM
    participant Customer

    Human->>Agent: "Handle new leads"
    Agent->>CRM: Check for new entries
    CRM-->>Agent: 12 new leads
    Agent->>Agent: Enrich from Apollo
    Agent->>Agent: Score by fit
    Agent->>Agent: Route by territory
    Agent-->>Human: "3 hot leads need your call"
    Human->>Customer: Makes the call
```

**Tools:** Mermaid + custom CSS for step-by-step reveal

**Emotional impact:** "I see exactly who does what."

---

### Concept 8: The Capacity Wall

**What it teaches:** Humans have limits; agents scale

**Visualization:** Physics-based (like Tetris)
- Tasks fall as blocks
- Single "human" catcher can only grab so many
- Pile overflows, blocks fall off screen
- Add "agent" catcher → two catchers, pile stays manageable

**Tools:** Matter.js

**Emotional impact:** Visceral. You *feel* the overflow, then the relief.

---

### Concept 9: The "What Just Happened" Replay

**What it teaches:** Transparency builds trust

**Visualization:** Timeline scrubber for overnight agent activity
- Shows 50 invoices processed
- Scrubber lets you replay each decision
- See what it checked, approved, flagged

**Tools:** Custom Canvas timeline, GSAP for scrubbing

**Emotional impact:** "I can see everything it did. No black box."

---

### Concept 10: The Coworker Comparison Card

**What it teaches:** Direct, honest comparison

**Visualization:** Side-by-side cards, clean design

| | Human Colleague | AI Agent |
|---|---|---|
| Annual cost | $65,000 | ~$3,000 |
| Hours/week | 40 | 168 |
| Sick days | Yes | No |
| Vacation | 2-4 weeks | None |
| Gets better over time | Yes | Yes |
| Handles ambiguity | Excellent | Needs help |
| Handles volume | Limited | Unlimited |
| Makes judgment calls | Yes | Asks first |
| Builds relationships | Yes | No |

**Tools:** Pure HTML/CSS, Animate.css for entrance

**Emotional impact:** Simple. Stark. Undeniable.

---

### Concept 11: The Learning Loop

**What it teaches:** Agents improve from corrections

**Visualization:**
1. Agent makes a decision
2. Human corrects it
3. Visual "memory" forms (brain icon pulses)
4. Similar situation appears
5. Agent gets it right this time

**Tools:** Rough.js (sketchy feel), GSAP (animation)

**Emotional impact:** "It learned from me."

---

### Concept 12: The Coverage Map

**What it teaches:** Agent handles the routine so you can focus

**Visualization:** Waffle chart or treemap
- All your tasks as squares
- Color-coded: Routine (80%) vs. Judgment (20%)
- Routine squares get "handed off" to agent
- What remains: the 20% that matters

**Tools:** D3.js or Chart.js

**Emotional impact:** "I should spend my time on *these*."

```
Before:                    After (with agent):
┌──────────────────────┐   ┌──────────────────────┐
│░░░░░░░░░░░░░░░░░░░░░░│   │                      │
│░░░░░░░░░░░░░░░░░░░░░░│   │   Agent handles      │
│░░░░░░░░░░░░░░░░░░░░░░│   │                      │
│░░░░░░░░░░░░░░░░░░░░░░│   │                      │
│░░░░░░░░██████████░░░░│   │      ██████████      │
│░░░░░░░░██ YOU ██░░░░░│   │      ██ YOU ██       │
└──────────────────────┘   └──────────────────────┘
  100% of your time          20% high-value focus
```

---

<a name="combination-patterns"></a>
## 21. Combination Patterns (Named Stacks)

### The Explainer Stack
For educational content that builds understanding:
```
Mermaid (structure) + Rough.js (approachable) + GSAP (timing) + KaTeX (formulas)
```

### The Dashboard Stack
For data-rich presentations:
```
Chart.js (charts) + CountUp.js (metrics) + AOS (scroll reveal) + Lottie (feedback)
```

### The Interactive Demo Stack
For hands-on learning:
```
Fabric.js (drag-drop) + Matter.js (physics) + GSAP (animation) + Howler (audio feedback)
```

### The Story Stack
For narrative-driven content:
```
GSAP + ScrollMagic (scroll-driven) + Typed.js (dialogue) + Lottie (moments)
```

### The Technical Tutorial Stack
For developer education:
```
Prism.js (code) + KaTeX (math) + Mermaid (diagrams) + AOS (progressive reveal)
```

---

<a name="asset-selection-by-teaching-goal"></a>
## 22. Asset Selection by Teaching Goal

| Teaching Goal | Primary Tool | Supporting Tools |
|---------------|--------------|------------------|
| "Show capacity difference" | GSAP timeline | CountUp.js, Lottie |
| "Explain a process" | Mermaid | GSAP for animation |
| "Make technical approachable" | Rough.js | Caveat font, soft colors |
| "Build trust through transparency" | Canvas timeline | GSAP scrubber |
| "Show accumulation/overflow" | Matter.js | — |
| "Compare options" | HTML/CSS cards | Animate.css entrance |
| "Reveal data progressively" | Chart.js + AOS | CountUp.js |
| "Simulate AI response" | Typed.js | Lottie thinking animation |
| "Explain ML concepts" | KaTeX + Canvas | Rough.js for friendly feel |
| "Interactive task sorting" | Fabric.js | — |

---

<a name="recipes"></a>
## 23. Recipes — Common Visual Patterns

### Blog Post Hero
```html
<div style="text-align: center; padding: 80px 20px; background: linear-gradient(135deg, #f8fafc, #e8f4f8);">
  <h1 class="animate__animated animate__fadeIn"
      style="font-family: 'Playfair Display', serif; font-size: 3rem; color: #1e3a5f;">
    The Future of AI at Work
  </h1>
  <p class="animate__animated animate__fadeInUp animate__delay-1s"
     style="font-family: 'Inter', sans-serif; font-size: 1.2rem; color: #64748b; max-width: 600px; margin: 1rem auto;">
    How 50-person firms are deploying AI workers across every department
  </p>
</div>
```

### Social Media Stat Card
```html
<div style="background: white; border-radius: 16px; padding: 32px; text-align: center; box-shadow: 0 4px 24px rgba(0,0,0,0.08); max-width: 300px;">
  <lottie-player src="assets/lottie/data-analytics.json"
    style="width: 120px; height: 120px; margin: 0 auto;" loop autoplay></lottie-player>
  <div style="font-family: 'Poppins', sans-serif; font-size: 3rem; font-weight: 800; color: #1e3a5f;">47%</div>
  <div style="font-family: 'Inter', sans-serif; color: #64748b;">Reduction in Manual Work</div>
</div>
```

### Team Section with DiceBear Avatars
```html
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; text-align: center;">
  <div>
    <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Sarah" width="80" height="80" style="border-radius: 50%;">
    <div style="font-family: 'Inter', sans-serif; font-weight: 600; margin-top: 8px;">Sarah Chen</div>
    <div style="font-family: 'Inter', sans-serif; font-size: 0.85rem; color: #64748b;">Finance</div>
  </div>
  <!-- Repeat for each team member, change seed -->
</div>
```

### Hand-Drawn "AI + Human" Diagram
```html
<canvas id="aiHumanDiagram" width="500" height="200"></canvas>
<script>
  const rc = rough.canvas(document.getElementById('aiHumanDiagram'));
  const ctx = document.getElementById('aiHumanDiagram').getContext('2d');

  rc.rectangle(20, 40, 180, 80, { roughness: 1.5, fill: '#e8f4fd', fillStyle: 'hachure' });
  rc.rectangle(300, 40, 180, 80, { roughness: 1.5, fill: '#d4edda', fillStyle: 'hachure' });
  rc.line(200, 80, 300, 80, { roughness: 1, strokeWidth: 2 });

  rc.circle(250, 80, 30, { roughness: 1, fill: '#fff3cd', fillStyle: 'solid' });

  ctx.font = '16px Inter';
  ctx.textAlign = 'center';
  ctx.fillStyle = '#333';
  ctx.fillText('AI Worker', 110, 85);
  ctx.fillText('Human', 390, 85);
  ctx.font = '12px Inter';
  ctx.fillText('Review', 250, 84);
</script>
```

### Staggered Notification Cards
```html
<div style="display: flex; flex-direction: column; gap: 12px; max-width: 400px;">
  <div class="animate__animated animate__fadeInRight" style="animation-delay: 0.1s; background: white; padding: 16px; border-radius: 8px; border-left: 4px solid #27ae60; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
    <strong>Invoice approved</strong> — Meridian Corp, $12,400
  </div>
  <div class="animate__animated animate__fadeInRight" style="animation-delay: 0.2s; background: white; padding: 16px; border-radius: 8px; border-left: 4px solid #3498db; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
    <strong>New lead scored</strong> — TechVentures, 85/100
  </div>
  <div class="animate__animated animate__fadeInRight" style="animation-delay: 0.3s; background: white; padding: 16px; border-radius: 8px; border-left: 4px solid #9b59b6; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
    <strong>Offer letter ready</strong> — Marcus Rivera, Sr. Analyst
  </div>
</div>
```

### Scroll-Stopping Social Banner
```html
<div style="width: 1200px; height: 630px; background: linear-gradient(135deg, #1e3a5f, #2c5282); display: flex; align-items: center; padding: 60px; color: white; position: relative; overflow: hidden;">
  <div style="position: absolute; top: -100px; right: -100px; width: 400px; height: 400px; background: rgba(52,152,219,0.15); border-radius: 50%;"></div>
  <div style="position: relative; z-index: 1;">
    <div style="font-family: 'Poppins', sans-serif; font-size: 3.5rem; font-weight: 800; line-height: 1.2; margin-bottom: 20px;">
      5 AI Workers.<br>4 Departments.<br>1 Monday Morning.
    </div>
    <div style="font-family: 'Inter', sans-serif; font-size: 1.3rem; opacity: 0.85;">
      See what your team accomplished before you opened your laptop.
    </div>
  </div>
  <lottie-player src="assets/lottie/working-person.json" background="transparent" speed="0.8" style="width: 300px; height: 300px; position: absolute; right: 60px; bottom: 0;" loop autoplay></lottie-player>
</div>
```

---

<a name="lessons-learned"></a>
## 24. Lessons Learned

### Loading Performance
- **Fonts:** Always use `<link rel="preconnect">` before Google Fonts link — cuts 100-200ms off load time
- **Icons:** Don't load all 5 icon libraries unless you need them. Pick one (Font Awesome is the safest default)
- **Lottie:** Large animations (200 KB+) should use `hover` instead of `autoplay` if there are many on the page
- **Animate.css:** The full CSS is 80 KB. If you only need `fadeIn` and `fadeInUp`, write those 10 lines of CSS yourself

### CDN Reliability
- **jsDelivr** is the most reliable CDN for npm packages — use it as your default
- **cdnjs** (Cloudflare-backed) is the most reliable for standalone libraries
- **unpkg** works but is slower — use only when jsDelivr doesn't have the package
- **Corporate firewalls** sometimes block CDNs. For mission-critical demos, consider inlining the CSS or hosting locally as backup

### Rough.js Gotchas
- Canvas must have explicit `width` and `height` attributes (not just CSS)
- Each `rough.canvas()` call re-draws — clear the canvas first if updating
- `fillStyle: 'hachure'` is the signature sketchy look — `solid` looks too clean
- Text must be drawn with native `ctx.fillText()` after Rough shapes — Rough.js doesn't do text

### DiceBear Gotchas
- The API has rate limits — for production, self-host or cache the SVGs
- Some styles produce very different-looking avatars (don't mix styles in one UI)
- The `seed` parameter accepts any string — use real names for consistent-looking teams
- `backgroundColor` parameter does NOT include the `#` — use `backgroundColor=667eea` not `backgroundColor=#667eea`

### SVG Illustration Tips
- unDraw illustrations use a single accent color — find it and replace globally for brand matching
- Open Doodles are black/white with skin-tone fills — they work on any background color
- Keep SVGs under 10 KB for inline use — larger ones should be `<img>` loaded
- SVGs from unDraw and Open Doodles are MIT/CC0 — no attribution needed

### Animation Best Practices
- Stagger delay should be 0.1s per element — faster than 0.05s looks simultaneous, slower than 0.3s feels laggy
- Never use `animate__infinite` on more than 2 elements per viewport — it's distracting
- `animate__fadeInUp` is the most versatile entrance — use it as your default
- For social media banners (static output), animations don't apply — use strong visual hierarchy instead

---

<a name="color-palette"></a>
## Color Palette

```css
:root {
  /* Primary */
  --primary-blue: #0078d4;
  --accent-purple: #8764b8;
  --accent-teal: #008272;

  /* Status */
  --success: #107c10;
  --warning: #f7630c;
  --error: #d13438;

  /* Neutral */
  --background: #f3f2f1;
  --surface: #ffffff;
  --border: #edebe9;

  /* Text */
  --text-primary: #323130;
  --text-secondary: #605e5c;
  --text-tertiary: #8a8886;

  /* Dark Mode (for explainers & cinematic demos) */
  --dark-bg: #1a1a2e;
  --dark-surface: #16213e;
  --dark-text: #e6f1ff;
  --dark-dim: #8892b0;
  --neon-cyan: #64ffda;
  --neon-purple: #7c4dff;
  --neon-pink: #ff6b9d;
  --neon-yellow: #ffd93d;
}
```

---

<a name="complete-cdn-reference"></a>
## 25. Complete CDN Reference

### Essential (Most Projects)
```html
<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

<!-- Icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<!-- Animations -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
```

### Data Visualization
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
```

### Animation & Interaction
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/vivus/0.4.6/vivus.min.js"></script>
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
```

### STEM & Code
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
```

### Physics & Canvas
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/matter-js/0.19.0/matter.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.7.0/p5.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.3.1/fabric.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.min.js"></script>
```

### Micro-Interactions
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/typed.js/2.0.16/typed.umd.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/countup.js/2.8.0/countUp.umd.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/hover.css/2.3.1/css/hover-min.css">
<script src="https://cdn.jsdelivr.net/npm/tsparticles@2.12.0/tsparticles.bundle.min.js"></script>
```

### Audio
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/howler/2.2.3/howler.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>
```

### 3D & Advanced
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
```

### Presentation
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/ScrollMagic/2.0.8/ScrollMagic.min.js"></script>
```

### Export & Utility
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/pptxgenjs"></script>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
```

---

<a name="file-structure"></a>
## 26. File Structure

```
cD2nS4hW9k/
├── index.html              # Live demo showcasing every asset type (2060 lines)
├── README.md               # This file
└── assets/
    ├── lottie/             # JSON-based vector animations
    │   ├── success-check.json      (25 KB)
    │   ├── loading-spinner.json    (11 KB)
    │   ├── heart-pulse.json        (60 KB)
    │   ├── rocket-launch.json      (186 KB)
    │   ├── data-analytics.json     (205 KB)
    │   └── working-person.json     (84 KB)
    │
    ├── undraw/             # Professional flat SVG illustrations
    │   ├── team-collaboration.svg
    │   ├── programming.svg
    │   ├── data-trends.svg
    │   ├── mobile-app.svg
    │   ├── secure-files.svg
    │   └── website-builder.svg
    │
    ├── doodles/            # Hand-drawn character SVGs (CC0 license)
    │   ├── sitting.svg
    │   ├── reading.svg
    │   ├── coffee.svg
    │   ├── dancing.svg
    │   ├── meditating.svg
    │   └── loving.svg
    │
    └── stock/              # Curated stock photography
        ├── metadata.json   # Full attribution data
        ├── unsplash/       # 5 photos (business, tech, office, nature, abstract)
        └── pexels/         # 5 photos (business, tech, office, nature, abstract)
```

---

*Last updated: February 2026*
*Merged from CDN Arsenal KB, Gold Standard, and Assets README into single definitive reference*
