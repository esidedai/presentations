# Programmatic Animated PowerPoint Generation: python-pptx, PptxGenJS, and Workaround Pipelines

## 1. python-pptx: Capabilities and Limitations

### What It Can Do Natively

python-pptx is a mature Python library for creating, reading, and updating `.pptx` files. Its documented feature set includes:[^1]

- **Slides**: Add slides from any slide layout, reorder slides, duplicate slides
- **Text**: Populate placeholders, add textboxes, control font size/bold/italic/color, paragraph alignment, bullet levels, hyperlinks
- **Images**: Add images at arbitrary position and size (PNG, JPEG, GIF, BMP, TIFF)
- **Shapes**: Add auto shapes (rectangles, circles, flowchart shapes, arrows, callouts, etc.), group shapes, freeform shapes
- **Tables**: Create tables with custom row/column dimensions and cell formatting
- **Charts**: Column, bar, line, pie, doughnut, XY scatter, and bubble charts with data labels, legends, and formatting[^1]
- **Video**: Embed video files (MP4, MOV, etc.) via `shapes.add_movie()` with poster frames[^2]
- **Properties**: Access/change core document properties (title, subject, author)
- **Slide masters and layouts**: Full support for master slides and layout inheritance
- **Shadow**: Basic shadow formatting on shapes via `shape.shadow` (with caveats—the API is partially implemented)[^3]

### What It Cannot Do

This is the critical gap for your use case:

- **No entrance/exit animations**: python-pptx has no API for adding shape-level animations (Fly In, Fade, Appear, Wipe, motion paths, etc.). This was formally confirmed in a January 2026 feature request.[^4]
- **No slide transitions**: There is no built-in method to add slide transitions (Fade, Push, Morph, etc.).[^5]
- **No morph transitions**: Morph is not exposed in the API. The XML structure has been reverse-engineered (see workarounds below), but there's no native support.[^6]
- **No timed builds**: No way to set "After Previous" or "With Previous" animation sequencing.
- **No motion paths**: No API for custom motion path animations.
- **Limited effect support**: Shadow is partially implemented; glow, reflection, and 3D effects are mostly out of scope.[^3]

### The XML Escape Hatch

python-pptx is built on `lxml` and exposes the underlying XML element tree via the `.element` property on every object. This is the foundation for all workarounds:[^7][^8]

```python
# Access raw XML of a slide
slide_element = slide.element
# Use XPath to find elements
results = slide_element.xpath('.//p:transition', namespaces=nsmap)
# Insert new elements using lxml methods
from lxml import etree
child = etree.SubElement(parent, '{namespace}tagname')
# Or use addnext/addprevious for precise placement
existing_element.addnext(new_element)
```

***

## 2. PptxGenJS: Capabilities and Limitations

### What It Can Do Natively

PptxGenJS is a JavaScript library for generating `.pptx` files from Node.js, React, Angular, or the browser:[^9]

- **Text**: Rich text with fonts, colors, sizes, bold/italic/underline, bullet points, alignment, RTL text, Asian fonts
- **Images**: PNG, JPEG, GIF (including **animated GIFs**), SVG, from URL, path, or base64 data[^10]
- **Shapes**: Rectangles, circles, lines, arrows, and all standard auto shapes with fills, borders, shadows
- **Tables**: Full table support with cell formatting, auto-paging (overflow to new slides)[^9]
- **Charts**: Bar, column, line, area, pie, doughnut, scatter, bubble, and combo charts
- **Media**: Video (MP4, MOV), audio (MP3, WAV), and YouTube embeds (Microsoft 365 only)[^11]
- **SVG support**: Native SVG embedding[^9]
- **HTML tables**: Convert HTML `<table>` elements directly to PowerPoint slides[^12]
- **Slide Masters**: Define reusable slide master templates for branding[^9]
- **Export options**: Download as `.pptx`, export as base64, Blob, Buffer, or Node stream[^9]

### What It Cannot Do

- **No slide transitions**: There is no API for adding slide transitions. This has been requested on Stack Overflow with no resolution.[^13]
- **No shape animations**: No entrance, exit, emphasis, or motion path animations.[^13]
- **No morph transitions**: Not supported.
- **No timed builds or sequencing**: No animation timeline control.

### python-pptx vs. PptxGenJS Comparison

| Feature | python-pptx | PptxGenJS |
|---|---|---|
| Language | Python | JavaScript (Node.js + Browser) |
| Slides, text, shapes | ✅ Full | ✅ Full |
| Tables | ✅ | ✅ (with auto-paging) |
| Charts | ✅ (bar, line, pie, scatter) | ✅ (bar, line, pie, scatter, combo) |
| Images (PNG/JPEG) | ✅ | ✅ |
| Animated GIFs | ⚠️ Embeds as static | ✅ Animated in M365[^9] |
| SVG | ❌ Not native | ✅ Native[^9] |
| Video embedding | ✅ `add_movie()`[^2] | ✅ `addMedia()`[^11] |
| YouTube embed | ❌ | ✅ (M365 only)[^11] |
| HTML table → slides | ❌ | ✅ `tableToSlides()`[^12] |
| Slide transitions | ❌ (XML workaround) | ❌ |
| Shape animations | ❌ (XML workaround) | ❌ |
| Morph transitions | ❌ (XML workaround) | ❌ |
| Raw XML access | ✅ Full lxml access | ❌ Limited |
| Slide masters | ✅ | ✅ |
| Read existing .pptx | ✅ Full round-trip[^1] | ❌ Create only |

**Key insight**: Neither library natively supports animations or transitions. python-pptx has the edge for workarounds because of full lxml XML access. PptxGenJS has the edge for media richness (animated GIFs, SVGs, YouTube).

***

## 3. Workarounds for Animation

### Workaround 1: Raw XML Injection for Slide Transitions (python-pptx)

The OOXML format stores transitions as `<p:transition>` elements within each slide's XML. You can inject these directly:[^5]

```python
from pptx import Presentation
from lxml import etree

prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts)

# Define transition XML (e.g., Fade)
transition_xml = '''
<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">
  <mc:Choice xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main" Requires="p14">
    <p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
                  spd="slow" p14:dur="2000">
      <p:fade />
    </p:transition>
  </mc:Choice>
  <mc:Fallback>
    <p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="slow">
      <p:fade />
    </p:transition>
  </mc:Fallback>
</mc:AlternateContent>
'''
transition_element = etree.fromstring(transition_xml)
slide.element.append(transition_element)
prs.save('with_transition.pptx')
```

This technique is confirmed working by multiple developers including the md2pptx project maintainer.[^6][^5]

### Workaround 2: Morph Transition via XML (python-pptx)

Morph transitions are PowerPoint's most powerful pseudo-animation. The key discovery: morph requires two slides with identically-named shapes at different positions/sizes. The XML difference is a single block added to slide 2:[^6]

```python
morph_xml = '''
<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">
  <mc:Choice xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main"
             Requires="p159">
    <p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
                  xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main"
                  spd="slow" p14:dur="2000">
      <p159:morph option="byObject"/>
    </p:transition>
  </mc:Choice>
  <mc:Fallback>
    <p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="slow">
      <p:fade/>
    </p:transition>
  </mc:Fallback>
</mc:AlternateContent>
'''
```

**Critical requirement**: Shapes on both slides must share the same name (as seen in PowerPoint's Selection Pane). In python-pptx, set `shape.name` identically on both slides. Unfilled placeholders can break morph.[^6]

**Morph as pseudo-animation strategy**: An AI agent can generate a sequence of 5–20 slides where each slide moves/resizes/recolors elements incrementally, then apply morph transitions between them. The result looks like a smooth animation in slideshow mode.

### Workaround 3: Entrance/Exit Animations via Raw XML (python-pptx)

Shape-level animations are stored in the `<p:timing>` element within a slide. The XML is considerably more complex than transitions, involving timing nodes (`p:par`, `p:seq`, `p:cTn`), animation behaviors, and target elements. Here's a simplified example for a Fade entrance animation:[^2][^4]

```python
timing_xml = '''
<p:timing xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:tnLst>
    <p:par>
      <p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">
        <p:childTnLst>
          <p:seq concurrent="1" nextAc="seek">
            <p:cTn id="2" dur="indefinite" nodeType="mainSeq">
              <p:childTnLst>
                <p:par>
                  <p:cTn id="3" fill="hold">
                    <p:stCondLst>
                      <p:cond delay="0"/>
                    </p:stCondLst>
                    <p:childTnLst>
                      <p:par>
                        <p:cTn id="4" fill="hold">
                          <p:stCondLst>
                            <p:cond delay="0"/>
                          </p:stCondLst>
                          <p:childTnLst>
                            <p:par>
                              <p:cTn id="5" presetID="10" presetClass="entr"
                                     presetSubtype="0" fill="hold"
                                     nodeType="afterEffect">
                                <p:stCondLst>
                                  <p:cond delay="0"/>
                                </p:stCondLst>
                                <p:childTnLst>
                                  <p:set>
                                    <p:cBhvr>
                                      <p:cTn id="6" dur="1" fill="hold">
                                        <p:stCondLst>
                                          <p:cond delay="0"/>
                                        </p:stCondLst>
                                      </p:cTn>
                                      <p:tgtEl>
                                        <p:spTgt spid="SHAPE_ID"/>
                                      </p:tgtEl>
                                      <p:attrNameLst>
                                        <p:attrName>style.visibility</p:attrName>
                                      </p:attrNameLst>
                                    </p:cBhvr>
                                    <p:to><p:strVal val="visible"/></p:to>
                                  </p:set>
                                  <p:animEffect transition="in" filter="fade">
                                    <p:cBhvr>
                                      <p:cTn id="7" dur="500"/>
                                      <p:tgtEl>
                                        <p:spTgt spid="SHAPE_ID"/>
                                      </p:tgtEl>
                                    </p:cBhvr>
                                  </p:animEffect>
                                </p:childTnLst>
                              </p:cTn>
                            </p:par>
                          </p:childTnLst>
                        </p:cTn>
                      </p:par>
                    </p:childTnLst>
                  </p:cTn>
                </p:par>
              </p:childTnLst>
            </p:cTn>
            <p:prevCondLst>
              <p:cond evt="onPrev" delay="0">
                <p:tgtEl><p:sldTgt/></p:tgtEl>
              </p:cond>
            </p:prevCondLst>
            <p:nextCondLst>
              <p:cond evt="onNext" delay="0">
                <p:tgtEl><p:sldTgt/></p:tgtEl>
              </p:cond>
            </p:nextCondLst>
          </p:seq>
        </p:childTnLst>
      </p:cTn>
    </p:par>
  </p:tnLst>
</p:timing>
'''
```

Replace `SHAPE_ID` with the shape's `sp` id (accessible via `shape.shape_id`). This is fragile but functional. The recommended approach for an AI agent: **create a helper function that generates the timing XML for common animation presets** (Fade=10, Fly=2, Wipe=22, Appear=1) and injects it.[^4][^2]

**Caveat**: When animations use non-OpenXML features (e.g., "Bounce end"), PowerPoint wraps `<p:timing>` in `<mc:AlternateContent>`, and python-pptx's `add_movie()` can conflict with existing timing elements, causing file corruption.[^14]

### Workaround 4: Pre-rendered Animated GIFs / MP4s

This is the most reliable approach for complex animations:

**Pipeline for an AI coding agent:**

1. **Generate the animation** in HTML/CSS/JS (using GSAP, D3, Chart.js, etc.)
2. **Capture frames** using Puppeteer or Playwright headless browser
3. **Compile to GIF or MP4** using ffmpeg or a GIF encoder library
4. **Embed in PowerPoint** using python-pptx's `add_movie()` (for MP4) or PptxGenJS's `addImage()` (for animated GIF)

```bash
# Capture frames with Puppeteer, then compile
ffmpeg -framerate 30 -i frame_%04d.png -vf "scale=1280:-1" -pix_fmt yuv420p output.mp4
# Or create GIF
ffmpeg -framerate 15 -i frame_%04d.png -vf "fps=10,scale=640:-1:flags=lanczos" output.gif
```

Animated GIFs display animated in Microsoft 365 and newer desktop PowerPoint when embedded via PptxGenJS.[^10][^9]

### Workaround 5: GSAP Animation → GIF Pipeline

GSAP animations can be captured frame-by-frame by hooking into the tween's `onUpdate` callback, writing SVG data to a canvas, and using `modern-gif` to create the GIF:[^15]

1. Set up GSAP tween with `onUpdate` that captures SVG → canvas
2. After tween completes, convert rasterized frames to GIF via `modern-gif`
3. Embed the resulting GIF in PPTX

This runs entirely in Node.js with a headless browser.[^16][^15]

### Workaround 6: Slidev → PPTX Export

Slidev (sli.dev) lets you write presentations in Markdown with Vue components, animations, and transitions, then export to PPTX via Playwright:[^17]

```bash
npm init slidev@latest
# Write slides in Markdown with animations
slidev export --format pptx --with-clicks
```

Each animation step becomes a separate slide image in the PPTX. The `--with-clicks` flag captures each click-triggered animation state as its own slide. Text is rasterized (not editable), but the visual fidelity is high.[^17]

***

## 4. CDN Libraries That Are Game-Changers

### Chart and Data Visualization

| Library | Output Format | PowerPoint Integration | Best For |
|---|---|---|---|
| **QuickChart.io** | PNG/SVG via URL API | Fetch image URL → embed in PPTX[^18] | Quick chart images, no rendering needed |
| **Chart.js** | Canvas → PNG export[^19] | Export PNG → embed as image | Interactive charts rendered server-side |
| **D3.js** | SVG (DOM) | Export via `saveSvgAsPng` or `svg-exportJS` → embed[^20] | Complex custom visualizations |
| **Vega/Vega-Lite** | SVG/PNG/Canvas | Server-side render → embed | Declarative grammar of graphics |
| **Mermaid.js** | SVG | Render → PNG → embed | Diagrams, flowcharts, sequence diagrams |
| **Rough.js** | SVG/Canvas | Export → PNG → embed | Hand-drawn style sketches |

**QuickChart.io** deserves special attention: it renders Chart.js configurations as images via a simple GET request URL, requiring no browser or rendering infrastructure. An AI agent can construct a chart URL and fetch the PNG directly:[^18]

```
https://quickchart.io/chart?c={type:'bar',data:{labels:['Q1','Q2','Q3'],datasets:[{data:[10,20,30]}]}}
```

### Animation and Motion Libraries

| Library | Capture Method | Output | Notes |
|---|---|---|---|
| **GSAP** | `onUpdate` → canvas → `modern-gif`[^15] | GIF/MP4 | Most popular web animation library |
| **Lottie (lottie-web)** | Render frames → PNG sequence[^21] | GIF/MP4 | After Effects animations as JSON |
| **Anime.js** | Puppeteer frame capture | GIF/MP4 | Lightweight alternative to GSAP |
| **Three.js** | Canvas screenshot per frame | GIF/MP4 | 3D animations and visualizations |
| **p5.js** | `saveFrames()` built-in | PNG sequence → MP4 | Creative coding / generative art |

### DOM-to-PowerPoint Converters

- **dom-to-pptx** (v1.1.5): Traverses the DOM, calculates computed styles (Flexbox/Grid positions, gradients, shadows), and maps them to **native editable PowerPoint shapes**—not screenshots. Supports SVG vector export (`svgAsVector` option), font embedding, and gradient parsing.[^22]
- **HTML2PPTX**: Node.js library that converts HTML files to PPTX with CSS transformation, layout handling, and image conversion.[^23]
- **PptxGenJS `tableToSlides()`**: Converts any HTML `<table>` element to PowerPoint slides while preserving CSS styling.[^12]

### SVG Export Tools

- **svg-exportJS**: Client-side library that exports SVG DOM elements to SVG files, PNG, JPEG, or PDF. Originally built for D3 chart export. Handles external CSS inlining, custom fonts, hidden elements, and embedded images.[^20]
- **saveSvgAsPng**: Inlines stylesheets and images into SVG, renders through canvas to PNG.[^24]

***

## 5. Real-World Projects and Pipelines

### Open-Source AI Presentation Generators

**Presenton** (github.com/presenton/presenton): The most feature-complete open-source option. Generates presentations from prompts or uploaded documents using OpenAI, Gemini, or Anthropic. Supports custom templates with HTML/Tailwind CSS, exports to PPTX and PDF, and includes an MCP server for integration with AI agents. Also supports creating templates from existing PPTX files.[^25]

**AI-PPT-Generator** (github.com/Kanishk2327/AI-PPT-Generator): End-to-end pipeline: topic → DuckDuckGo search → BeautifulSoup scraping → Gemini 1.5 Flash synthesis → python-pptx slide generation.[^26]

**pptGEN** (github.com/NerdyVisky/pptGEN-dev): Real-time lecture slide generation from live speech using Deepgram transcription + OpenAI embeddings + python-pptx. Generates slides within 15 seconds of speech.[^27]

**OpenGamma** (AI Anytime YouTube): Open-source Gamma alternative with voice input, AI image generation via DALL-E, multi-language support, and one-click PPTX export via python-pptx.[^28]

### Pipeline Architecture for an AI Coding Agent

The recommended architecture for a coding agent like Claude Code:

```
┌─────────────────────────────────────────────────────────┐
│                    AI Agent Pipeline                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. CONTENT GENERATION (LLM)                           │
│     └── Generate structured JSON: titles, bullets,      │
│         chart data, image prompts                       │
│                                                         │
│  2. VISUAL ASSET CREATION                              │
│     ├── Charts: QuickChart.io API → PNG                │
│     ├── Diagrams: Mermaid CLI → SVG → PNG              │
│     ├── Animations: HTML+GSAP → Puppeteer → GIF/MP4   │
│     └── Icons: fetch from CDN (Heroicons, Lucide)      │
│                                                         │
│  3. SLIDE ASSEMBLY (python-pptx)                       │
│     ├── Create slides from layouts                      │
│     ├── Place text, images, shapes                      │
│     ├── Embed GIFs/MP4s for animation                  │
│     └── Inject transition XML (morph/fade)              │
│                                                         │
│  4. POST-PROCESSING                                    │
│     └── Validate XML, save .pptx                       │
└─────────────────────────────────────────────────────────┘
```

### The Morph-Heavy Approach (Most Agent-Friendly)

For an AI agent operating in a terminal, the morph transition approach is the most practical path to "animated" presentations without external rendering infrastructure:

1. **Generate slide pairs**: For each "animation," create two consecutive slides with the same shapes (same `shape.name`) at different positions/sizes/rotations.
2. **Inject morph XML**: Append the morph transition XML to the second slide.
3. **Chain sequences**: A 10-element "build" animation becomes 10 slides with morph transitions, each revealing one more element.
4. **Set auto-advance**: Add `advTm="2000"` to the transition XML for automatic 2-second advances.

This requires only python-pptx + lxml—no browser, no rendering, no external services. The result plays as smooth animations in PowerPoint 2019/2021/365.

### Complete Minimal Example

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from lxml import etree

def add_morph_transition(slide, duration_ms=1000):
    """Inject morph transition XML into a slide."""
    xml = f'''
    <mc:AlternateContent
      xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">
      <mc:Choice
        xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main"
        Requires="p159">
        <p:transition
          xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
          xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main"
          spd="slow" p14:dur="{duration_ms}" advTm="{duration_ms + 500}">
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

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Slide 1: Shape at position A
slide1 = prs.slides.add_slide(prs.slide_layouts[^6])  # blank layout
shape1 = slide1.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1), Inches(3), Inches(2), Inches(2)
)
shape1.name = "AnimatedBox"  # MUST match across slides for morph

# Slide 2: Same shape at position B → morph animates the movement
slide2 = prs.slides.add_slide(prs.slide_layouts[^6])
shape2 = slide2.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8), Inches(1), Inches(4), Inches(4)
)
shape2.name = "AnimatedBox"  # Same name triggers morph
add_morph_transition(slide2, duration_ms=1500)

prs.save('morph_animation.pptx')
```

***

## 6. Commercial Alternatives Worth Noting

If the open-source workarounds prove too fragile, two commercial Python libraries offer full animation APIs:

- **Aspose.Slides for Python** supports entrance/exit animations, morph transitions, all transition types, and animation sequencing with a clean Python API.[^29]
- **Spire.Presentation for Python** provides `Timeline.MainSequence.AddEffect()` for adding animations to shapes, including Fly In, Fade, Appear, and custom paragraph-level animations.[^30]

Both are paid products but may be worth it for production pipelines requiring reliable animation support.

***

## 7. Key Recommendations for an AI Coding Agent

1. **Use python-pptx as the primary engine** for slide creation—it has the richest XML access for workarounds and full round-trip capability.[^1]
2. **Use PptxGenJS as a secondary option** when you need animated GIF or SVG embedding in a Node.js environment.[^9]
3. **Favor morph transitions** over raw animation XML—morph is simpler to generate, more reliable, and produces professional results.[^6]
4. **Use QuickChart.io** for charts when you don't want to spin up a browser. For complex visualizations, use D3 + Puppeteer → PNG.[^18]
5. **Use dom-to-pptx** when you need to convert rich HTML layouts to editable PowerPoint natively.[^22]
6. **For true animations** (motion, particles, complex sequences), render HTML+GSAP in a headless browser, capture as MP4/GIF, and embed.[^15]
7. **Keep a library of XML templates** for common transitions (fade, morph, wipe, push) that the agent can inject parametrically.[^5]
8. **Validate the output** by round-tripping: open in python-pptx after saving to catch XML corruption early.[^14]

---

## References

1. [python-pptx — python-pptx 1.0.0 documentation](https://python-pptx.readthedocs.io) - python-pptx is a Python library for creating, reading, and updating PowerPoint (.pptx) files. A typi...

2. [Movie — python-pptx 0.6.22 documentation](https://python-pptx.readthedocs.io/en/stable/dev/analysis/shp-movie.html) - PowerPoint allows a video to be inserted into a slide and run in slide show mode. In the PowerPoint ...

3. [Shadow — python-pptx 1.0.0 documentation - Read the Docs](https://python-pptx.readthedocs.io/en/latest/dev/analysis/shp-shadow.html) - A shadow is one type of “effect”. The others are glow/soft-edges and reflection. Shadow may be of ty...

4. [Feature Request: Support for Adding Shape Animations (Entrance ...](https://github.com/scanny/python-pptx/issues/1106) - After extensive testing and research, I confirmed that python-pptx currently does not support adding...

5. [Python PPTX workaround to add Transitions to slides - Stack Overflow](https://stackoverflow.com/questions/73901095/python-pptx-workaround-to-add-transitions-to-slides) - As I could not find a function, my idea is to use workaround functions (going deep into xml): where ...

6. [how to activate and utilize the MORPH transision feature · Issue #942](https://github.com/scanny/python-pptx/issues/942) - Hi, I was wondering if it was currently possible to activate and use the morph feature for transitio...

7. [Understanding xmlchemy — python-pptx 1.0.0 documentation](https://python-pptx.readthedocs.io/en/latest/dev/xmlchemy.html) - xmlchemy is an object-XML mapping layer somewhat reminiscent of SQLAlchemy, hence the name. Mapping ...

8. [Finding A Child Element If It Exists When Manipulating PowerPoint ...](https://stackoverflow.com/questions/68521561/finding-a-child-element-if-it-exists-when-manipulating-powerpoint-xml-with-pytho) - I've implemented a few functions that manipulate the XML tree. In a few places I need to find a chil...

9. [pptxgenjs - NPM](https://www.npmjs.com/package/pptxgenjs) - PptxGenJS lets you generate professional PowerPoint presentations in JavaScript - directly from Node...

10. [Images | PptxGenJS - GitHub Pages](https://gitbrent.github.io/PptxGenJS/docs/api-images.html) - Animated gifs: only shown animated on Microsoft 365/Office365 and the newest desktop versions, older...

11. [Media | PptxGenJS - GitHub Pages](https://gitbrent.github.io/PptxGenJS/docs/api-media/) - Media enables the addition of audio, video and online video to Slides. Usage // Path: full or relati...

12. [HTML-to-PowerPoint | PptxGenJS - GitHub Pages](https://gitbrent.github.io/PptxGenJS/html2pptx/) - About HTML-to-PPTX. The tableToSlides method generates a presentation from an HTML table element id....

13. [Add transitions to the PowerPoint slides with PptxGenJS](https://stackoverflow.com/questions/63369151/add-transitions-to-the-powerpoint-slides-with-pptxgenjs) - Recently, I have been playing with the PptxGenJS API to generate some cool PowerPoint slides and I w...

14. [`add_movie` corrupts powerpoint file when a non-openxml feature is ...](https://github.com/scanny/python-pptx/issues/954) - When a non-openxml feature is used in animations, Powerpoint wraps the <p:timing> element in a <mc:A...

15. [How to Create Animated GIFs from GSAP Animations - SitePoint](https://www.sitepoint.com/create-animated-gifs-from-gsap-animations/) - Learn the simple steps involved in converting animations created using GSAP into animated GIFs using...

16. [How to Create Animated GIFs from GSAP Animations - Paul Scanlon](https://www.paulie.dev/articles/2023/11/how-to-create-animated-gifs-from-sap-animations) - In this article, I'm going to explain how you can convert animations created using GSAP into animate...

17. [Exporting | Slidev](https://sli.dev/guide/exporting) - PPTX ​. Slidev can also export your slides as a PPTX file: bash $ slidev export --format pptx. Note ...

18. [QuickChart: Open Source Chart Image API](https://quickchart.io) - Create a chart image with one API call and embed it anywhere. Send charts in email and other platfor...

19. [How to download and export Chart.js images](https://quickchart.io/documentation/chart-js/image-export/) - chartjs-to-image is a node library that can export your chart to file or data URL. It's a little sim...

20. [sharonchoong/svg-exportJS - GitHub](https://github.com/sharonchoong/svg-exportJS) - A Javascript library to export svg charts from the DOM and download them as an SVG file, PDF, or ras...

21. [Exporting Lottie Animations with Images - YouTube](https://www.youtube.com/watch?v=Sx3n5OhJQV4) - ... export Lottie Animations using Images! Unacademy Recap: https://recap.unacademy.com/ LottieFiles...

22. [atharva9167j/dom-to-pptx - GitHub](https://github.com/atharva9167j/dom-to-pptx) - A client-side library that converts any HTML element into a fully editable PowerPoint slide. **dom-t...

23. [HTML Conversion to PowerPoint PPTX via Free Node.js Library](https://products.fileformat.com/presentation/nodejs/html2pptx/) - HTML2PPTX is an open source Node.js Library for loading and converting simple as well as Advanced HT...

24. [Exporting D3 charts to SVG and PNG: a library - Thibaud Colas](https://thib.me/exporting-d3-charts-to-svg-and-png) - I've been very interested in the topic of exporting PNG or SVG assets from D3 charts created with SV...

25. [Open-Source AI Presentation Generator and API (Gamma ... - GitHub](https://github.com/presenton/presenton) - Presenton is an open-source application for generating presentations with AI — all running locally o...

26. [Kanishk2327/AI-PPT-Generator - GitHub](https://github.com/Kanishk2327/AI-PPT-Generator) - AI-Powered Automated Presentation Generator. An end-to-end Python pipeline that transforms any topic...

27. [NerdyVisky/pptGEN-dev: Generating lectures slides on the fly as the ...](https://github.com/NerdyVisky/pptGEN-dev) - pptGEN is an executable application designed to generate lecture slides within 15 seconds, synchroni...

28. [Build a PPT Generation AI tool like Gamma, Genspark, and Skywork](https://www.youtube.com/watch?v=zzQ74FTiGY8) - Open Source AI Presentation Generator In this video, I build OpenGamma from scratch - a completely o...

29. [Manage Slide Transitions in Presentations Using Python](https://docs.aspose.com/slides/python-net/slide-transition/) - Discover how to customize slide transitions in Aspose.Slides for Python via .NET, with step-by-step ...

30. [Python: Add or Extract Animations in PowerPoint](https://www.e-iceblue.com/Tutorials/Python/Spire.Presentation-for-Python/Program-Guide/Image-and-Shapes/Python-Add-or-Extract-Animations-in-PowerPoint.html) - In this article, we will demonstrate how to add animations to shapes in PowerPoint along with how to...

