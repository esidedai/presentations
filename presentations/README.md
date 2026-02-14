# Presentations

## Overview
Each presentation gets its own dated folder. This keeps everything organized and makes it easy to track versions, content, and assets specific to each event.

---

## Folder Naming Convention

```
YYYY-MM-descriptor/

Examples:
- 2026-02-live-event/
- 2026-03-investor-pitch/
- 2026-04-team-training/
- 2026-05-product-launch/
```

**Why date-first?**
- Sorts chronologically automatically
- Easy to find recent presentations
- Clear timeline of your presentation history

---

## Standard Presentation Structure

Each presentation folder should contain:

```
2026-XX-event-name/
├── content/
│   ├── outline.md           # Slide-by-slide outline
│   ├── script.md            # Speaker notes
│   ├── data.json            # Data for charts (if applicable)
│   └── research.md          # Background research/sources
│
├── assets-local/            # Assets ONLY for this presentation
│   ├── custom-diagram.png
│   ├── event-photo.jpg
│   └── ...
│
├── output/                  # Generated PPTX files (versioned)
│   ├── event-v1.0.pptx
│   ├── event-v1.1.pptx
│   └── event-FINAL.pptx
│
├── generate.py              # Script to generate this presentation
├── config.json              # Presentation settings (theme, colors, etc.)
└── README.md                # Presentation metadata
```

---

## Workflow

### 1. Create New Presentation
```bash
cd presentations
mkdir 2026-XX-your-event
cd 2026-XX-your-event
```

### 2. Create Content
- Write `content/outline.md` - what goes on each slide
- Add `content/script.md` - what you'll say
- Prepare `content/data.json` - any chart data

### 3. Add Local Assets
- Put event-specific images in `assets-local/`
- Reference shared brand assets from `../../assets/`

### 4. Generate Presentation
```bash
python generate.py
```

### 5. Iterate
- Make changes to content or generate.py
- Re-run `python generate.py`
- Output saves as new version automatically

---

## Version Control

### Version Naming
- `v1.0.pptx` - First complete draft
- `v1.1.pptx` - Minor edits, content tweaks
- `v2.0.pptx` - Major revision
- `FINAL.pptx` - What you actually presented
- `FINAL-EDITED.pptx` - Post-presentation updates

### When to Version
- After each major content change
- Before sharing with stakeholders
- Before the actual presentation (save as FINAL)

---

## Best Practices

1. **One folder per presentation** - Don't mix events
2. **Keep content separate from code** - `content/` vs `generate.py`
3. **Use relative paths** - `../../assets/` not absolute paths
4. **Document decisions** - Update README.md with notes about what worked/didn't
5. **Archive after event** - Move old presentations to `archive/` folder

---

## Templates

Instead of starting from scratch, copy a template:

```bash
cp -r ../templates/business-standard 2026-XX-your-event
```

Then customize the content and settings.

---

**Keep presentations isolated** - each event is self-contained and reproducible.
