# Assets Library

## Overview
This is your **shared asset library** - all reusable brand assets, team photos, illustrations, and stock imagery live here.

**Key Principle**: Each asset stored here once, referenced by all presentations.

---

## Directory Structure

### 📁 `brand/`
**Your brand identity assets**

- `logos/` - Logo variations (primary, white, icon-only, stacked)
- `colors/` - Brand color documentation
- `fonts/` - Typography guidelines

### 📁 `team/`
**People and team assets**

- `headshots/` - Individual team member photos (professional headshots)
- `group-photos/` - Team photos, office photos, event photos

### 📁 `illustrations/`
**Custom illustrations and graphics**

- `concepts/` - Abstract concept illustrations
- `icons/` - Custom icon set
- `diagrams/` - Reusable diagrams (architecture, process flows, etc.)

### 📁 `stock/`
**Licensed stock photography you own**

- `business/` - Business meeting, handshake, office scenes
- `technology/` - Tech equipment, code, servers, digital
- `lifestyle/` - People, activities, environments

### 📁 `templates/`
**Reusable visual templates**

- `backgrounds/` - Background images for slides
- `slide-layouts/` - Pre-designed slide layout templates

---

## Asset Naming Convention

### For Team Photos
```
firstname-lastname.png          (e.g., john-doe.png)
firstname-lastname-alt.png      (alternate pose)
role-firstname.png              (e.g., ceo-sarah.png)
```

### For Logos
```
logo-primary.png                (main logo)
logo-white.png                  (for dark backgrounds)
logo-black.png                  (for light backgrounds)
logo-icon.png                   (icon/mark only)
logo-stacked.png                (vertical layout)
```

### For Stock/Illustrations
```
category-description.png        (e.g., business-meeting.png)
category-description-001.png    (numbered variations)
```

---

## Best Practices

1. **One Source of Truth**: Assets live here, presentations reference them
2. **Optimize for PowerPoint**:
   - Max width: 1920px for full-slide images
   - Max size: <5MB per image
   - Format: PNG for logos/graphics, JPG for photos
3. **Version Control**: Keep original high-res files separately, store optimized versions here
4. **Consistent Naming**: Follow conventions above for easy searching
5. **Documentation**: Update `colors.md` and `fonts.md` when brand changes

---

## Usage in Presentations

Instead of copying assets to each presentation:

```python
# ✅ Good - Reference shared asset
slide.shapes.add_picture(
    "../../assets/brand/logos/logo-primary.png",
    ...
)

# ❌ Bad - Copying asset to presentation folder
# Creates duplicates, hard to update globally
```

---

**Maintain this library carefully** - it's the foundation of all your presentations.
