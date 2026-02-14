# Presentation Generator Skill

## Overview

The **Presentation Generator** skill enables Claude Code to create professional PowerPoint presentations programmatically from natural language requests.

---

## 🎯 What It Does

Generates complete `.pptx` presentations with:
- AI-generated images (Ideogram)
- Data visualizations (QuickChart.io charts)
- Stock photography (Unsplash/Pexels)
- Diagrams and flowcharts (Mermaid)
- Custom avatars (DiceBear)
- Professional formatting and transitions

---

## 💬 How to Use

### Basic Usage
```
Create a presentation about quarterly sales performance
```

### With Style Specification
```
Create a business presentation about AI adoption with 8 slides
```

### With Content Specifics
```
Create an educational presentation explaining the water cycle,
include diagrams and use a friendly tone
```

### Marketing Deck
```
Create a marketing deck for our new product launch,
include hero images and customer testimonials
```

---

## 🎨 Presentation Types

### Business Presentation
**Best for**: Quarterly reviews, sales pitches, board meetings
**Features**:
- QuickChart.io data visualizations
- Clean, professional typography
- Stock photography for credibility
- Morph transitions for data reveals
- Tables and bullet points

**Example Request**: "Create a business presentation on Q4 revenue growth"

---

### Educational Content
**Best for**: Training materials, tutorials, explainer decks
**Features**:
- Mermaid diagrams and flowcharts
- Step-by-step progressions
- Friendly fonts (rounded, approachable)
- Illustrations and icons
- Clear structure with summaries

**Example Request**: "Create an educational presentation on how neural networks work"

---

### Marketing Deck
**Best for**: Product launches, campaigns, client pitches
**Features**:
- AI-generated hero images (Ideogram)
- Bold, attention-grabbing typography
- Visual storytelling
- DiceBear team avatars
- High-impact visuals

**Example Request**: "Create a marketing deck for our SaaS product targeting CTOs"

---

## 🔧 Parameters (Optional)

You can specify:
- **Slides**: Number of slides (default: 8-10)
- **Style**: Business, Educational, Marketing, Minimal
- **Color Scheme**: Primary color preference
- **Tone**: Professional, Casual, Technical, Friendly
- **Include**: Specific elements (charts, diagrams, photos, etc.)

### Examples with Parameters
```
Create a 12-slide business presentation on AI adoption,
use blue color scheme, professional tone, include charts

Create a 6-slide educational presentation on Python basics,
casual tone, include code examples and diagrams
```

---

## 🚀 Behind the Scenes

When you make a request, the skill:

1. **Analyzes Your Request**
   - Extracts topic, type, tone, requirements
   - Determines optimal slide count and structure

2. **Generates Outline**
   - Creates logical flow of slides
   - Identifies where visuals are needed

3. **Fetches Visual Assets**
   - Calls Ideogram for custom images
   - Generates charts via QuickChart.io
   - Fetches stock photos from Unsplash/Pexels
   - Creates diagrams with Mermaid
   - Generates avatars via DiceBear

4. **Builds Presentation**
   - Creates slides with python-pptx
   - Applies formatting and layouts
   - Adds transitions (morph, fade)
   - Embeds all visual assets

5. **Exports**
   - Saves as `.pptx` file
   - Provides download link

---

## 📋 Slide Templates

The skill uses these slide templates:

### Title Slide
- Large heading
- Subtitle
- Optional avatar/logo
- Gradient or solid background

### Section Header
- Bold section title
- Optional decorative shape
- Transition to new topic

### Content Slide
- Title
- Bullet points or paragraphs
- Optional supporting image

### Data Slide
- Chart or graph
- Title and caption
- Key insights highlighted

### Diagram Slide
- Flowchart or process diagram
- Title and labels
- Arrows and connections

### Image Slide
- Full-bleed image or hero visual
- Overlay text (optional)
- Caption or credit

### Comparison Slide
- Two-column layout
- Side-by-side comparison
- Visual balance

### Closing Slide
- Summary or call-to-action
- Contact information
- Thank you message

---

## 🎨 Design Patterns

### Business
- **Fonts**: Segoe UI, Calibri
- **Colors**: Blues, grays, professional palette
- **Layout**: Clean, lots of whitespace
- **Visuals**: Charts, data, stock photos

### Educational
- **Fonts**: Poppins, Inter
- **Colors**: Warm, approachable tones
- **Layout**: Step-by-step, progressive
- **Visuals**: Diagrams, icons, illustrations

### Marketing
- **Fonts**: Bold sans-serif
- **Colors**: Brand colors, high contrast
- **Layout**: Dynamic, asymmetric
- **Visuals**: AI-generated, eye-catching

### Minimal
- **Fonts**: Simple, one or two max
- **Colors**: Monochrome or duotone
- **Layout**: Lots of negative space
- **Visuals**: Sparse, intentional

---

## 📊 API Integrations

### Ideogram (AI Images)
- **Usage**: Custom hero images, conceptual visuals
- **Quality**: High (professional photography style)
- **Speed**: ~5-10 seconds per image
- **Cost**: Paid API (per image)

### QuickChart.io (Charts)
- **Usage**: Bar, line, pie, doughnut charts
- **Quality**: High (Chart.js rendering)
- **Speed**: < 1 second
- **Cost**: Free (no auth needed)

### Unsplash (Stock Photos)
- **Usage**: Professional stock photography
- **Quality**: Very high (curated)
- **Speed**: ~2-3 seconds
- **Cost**: Free (with attribution)

### Pexels (Stock Photos)
- **Usage**: Backup for Unsplash
- **Quality**: High
- **Speed**: ~2-3 seconds
- **Cost**: Free

### DiceBear (Avatars)
- **Usage**: Team members, user profiles
- **Quality**: Good (consistent style)
- **Speed**: < 1 second
- **Cost**: Free (no auth needed)

### Mermaid (Diagrams)
- **Usage**: Flowcharts, sequence diagrams, etc.
- **Quality**: High (clean, professional)
- **Speed**: ~1-2 seconds
- **Cost**: Free (mermaid.ink)

---

## ⚙️ Configuration

### Required API Keys
Set in `.env` file:
```bash
IDEOGRAM_API_KEY=your_key_here
PEXELS_API_KEY=your_key_here
UNSPLASH_ACCESS_KEY=your_key_here
```

### Optional Settings
```python
# In your request, you can specify:
- max_slides: int (default: 10)
- style: "business" | "educational" | "marketing" | "minimal"
- color_scheme: "blue" | "purple" | "green" | "monochrome"
- include_charts: bool
- include_ai_images: bool
- include_diagrams: bool
```

---

## 🔍 Examples

### Example 1: Quick Business Deck
**Request**: "Create a presentation on Q4 sales results"

**Output**:
- 8 slides
- Title → Executive Summary → Q1-Q4 Charts (with morph) → Key Insights → Next Steps
- QuickChart bar/line charts
- Professional blue color scheme
- Fade/morph transitions

---

### Example 2: Educational Tutorial
**Request**: "Explain how machine learning works for beginners"

**Output**:
- 10 slides
- Title → What is ML? → Types of ML → How It Works (diagram) → Real Examples → Summary
- Mermaid flowcharts for concepts
- Friendly fonts and colors
- Step-by-step reveals

---

### Example 3: Marketing Launch
**Request**: "Create a launch deck for our AI writing assistant"

**Output**:
- 12 slides
- Hero image (Ideogram) → Problem → Solution → Features → Demo → Pricing → CTA
- AI-generated product visuals
- Bold typography
- High-impact transitions

---

## 🚨 Error Handling

### If API Fails
- **Ideogram down**: Falls back to Unsplash stock photos
- **Unsplash down**: Falls back to Pexels
- **QuickChart down**: Uses python-pptx native charts
- **Mermaid down**: Uses text-based process descriptions

### If Request is Unclear
The skill will:
1. Ask clarifying questions
2. Suggest a default structure
3. Proceed with best guess (business style, 8 slides)

---

## 📁 Output

### Generated Files
- `{topic}_presentation.pptx` - The main presentation
- `assets/` - Cached visual assets (for reuse)

### File Location
Default: `.ai/showcase/output/`

You can specify custom output path in request.

---

## 🎓 Tips for Best Results

### Be Specific
❌ "Create a presentation"
✅ "Create a business presentation on AI adoption with 8 slides, include charts"

### Specify Visuals
❌ "Make it look nice"
✅ "Include AI-generated hero images and data charts"

### Indicate Audience
❌ "Create a deck"
✅ "Create a deck for executive stakeholders (non-technical)"

### Provide Data (If Available)
❌ "Show our growth"
✅ "Show our growth: Q1: $12M, Q2: $19M, Q3: $15M, Q4: $25M"

---

## 🔄 Iterating

You can request modifications:
```
Make slide 3 more visual
Add a diagram on slide 5
Change the color scheme to purple
Add 2 more slides about competitive analysis
Regenerate slide 7 with a different image
```

---

## 🧪 Testing

To test the skill capabilities without making a full presentation:
```bash
cd .ai/showcase
python api_utils.py  # Tests all API integrations
```

To see the full showcase of capabilities:
```bash
cd .ai/showcase
python showcase_presentation.py  # Generates demo deck
```

Open `output/capabilities-showcase.pptx` to see what's possible.

---

## 📖 Reference

### Full Documentation
- **Showcase**: [../showcase/SHOWCASE.md](../showcase/SHOWCASE.md)
- **PowerPoint Guide**: [../reference/Programmatic Animated PowerPoint Guide.md](../reference/Programmatic%20Animated%20PowerPoint%20Guide.md)
- **CDN Arsenal**: [../reference/CDN-ARSENAL-KB.md](../reference/CDN-ARSENAL-KB.md)
- **API Utils**: [../showcase/api_utils.py](../showcase/api_utils.py)

### Gold Standards (Coming Soon)
- `../gold-standards/business-presentation.py`
- `../gold-standards/educational-content.py`
- `../gold-standards/marketing-deck.py`

---

## 🛠️ Technical Stack

- **python-pptx**: Core PowerPoint generation
- **lxml**: XML manipulation for transitions
- **requests**: API calls
- **Pillow**: Image processing
- **python-dotenv**: Environment variable management

---

## 🎯 Roadmap

### Phase 1 (Current)
- ✅ 8-slide showcase
- ✅ All API integrations
- ✅ Morph/fade transitions
- ✅ Documentation

### Phase 2 (Next)
- ⬜ Gold standard templates
- ⬜ Slide-level customization
- ⬜ Animation effects (entrance/exit)
- ⬜ Video embedding

### Phase 3 (Future)
- ⬜ HTML → PPTX (Puppeteer rendering)
- ⬜ GSAP animation captures
- ⬜ Lottie → GIF pipeline
- ⬜ Custom themes/templates

---

**Version**: 1.0.0
**Created**: February 14, 2026
**Author**: Claude Code
