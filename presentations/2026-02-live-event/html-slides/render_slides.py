"""
HTML Slides to PNG Renderer
Uses Playwright to render HTML slides to high-quality PNG images.
Single browser instance for speed.
"""

import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("ERROR: Playwright not installed")
    print("Install with: pip install playwright && playwright install chromium")
    sys.exit(1)


class HTMLSlideRenderer:
    """Render HTML slides to PNG using Playwright (single browser instance)"""

    def __init__(self, slides_dir, output_dir, width=1920, height=1080, scale=1):
        self.slides_dir = Path(slides_dir)
        self.output_dir = Path(output_dir)
        self.width = width
        self.height = height
        self.scale = scale
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def render_all(self):
        html_files = sorted(self.slides_dir.glob('*.html'))
        if not html_files:
            print(f"No HTML files found in {self.slides_dir}")
            return []

        print("=" * 60)
        print("HTML SLIDE RENDERER")
        print("=" * 60)
        print(f"Slides: {self.slides_dir}")
        print(f"Output: {self.output_dir}")
        print(f"Viewport: {self.width}x{self.height} @ {self.scale}x")
        print(f"Found {len(html_files)} slides")
        print("=" * 60)

        rendered = []

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(
                viewport={"width": self.width, "height": self.height},
                device_scale_factor=self.scale,
            )

            for html_file in html_files:
                out = self.output_dir / html_file.with_suffix(".png").name
                try:
                    file_url = html_file.absolute().as_uri()
                    page.goto(file_url)
                    page.wait_for_load_state("networkidle")
                    page.wait_for_timeout(400)

                    # Hide the toolbar if present
                    page.evaluate("document.getElementById('slide-toolbar')?.remove()")

                    page.screenshot(path=str(out), full_page=False, type="png")
                    rendered.append(out)
                    print(f"  [OK] {html_file.name} -> {out.name}")
                except Exception as e:
                    print(f"  [X]  {html_file.name}: {e}")

            browser.close()

        print(f"\nCOMPLETE: {len(rendered)}/{len(html_files)} rendered")
        return rendered


def main():
    base = Path(__file__).parent
    renderer = HTMLSlideRenderer(
        slides_dir=base / "slides",
        output_dir=base / "output",
        width=1920,
        height=1080,
        scale=1,  # 1x = native 1920x1080 PNGs (smaller files, correct for pptx)
    )
    rendered = renderer.render_all()
    if rendered:
        print(f"\n[OK] PNGs ready in: {renderer.output_dir}")
        print("Next: python assemble_pptx.py")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
