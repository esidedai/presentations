# Asset Acquisition & Management Workflow

**Complete guide to bringing in professional assets from various sources and using them in presentations.**

---

## Table of Contents
1. [Asset Sources Overview](#asset-sources-overview)
2. [Figma Sync Workflow](#figma-sync-workflow)
3. [DrawKit Assets](#drawkit-assets)
4. [CDN Resources](#cdn-resources)
5. [API-Based Asset Generation](#api-based-asset-generation)
6. [Asset Organization](#asset-organization)
7. [Showcase Examples](#showcase-examples)

---

## Asset Sources Overview

### Our Multi-Source Asset Strategy
We acquire professional assets from multiple sources to ensure quality and variety:

| Source | Asset Types | Format | Location | Acquisition Method |
|--------|-------------|--------|----------|-------------------|
| **Figma** | Logos, team photos, custom graphics | PNG | `assets/*` | Automated sync script |
| **DrawKit** | Illustrations | SVG, PNG, GIF | `assets/illustrations/` | Manual download + organization |
| **unDraw** | Concept illustrations | SVG, PNG | `assets/illustrations/concepts/` | Manual download |
| **CDN Libraries** | Icons, fonts | SVG, WOFF2 | Referenced via URL | Direct CDN links |
| **Ideogram API** | AI-generated images | PNG | Generated on-demand | API call |
| **QuickChart** | Charts & graphs | PNG | Generated on-demand | API call |
| **Mermaid** | Diagrams | PNG, SVG | Generated on-demand | API call |
| **Unsplash/Pexels** | Stock photos | JPG | Generated on-demand | API call |
| **DiceBear** | Avatars | PNG | Generated on-demand | API call |

---

## Figma Sync Workflow

### Purpose
Sync professional design assets from Figma directly into the project structure with automatic categorization.

### Setup

1. **Get Figma Access Token**
   - Go to https://www.figma.com/settings
   - Scroll to "Personal access tokens"
   - Generate new token
   - Copy to `.env` file

2. **Get Figma File Key**
   - Open your Figma file
   - URL format: `https://www.figma.com/file/{FILE_KEY}/filename`
   - Copy the FILE_KEY to `.env`

3. **Configure .env**
   ```bash
   FIGMA_ACCESS_TOKEN=figd_xxxxxxxxxxxxxxxxxxxxx
   FIGMA_FILE_KEY=aBcDeFgHiJkLmNoPqRsTuVwXyZ
   ```

### Running the Sync

```bash
cd scripts
python figma_sync.py
```

### What It Does

1. **Connects to Figma** and fetches file structure
2. **Analyzes pages and frames** to categorize assets:
   - **Logos** → `assets/brand/logos/`
   - **Team photos** → `assets/team/headshots/`
   - **Illustrations** → `assets/illustrations/concepts/`
   - **Icons** → `assets/illustrations/icons/`
   - **Other** → `assets/illustrations/concepts/`

3. **Exports all assets** as PNG at 2x scale
4. **Saves manifest** (`figma-sync-manifest.json`) with:
   - File metadata
   - Sync timestamp
   - Asset organization
   - Downloaded file paths

### Example Output

```
============================================================
FIGMA ASSET SYNC
============================================================
Connecting to Figma file: aBcDeFgHiJkLmNoPqRsTuVwXyZ...

File: Company Presentation Assets
Last modified: 2026-02-14T09:30:00Z

============================================================
FIGMA FILE STRUCTURE
============================================================

Page: Logos
  ID: 123:456
  Frames: 3
    - Company Logo (FRAME) [ID: 123:457]
    - Partner Logo 1 (FRAME) [ID: 123:458]
    - Partner Logo 2 (FRAME) [ID: 123:459]

Page: Team
  ID: 123:460
  Frames: 4
    - Zak Ali Headshot (FRAME) [ID: 123:461]
    - Dr. Humaira Waqas (FRAME) [ID: 123:462]
    ...

============================================================
ASSET SUMMARY
============================================================
Logos: 3
Team Photos: 4
Illustrations: 12
Icons: 8
Other: 3
Total: 30

============================================================
Download all assets? (y/n): y

Downloading 3 logos...
  [OK] company-logo.png
  [OK] partner-logo-1.png
  [OK] partner-logo-2.png

Downloading 4 team photos...
  [OK] zak-ali-headshot.png
  [OK] dr-humaira-waqas.png
  ...

============================================================
SYNC COMPLETE
============================================================
Downloaded 30 assets
Assets saved to: C:\Dev\Projects\Presentations\assets
Manifest saved to: C:\Dev\Projects\Presentations\assets\figma-sync-manifest.json
```

### Categorization Logic

The script auto-categorizes based on page/frame names:
- Contains "logo" → Logos folder
- Contains "team", "headshot", "photo" → Team folder
- Contains "icon" → Icons folder
- Contains "illustration", "graphic" → Illustrations folder
- Everything else → Other (goes to illustrations/concepts)

### Manifest File

The `figma-sync-manifest.json` tracks what was downloaded:

```json
{
  "file_key": "aBcDeFgHiJkLmNoPqRsTuVwXyZ",
  "file_name": "Company Presentation Assets",
  "sync_date": "2026-02-14T09:30:00Z",
  "organization": {
    "logos": [
      {"name": "Company Logo", "id": "123:457", "page": "Logos"}
    ],
    "team": [
      {"name": "Zak Ali Headshot", "id": "123:461", "page": "Team"}
    ],
    ...
  },
  "downloaded": [
    "C:\\Dev\\Projects\\Presentations\\assets\\brand\\logos\\company-logo.png",
    ...
  ]
}
```

---

## DrawKit Assets

### What is DrawKit?
DrawKit provides free and premium illustration packs. We use the **Creativity & Design** pack.

### Asset Formats
- **SVG** - Vector (scalable, editable)
- **PNG** - Raster (ready to use)
- **GIF** - Animated (for process illustrations)

### Directory Structure

```
assets/illustrations/
├── _source/
│   └── drawkit-creativity/    # Original downloaded pack (ZIP contents)
├── concepts/
│   ├── creativity-design/     # Organized DrawKit illustrations
│   │   ├── creative-woman.svg
│   │   ├── creative-woman.png
│   │   ├── team-collaboration.svg
│   │   └── team-collaboration.png
│   ├── undraw_*.png          # unDraw illustrations
│   └── *.png                 # Other concept illustrations
```

### How We Acquired DrawKit Assets

1. **Downloaded pack** from https://www.drawkit.com/product/creativity-design-illustrations
2. **Extracted ZIP** to `assets/illustrations/_source/drawkit-creativity/`
3. **Organized into concepts/** by theme:
   - Team & collaboration
   - Creative work
   - Office & workspace
   - Innovation & ideas

4. **Converted SVG to PNG** (where needed):
   ```bash
   # Using Inkscape or online converters
   inkscape creative-woman.svg --export-png=creative-woman.png --export-width=1200
   ```

### Using DrawKit Assets in Code

```python
from pathlib import Path

# SVG (for PptxGenJS - browser-based)
illustration = Path("assets/illustrations/concepts/creativity-design/team-collaboration.svg")

# PNG (for python-pptx)
illustration = Path("assets/illustrations/concepts/creativity-design/team-collaboration.png")

# Add to slide
slide.shapes.add_picture(str(illustration), Inches(8), Inches(2), width=Inches(7))
```

### DrawKit vs unDraw

| DrawKit | unDraw |
|---------|--------|
| More detailed, realistic style | Minimalist, flat design |
| Fewer free options | Fully free, open source |
| Better for corporate/professional | Better for tech/startup |
| Available as SVG, PNG, GIF | Available as SVG, PNG |

---

## CDN Resources

### What Are CDNs?
Content Delivery Networks host libraries (fonts, icons, frameworks) accessible via URL. No download needed.

### CDN Arsenal We Use

#### 1. **Google Fonts CDN**
**Purpose**: Professional typography

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
```

**Available Fonts**:
- **Inter** - Modern sans-serif (body text)
- **Poppins** - Geometric sans-serif (headings)
- **Playfair Display** - Serif (hero titles)
- **Fira Code** - Monospace (code/data)
- **Roboto Mono** - Monospace alternative
- **Caveat** - Handwritten (casual notes)

**Usage in python-pptx**:
```python
paragraph.font.name = 'Inter'
paragraph.font.size = Pt(24)
```

#### 2. **Font Awesome CDN**
**Purpose**: 2000+ professional icons

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
```

**Icon Categories**:
- Business (briefcase, chart-line, handshake)
- Technology (laptop, server, database)
- Communication (envelope, phone, comments)
- Social (linkedin, twitter, github)

**Accessing Icons**:
```python
# Use downloaded PNG versions or reference via HTML
icon_url = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/svgs/solid/chart-line.svg"
```

#### 3. **Bootstrap Icons CDN**
**Purpose**: 1800+ clean, minimal icons

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
```

**Usage**: Similar to Font Awesome, but lighter style

#### 4. **Remix Icon CDN**
**Purpose**: 2800+ neutral-style icons

We downloaded the Remix Icon pack and placed it in:
```
assets/brand/logos/remix-icons/
├── fill/
│   └── logos/
│       ├── google-fill.png
│       ├── microsoft-fill.png
│       └── ...
└── line/
    └── logos/
        ├── google-line.png
        └── ...
```

**200+ brand logos included**: Google, Microsoft, GitHub, LinkedIn, etc.

#### 5. **Chart.js via QuickChart.io**
**Purpose**: Professional charts without browser rendering

```python
# No CDN link needed - API generates PNG
APIUtils.generate_quickchart(config, "chart.png")
```

See [API-Based Asset Generation](#api-based-asset-generation) section.

---

## API-Based Asset Generation

### Overview
Instead of downloading static assets, we generate them on-demand via APIs.

### 1. Ideogram API (AI Image Generation)

**What it does**: Text-to-image generation

**Setup**:
```bash
# .env
IDEOGRAM_API_KEY=your_api_key_here
```

**Usage**:
```python
from api_utils import APIUtils

APIUtils.generate_ideogram_image(
    prompt="Modern office workspace with laptop, natural lighting, professional",
    output_path="workspace.png",
    aspect_ratio="ASPECT_16_9",
    model="V_2_TURBO"
)
```

**Parameters**:
- `aspect_ratio`: `ASPECT_16_9`, `ASPECT_1_1`, `ASPECT_9_16`, `ASPECT_4_3`
- `model`: `V_2_TURBO` (fast), `V_2` (quality), `V_1` (legacy)

**When to use**: Custom visuals not available in stock libraries

### 2. QuickChart.io (Chart Generation)

**What it does**: Converts Chart.js configs to PNG images

**Setup**: No API key needed (free tier)

**Usage**:
```python
chart_config = {
    "type": "bar",
    "data": {
        "labels": ["Q1", "Q2", "Q3", "Q4"],
        "datasets": [{
            "label": "Revenue",
            "data": [12, 19, 15, 25],
            "backgroundColor": "rgba(0, 120, 212, 0.85)"
        }]
    },
    "options": {
        "plugins": {
            "datalabels": {
                "anchor": "end",
                "align": "top",
                "font": {"size": 28, "weight": "bold"}
            }
        }
    }
}

APIUtils.generate_quickchart(chart_config, "chart.png", width=1600, height=800)
```

**Advanced Features**:
- Data labels (`plugins.datalabels`)
- Annotations (`plugins.annotation`)
- Mixed chart types (bar + line)
- Custom colors and gradients
- Gallery: https://quickchart.io/gallery/

**When to use**: Any chart or graph

### 3. Mermaid Diagrams

**What it does**: Text-to-diagram conversion

**Setup**: No API key needed (uses mermaid.ink)

**Usage**:
```python
mermaid_code = """
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Action 1]
    B -->|No| D[Action 2]
    C --> E[End]
    D --> E

    style A fill:#0078d4,stroke:#0078d4,color:#fff
    style E fill:#107c10,stroke:#107c10,color:#fff
"""

APIUtils.generate_mermaid_diagram(mermaid_code, "diagram.png", theme="default")
```

**Diagram Types**:
- `graph` - Flowcharts
- `sequenceDiagram` - Sequence diagrams
- `classDiagram` - Class diagrams
- `stateDiagram` - State machines
- `gantt` - Gantt charts
- `pie` - Pie charts

**Themes**: `default`, `dark`, `forest`, `neutral`

**When to use**: Process flows, system architecture, timelines

### 4. Unsplash (Stock Photos)

**What it does**: Curated professional photography

**Setup**:
```bash
# .env
UNSPLASH_ACCESS_KEY=your_access_key_here
```

**Usage**:
```python
APIUtils.get_unsplash_image(
    query="business teamwork collaboration",
    output_path="team.jpg",
    orientation="landscape"
)
```

**Orientations**: `landscape`, `portrait`, `squarish`

**When to use**: Professional stock photography (primary source)

### 5. Pexels (Stock Photos - Backup)

**What it does**: Alternative stock photo source

**Setup**:
```bash
# .env
PEXELS_API_KEY=your_api_key_here
```

**Usage**:
```python
APIUtils.get_pexels_image(
    query="technology innovation",
    output_path="tech.jpg",
    orientation="landscape"
)
```

**Orientations**: `landscape`, `portrait`, `square`

**When to use**: Fallback when Unsplash doesn't have what you need

### 6. DiceBear (Avatars)

**What it does**: Generates consistent avatars from seeds

**Setup**: No API key needed (free)

**Usage**:
```python
APIUtils.get_dicebear_avatar(
    seed="john_doe",
    output_path="avatar.png",
    style="avataaars",
    size=200
)
```

**Styles**:
- `avataaars` - Cartoon characters
- `bottts` - Robots
- `pixel-art` - 8-bit style
- `fun-emoji` - Emoji faces
- `lorelei` - Line art portraits
- `personas` - Colorful characters
- `initials` - Letter-based
- `shapes` - Abstract shapes

**When to use**: Team members without photos, placeholder profiles

---

## Asset Organization

### Directory Structure

```
assets/
├── brand/
│   ├── logos/
│   │   ├── eSided-Logo.png              # Company logo
│   │   └── remix-icons/                 # 200+ brand logos
│   │       ├── fill/logos/*.png
│   │       └── line/logos/*.png
│   ├── colors/
│   │   └── palette.json                 # Brand color definitions
│   └── fonts/
│       └── custom-fonts/                # Custom web fonts
│
├── team/
│   ├── headshots/                       # Individual photos
│   │   ├── zak-ali.png
│   │   ├── dr-humaira-waqas.png
│   │   └── ...
│   └── group-photos/                    # Team photos
│
├── illustrations/
│   ├── concepts/                        # Topic-based illustrations
│   │   ├── creativity-design/          # DrawKit pack
│   │   ├── undraw_*.png                # unDraw illustrations
│   │   ├── drawing-a-home.png
│   │   └── ...
│   ├── diagrams/                        # Generated diagrams
│   ├── icons/                           # Icon sets
│   └── _source/                         # Original downloaded packs
│       └── drawkit-creativity/
│
├── stock/                               # Stock photography
│   ├── business/
│   ├── technology/
│   └── lifestyle/
│
└── templates/
    ├── backgrounds/                     # Slide backgrounds
    └── slide-layouts/                   # Reusable layouts

presentations/
├── YYYY-MM-event/
│   ├── assets-local/                    # Event-specific assets
│   │   ├── Team-Pictures/
│   │   ├── Title-Slide-Illustration.png
│   │   └── eSided-Logo.png
│   ├── content/
│   ├── generate.py
│   └── output/
```

### Asset Naming Conventions

- **Lowercase with hyphens**: `team-collaboration.png`
- **Descriptive names**: `undraw_creative_woman_re_u5tk.png`
- **Brand assets**: Keep original names for recognition
- **Generated assets**: Prefix with purpose: `chart_roi.png`, `diagram_workflow.png`

### Asset Selection Priority

When building a slide, follow this order:

1. **Project-specific** (`presentations/*/assets-local/`)
2. **Team photos** (`assets/team/`)
3. **Brand assets** (`assets/brand/`)
4. **Existing illustrations** (`assets/illustrations/concepts/`)
5. **Stock photos** (Unsplash → Pexels)
6. **Generate via API** (Ideogram as last resort)

---

## Showcase Examples

### Location
`.ai/showcase/` contains working examples of all capabilities.

### Files

1. **`api_utils.py`** - API wrapper utilities
   - Ideogram, QuickChart, Mermaid, Unsplash, Pexels, DiceBear
   - Error handling and caching
   - Test mode for verification

2. **`showcase_presentation.py`** - Complete example presentation
   - 8 slides demonstrating all features
   - Morph transitions
   - Mixed API usage
   - Professional layouts

3. **`SHOWCASE.md`** - Complete documentation
   - API references
   - Code patterns
   - Best practices
   - Learning path

### Running the Showcase

```bash
cd .ai/showcase
python showcase_presentation.py
```

Output: `output/capabilities-showcase.pptx`

### Testing APIs

```bash
cd .ai/showcase
python api_utils.py
```

This generates sample assets in `test_output/`:
- `ideogram.png` - AI-generated image
- `chart.png` - QuickChart example
- `diagram.png` - Mermaid flowchart
- `avatar.png` - DiceBear avatar
- `unsplash.png` - Stock photo
- `pexels.png` - Alternative stock photo

### Showcase Slide Breakdown

1. **Title Slide** - Custom design + DiceBear avatar
2. **Chart** - QuickChart.io bar chart
3. **Chart Animation** - Morph transition demo
4. **AI Image** - Ideogram generated workspace
5. **Stock Photos** - Unsplash + Pexels side-by-side
6. **Diagram** - Mermaid flowchart
7. **Avatar Grid** - 6 DiceBear styles
8. **Full Integration** - All techniques combined

---

## Quick Reference Commands

### Figma Sync
```bash
cd scripts
python figma_sync.py
```

### Test APIs
```bash
cd .ai/showcase
python api_utils.py
```

### Generate Showcase
```bash
cd .ai/showcase
python showcase_presentation.py
```

### Generate Presentation
```bash
cd presentations/2026-02-live-event
python generate.py
```

---

## Environment Variables Summary

Required in `.env`:

```bash
# API Keys
IDEOGRAM_API_KEY=your_ideogram_key
UNSPLASH_ACCESS_KEY=your_unsplash_key
PEXELS_API_KEY=your_pexels_key

# Figma (for asset sync)
FIGMA_ACCESS_TOKEN=figd_xxxxxxxxxxxxx
FIGMA_FILE_KEY=aBcDeFgHiJkLmNoPqRsTuVwXyZ
```

**Free APIs** (no keys needed):
- QuickChart.io
- Mermaid.ink
- DiceBear

---

## Best Practices Summary

1. **Check existing assets FIRST** before generating new ones
2. **Use Figma sync** for branded assets (logos, team photos)
3. **Use unDraw/DrawKit** for concept illustrations
4. **Use QuickChart** for all charts (not matplotlib)
5. **Use Mermaid** for diagrams (not manual drawing)
6. **Unsplash primary, Pexels backup** for stock photos
7. **Ideogram as last resort** for custom visuals
8. **Cache generated assets** to avoid redundant API calls
9. **Organize by purpose**, not by source
10. **Document in manifest** for team collaboration

---

**Last Updated**: February 14, 2026
**Maintainer**: Development Team
**Related Docs**: `MEMORY.md`, `.ai/showcase/SHOWCASE.md`, `RETROSPECTIVE.md`
