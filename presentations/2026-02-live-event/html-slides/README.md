# HTML-Powered Slide Generation (V3)

**Breaking free from python-pptx limitations with HTML/CSS/JS**

---

## The Big Idea

Instead of fighting python-pptx constraints, design slides in **HTML/CSS** (where you have full creative control), render to **PNG** with Playwright, then assemble into **PowerPoint**.

### Why This Works

| Feature | python-pptx | HTML/CSS |
|---------|------------|----------|
| **Design flexibility** | ⭐⭐ Limited | ⭐⭐⭐⭐⭐ Complete |
| **Typography** | Basic | Full (Google Fonts, custom fonts, kerning, line-height) |
| **Layouts** | Manual positioning | Flexbox, Grid, modern CSS |
| **Effects** | None | Gradients, shadows, borders, animations |
| **Preview** | None (regenerate to see) | Browser (instant feedback) |
| **Debugging** | Difficult | Chrome DevTools |
| **SVG support** | Limited | Native |
| **Iteration speed** | Slow | Fast |

---

## Directory Structure

```
html-slides/
├── slides/                   # HTML slides
│   ├── 01-title.html
│   ├── 02-team.html
│   └── 03-chart.html
├── styles/
│   └── brand.css            # eSided branding (curves, logo, colors)
├── output/                  # Generated PNGs
│   ├── 01-title.png
│   ├── 02-team.png
│   └── 03-chart.png
├── render_slides.py         # HTML → PNG (Playwright)
├── assemble_pptx.py         # PNG → PowerPoint
└── README.md                # This file
```

---

## Setup

### 1. Install Playwright

```bash
pip install playwright
playwright install chromium
```

### 2. Verify Installation

```bash
cd html-slides
python render_slides.py --help
```

---

## Workflow

### Step 1: Design Slides in HTML

**Open `slides/01-title.html` in browser** to preview:

```bash
# macOS/Linux
open slides/01-title.html

# Windows
start slides/01-title.html
```

**Edit HTML/CSS** using your favorite editor. See changes instantly by refreshing the browser.

**Key Files:**
- `styles/brand.css` - eSided branding (automatically included)
- Each slide is a standalone HTML file (1920x1080px)

### Step 2: Render to PNG

```bash
python render_slides.py
```

**What happens:**
1. Playwright launches headless Chromium
2. Each HTML file is rendered at 1920x1080 @ 2x scale (retina)
3. Screenshots saved to `output/`

**Output:**
```
output/
├── 01-title.png      # 3840x2160 (2x scale)
├── 02-team.png
└── 03-chart.png
```

### Step 3: Assemble PowerPoint

```bash
python assemble_pptx.py
```

**What happens:**
1. Creates blank PowerPoint (16:9)
2. Adds each PNG as a full-slide image
3. Saves to `../output/V3_HTML_Powered.pptx`

**Output:**
```
presentations/2026-02-live-event/output/V3_HTML_Powered.pptx
```

---

## Creating New Slides

### Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1920, initial-scale=1">
  <title>Slide X: Title</title>

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;600&display=swap" rel="stylesheet">

  <!-- Brand Styles (eSided branding) -->
  <link rel="stylesheet" href="../styles/brand.css">

  <style>
    /* Custom styles for this slide */
  </style>
</head>
<body>
  <!-- eSided Branding (automatically included from brand.css) -->
  <div class="curve-top"></div>
  <div class="curve-left"></div>
  <div class="curve-bottom"></div>
  <img src="../../assets-local/eSided-Logo.png" class="esided-logo">

  <!-- Your Content -->
  <div class="content">
    <h1 class="hero-title">Your Title</h1>
  </div>

  <!-- Website Info -->
  <div class="website-info">www.eSided.com | info@esided.com</div>
</body>
</html>
```

### Available CSS Classes (from `brand.css`)

**Branding:**
- `.curve-top`, `.curve-left`, `.curve-bottom` - Decorative curves
- `.esided-logo` - Logo positioning
- `.website-info` - Bottom-right contact

**Typography:**
- `.hero-title` - Playfair Display 96px
- `.subtitle` - Inter 48px
- `.slide-title` - Playfair Display 72px (centered)
- `.body-text` - Inter 32px
- `.caption` - Inter 24px

**Layout:**
- `.content` - Safe content area (with padding)
- `.flex-center` - Flexbox center
- `.grid-2col` - 2-column grid
- `.team-grid` - 4-column team layout

**Brand Colors (CSS variables):**
```css
--brand-blue: #0078d4;
--brand-purple: #8764b8;
--dark-gray: #323130;
--success-green: #107c10;
--white: #ffffff;
```

---

## Design Tips

### 1. Use Browser DevTools

- Right-click → Inspect Element
- Modify CSS live
- Copy working CSS to your HTML file

### 2. 16:9 Ratio is Sacred

- Body is always `1920px × 1080px`
- Don't change these dimensions
- Rendered at 2x for retina quality (3840x2160)

### 3. Fonts Load from Google Fonts

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
```

**Available:**
- Playfair Display (serif, for titles)
- Inter (sans-serif, for body)
- Add more as needed

### 4. Embed Charts from QuickChart

```html
<img src="https://quickchart.io/chart?c={...}" alt="Chart">
```

See `03-chart.html` for example.

### 5. Use CSS Grid for Complex Layouts

```css
.grid-team {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 50px;
}
```

Much easier than manual positioning!

---

## Advantages vs python-pptx

### ✅ Pros

1. **Full design control** - CSS can do anything
2. **Instant preview** - Open in browser, refresh to see changes
3. **Modern tools** - Flexbox, Grid, transforms, transitions
4. **Better typography** - Google Fonts, kerning, line-height
5. **SVG support** - Use DrawKit/unDraw directly
6. **Debugging** - Chrome DevTools
7. **Reusable components** - CSS classes, includes
8. **Version control friendly** - HTML is human-readable

### ⚠️ Cons

1. **Not editable in PowerPoint** - Slides are images
2. **Larger file size** - PNGs vs. native PowerPoint objects
3. **No PowerPoint animations** - Can't use morph transitions
4. **Requires Playwright** - Extra dependency
5. **Slower generation** - Browser rendering takes time

### When to Use

- **Use HTML approach** when design quality > editability
- **Use python-pptx** when users need to edit text in PowerPoint

---

## Performance

### Rendering Speed

- ~2-3 seconds per slide (Playwright startup + rendering)
- 10 slides ≈ 25-30 seconds total
- Can be parallelized if needed

### File Size

- PNG per slide: ~500KB - 2MB (depends on content)
- 10-slide deck: ~5-15MB
- Larger than native PowerPoint, but acceptable

---

## Troubleshooting

### Fonts not loading

**Problem:** Fonts default to system fonts

**Solution:** Check internet connection (Google Fonts needs to download)

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
```

### Images not showing

**Problem:** Relative paths incorrect

**Solution:** Check path from HTML to asset

```html
<!-- From slides/01-title.html to assets-local/ -->
<img src="../../assets-local/eSided-Logo.png">
```

### Playwright not installed

```bash
pip install playwright
playwright install chromium
```

### Slide cut off

**Problem:** Content outside 1920x1080 viewport

**Solution:** Use `overflow: hidden` on body (already in brand.css)

---

## Examples

### Slide 1: Title Slide
- Hero title with Playfair Display
- Subtitle with Inter
- Title illustration on right
- eSided branding elements

### Slide 2: Team Grid
- 4-column CSS Grid
- Team photos with rounded corners
- Names and roles centered
- Professional spacing

### Slide 3: Chart Embed
- QuickChart.io embedded chart
- Chart container with shadow
- Key insight callout below
- All branded

---

## Next Steps

1. **Add more slides** - Copy template, modify content
2. **Customize styles** - Edit `brand.css` or add slide-specific CSS
3. **Integrate APIs** - Embed QuickChart, Mermaid, Ideogram images
4. **Build library** - Create reusable slide templates

---

## The Future: V4?

Potential enhancements:

- **Automated slide generation** - Python script generates HTML from data
- **Component library** - Reusable HTML templates (title, bullet list, chart, etc.)
- **GSAP animations** - Export as animated GIFs
- **Lottie integration** - JSON animations → GIF → embed
- **Responsive charts** - Chart.js directly in HTML
- **Interactive prototypes** - Test presentations in browser first

---

**This is V3: HTML-powered slide generation**

Breaking free from python-pptx constraints with the power of modern web technologies.
