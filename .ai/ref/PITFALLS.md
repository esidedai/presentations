# Pitfalls — Solved Issues & Scar Tissue

**Every solved bug is a gift to future sessions. Add to this file before closing.**

## Layout

1. **Logo zone conflict.** Top-left 0-120px top, 0-350px left is the logo zone. Never place content (headings, act labels) there. Use `justify-content: center` to vertically center content, or pad top 160px+ to clear.

2. **No solid-color highlight cards.** Full `background: var(--brand-blue)` cards are aggressive. Use `border-top` color accent on the lead card, keep all card backgrounds white.

3. **Transition slides = centered text only.** No illustration, no split layout. Whitespace is the design. Less is more on pivot slides.

4. **Tables don't work on slides.** HTML `<table>` looks messy at presentation scale. Use side-by-side card columns instead — each column a rounded card with its own header + stacked rows.

5. **Content vs logo overlap.** Use `justify-content: center` or pad top 160px+ to keep content below the logo.

## Brand

6. **Purple is NOT a brand color for content.** Only use `--brand-blue` (#0078d4) for accents. Purple (#8764b8) was only in the old gradient. Don't let it creep into borders, text, or fills.

7. **Title slide: no background SVG.** Hex patterns in `light-background-with-shapes.svg` conflict with the logo. Title and closing slides skip the bg.

## Export

8. **html2canvas = gray backgrounds.** SOLVED. Use Playwright instead. Never go back to html2canvas.

9. **Playwright toolbar removal.** Must strip the dev toolbar before screenshot: `page.evaluate("document.getElementById('slide-toolbar')?.remove()")`. Already in render_slides.py but don't forget if rewriting.

10. **Write tool requires Read first.** When writing files programmatically in Claude, read at least 1 line first or the Write tool will error. Known Claude Code quirk.

## Process

11. **Start with scar tissue list.** Read PITFALLS.md BEFORE designing, not after making the same mistake.

12. **Test PowerPoint export early.** Don't wait until all slides are done. Export a few early to catch rendering issues.

13. **Old slides in output folder.** After rebuilding, check that no orphaned PNGs from previous versions remain in the output folder.
