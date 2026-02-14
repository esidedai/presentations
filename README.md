# Programmatic PowerPoint Presentation Generator

> **Generate professional PowerPoint presentations programmatically using python-pptx and external APIs**

Built for **Claude Code** to create presentations from natural language.

---

## 🎯 What This Is

A complete system for generating `.pptx` presentations with:
- ✅ **AI-Generated Images** (Ideogram)
- ✅ **Data Visualizations** (QuickChart.io)
- ✅ **Stock Photography** (Unsplash, Pexels)
- ✅ **Diagrams & Flowcharts** (Mermaid)
- ✅ **Custom Avatars** (DiceBear)
- ✅ **Smooth Transitions** (Morph, Fade)
- ✅ **Professional Formatting** (Fonts, Colors, Layouts)

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up API Keys
Create a `.env` file (already exists, update with your keys):
```bash
IDEOGRAM_API_KEY=your_key_here
PEXELS_API_KEY=your_key_here
UNSPLASH_ACCESS_KEY=your_key_here
```

### 3. Generate the Showcase
```bash
cd .ai/showcase
python showcase_presentation.py
```

**Output**: `output/capabilities-showcase.pptx` - An 8-slide presentation demonstrating all capabilities.

### 4. Open in PowerPoint
Open the `.pptx` file and run the slideshow to see morph transitions in action!

---

## 📁 Project Structure

```
Presentations/
├── .ai/                                 # AI-powered tools and resources
│   ├── skills/
│   │   └── presentation-generator.md   # Claude Code skill definition
│   ├── reference/
│   │   ├── Programmatic Animated PowerPoint Guide.md
│   │   ├── CDN-ARSENAL-KB.md
│   │   └── CDN-ARSENAL-README.md
│   ├── showcase/
│   │   ├── api_utils.py                # API integration utilities
│   │   ├── showcase_presentation.py    # Generates the showcase
│   │   ├── SHOWCASE.md                 # Full documentation
│   │   └── output/
│   │       └── capabilities-showcase.pptx
│   └── gold-standards/                 # Coming soon: templates
│
├── .env                                # API keys (DO NOT COMMIT)
├── .gitignore
├── requirements.txt
└── README.md                           # This file
```

---

## 🎨 Capabilities Demonstrated

### Slide 1: Title Slide
- Custom typography
- Background shapes
- DiceBear avatar integration

### Slide 2: Chart Generation
- QuickChart.io integration
- Bar charts with custom data
- Professional formatting

### Slide 3: Chart Animation
- **Morph transition** (smooth animation between slides)
- Updated chart data
- Demonstrates PowerPoint's most powerful transition

### Slide 4: AI-Generated Images
- Ideogram API integration
- Text-to-image generation
- High-quality professional visuals

### Slide 5: Stock Photography
- Unsplash + Pexels integration
- Fallback strategy (primary/backup)
- Side-by-side layouts

### Slide 6: Diagram Generation
- Mermaid flowcharts
- Process documentation
- Code-to-diagram pipeline

### Slide 7: Avatar Grid
- DiceBear API (6 different styles)
- Grid layout patterns
- Team member visualizations

### Slide 8: Full Integration
- All capabilities combined
- Complex layouts
- Hero image + chart + bullets

**Full details**: [`.ai/showcase/SHOWCASE.md`](.ai/showcase/SHOWCASE.md)

---

## 🔧 API Integrations

| API | Purpose | Auth Required | Cost |
|-----|---------|---------------|------|
| **QuickChart.io** | Charts (bar, line, pie) | ❌ No | Free |
| **DiceBear** | Avatars (20+ styles) | ❌ No | Free |
| **Mermaid.ink** | Diagrams & flowcharts | ❌ No | Free |
| **Ideogram** | AI-generated images | ✅ Yes | Paid |
| **Unsplash** | Stock photography | ✅ Yes | Free |
| **Pexels** | Stock photography | ✅ Yes | Free |

---

## 📖 Documentation

### For Users
- **[Skill Definition](.ai/skills/presentation-generator.md)** - How to use the skill with Claude Code
- **[Showcase Documentation](.ai/showcase/SHOWCASE.md)** - Complete capabilities reference

### For Developers
- **[PowerPoint Guide](.ai/reference/Programmatic%20Animated%20PowerPoint%20Guide.md)** - python-pptx deep dive
- **[CDN Arsenal](.ai/reference/CDN-ARSENAL-KB.md)** - Web assets and libraries reference
- **[API Utils Source](.ai/showcase/api_utils.py)** - API integration code

---

## 🎯 Use Cases

### Business Presentations
- Quarterly reviews
- Sales pitches
- Board meetings
- Data-driven reports

**Example**: "Create a business presentation on Q4 revenue growth with charts"

### Educational Content
- Training materials
- Tutorials
- Course content
- Explainer decks

**Example**: "Create an educational presentation on how neural networks work"

### Marketing Decks
- Product launches
- Campaign pitches
- Client proposals
- Brand presentations

**Example**: "Create a marketing deck for our SaaS product targeting CTOs"

---

## 🧪 Testing

### Test All APIs
```bash
cd .ai/showcase
python api_utils.py
```

This generates test assets in `test_output/`:
- QuickChart bar chart
- DiceBear avatar
- Mermaid diagram
- Ideogram AI image
- Unsplash photo
- Pexels photo

### Generate Showcase
```bash
cd .ai/showcase
python showcase_presentation.py
```

Output: `output/capabilities-showcase.pptx`

---

## 💡 How to Use with Claude Code

Just ask in natural language:

```
Create a presentation about quarterly sales performance
```

```
Create a business presentation on AI adoption with 8 slides, include charts
```

```
Create an educational presentation explaining the water cycle with diagrams
```

Claude Code will:
1. Analyze your request
2. Generate an outline
3. Fetch visual assets (charts, images, diagrams)
4. Build the presentation
5. Export as `.pptx`

**See**: [`.ai/skills/presentation-generator.md`](.ai/skills/presentation-generator.md) for full usage guide

---

## 🔄 Workflow

```
User Request
    ↓
Claude Code analyzes intent
    ↓
Generate outline
    ↓
Fetch visual assets (parallel)
  ├── Ideogram (AI images)
  ├── QuickChart (charts)
  ├── Unsplash/Pexels (photos)
  ├── Mermaid (diagrams)
  └── DiceBear (avatars)
    ↓
Build slides with python-pptx
    ↓
Apply transitions (morph/fade)
    ↓
Export .pptx
```

---

## 🎨 Design Philosophy

### Two Lenses

**1. Showcase (What's Possible)**
- Demonstrates **all capabilities**
- Shows API integrations
- Proves the pipeline works
- Reference for developers

**2. Gold Standards (Specific Use Cases)**
- Business presentations
- Educational content
- Marketing decks
- Minimal/clean styles

Start with **Showcase**, derive **Gold Standards** from proven capabilities.

---

## 🛠️ Technical Stack

- **python-pptx**: PowerPoint generation
- **lxml**: XML manipulation (transitions)
- **Pillow**: Image processing
- **requests**: HTTP API calls
- **python-dotenv**: Environment variables

**Python**: 3.10+ (tested on 3.14)

---

## 📊 Stats

- **8 slides** in the showcase
- **6 API integrations**
- **2 transition types** (morph, fade)
- **20+ DiceBear styles** available
- **Infinite charts** via QuickChart.io
- **Infinite images** via Ideogram

---

## 🚨 Known Limitations

### python-pptx Limitations
- ❌ No native animation support (entrance/exit effects)
- ❌ No native slide transition support
- ✅ **Workaround**: XML injection (implemented for morph/fade)

### Morph Transition Requirements
- Requires PowerPoint 2019/365
- Falls back to fade on older versions
- Shapes must have same names across slides

### API Dependencies
- Ideogram requires paid API key
- Rate limits may apply (esp. Unsplash free tier)
- Network required (no offline mode)

**See**: [PowerPoint Guide](.ai/reference/Programmatic%20Animated%20PowerPoint%20Guide.md) for workarounds

---

## 🔜 Roadmap

### Phase 1 (✅ Complete)
- ✅ API integrations (6 services)
- ✅ 8-slide showcase
- ✅ Morph/fade transitions
- ✅ Full documentation

### Phase 2 (Next)
- ⬜ Gold standard templates (business, educational, marketing)
- ⬜ Slide-level customization
- ⬜ Theme support
- ⬜ Animation effects (entrance/exit via XML)

### Phase 3 (Future)
- ⬜ HTML → PPTX (Puppeteer rendering)
- ⬜ GSAP animation captures
- ⬜ Lottie → GIF pipeline
- ⬜ Video embedding

---

## 🤝 Contributing

This is built for Claude Code to use programmatically. To extend:

1. **Add new API**: Update `api_utils.py`
2. **Add new slide pattern**: Add to `showcase_presentation.py`
3. **Create gold standard**: Add to `.ai/gold-standards/`
4. **Document**: Update SHOWCASE.md

---

## 📝 License

Research files, APIs, and CDN libraries have their own licenses. See:
- [CDN Arsenal Reference](.ai/reference/CDN-ARSENAL-KB.md) for attribution
- Individual API terms of service

This codebase: MIT (or specify your license)

---

## 🙏 Credits

### APIs Used
- **Ideogram** - AI image generation
- **QuickChart.io** - Chart rendering
- **Unsplash** - Stock photography
- **Pexels** - Stock photography
- **DiceBear** - Avatar generation
- **Mermaid.ink** - Diagram rendering

### Libraries
- **python-pptx** - PowerPoint file generation
- **lxml** - XML manipulation

---

## 📧 Support

For issues or questions:
1. Check [SHOWCASE.md](.ai/showcase/SHOWCASE.md) for capabilities
2. Review [Skill Definition](.ai/skills/presentation-generator.md) for usage
3. Test APIs with `python api_utils.py`
4. Open an issue (if using Git)

---

**Version**: 1.0.0
**Created**: February 14, 2026
**Built with**: Claude Code & python-pptx
**Powered by**: Ideogram, QuickChart, Unsplash, Pexels, DiceBear, Mermaid
