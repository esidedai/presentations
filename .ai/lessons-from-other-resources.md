# Lessons from Other Resources

**Purpose:** Transfer proven patterns from LinkedIn infographics and Resume-Vault to professional presentation generation.

**Last updated:** 2026-02-14

---

## Core Philosophy: Layout is Tetris, Not Font Shrinking

### The Critical Insight from LAYOUT-REASONING.md

**When content doesn't fit: REARRANGE, don't shrink.**

This is the #1 mistake in automated presentation generation:
- ❌ "Make text 7px so it fits" → Unreadable
- ✅ "Stack short pieces, pair by height, match width needs" → Professional

### The Two-Dimension Rule

**Vertical dimension (height):** Match pieces by height so rows don't have dead space
- Tall + Tall = ✓ Balanced
- Short + Short = ✓ Balanced
- Tall + Short = ✗ Dead space

**Horizontal dimension (width):** Match width-hungry content to wider columns
- Pills/tags = width-hungry → wider column
- Text lines = width-indifferent → narrower column is fine

**Application to slides:** When converting content outlines to slides, measure each content block's height AND width needs BEFORE laying out the slide.

---

## The Six-Step Layout Process (Apply to Every Slide)

### Step 1: Measure the Pieces
Before touching layout, categorize each content block:

**Height categories:**
- Tiny: < 50px (single line, small icon)
- Short: 50-80px (3-4 bullets, tag cloud)
- Medium: 80-140px (paragraph, small chart)
- Tall: 140-200px (6+ bullets, medium chart)
- Very tall: > 200px (large chart, diagram)

**Width flexibility:**
- Fixed width: breaks if narrowed (wide tables, code)
- Width-hungry: works narrow but cramps (pills, cards, grids)
- Width-indifferent: reads fine either way (text, checklists)

### Step 2: Identify Culprits
Look for mismatches:
- **Height problem:** 40px piece next to 140px piece = 100px wasted
- **Width problem:** Pills squeezed into narrow column, text swimming in wide column

### Step 3: Classify Content Type

| Type | Behavior | Can Move? | Examples |
|------|----------|-----------|----------|
| **Narrative** | Part of reading flow | Limited | Problem statement, solution description |
| **Reference** | Lookup info | Very flexible | Team info, tech stack, metadata |
| **Anchor** | Creates rhythm | Should stay prominent | Section headers, transitions |
| **Hero** | Centerpiece | Fixed position | Core value prop, key chart |
| **Conclusion** | Wraps up | Should stay at end | CTA, contact info |

**Key insight:** Reference content can go almost anywhere—sidebar, footer, stacked. It doesn't need prime real estate.

### Step 4: Find Natural Pairings (Height)
Pair pieces by HEIGHT first:
- Tall with tall
- Short with short
- Tiny gets absorbed (stacked)

### Step 4b: Assign Column Positions (Width)
After pairing, decide LEFT vs RIGHT:
- **Width-hungry content gets the wider column**
- Exception: Conceptual reading order (A then B) can override width preference

### Step 5: Apply Layout Patterns
See patterns below.

---

## Layout Patterns for Slides

### Pattern A: Stack Short Pieces
```
┌─────────────────┬───────────────────┐
│ SHORT PIECE 1   │                   │
│ [pills/tags]    │  MEDIUM PIECE     │
│                 │  [text/chart]     │
│ SHORT PIECE 2   │                   │
│ [pills/tags]    │                   │
└─────────────────┴───────────────────┘
```
**Use when:** Multiple short content blocks (tech stack, team roles, metrics)

### Pattern B: Full-Width Anchors
```
┌─────────────────────────────────────┐
│ FULL WIDTH ANCHOR (problem)         │
├─────────────────┬───────────────────┤
│ LEFT            │ RIGHT             │
├─────────────────┴───────────────────┤
│ FULL WIDTH ANCHOR (solution)        │
└─────────────────────────────────────┘
```
**Use when:** Creating rhythm between content-dense slides

### Pattern C: Hero Section Framing
```
┌─────────────────────────────────────┐
│ ┌─────────────────────────────────┐ │
│ │  HERO CONTENT (background,      │ │
│ │  border, visual emphasis)       │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```
**Use when:** Highlighting the most important content (value prop, key metric, solution diagram)

### Pattern D: 2-Column Content Flow
```
┌─────────────────────────────────────┐
│ → Item 1          │ → Item 4        │
│ → Item 2          │ → Item 5        │
│ → Item 3          │ → Item 6        │
└─────────────────────────────────────┘
```
**Use when:** Long lists that need to stay visible (responsibilities, features, benefits)

---

## Format Adaptation: Slide vs Portrait vs Landscape

### Fixed vs Flexible Dimensions

| Constraint | When to Use | Slide Example |
|------------|-------------|---------------|
| Fixed both | Exact slide dimensions | `width: 1280px; height: 720px` (16:9) |
| Width fixed, height flexible | Scrolling content (bad for slides) | Avoid for presentations |

**Default for slides:** Both dimensions FIXED. No scrolling.

### Format-Specific Breathing Room

**Don't inherit cramped sizes from a tighter format.**

| Format | Vertical Space | Font Strategy |
|--------|----------------|---------------|
| Landscape 16:9 (720px) | Tight | Use font floors (24pt min body) |
| Portrait 9:16 (1920px) | 167% more room | Go ABOVE floors (32pt+ body) |
| Square 1:1 (1080px) | 50% more than landscape | Scale up proportionally |

**Example from Resume-Vault:**
- Landscape resume (720px height): 10-12px body text (cramped but acceptable)
- Portrait resume (1056px height): 11.5-13px body text (47% more room = larger fonts)

**Application to presentations:**
- Standard 16:9 slide: 24pt body minimum, 36-48pt headers
- Vertical story format: 32pt body minimum, 54-72pt headers
- Square social post: 28pt body, 42-60pt headers

---

## Typography Hierarchy (From LinkedIn + Resumes)

### Professional Presentation Scale

```
Hero/Title:   Playfair Display Bold 72pt (#323130 dark gray)
Subtitle:     Inter SemiBold 36pt (#0078d4 brand blue)
Section Head: Inter Bold 32pt (#323130)
Body:         Inter Regular 24pt (#323130)
Caption:      Inter Regular 18pt (#8e8e93)
Code/Data:    Fira Code Regular 20-24pt (#323130)
```

**Why these sizes?**
- **72pt titles** are visible from the back of a room
- **36pt subtitles** create clear hierarchy without shouting
- **24pt body** is the FLOOR for readability on projectors
- **18pt captions** for source citations, footnotes

**Contrast with Resume-Vault landscape (720px):**
- Resume header: 28px (equivalent to ~37pt at 96dpi)
- Resume section: 16px (equivalent to ~21pt)
- Resume body: 12px (equivalent to ~16pt)

**Why smaller?** Resume is read at arm's length on screen. Presentation is viewed across a room. Scale accordingly.

---

## Content Density Adaptation

### High Density (6+ bullets, 4 charts, rich narrative)
```css
.bullet-list {
    column-count: 2;
    column-gap: 28px;
}

.card-grid {
    grid-template-columns: 1fr 1fr;  /* 2×2 = 4 cards */
}

/* Tighter spacing */
.slide-content {
    gap: 14px;
}
```

### Lean Density (3-4 bullets, 1-2 charts, simple message)
```css
.bullet-list {
    column-count: 1;
    max-width: 600px;
}

.card-grid {
    grid-template-columns: 1fr;  /* Single column, centered */
}

/* Generous spacing, center vertically */
.slide-content {
    gap: 24px;
    justify-content: center;
}
```

**The principle:** Dense content compresses. Lean content spreads. Same template, different parameters.

---

## Anti-Patterns (What NOT to Do)

### ❌ Shrinking Fonts to Fit
**Symptom:** 14px text on a slide meant for a projector
**Real problem:** Layout mismatch, not content volume
**Fix:** Rearrange pieces, use 2-column flow, or split into 2 slides

### ❌ Cutting Content to Fit
**Symptom:** Removing key bullets to make slide "cleaner"
**Real problem:** Inefficient space use
**Fix:** Rearrange first, condense only if layout is optimal

### ❌ Pairing by Position Instead of Fit
**Symptom:** "Left column has these because that's where they were in the outline"
**Real problem:** Treating layout as fixed instead of flexible
**Fix:** Re-derive pairings from height + width needs

### ❌ Ignoring Width Needs
**Symptom:** Pills/tags cramped in narrow column, text swimming in wide column
**Real problem:** Only thinking about height, not width
**Fix:** Match width-hungry content to wider columns

### ❌ Gray Backgrounds
**Symptom:** Using #f3f2f1 or #e5e7eb backgrounds
**Why wrong:** Projectors wash out gray, making it look dirty white
**Fix:** Use white (#ffffff) or brand colors only

### ❌ Unreadable Charts
**Symptom:** Chart.js default font sizes (12pt labels, 10pt axes)
**Real problem:** Not adapting chart config for presentation viewing distance
**Fix:** 28pt+ data labels, 22pt+ axis labels, 32pt+ titles

---

## Visual Toolkit Mapping (From LinkedIn to Presentations)

### CDN Arsenal for Presentations

| Presentation Need | Best Tool | Why | Source |
|-------------------|-----------|-----|--------|
| Charts | QuickChart.io | Advanced Chart.js configs, instant PNG | LinkedIn VISUAL-TOOLKIT |
| Diagrams | Mermaid | Text-to-diagram, version-controlled | LinkedIn + MEMORY.md |
| Icons | Font Awesome / Bootstrap Icons | 2000+ professional icons | LinkedIn VISUAL-TOOLKIT |
| Illustrations | unDraw / DrawKit SVGs | Brand-colorable, consistent | MEMORY.md assets |
| Photos | Unsplash / Pexels | Curated, professional | MEMORY.md |
| Custom images | Ideogram | AI-generated backgrounds, concepts | LinkedIn VISUAL-TOOLKIT |
| Hand-drawn feel | Rough.js | Humanize technical content | LinkedIn VISUAL-TOOLKIT |
| Stat animations | CountUp.js | Number reveals (interactive only) | LinkedIn VISUAL-TOOLKIT |

**Key difference from LinkedIn:**
- LinkedIn: 1080x1350px infographics for social media scroll-stopping
- Presentations: 1280x720px slides for room viewing and professional delivery

**Shared principles:**
1. Professional assets FIRST (don't generate what already exists)
2. Use CDN tools for advanced features (don't settle for basic CSS)
3. Match tool to insight (not tool to "what looks cool")

---

## The Brief Process (Adapted from LinkedIn INFOGRAPHIC-BRIEF-PROCESS.md)

### Why This Matters for Presentations

**Default behavior:** Claude reads content outline → jumps to slide generation → produces competent but generic output

**Problem:** Signal degradation through delegation. Surface facts transfer. Deeper insight does not.

**Solution:** Excavation BEFORE production.

### The Process (Adapted for Presentations)

#### Phase 1: Claude Reads Outline and Proposes (10 min)
Claude reads the presentation outline and proposes:
- What are the 3 deepest insights?
- What is the core narrative arc?
- What emotional journey should the audience take?

**Not:** "What are the biggest data points?"
**But:** "What would make the CEO stop mid-meeting and say 'wait, explain that'?"

#### Phase 2: Expert Reacts (5 min)
User provides honest pushback:
- "That's surface. The deeper point is..."
- "You're describing the symptom. The cause is..."
- "You defaulted to data. The real insight is about [human behavior]"

#### Phase 3: Claude Goes Deeper (10 min)
Claude tries again:
- Questions first instinct
- Looks for the layer underneath
- Finds tension, counterintuitive angles
- Proposes insights harder to visualize but more worth saying

#### Phase 4: Convergence (5 min)
User and Claude converge on insights that pass:
- **Screenshot test:** Would someone photo this slide and send it to a colleague?
- **Attribution test:** Could this only come from this specific experience?
- **Discomfort test:** Does this challenge a default assumption?

#### Phase 5: Write the Slide Story (15 min)
Before any HTML/CSS, write narrative backbone (150-300 words per slide):
1. **Opening frame:** What does viewer see first? What emotion?
2. **The argument:** What is the one claim this slide makes?
3. **The evidence:** What data/example supports it?
4. **The reframe:** What did they believe before? What after?
5. **The residue:** What one sentence do they remember tomorrow?
6. **Visual direction:** What tool? What mood? Why does this visual serve the insight?

#### Phase 6: Build (30-60 min per slide)
With slide story written and approved, build using full toolkit.

**Every design choice traces back to the story.**

---

## Validation Scorecard (Adapted from LinkedIn FACTORY-SPEC.md)

Fill this out AFTER building each slide. Gold standard forcing function.

| Dimension | Question | How to Score |
|-----------|----------|-------------|
| **Toolkit depth** | Which CDN tools were used beyond fonts and CSS? | List every tool. "Fonts + CSS" alone = failure |
| **Asset integration** | Was a professional asset used (unDraw, DrawKit, team photo)? | Y/N + rationale |
| **Insight fidelity** | Does the visual make this specific insight sharper? Or could this layout work with any data? | 1-5 (5 = only works for this insight) |
| **Screenshot test** | Would an executive screenshot this slide? | Y/N, be honest |
| **Readability** | All text 24pt+? Charts readable from 10 feet? | Y/N |
| **Novelty** | Seen this exact layout 1,000 times before? | 1-5 (5 = fresh approach) |
| **Visual/text ratio** | Communicating visually, or text in colored boxes? | 1-5 (5 = visual IS the argument) |

**Minimum bar for professional quality:**
- No dimension below 3/5
- Toolkit depth must include at least one JS-based viz or professional asset
- Screenshot test must be Y
- Readability must be Y

---

## Layout Examples from Resume-Vault

### Three-Column Grid (1280x720 landscape)
**From:** `bank-reconciliation-specialist.html`, `customer-outreach-agent.html`

```css
.resume-main-content {
    display: grid;
    grid-template-columns: 280px 380px 1fr;  /* Left | Center | Right */
    gap: 15px;
    padding: 15px;
    height: 635px;  /* 720 - 85px header */
}
```

**Why this works:**
- **Left (280px):** Narrow column for width-indifferent content (competencies tags, activities checklist)
- **Center (380px):** Medium column for narrative (summary, responsibilities)
- **Right (1fr):** Flexible wide column for width-hungry content (business value grid, card layouts)

**Height pairing:**
- Competencies (60px) + Activities (80px) = ~140px total, pairs with center Summary (90px) + some of Responsibilities
- Success Measures (120px) in left pairs with tall content in center

**Application to presentations:** Use similar 3-column grid for content-dense slides where left = reference, center = narrative, right = visual evidence.

### Skill Tags Grid Pattern
```css
.skill-tags {
    display: grid;
    grid-template-columns: 1fr 1fr;  /* 2 columns */
    gap: 6px;
}

.skill-tag {
    background: #7c2d12;  /* Brand color */
    color: white;
    padding: 6px 8px;
    border-radius: 12px;
    font-size: 10px;
    font-weight: 500;
    text-align: center;
}
```

**Application to presentations:** Tech stack, feature lists, competency tags. Scale up font size (18-20pt for slides vs 10px for resumes).

### Business Value Grid (2x2 cards)
```css
.business-value-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
}

.value-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 6px;
    padding: 6px;
}
```

**Application to presentations:** Benefits breakdown, feature comparison, framework quadrants. Increase padding (20-30px for slides vs 6px for resumes).

---

## Style Rules (From LinkedIn STYLE-RULES.md)

### Banned Patterns (Apply to Presentation Text)

**Punctuation:**
- ❌ Em dash (—) → Use comma or restructure
- ❌ Exclamation point (!) → Never
- ❌ Ellipsis (...) → Never

**Contrast frames:**
- ❌ "Not X, but Y"
- ❌ "Your team isn't slow. They're stuck."

**Scripted pivots:**
- ❌ "Here's the thing"
- ❌ "Let that sink in"

**Hype language:**
- ❌ "game-changer", "revolutionary", "transform", "unlock", "disrupt"

**Minimizers:**
- ❌ "simply", "just", "obviously", "clearly", "easily"

### Language Rules

**Tone:**
- Direct, warm, honest
- Short sentences (no more than 25 words)
- Concrete over abstract
- Examples over principles

**Application to slides:**
- Bullet points: 1 line max, action-oriented
- Headers: Clear claim, not vague topic
- Data labels: Specific units, formatted clearly

---

## File Structure (Transferred from LinkedIn + Resume-Vault)

### Resume-Vault Pattern
```
Resume-Vault/
├── geomark/
│   ├── resumes/
│   │   ├── bank-reconciliation-specialist.html           # Landscape
│   │   └── bank-reconciliation-specialist-portrait.html  # Portrait
│   └── reference/
│       └── improved-resume-example.html
```

**Key insight:** Separate landscape and portrait versions. Don't try to make one responsive file do both.

### LinkedIn Pattern
```
LinkedIn/
├── Infographics/
│   └── article-slug/
│       ├── brief.md                        # Excavation process output
│       ├── 01-title-type.html              # Numbered, sequential
│       ├── 02-title-type.html
│       ├── assets/
│       │   └── bg-concept.png              # Generated Ideogram backgrounds
│       └── post-text.md                    # Accompanying LinkedIn post text
```

### Recommended Pattern for Presentations
```
presentations/YYYY-MM-event/
├── brief.md                                # Excavation process (narrative arc, insights)
├── content/
│   └── outline.md                          # Slide-by-slide content plan
├── slides/
│   ├── 01-title.html                       # Individual slide files for iteration
│   ├── 02-problem.html
│   ├── 03-solution.html
│   └── ...
├── assets-local/                           # Event-specific assets
│   ├── Team-Pictures/
│   └── Title-Slide-Illustration.png
├── generate.py                             # Final assembly script
└── output/
    └── presentation.pptx                   # Assembled final deck
```

**Why individual slide files?**
1. Easier to iterate on single slide without re-running entire deck
2. Can test in browser with proper dimensions
3. Can export individual slides as PNG for sharing
4. Mirrors LinkedIn infographic pattern (proven workflow)

---

## Decision Tree (Adapted from LAYOUT-REASONING.md)

```
Content doesn't fit on slide?
│
├─► Did you measure piece heights AND widths?
│   └─► No → Go to Step 1 (measure)
│
├─► Is there dead space next to short pieces?
│   └─► Yes → Stack short pieces together
│
├─► Is width-hungry content in narrow column?
│   └─► Yes → Swap column positions
│
├─► Is reference content taking prime space?
│   └─► Yes → Move to sidebar or footer
│
├─► Are you using font sizes below 24pt for body text?
│   └─► Yes → Increase sizes, rearrange if needed
│
├─► Is content sparse and slide feels empty?
│   └─► Yes → Use generous spacing, center vertically
│
├─► Is content dense and slide feels cramped?
│   └─► Yes → Use 2-column flows, split into 2 slides
│
└─► Still doesn't fit after all of the above?
    └─► NOW consider splitting into 2 slides (not smaller fonts)
```

---

## Voice and Layout Work Together

**Subtle but real insight from LAYOUT-REASONING.md:**

| Voice | Perception |
|-------|------------|
| "Core Competencies", "Systems Integration" | Feels cramped, corporate |
| "What It's Good At", "What Systems Does It Interact With" | Feels spacious, readable |

**Application to presentations:**
- Header: "Key Takeaways" vs "What You'll Remember Tomorrow" (human > corporate)
- Bullet: "Reduces coordination overhead" vs "Eliminates 5 handoffs that slow you down" (specific > abstract)

The words affect how the layout *feels*.

---

## Checklist Before Finalizing Any Slide

### Vertical Dimension
- [ ] Measured all piece heights
- [ ] No tiny piece paired with tall piece
- [ ] Short pieces stacked together
- [ ] Tall pieces paired with tall pieces

### Horizontal Dimension
- [ ] Identified width-hungry content
- [ ] Width-hungry content in wider columns
- [ ] Width-indifferent content in narrower columns

### Typography
- [ ] All body text 24pt minimum
- [ ] All headers 32pt minimum
- [ ] Chart labels 28pt minimum
- [ ] Using professional font hierarchy (Inter + Playfair Display)

### Brand Consistency
- [ ] eSided logo at top (0.6", 0.35" from top-left, 1.5" width)
- [ ] Website info at bottom right (12pt Inter)
- [ ] Curved decorative shapes (top blue, left purple, bottom blue)
- [ ] White background (never gray)

### Asset Usage
- [ ] Checked `assets/illustrations/concepts/` for existing illustrations
- [ ] Checked `assets-local/` for project-specific assets
- [ ] Used professional assets before generating new ones
- [ ] Professional photos over stock illustrations where appropriate

### Toolkit Depth
- [ ] Used at least one CDN tool beyond fonts (Chart.js, Mermaid, icons)
- [ ] Used professional asset (unDraw, DrawKit, team photo, QuickChart)
- [ ] Visual serves the insight (not decoration)

### Validation
- [ ] Screenshot test: Would exec share this slide?
- [ ] Readability test: Can text be read from 10 feet?
- [ ] Novelty test: Fresh approach, not training data default?
- [ ] Insight fidelity: Visual makes THIS insight sharper?

---

## Key Takeaways

1. **Layout is Tetris:** Rearrange pieces by height and width needs. Never shrink fonts to fit.

2. **Two dimensions matter:** Match pieces by HEIGHT (vertical), then assign positions by WIDTH (horizontal).

3. **Format adaptation:** Don't inherit cramped sizes. Slides have different viewing distance than resumes. Scale accordingly.

4. **Brief before build:** Excavate insights BEFORE production. 20 minutes of thinking beats 2 hours of rework.

5. **Professional assets first:** Check existing assets before generating. Never generate what already exists.

6. **Toolkit depth:** Use CDN arsenal. "Fonts + CSS" alone = amateur hour.

7. **Voice matters:** Human headings make whitespace feel generous. Corporate jargon makes it feel cramped.

8. **Validation scorecard:** Fill it out. Be honest. No dimension below 3/5.

---

## What to Document Next

As you build presentations, capture:
1. **Slide patterns that work:** New layout patterns specific to presentation content
2. **QuickChart configs:** Proven chart configurations for readability at distance
3. **Mermaid templates:** Diagram patterns for common presentation concepts
4. **Asset sources:** Where you found great illustrations, what keywords worked
5. **Mistakes:** What looked good in HTML but failed in PowerPoint export

**Where:** `presentations/.ai/patterns/` directory
- `slide-layouts.md` - Proven layout patterns
- `chart-configs.md` - QuickChart configurations
- `diagram-templates.md` - Mermaid patterns
- `asset-library.md` - Curated asset sources
- `export-gotchas.md` - HTML → PowerPoint conversion issues
