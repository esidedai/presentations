# Programmatic PowerPoint Capabilities Showcase

## Overview

This showcase demonstrates **all capabilities** available for programmatic PowerPoint generation using:
- **python-pptx** - Core presentation library
- **External APIs** - Ideogram, Unsplash, Pexels, QuickChart.io, DiceBear, Mermaid
- **XML Workarounds** - Morph transitions, fade transitions, custom animations

**Generated File**: [`output/capabilities-showcase.pptx`](output/capabilities-showcase.pptx)

---

## 📊 Slides Breakdown

### Slide 1: Title Slide with Custom Design
**Demonstrates:**
- Custom text formatting and positioning
- Background shapes and colors
- DiceBear avatar integration

**Code Pattern:**
```python
# Add background
background = slide.shapes.add_shape(
    1,  # Rectangle
    Inches(0), Inches(0),
    prs.slide_width, prs.slide_height
)
background.fill.solid()
background.fill.fore_color.rgb = RGBColor(243, 242, 241)

# Add title with custom font
title_box = slide.shapes.add_textbox(
    Inches(1), Inches(2.5), Inches(11.333), Inches(1.5)
)
title_frame = title_box.text_frame
title_frame.text = "Your Title Here"
for run in title_frame.paragraphs[0].runs:
    run.font.size = Pt(54)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 120, 212)
    run.font.name = 'Segoe UI'

# Add DiceBear avatar
APIUtils.get_dicebear_avatar("seed", "avatar.png", style="bottts")
slide.shapes.add_picture("avatar.png", Inches(6.1), Inches(5.8), width=Inches(1.1))
```

**Key Takeaway**: Background shapes + custom text formatting + API-generated avatars = professional title slides

---

### Slide 2: Chart Generation (QuickChart.io)
**Demonstrates:**
- No-render chart generation via URL API
- QuickChart.io integration
- Chart embedding

**Code Pattern:**
```python
# Chart configuration (Chart.js format)
chart_config = {
    "type": "bar",
    "data": {
        "labels": ["Q1", "Q2", "Q3", "Q4"],
        "datasets": [{
            "label": "Revenue (Millions)",
            "data": [12, 19, 15, 25],
            "backgroundColor": "rgba(0, 120, 212, 0.7)"
        }]
    },
    "options": {
        "title": {"display": True, "text": "Quarterly Revenue 2025"},
        "scales": {"yAxes": [{"ticks": {"beginAtZero": True}}]}
    }
}

# Generate and embed
APIUtils.generate_quickchart(chart_config, "chart.png", width=900, height=500)
slide.shapes.add_picture("chart.png", Inches(2.5), Inches(2), width=Inches(8.3))
```

**Key Takeaway**: QuickChart.io = instant charts without browser rendering. Just configure → fetch → embed.

**API Docs**: https://quickchart.io/documentation/

---

### Slide 3: Chart Animation with Morph Transition
**Demonstrates:**
- Morph transitions (PowerPoint's smooth animation feature)
- Same layout, different data
- XML injection technique

**Code Pattern:**
```python
# Create slide with updated chart (same position as previous slide)
slide = prs.slides.add_slide(prs.slide_layouts[6])

# Add updated chart at EXACT same position
slide.shapes.add_picture("updated_chart.png", Inches(2.5), Inches(2), width=Inches(8.3))

# Inject morph transition XML
xml = '''
<mc:AlternateContent
  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">
  <mc:Choice
    xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main"
    Requires="p159">
    <p:transition
      xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
      xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main"
      spd="slow" p14:dur="1500">
      <p159:morph option="byObject"/>
    </p:transition>
  </mc:Choice>
  <mc:Fallback>
    <p:transition
      xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
      spd="slow">
      <p:fade/>
    </p:transition>
  </mc:Fallback>
</mc:AlternateContent>
'''
slide.element.append(etree.fromstring(xml))
```

**Key Takeaway**: Morph transitions = smooth animations. Keep shapes at same position, morph does the rest.

**Requirements**: PowerPoint 2019/365 for morph. Falls back to fade on older versions.

---

### Slide 4: AI-Generated Images (Ideogram)
**Demonstrates:**
- Text-to-image generation
- Ideogram API integration
- High-quality visual assets

**Code Pattern:**
```python
# Generate AI image from prompt
prompt = "Modern minimalist office workspace with laptop, coffee, natural lighting"
APIUtils.generate_ideogram_image(
    prompt,
    "ai_image.png",
    aspect_ratio="ASPECT_16_9",
    model="V_2_TURBO"
)

# Embed in presentation
slide.shapes.add_picture("ai_image.png", Inches(1.5), Inches(2), width=Inches(10.3))

# Add caption
caption_box = slide.shapes.add_textbox(Inches(1.5), Inches(6.5), Inches(10.3), Inches(0.6))
caption_box.text_frame.text = f'Prompt: "{prompt}"'
```

**Key Takeaway**: AI images on demand. No stock photo searching. Just describe what you need.

**Aspect Ratios**: `ASPECT_16_9`, `ASPECT_1_1`, `ASPECT_9_16`, `ASPECT_4_3`

**Models**:
- `V_2_TURBO` - Fast, good quality
- `V_2` - Slower, higher quality
- `V_1` - Legacy model

---

### Slide 5: Stock Photography (Unsplash + Pexels)
**Demonstrates:**
- Fallback strategy (Unsplash primary, Pexels backup)
- Search-based image retrieval
- Side-by-side image layouts

**Code Pattern:**
```python
# Unsplash (primary)
APIUtils.get_unsplash_image(
    "teamwork business",
    "unsplash.png",
    orientation="landscape"
)
slide.shapes.add_picture("unsplash.png", Inches(0.8), Inches(1.8), width=Inches(5.8))

# Pexels (backup/alternative)
APIUtils.get_pexels_image(
    "technology innovation",
    "pexels.png",
    orientation="landscape"
)
slide.shapes.add_picture("pexels.png", Inches(6.8), Inches(1.8), width=Inches(5.8))
```

**Key Takeaway**: Multiple stock photo sources = higher reliability. Try Unsplash, fall back to Pexels if needed.

**Orientations**: `landscape`, `portrait`, `squarish` (Unsplash) / `square` (Pexels)

---

### Slide 6: Diagram Generation (Mermaid)
**Demonstrates:**
- Flowchart/diagram from text syntax
- Mermaid integration via mermaid.ink
- Process documentation visualization

**Code Pattern:**
```python
# Write diagram in Mermaid syntax
mermaid_code = """
graph TD
    A[User Request] --> B{Presentation Generator}
    B --> C[Generate Outline]
    B --> D[Fetch Visual Assets]
    C --> E[Create Slides]
    D --> E
    E --> F[Apply Transitions]
    F --> G[Export PPTX]

    style A fill:#0078d4,stroke:#0078d4,color:#fff
    style G fill:#107c10,stroke:#107c10,color:#fff
"""

# Generate and embed
APIUtils.generate_mermaid_diagram(mermaid_code, "diagram.png", theme="default")
slide.shapes.add_picture("diagram.png", Inches(2), Inches(1.8), width=Inches(9.3))
```

**Key Takeaway**: Diagrams as code. No drawing tools needed. Just describe the flow in text.

**Diagram Types**: `graph`, `sequenceDiagram`, `classDiagram`, `stateDiagram`, `gantt`, `pie`

**Themes**: `default`, `dark`, `forest`, `neutral`

**Mermaid Docs**: https://mermaid.js.org/

---

### Slide 7: Avatar Grid (DiceBear)
**Demonstrates:**
- Multiple avatar styles
- Grid layout
- No authentication needed (free API)

**Code Pattern:**
```python
avatar_data = [
    ("Alice", "avataaars"),    # Cartoon characters
    ("Bob", "bottts"),         # Robots
    ("Charlie", "pixel-art"),  # 8-bit style
    ("Diana", "fun-emoji"),    # Emoji faces
    ("Eve", "lorelei"),        # Line art portraits
    ("Frank", "personas"),     # Colorful characters
]

for i, (name, style) in enumerate(avatar_data):
    col = i % 3
    row = i // 3
    x = start_x + (col * spacing)
    y = start_y + (row * spacing)

    # Generate avatar
    APIUtils.get_dicebear_avatar(name, f"avatar_{name}.png", style=style, size=200)
    slide.shapes.add_picture(f"avatar_{name}.png", Inches(x), Inches(y), width=Inches(1.3))
```

**Key Takeaway**: DiceBear = instant avatars. No signup, no auth. Just pick a style and seed.

**Popular Styles**: `avataaars`, `bottts`, `pixel-art`, `fun-emoji`, `lorelei`, `personas`, `initials`, `shapes`

**API URL Pattern**: `https://api.dicebear.com/7.x/{style}/png?seed={name}&size={size}`

---

### Slide 8: Full Integration
**Demonstrates:**
- All capabilities combined in one slide
- Complex layouts
- Hero image + chart + bullet points
- Title bar with colored background

**Code Pattern:**
```python
# Background title bar
title_bg = slide.shapes.add_shape(
    1, Inches(0), Inches(0), prs.slide_width, Inches(1.2)
)
title_bg.fill.solid()
title_bg.fill.fore_color.rgb = RGBColor(0, 120, 212)

# AI hero image
APIUtils.generate_ideogram_image(
    "Abstract technology network, blue purple tones",
    "hero.png",
    aspect_ratio="ASPECT_16_9"
)
slide.shapes.add_picture("hero.png", Inches(0.5), Inches(1.5), width=Inches(7))

# Mini chart overlay
chart_config = {"type": "line", "data": {...}}
APIUtils.generate_quickchart(chart_config, "mini_chart.png", width=500, height=300)
slide.shapes.add_picture("mini_chart.png", Inches(8), Inches(1.5), width=Inches(4.5))

# Bullet points
for i, text in enumerate(bullets):
    bullet_box = slide.shapes.add_textbox(...)
    bullet_box.text_frame.text = f"• {text}"
```

**Key Takeaway**: Complex professional slides = layering simple techniques. Shapes + images + text + positioning.

---

## 🎨 Capabilities Reference

### Text & Formatting
- Custom fonts (any system font)
- Font sizes, colors, bold/italic
- Alignment (left, center, right)
- Bullet points and numbered lists
- Text boxes at any position

### Shapes
- Rectangles, circles, arrows
- Solid fills and outlines
- Custom colors (RGB)
- Layering (z-order)

### Images
- **AI-Generated**: Ideogram API
- **Stock Photos**: Unsplash, Pexels
- **Charts**: QuickChart.io (Chart.js configs)
- **Diagrams**: Mermaid (flowcharts, sequences, etc.)
- **Avatars**: DiceBear (20+ styles)
- **Custom**: Any PNG/JPG file

### Transitions
- **Fade**: Smooth fade between slides
- **Morph**: Animate changes between shapes/positions
- **Duration**: Customizable timing (milliseconds)
- **Fallback**: Older PowerPoint versions fall back gracefully

### Layouts
- Blank canvas (full control)
- Title slides
- Content slides
- Two-column layouts
- Custom positioning with Inches()

---

## 🔧 Technical Details

### Dependencies
```txt
python-pptx>=0.6.21
lxml>=5.0.0
Pillow>=10.0.0
requests>=2.31.0
python-dotenv>=1.0.0
```

### Environment Variables Required
```bash
IDEOGRAM_API_KEY=...
PEXELS_API_KEY=...
UNSPLASH_ACCESS_KEY=...
```

### No Auth Needed (Free APIs)
- QuickChart.io
- DiceBear
- Mermaid.ink

---

## 🚀 Usage

### Generate the Showcase
```bash
cd .ai/showcase
python showcase_presentation.py
```

### Output
- `output/capabilities-showcase.pptx` - The presentation
- `assets/` - All generated images cached

### Testing APIs
```bash
cd .ai/showcase
python api_utils.py
```
This tests all API integrations and generates sample assets in `test_output/`.

---

## 📖 API Reference

### Ideogram
```python
APIUtils.generate_ideogram_image(
    prompt="description of image",
    output_path="image.png",
    aspect_ratio="ASPECT_16_9",  # or ASPECT_1_1, ASPECT_9_16
    model="V_2_TURBO"             # or V_2, V_1
)
```

### QuickChart
```python
APIUtils.generate_quickchart(
    chart_config={...},  # Chart.js config object
    output_path="chart.png",
    width=800,
    height=600
)
```

### DiceBear
```python
APIUtils.get_dicebear_avatar(
    seed="unique_identifier",
    output_path="avatar.png",
    style="avataaars",  # or bottts, pixel-art, etc.
    size=200
)
```

### Mermaid
```python
APIUtils.generate_mermaid_diagram(
    mermaid_code="graph TD\n    A-->B",
    output_path="diagram.png",
    theme="default"  # or dark, forest, neutral
)
```

### Unsplash
```python
APIUtils.get_unsplash_image(
    query="business meeting",
    output_path="photo.png",
    orientation="landscape"  # or portrait, squarish
)
```

### Pexels
```python
APIUtils.get_pexels_image(
    query="technology",
    output_path="photo.png",
    orientation="landscape"  # or portrait, square
)
```

---

## 💡 Best Practices

### Image Sizes
- **Hero images**: 1920x1080 (16:9) for full-slide backgrounds
- **Charts**: 800-900px width for clarity
- **Avatars**: 150-200px for profile pics
- **Diagrams**: 900-1000px width for readability

### API Call Strategy
1. **QuickChart first** for charts (fastest, no auth)
2. **Ideogram for custom visuals** (unique, high quality)
3. **Unsplash primary, Pexels backup** for stock photos
4. **DiceBear for avatars** (free, consistent)
5. **Mermaid for diagrams** (code-based, version-controllable)

### Performance
- **Cache generated assets**: Don't regenerate on every run
- **Use smaller image sizes**: PowerPoint compresses anyway
- **Batch API calls**: Generate all assets before creating slides
- **Error handling**: Always have fallbacks (default images)

### Transitions
- **Use morph sparingly**: 2-3 times per presentation max
- **Fade for everything else**: Professional and reliable
- **Duration**: 800-1500ms (too fast = jarring, too slow = boring)
- **Test in PowerPoint**: Transitions only work in slideshow mode

---

## 🎓 Learning Path

### Beginner
1. Start with **Slide 1** (text + shapes + one API)
2. Add **Slide 2** (charts via QuickChart)
3. Add **Slide 7** (avatar grid)

### Intermediate
4. Implement **Slide 3** (morph transitions)
5. Add **Slide 6** (Mermaid diagrams)
6. Add **Slide 5** (stock photos with fallback)

### Advanced
7. Implement **Slide 4** (AI-generated images)
8. Create **Slide 8** (complex layouts)
9. Build custom gold standards from these patterns

---

## 📚 Further Reading

- [python-pptx Documentation](https://python-pptx.readthedocs.io/)
- [QuickChart.io Docs](https://quickchart.io/documentation/)
- [Ideogram API](https://ideogram.ai/api/docs)
- [Mermaid Syntax](https://mermaid.js.org/intro/)
- [DiceBear Styles](https://www.dicebear.com/styles/)

---

**Created**: February 14, 2026
**Last Updated**: February 14, 2026
**Author**: Claude Code Presentation Generator
