# Utility Scripts

## Overview
Helper scripts for common tasks across all presentations.

---

## Available Scripts

### `asset-optimizer.py`
Optimize images for PowerPoint (resize, compress, format conversion)

**Usage**:
```bash
python scripts/asset-optimizer.py path/to/image.jpg
```

**What it does**:
- Resizes to max 1920px width
- Compresses to <5MB
- Converts to optimal format (PNG for graphics, JPG for photos)

---

### `bulk-resize.py`
Batch resize multiple images

**Usage**:
```bash
python scripts/bulk-resize.py path/to/folder/ --width 1920
```

---

### `template-generator.py`
Create a new presentation from template

**Usage**:
```bash
python scripts/template-generator.py business-standard 2026-03-new-event
```

---

### `presentation-stats.py`
Generate statistics about your presentations (total count, most-used assets, etc.)

**Usage**:
```bash
python scripts/presentation-stats.py
```

---

## Creating New Scripts

Add utility scripts here that help with:
- Asset management
- Batch operations
- Reporting
- Automation

Keep scripts generic and reusable across presentations.
