# Presentation Templates

## Overview
Reusable presentation templates for different use cases. Copy a template to start a new presentation quickly.

---

## Available Templates

### 📊 `business-standard/`
**For**: Quarterly reviews, sales pitches, business updates

**Features**:
- Clean, professional design
- Data visualization focused
- Chart-heavy layouts
- Professional color scheme (blues, grays)

**Best for**: Executives, stakeholders, board meetings

---

### 📚 `educational/`
**For**: Training, tutorials, workshops, course content

**Features**:
- Friendly, approachable design
- Diagram and illustration focused
- Step-by-step layouts
- Warm, inviting colors

**Best for**: Team training, customer onboarding, educational events

---

### 🚀 `marketing/`
**For**: Product launches, campaigns, brand presentations

**Features**:
- Bold, attention-grabbing design
- Visual storytelling focus
- Hero image layouts
- Brand color emphasis

**Best for**: Product launches, client pitches, marketing campaigns

---

## How to Use

### Copy a Template
```bash
cd presentations
cp -r ../templates/business-standard 2026-XX-your-event
cd 2026-XX-your-event
```

### Customize
1. Update `config.json` with your settings
2. Edit `content/outline.md` with your content
3. Modify `generate.py` if needed
4. Run `python generate.py`

---

## Creating Your Own Template

After creating a successful presentation:

1. **Copy to templates**:
   ```bash
   cp -r presentations/2026-XX-event templates/my-custom-template
   ```

2. **Clean it up**:
   - Remove event-specific content
   - Replace with placeholder text
   - Document customization points in README

3. **Make it reusable**:
   - Parameterize colors, fonts in `config.json`
   - Add clear comments in `generate.py`
   - Include example `outline.md`

---

## Template Structure

Each template should contain:
```
template-name/
├── content/
│   ├── outline-example.md      # Example outline
│   └── data-example.json       # Example data
├── generate.py                 # Generation script
├── config.json                 # Default settings
└── README.md                   # Template documentation
```

---

**Templates save time** - invest in building good ones after your first few presentations.
