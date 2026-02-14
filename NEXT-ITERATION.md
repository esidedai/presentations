# Next Iteration: Professional-Grade Presentation Generation

## Current State
✅ Functional 28-slide presentation generated
✅ API integrations working (Ideogram, QuickChart, Mermaid)
✅ Figma assets downloaded (230 assets)
❌ Visual quality below professional standards
❌ Didn't leverage existing professional assets
❌ Didn't use CDN arsenal capabilities

---

## What Changes for V2

### 1. **Asset-First Approach**
**Before generating ANY image:**
```python
# 1. Check existing professional assets
if exists(f"assets-local/Title-Slide-Illustration.png"):
    use_existing_asset()
elif exists(f"assets/illustrations/concepts/undraw_{theme}.png"):
    use_undraw_illustration()
else:
    # Last resort: generate with Ideogram
    generate_ideogram_image()
```

**Concrete changes:**
- **Slide 1 (Title)**: Use `Title-Slide-Illustration.png` from assets-local
- **Slide 11 (Meet Meridian)**: Use team photos from `assets-local/Team-Pictures/`
- **Slide 6-25**: Use unDraw illustrations instead of generating new images

---

### 2. **Hybrid PptxGenJS + python-pptx Approach**

**Design-rich slides → PptxGenJS:**
```javascript
// Title slide with SVG illustration
pptx.addSlide()
  .addText("The AI Workforce", {
    x: 0.5, y: 2.5, w: 7, h: 2,
    fontSize: 72,
    fontFace: 'Playfair Display',
    bold: true,
    color: '323130'
  })
  .addImage({
    path: 'assets-local/Title-Slide-Illustration.png',
    x: 8, y: 2, w: 7, h: 5
  });
```

**Data-heavy slides → python-pptx:**
```python
# Charts, diagrams, automation
slide = prs.slides.add_slide(...)
slide.shapes.add_picture(chart_path, ...)
```

**Merge strategy:**
1. Generate design slides with PptxGenJS (1, 11, 27, 28)
2. Generate data slides with python-pptx (13, 14, 18, 26)
3. Merge presentations using python-pptx's presentation combining

---

### 3. **Advanced QuickChart Configurations**

**Current (basic):**
```python
chart_config = {
    "type": "bar",
    "data": { "labels": [...], "datasets": [...] }
}
```

**V2 (professional):**
```python
chart_config = {
    "type": "bar",
    "data": {
        "labels": ["Platform Cost", "Configuration", "Value Created", "Net ROI"],
        "datasets": [{
            "label": "Amount ($K)",
            "data": [-100, -47, 479.6, 332.6],
            "backgroundColor": [
                "rgba(211, 52, 56, 0.8)",   # Red for costs
                "rgba(211, 52, 56, 0.8)",
                "rgba(16, 124, 16, 0.8)",   # Green for value
                "rgba(0, 120, 212, 0.8)"    # Blue for net
            ],
            "borderColor": [
                "rgb(211, 52, 56)",
                "rgb(211, 52, 56)",
                "rgb(16, 124, 16)",
                "rgb(0, 120, 212)"
            ],
            "borderWidth": 2
        }]
    },
    "options": {
        "plugins": {
            "datalabels": {
                "anchor": "end",
                "align": "top",
                "formatter": (value) => {
                    return value > 0 ? '+$' + value + 'K' : '$' + value + 'K';
                },
                "font": {
                    "weight": "bold",
                    "size": 16
                }
            },
            "annotation": {
                "annotations": {
                    "line1": {
                        "type": "line",
                        "yMin": 0,
                        "yMax": 0,
                        "borderColor": "rgb(50, 49, 48)",
                        "borderWidth": 2,
                        "label": {
                            "content": "Break-even",
                            "enabled": true
                        }
                    }
                }
            }
        },
        "scales": {
            "y": {
                "ticks": {
                    "callback": (value) => '$' + value + 'K',
                    "font": { "size": 14 }
                },
                "grid": {
                    "color": "rgba(0, 0, 0, 0.05)"
                }
            },
            "x": {
                "ticks": {
                    "font": { "size": 14 }
                }
            }
        },
        "legend": {
            "display": false
        }
    }
}
```

**Key improvements:**
- Color-coded bars (red = costs, green = value, blue = net)
- Data labels on bars (no legend hunting)
- Break-even line annotation
- Professional formatting ($XXXk format)
- Subtle grid lines
- Larger font sizes for readability

---

### 4. **Professional Typography Implementation**

**Create typography helper:**
```python
class Typography:
    """Professional typography system"""

    FONTS = {
        'hero': ('Playfair Display', 72, True),
        'title': ('Inter', 48, True),
        'subtitle': ('Inter', 32, False),
        'body': ('Inter', 24, False),
        'caption': ('Inter', 18, False),
        'code': ('Fira Code', 20, False)
    }

    COLORS = {
        'primary': RGBColor(50, 49, 48),      # Dark gray
        'accent': RGBColor(0, 120, 212),      # Brand blue
        'secondary': RGBColor(135, 100, 184), # Brand purple
        'muted': RGBColor(142, 142, 147)      # Light gray
    }

    @staticmethod
    def apply(text_frame, style='body', color='primary'):
        """Apply typography style to text frame"""
        font_name, size, bold = Typography.FONTS[style]
        color_rgb = Typography.COLORS[color]

        for paragraph in text_frame.paragraphs:
            paragraph.font.name = font_name
            paragraph.font.size = Pt(size)
            paragraph.font.bold = bold
            paragraph.font.color.rgb = color_rgb

# Usage:
title_frame = slide.shapes.add_textbox(...).text_frame
title_frame.text = "The AI Workforce"
Typography.apply(title_frame, style='hero', color='primary')
```

---

### 5. **Illustration Selection Logic**

**Create asset selector:**
```python
class IllustrationSelector:
    """Smart selection of professional illustrations"""

    THEMES = {
        'team': ['undraw_team_collaboration', 'undraw_team_page', 'undraw_team_spirit'],
        'process': ['undraw_our_solution', 'undraw_live_collaboration'],
        'thinking': ['undraw_in_thought', 'undraw_creative_woman'],
        'office': ['undraw_in_the_office'],
        'growth': ['undraw_startup_life', 'undraw_building_blocks'],
        'decision': ['undraw_swipe_options'],
        'wellness': ['undraw_healthy_lifestyle']
    }

    @staticmethod
    def get_illustration(theme, variant=0):
        """Get professional illustration path by theme"""
        base_path = Path("assets/illustrations/concepts")

        if theme in IllustrationSelector.THEMES:
            options = IllustrationSelector.THEMES[theme]
            illustration_name = options[variant % len(options)]

            # Find matching file (unDraw illustrations have long suffixes)
            matches = list(base_path.glob(f"{illustration_name}*.png"))
            if matches:
                return matches[0]

        # Fallback: check assets-local
        local_path = Path("assets-local") / f"{theme}.png"
        if local_path.exists():
            return local_path

        return None

# Usage:
illustration = IllustrationSelector.get_illustration('team', variant=0)
if illustration:
    slide.shapes.add_picture(str(illustration), Inches(8), Inches(2), width=Inches(7))
```

---

### 6. **Mermaid with Custom Themes**

**Current:**
```python
mermaid_code = """
graph TD
    A --> B
"""
```

**V2 (professional styling):**
```python
mermaid_code = """
%%{init: {'theme':'base', 'themeVariables': {
  'primaryColor':'#e3f2fd',
  'primaryTextColor':'#323130',
  'primaryBorderColor':'#0078d4',
  'lineColor':'#0078d4',
  'secondaryColor':'#c8e6c9',
  'tertiaryColor':'#fff3e0'
}}}%%
graph TD
    A[Invoice arrives] --> B[Extract data]
    B --> C[Apply rules]
    C --> D{Amount > $50K?}
    D -->|Yes| E[Alert partner]
    D -->|No| F[Post to QB]

    classDef startNode fill:#e3f2fd,stroke:#0078d4,stroke-width:3px
    classDef processNode fill:#f3f2f1,stroke:#323130,stroke-width:2px
    classDef decisionNode fill:#fff3e0,stroke:#ff8c00,stroke-width:2px
    classDef endNode fill:#c8e6c9,stroke:#107c10,stroke-width:3px

    class A startNode
    class B,C processNode
    class D decisionNode
    class E,F endNode
"""
```

**Key improvements:**
- Custom color palette matching brand
- Node type differentiation (start, process, decision, end)
- Descriptive labels (not abbreviations)
- Professional stroke widths

---

### 7. **Team Slide with Actual Photos**

**New Slide 11 Implementation:**
```python
def create_team_slide(self):
    """Create team slide with actual professional photos"""
    slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])

    # Title
    title = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(15), Inches(0.8))
    title.text_frame.text = "Meet Meridian Group Leadership"
    Typography.apply(title.text_frame, 'title', 'primary')

    # Team photos in grid (2x2)
    team = [
        {'name': 'Zak Ali', 'role': 'CEO', 'photo': 'Zak-Ali.png'},
        {'name': 'Dr. Humaira Waqas', 'role': 'CFO', 'photo': 'Dr-Humaira-Waqas.png'},
        {'name': 'Dr. Kamran Malik', 'role': 'CTO', 'photo': 'Dr-Kamran-Malik.png'},
        {'name': 'Olga Skeen', 'role': 'COO', 'photo': 'Olga-Skeen.png'}
    ]

    x_start = 1.5
    y_start = 2
    x_spacing = 3.5
    y_spacing = 3.5

    for i, person in enumerate(team):
        row = i // 2
        col = i % 2
        x = x_start + (col * x_spacing)
        y = y_start + (row * y_spacing)

        # Photo
        photo_path = Path(f"assets-local/Team-Pictures/{person['photo']}")
        if photo_path.exists():
            slide.shapes.add_picture(
                str(photo_path),
                Inches(x), Inches(y),
                width=Inches(2.5), height=Inches(2.5)
            )

        # Name
        name_box = slide.shapes.add_textbox(
            Inches(x), Inches(y + 2.7),
            Inches(2.5), Inches(0.4)
        )
        name_box.text_frame.text = person['name']
        Typography.apply(name_box.text_frame, 'subtitle', 'primary')
        name_box.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

        # Role
        role_box = slide.shapes.add_textbox(
            Inches(x), Inches(y + 3.1),
            Inches(2.5), Inches(0.3)
        )
        role_box.text_frame.text = person['role']
        Typography.apply(role_box.text_frame, 'caption', 'muted')
        role_box.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
```

---

## Implementation Plan for V2

### Phase 1: Asset Organization (1 hour)
1. Review all `assets-local/` files
2. Catalog unDraw illustrations by theme
3. Create asset selector utilities
4. Map slides → existing assets

### Phase 2: Helper Classes (2 hours)
1. Create `Typography` class
2. Create `IllustrationSelector` class
3. Create `ChartConfigurator` class (advanced QuickChart configs)
4. Create `MermaidThemer` class

### Phase 3: Hybrid Generation (3 hours)
1. Set up PptxGenJS environment
2. Generate design-rich slides (1, 11, 27, 28) with PptxGenJS
3. Generate data-heavy slides with python-pptx
4. Merge presentations

### Phase 4: Quality Pass (1 hour)
1. Review typography consistency
2. Verify color palette adherence
3. Check visual hierarchy
4. Test transitions and animations

---

## Expected Outcome

**V1 (Current):**
- Functional but basic
- Generic AI-generated images
- Simple charts
- No team photos
- Inconsistent typography

**V2 (Professional-Grade):**
- Visually stunning
- Professional existing assets
- Advanced charts with annotations
- Real team photos
- Consistent typography hierarchy
- Brand-aligned color palette
- Smooth morph transitions
- Rival manually-designed decks

**The difference:** V2 leverages the **full CDN arsenal** and **existing professional assets** we assembled, rather than generating everything from scratch.
