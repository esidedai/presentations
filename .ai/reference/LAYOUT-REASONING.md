# Layout Reasoning Spec v2.0

**Purpose:** A thinking framework for solving multi-format layout problems. Use this before writing CSS.

**When to use:** Any time content designed for one canvas shape must fit a different shape without losing information or readability.

---

## The Core Insight

**Layout problems are Tetris problems, not font problems.**

When content doesn't fit, the instinct is to shrink fonts. This is almost always wrong. The real solution is to rearrange pieces.

```
WRONG INSTINCT:          RIGHT INSTINCT:
"Make it smaller"        "Rearrange the pieces"
     ↓                        ↓
  7px fonts              Same fonts, better Tetris
  Unreadable             Readable
```

---

## The Two Dimensions

Layout has two dimensions. Most people only think about one.

### Vertical Dimension (Height)

> "Match pieces by HEIGHT so rows don't have dead space."

| Pairing | Result |
|---------|--------|
| Tall + Tall | ✓ Balanced |
| Short + Short | ✓ Balanced |
| Tall + Short | ✗ Dead space below short piece |

### Horizontal Dimension (Width)

> "Match WIDTH-HUNGRY content to WIDER columns."

| Content Type | Width Need | Column Preference |
|--------------|------------|-------------------|
| Pills, tags, cards | Width-hungry | Wider column |
| Wrapped text, grids | Width-hungry | Wider column |
| Short text lines | Width-indifferent | Either |
| Checklists, activities | Width-indifferent | Narrower is fine |

**The Two-Dimension Rule:**
1. Step 4 matches pieces by HEIGHT
2. Step 4b assigns positions by WIDTH
3. Both dimensions matter

---

## The Six-Step Process

### Step 1: Measure the Pieces

Before touching layout, measure each content block's height and width flexibility.

**Height categories:**

| Category | Height | Examples |
|----------|--------|----------|
| Tiny | < 50px | 4 pills, single line header |
| Short | 50-80px | 4-item checklist, small tag cloud |
| Medium | 80-140px | Paragraph, 3 h4+p pairs |
| Tall | 140-200px | 6-item list, 2×2 card grid |
| Very tall | > 200px | Large tables, multi-section blocks |

**Width flexibility:**

| Flexibility | Behavior | Examples |
|-------------|----------|----------|
| Fixed width | Breaks if narrowed | Wide tables, code blocks |
| Width-hungry | Works narrow but cramps | Pills, tags, card grids |
| Width-indifferent | Reads fine either way | Checklists, short text lines |
| Stackable | Can go vertical | Icon + text pairs |

**Create a piece inventory:**

```
| Piece | Height | Width Need | Notes |
|-------|--------|------------|-------|
| Header | 75px | Fixed | Full width always |
| Summary | 90px | Prefers width | Narrative anchor |
| Activities | 80px | Indifferent | 4 short lines |
| Competencies | 60px | Hungry | 4 pills need room |
| Systems | 45px | Hungry | 4 pills need room |
| Responsibilities | 130px | Prefers | 6 bullets |
| Success Measures | 120px | Medium | 3 h4+p pairs |
| When It Stops | 180px | Hungry | 2×2 card grid |
| Value Prop | 110px | Prefers | Conclusion |
```

---

### Step 2: Identify the Culprits

Look for mismatches in your current layout.

**Height culprits (vertical dead space):**
- Tiny piece (40px) next to tall piece (140px) = 100px wasted
- "Lonely" piece that doesn't match anything nearby

**Width culprits (cramped content):**
- Pills squeezed into narrow column
- Card grid forced into insufficient width
- Tags wrapping awkwardly

**Example diagnosis:**

```
HEIGHT PROBLEM:
┌─────────────────┬───────────────────┐
│ Success Measures│ Systems           │
│ ████████████████│ ████              │  ← 80px wasted
│ ████████████████│     (empty)       │
│ ████████████████│                   │
└─────────────────┴───────────────────┘
Systems (40px) paired with Success (120px) = height mismatch

WIDTH PROBLEM:
┌─────────────────────┬─────────────────────┐
│ [pill][pill]        │ ✓ Activity 1        │
│ [pill][pill]        │ ✓ Activity 2        │  ← Pills cramped
│ (wrapping badly)    │ (excess space)      │  ← Activities don't need this width
└─────────────────────┴─────────────────────┘
Width-hungry pills in narrow column, width-indifferent activities in wide column
```

---

### Step 3: Classify Content Type

Not all content is equal. Some tells the story. Some is just reference.

| Type | Behavior | Can Move? | Examples |
|------|----------|-----------|----------|
| **Narrative** | Part of reading flow | Limited | Summary, responsibilities, value prop |
| **Reference** | Lookup info, not read linearly | Very flexible | Systems, tags, metadata |
| **Anchor** | Creates visual rhythm | Should stay prominent | Headers, section dividers |
| **Hero** | Centerpiece, deserves emphasis | Fixed position | Core capabilities section |
| **Conclusion** | Wraps up, calls to action | Should stay at end | Value proposition, metrics |

**Key insight:** Reference content can go almost anywhere — footer, sidebar, stacked with other reference content. It doesn't need prime real estate.

---

### Step 4: Find Natural Pairings (Height)

Pair pieces by HEIGHT first:

- Tall with tall
- Short with short  
- Tiny gets absorbed into something else (stacked)

**Good pairings:**

```
Competencies (60px) + Systems (45px) = ~105px stacked ✓ (both reference, both pills)
Success Measures (120px) + When It Stops (180px) = both tall ✓ (both trust story)
Summary alone, full width ✓ (narrative anchor)
Value Prop alone, full width ✓ (conclusion)
```

**Bad pairings:**

```
Systems (45px) + Success (120px) = height mismatch ✗
Activities (80px) + When It Stops (180px) = height mismatch ✗
```

---

### Step 4b: Assign Column Positions (Width)

After pairing, decide which piece goes LEFT vs RIGHT.

**The Rule:** Width-hungry content gets the wider column.

| Pairing | Left (Narrower) | Right (Wider) | Why |
|---------|-----------------|---------------|-----|
| Activities + Pills | Activities | Pills | Pills need breathing room |
| Success + Cards | Success | Cards | 2×2 grid needs width |
| Text + Tags | Text | Tags | Tags wrap awkwardly when narrow |

**Grid assignment:**

```css
/* Activities (narrow) | Pills (wide) */
.hero-row {
    grid-template-columns: 250px 1fr;
}

/* Success (medium) | Cards (wide) */
.trust-row {
    grid-template-columns: 290px 1fr;
}
```

**Exception:** If content has conceptual reading order (A then B), that can override width preference. But usually width wins.

---

### Step 5: Apply Layout Patterns

**Pattern A: Stack short pieces**

```
┌─────────────────┬───────────────────┐
│ SHORT PIECE 1   │                   │
│ [pills]         │  MEDIUM PIECE     │
│                 │  [text lines]     │
│ SHORT PIECE 2   │                   │
│ [pills]         │                   │
└─────────────────┴───────────────────┘
```

Stacking creates a "column" that matches the height of the paired content.

**Pattern B: Full-width anchors**

```
┌─────────────────────────────────────┐
│ FULL WIDTH ANCHOR (narrative)       │
├─────────────────┬───────────────────┤
│ LEFT            │ RIGHT             │
├─────────────────┴───────────────────┤
│ FULL WIDTH ANCHOR (conclusion)      │
└─────────────────────────────────────┘
```

Full-width sections create rhythm and breathing room.

**Pattern C: Hero section framing**

```
┌─────────────────────────────────────┐
│ ┌─────────────────────────────────┐ │
│ │  HERO CONTENT (background,      │ │
│ │  border, visual emphasis)       │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

The most important content gets visual framing — subtle background, border, padding.

**Pattern D: 2-column content flow**

```
┌─────────────────────────────────────┐
│ → Item 1          │ → Item 4        │
│ → Item 2          │ → Item 5        │
│ → Item 3          │ → Item 6        │
└─────────────────────────────────────┘
```

Long lists flow into columns (CSS `column-count: 2`).

**Pattern E: Push to fill**

```
┌─────────────────────────────────────┐
│ [Content that doesn't fill page]    │
│                                     │
│                                     │
│ ┌─────────────────────────────────┐ │
│ │ CONCLUSION (margin-top: auto)   │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

For lean content, push conclusion to bottom so page feels full, not sparse.

---

## Format Adaptation

### Fixed vs Flexible Dimensions

| Constraint | When to Use | Example |
|------------|-------------|---------|
| Fixed both | Exact print, slide decks | `width: 1280px; height: 720px` |
| Width fixed, height flexible | Documents, web | `width: 816px; min-height: 1056px; height: auto` |
| Both flexible | Responsive web | `max-width: 816px; width: 100%` |

**Default to width-fixed, height-flexible** unless you have a specific reason for fixed height.

### Format-Specific Breathing Room

Don't inherit cramped sizes from a tighter format.

| Format | Vertical Space | Implication |
|--------|----------------|-------------|
| Landscape (720px) | Tight | Use font floors |
| Portrait (1056px) | 47% more room | Go ABOVE floors |

**Example:**

| Element | Landscape | Portrait |
|---------|-----------|----------|
| Body text | 10px (floor) | 11-11.5px |
| Section headers | 12px | 14px |
| Activities | 11px | 13px bold |

> "Portrait has more vertical space. Use it. Don't copy landscape's cramped sizes."

---

## Density Adaptation

The same template can handle different content volumes.

### High Density (6+ responsibilities, 4 cards, rich narrative)

```css
.responsibilities {
    column-count: 2;
    column-gap: 28px;
}

.behavior-grid {
    grid-template-columns: 1fr 1fr;  /* 2×2 = 4 cards */
}

/* Tighter spacing throughout */
.resume-main-content {
    gap: 14px;
}
```

### Lean Density (4 responsibilities, 2 cards, simple logic)

```css
.responsibilities {
    column-count: 1;
    max-width: 600px;
}

.behavior-grid {
    grid-template-columns: 1fr 1fr;  /* Still 2 columns, but only 2 cards */
}

/* Generous spacing, push footer down */
.resume-main-content {
    gap: 16px;
}

.value-proposition {
    margin-top: auto;
}
```

**The principle:** Dense content compresses. Lean content spreads. Same template, different parameters.

---

## Anti-Patterns

### ❌ Shrinking fonts to fit

**Symptom:** 7-8px text, squinting required
**Real problem:** Layout mismatch, not content volume
**Fix:** Rearrange pieces, use patterns

### ❌ Cutting content to fit

**Symptom:** Removing bullets, shortening descriptions
**Real problem:** Inefficient space use
**Fix:** Rearrange first, condense only if layout is already optimal

### ❌ Pairing by position instead of fit

**Symptom:** "Left column has these because that's where they were in landscape"
**Real problem:** Treating layout as fixed instead of flexible
**Fix:** Re-derive pairings from height + width needs

### ❌ Ignoring width needs

**Symptom:** Pills cramped in narrow column, text swimming in wide column
**Real problem:** Only thinking about height, not width
**Fix:** Apply Step 4b — match width-hungry content to wider columns

### ❌ Inheriting cramped sizes

**Symptom:** Portrait uses same 10px text as landscape
**Real problem:** Not adapting to format's available space
**Fix:** Increase sizes proportionally for roomier formats

### ❌ One-size-fits-all for density

**Symptom:** Lean content looks sparse, dense content looks cramped
**Real problem:** Not adapting layout parameters to content volume
**Fix:** Use density-adaptive patterns

---

## Decision Tree

```
Content doesn't fit in new canvas shape?
│
├─► Did you measure piece heights AND widths?
│   └─► No → Go to Step 1
│
├─► Is there dead space next to short pieces?
│   └─► Yes → Stack short pieces together (Pattern A)
│
├─► Is width-hungry content in a narrow column?
│   └─► Yes → Swap column positions (Step 4b)
│
├─► Is reference content taking prime space?
│   └─► Yes → Move to edge or stack (Step 3)
│
├─► Are you inheriting cramped sizes from a tighter format?
│   └─► Yes → Increase sizes for the roomier format
│
├─► Is content sparse and page feels empty?
│   └─► Yes → Use generous spacing, push conclusion down (Pattern E)
│
├─► Is content dense and page feels cramped?
│   └─► Yes → Use 2-column flows, tighter spacing
│
└─► Still doesn't fit after all of the above?
    └─► NOW consider condensing (shorter sentences, not smaller fonts)
```

---

## Worked Example: Landscape → Portrait

**Landscape (1280×720):**

```
┌────────────┬────────────┬────────────────────┐
│ LEFT 280px │ CENTER 380 │ RIGHT ~585px       │
│ Competen.  │ Summary    │ When It Stops 2×2  │
│ Activities │ Handles    │ Value Prop         │
│ Success    │ Systems    │                    │
└────────────┴────────────┴────────────────────┘
```

**Step 1 - Measure:**

| Piece | Height | Width Need |
|-------|--------|------------|
| Systems | 45px | Hungry (pills) |
| Competencies | 60px | Hungry (pills) |
| Activities | 80px | Indifferent (text lines) |
| Summary | 90px | Prefers (narrative) |
| Success | 120px | Medium |
| Handles | 130px | Prefers (bullets) |
| When It Stops | 180px | Hungry (card grid) |
| Value Prop | 110px | Prefers (conclusion) |

**Step 2 - Identify culprits:**
- Systems (45px) paired with anything = height mismatch
- In landscape, pills were in narrow left column = width mismatch

**Step 3 - Classify:**
- Systems = REFERENCE (can move freely)
- Competencies = REFERENCE (can stack with Systems)
- Activities = NARRATIVE but width-indifferent
- Summary, Handles, Value Prop = ANCHORS (full width)
- Success + When It Stops = NARRATIVE (trust story, both tall)

**Step 4 - Height pairings:**
- Competencies (60) + Systems (45) = ~105px stacked ✓
- Activities (80) pairs with stacked column (~105) ✓
- Success (120) + When It Stops (180) = both tall ✓

**Step 4b - Width assignment:**
- Activities = width-indifferent → LEFT (narrow)
- Competencies + Systems = width-hungry → RIGHT (wide)
- Success = medium width need → LEFT
- When It Stops = width-hungry cards → RIGHT

**Step 5 - Apply patterns:**

```
┌─────────────────────────────────────┐
│ Summary (full width anchor)         │
├───────────────┬─────────────────────┤
│ Activities    │ Competencies        │  ← Width-indifferent LEFT
│ (narrow)      │ Systems             │  ← Width-hungry RIGHT
│               │ (stacked pills)     │
├───────────────┴─────────────────────┤
│ Handles (full width, 2-col flow)    │
├───────────────┬─────────────────────┤
│ Success       │ When It Stops       │  ← Both tall
│ (medium)      │ (card grid)         │  ← Cards get more width
├───────────────┴─────────────────────┤
│ Value Prop (full width conclusion)  │
└─────────────────────────────────────┘
```

**Format adaptation:**
- Increase font sizes (portrait has more room)
- Add hero section framing to Activities + Pills row
- Use `min-height: 1056px; height: auto` (flexible)

**Result:** All content fits, readable fonts, no dead space, width-hungry content has room.

---

## Voice and Layout Work Together

A subtle but real insight:

**Same layout, different voice:**

| Voice | Perception |
|-------|------------|
| "Core Competencies", "Systems Integration" | Feels cramped, corporate |
| "What It's Good At", "What Systems Does It Interact With" | Feels spacious, readable |

Human headings make the same whitespace feel more generous. Cookie-cutter headings make it feel tight.

**Implication:** Layout reasoning isn't just about pixels. The words affect how the layout *feels*.

---

## Checklist Before Finalizing Layout

### Vertical Dimension
- [ ] Measured all piece heights
- [ ] No tiny piece paired with tall piece
- [ ] Short pieces stacked together
- [ ] Tall pieces paired with tall pieces

### Horizontal Dimension
- [ ] Identified width-hungry content
- [ ] Width-hungry content in wider columns
- [ ] Width-indifferent content in narrower columns

### Format Adaptation
- [ ] Using appropriate dimension constraints (fixed vs flexible)
- [ ] Font sizes appropriate for format's available space
- [ ] Not inheriting cramped sizes from tighter format

### Density Adaptation
- [ ] High density: 2-column flows, tighter spacing
- [ ] Lean density: generous spacing, push conclusion down

### Patterns Applied
- [ ] Full-width anchors create rhythm
- [ ] Hero section has visual framing
- [ ] Reference content at edges/stacked
- [ ] Content preserved (rearranged, not cut)

---

## Version History

| Version | Changes |
|---------|---------|
| v2.0 | Added horizontal dimension (width needs). Step 4b for column assignment. Format adaptation (fixed vs flexible, breathing room). Density adaptation. Hero section pattern. Voice/layout connection. Updated anti-patterns and decision tree. |
| v1.0 | Initial spec. Five-step process, vertical matching, patterns, anti-patterns, decision tree. |
