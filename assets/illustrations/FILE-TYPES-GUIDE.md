# File Types Guide - Illustrations & Design Assets

## Overview
This guide explains which file types go where and how to organize DrawKit and other design assets for maximum reusability.

---

## 📁 File Type Strategy

### **Source Files** (Editable, Version Controlled)
**Location**: `assets/illustrations/_source/`

These are your **master files** - never embed directly in PowerPoint.

| Format | Extension | Purpose | Tools |
|--------|-----------|---------|-------|
| **Vector Graphics** | `.svg` | Editable illustrations, color tweaking | Inkscape, Illustrator, Figma |
| **Animation Data** | `.json` | Lottie animations (from After Effects) | LottieFiles, Lottie Player |
| **After Effects** | `.aep` | Animation source files | Adobe After Effects |
| **Design Files** | `.ai`, `.sketch`, `.fig` | Original design files | Illustrator, Sketch, Figma |

**Why keep these?**
- ✅ Modify colors to match brand changes
- ✅ Resize without quality loss
- ✅ Extract individual elements
- ✅ Create variations

---

### **Production Files** (PowerPoint-Ready)
**Location**: `assets/illustrations/concepts/`, `icons/`, `diagrams/`

These are **optimized for PowerPoint** - what you actually embed.

| Format | Extension | Use Case | Max Size |
|--------|-----------|----------|----------|
| **PNG** | `.png` | Illustrations with transparency, icons, graphics | 1920px width, <2MB |
| **JPG** | `.jpg` | Photos, complex illustrations without transparency | 1920px width, <2MB |
| **GIF** | `.gif` | Animated illustrations (loops) | 800px width, <5MB |

**Why these formats?**
- ✅ Universal PowerPoint compatibility
- ✅ Predictable rendering
- ✅ Smaller file sizes
- ✅ No external dependencies

---

## 🎨 Recommended Folder Structure

```
assets/illustrations/
│
├── _source/                       # 🔐 MASTER FILES (editable)
│   ├── drawkit-creativity/
│   │   ├── svg/                   # SVG source files
│   │   ├── json/                  # Lottie JSON animations
│   │   ├── ae/                    # After Effects files
│   │   └── gif/                   # Animated GIFs
│   │
│   ├── custom-designs/            # Your custom illustrations
│   └── downloaded-packs/          # Other illustration packs
│
├── concepts/                      # 🎯 PRODUCTION (PowerPoint-ready)
│   ├── creativity-design/         # From DrawKit
│   │   ├── laptop-design-software.png
│   │   ├── sharpening-pencil.png
│   │   ├── drawing-home.png
│   │   └── ...
│   │
│   ├── business/
│   ├── technology/
│   └── teamwork/
│
├── icons/                         # 🔷 ICON SET
│   ├── ui-icons/                  # Interface icons
│   ├── social-media/              # Social platform icons
│   └── actions/                   # Action/verb icons
│
└── diagrams/                      # 📊 PROCESS DIAGRAMS
    ├── workflows/
    ├── architectures/
    └── timelines/
```

---

## 🔄 Workflow: SVG → Brand-Colored PNG

### Why This Matters
Your DrawKit SVG files have default colors. You want to match your brand colors.

### The Process

**1. Source (SVG)** → **2. Customize Colors** → **3. Export (PNG)** → **4. Use in PowerPoint**

### Tools You Can Use

#### Option A: Automated Script (Recommended)
```python
# scripts/svg-to-png.py
# Batch convert SVG to PNG with color replacement

from svglib.svglib import renderSVG
from reportlab.graphics import renderPM
from PIL import Image

def convert_svg_to_png(svg_path, png_path, color_map=None):
    """
    Convert SVG to PNG with optional color replacement

    color_map example: {'#6c5ce7': '#0078d4'}  # purple → your brand blue
    """
    # Implementation here
```

#### Option B: Manual (One-time Setup)
1. **Open SVG** in Inkscape or Illustrator
2. **Find & Replace** colors:
   - Default purple (`#6c5ce7`) → Your brand blue (`#0078d4`)
   - Default orange → Your accent color
3. **Export as PNG**: 1920px width, transparent background
4. **Save to** `assets/illustrations/concepts/creativity-design/`

#### Option C: Online Tools
- [Vecta.io/nano](https://vecta.io/nano) - SVG editor & color changer
- [SVGOMG](https://jakearchibald.github.io/svgomg/) - SVG optimizer
- Export from browser to PNG

---

## 📦 DrawKit Organization Plan

### Step 1: Copy Source Files
```bash
# Copy DrawKit source files to your project
cp -r "G:/Shared drives/T-Drive/Design-Assets/DrawKit/DrawKit_0068_Creativity_Design_Animation/DrawKit Animation Pack Creative & Design/SVG" \
  assets/illustrations/_source/drawkit-creativity/svg/

cp -r "G:/Shared drives/T-Drive/Design-Assets/DrawKit/.../JSON" \
  assets/illustrations/_source/drawkit-creativity/json/

cp -r "G:/Shared drives/T-Drive/Design-Assets/DrawKit/.../GIF" \
  assets/illustrations/_source/drawkit-creativity/gif/
```

### Step 2: Generate Brand-Colored PNGs
For your first presentation, you'll want:
- **Laptop Design Software** - for tech/design slides
- **Designer's Tools** - for creativity slides
- **Drawing on Pen Tablet** - for workflow slides
- **Complete the Puzzle** - for problem-solving slides

Convert these to PNG with your brand colors, save to `concepts/creativity-design/`

### Step 3: Catalog Available Illustrations
Create `_source/drawkit-creativity/CATALOG.md` listing all available illustrations by category.

---

## 🎯 For Your Live Event Presentation

### What You Need from DrawKit

Based on "Creativity & Design" theme, these illustrations are perfect for:
- Product design presentations
- Creative process explanations
- Tool/software demos
- Design thinking workshops

### Recommended Illustrations to Prepare

| SVG Source | Branded PNG Output | Use Case |
|------------|-------------------|----------|
| `Laptop Design Software.svg` | `laptop-design-blue.png` | "Our design tools" slide |
| `Designer's Tools.svg` | `designers-tools-blue.png` | "Features overview" slide |
| `Drawing on Pen Tablet.svg` | `creative-process-blue.png` | "How it works" slide |
| `Complete the Puzzle.svg` | `solution-puzzle-blue.png` | "Solving problems" slide |
| `Designer Brainstroming.svg` | `brainstorm-blue.png` | "Our approach" slide |

---

## 💡 Best Practices

### DO ✅
- **Keep SVG sources** - always editable
- **Version control SVG files** - track changes
- **Export PNGs optimized** - max 1920px, compressed
- **Organize by topic** - easier to find
- **Name descriptively** - `laptop-design-blue.png` not `image1.png`

### DON'T ❌
- **Don't embed SVG in PowerPoint** - poor compatibility
- **Don't use massive PNGs** - keep under 2MB
- **Don't edit PNGs directly** - edit SVG, re-export
- **Don't mix source and production** - separate folders

---

## 🔧 Quick Reference

### File Type Decision Tree

```
Do you need to edit colors/elements?
├─ YES → Use SVG (in _source/)
│   └─ Then export to PNG for PowerPoint
└─ NO → Use PNG directly (in concepts/)

Is it a photo or complex raster image?
├─ YES → Use JPG
└─ NO → Use PNG (for transparency)

Does it need to animate?
├─ YES → Use GIF or Lottie JSON
└─ NO → Use static PNG
```

---

## 📊 File Size Guidelines

| Asset Type | Max Width | Max Size | Format |
|------------|-----------|----------|--------|
| Full-slide image | 1920px | 2-3MB | PNG/JPG |
| Half-slide illustration | 1200px | 1-2MB | PNG |
| Icon | 200-400px | 100KB | PNG |
| Avatar/headshot | 400px | 200KB | PNG/JPG |
| Animated GIF | 800px | 5MB | GIF |
| Background | 1920px | 3MB | JPG |

---

## 🎨 Color Replacement Guide

### Your Brand Colors
(Update these based on your actual brand)
```
Primary Blue: #0078d4
Accent Purple: #8764b8
Dark Gray: #323130
Light Gray: #f3f2f1
Success Green: #107c10
```

### DrawKit Default Colors
(To be replaced)
```
Purple: #6c5ce7
Orange: #ff6b6b
Teal: #4ecdc4
```

### Replacement Map
```json
{
  "#6c5ce7": "#0078d4",  // Purple → Your blue
  "#ff6b6b": "#8764b8",  // Orange → Your purple
  "#4ecdc4": "#107c10"   // Teal → Your green
}
```

---

**Next Step**: Let me create a script to batch-convert your DrawKit SVGs to brand-colored PNGs!
