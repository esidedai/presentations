/**
 * Slide Toolbar — nav (prev/next/index) + PNG export preview
 * Include via: <script src="../shared/slide-toolbar.js"></script>
 * Hidden during export so it never appears in screenshots.
 */
(function () {
  // Don't run inside iframes (index.html thumbnails)
  if (window.self !== window.top) return;

  // Full slide manifest — used for prev/next navigation
  const slides = [
    { slug: '01-title',                title: 'Title' },
    { slug: '02-harvest-1800s',        title: 'The Harvest' },
    { slug: '03-combine-harvester',    title: 'Combine Harvester' },
    { slug: '04-switchboard-operators', title: 'Switchboard Operators' },
    { slug: '05-direct-dial',          title: 'Direct Dial' },
    { slug: '06-todays-reality',       title: "Today's Reality" },
    { slug: '07-million-dollar-bottleneck', title: 'Million-Dollar Bottleneck' },
    { slug: '08-tool-trap',            title: 'The Tool Trap' },
    { slug: '09-what-if-reframe',      title: 'What If We Reframe?' },
    { slug: '10-workers-vs-tools',     title: 'Workers vs. Tools' },
    { slug: '11-meet-meridian',        title: 'Meet Meridian' },
    { slug: '12-five-ai-workers',      title: '5 AI Workers' },
    { slug: '13-the-numbers',          title: 'The Numbers' },
    { slug: '14-invoice-processor',    title: 'Invoice Processor' },
    { slug: '15-what-really-changed',  title: 'What Really Changed' },
    { slug: '16-three-autonomy-modes', title: 'Three Autonomy Modes' },
    { slug: '17-what-happened-humans', title: 'What Happened to Humans?' },
    { slug: '18-compounding-effect',   title: 'Compounding Effect' },
    { slug: '19-real-asset',           title: 'The Real Asset' },
    { slug: '20-capital-lens',         title: 'Capital Lens' },
    { slug: '21-scar-tissue-test',     title: 'Scar Tissue Test' },
    { slug: '22-meridian-examples',    title: 'Meridian Examples' },
    { slug: '23-ai-changing-fast',     title: 'AI Changing Fast' },
    { slug: '24-asset-isnt-model',     title: "Asset Isn't the Model" },
    { slug: '25-like-hiring',          title: 'Like Hiring' },
    { slug: '26-two-paths',            title: 'Two Paths' },
    { slug: '27-getting-started',      title: 'Getting Started' },
    { slug: '28-closing-question',     title: 'The Question' },
  ];

  // Find current slide index
  const currentFile = location.pathname.split('/').pop().replace('.html', '');
  const idx = slides.findIndex(s => s.slug === currentFile);
  const prevSlide = idx > 0 ? slides[idx - 1] : null;
  const nextSlide = idx < slides.length - 1 ? slides[idx + 1] : null;
  const slideLabel = idx >= 0 ? `${idx + 1} / ${slides.length}` : '';

  // Build toolbar HTML
  const toolbar = document.createElement('div');
  toolbar.id = 'slide-toolbar';
  toolbar.innerHTML = `
    <div class="tb-left">
      <a href="${prevSlide ? prevSlide.slug + '.html' : '#'}" class="tb-btn tb-arrow ${!prevSlide ? 'tb-disabled' : ''}" title="${prevSlide ? prevSlide.title : ''}">&#8592;</a>
      <a href="../index.html" class="tb-btn tb-index">Index</a>
      <a href="${nextSlide ? nextSlide.slug + '.html' : '#'}" class="tb-btn tb-arrow ${!nextSlide ? 'tb-disabled' : ''}" title="${nextSlide ? nextSlide.title : ''}">&#8594;</a>
      <span class="tb-counter">${slideLabel}</span>
    </div>
    <div class="tb-right">
      <button class="tb-btn tb-export" id="tb-export-btn">Export PNG</button>
      <span class="tb-status" id="tb-status"></span>
    </div>
  `;

  const style = document.createElement('style');
  style.textContent = `
    #slide-toolbar {
      position: fixed;
      bottom: 24px;
      left: 24px;
      right: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      z-index: 9999;
      font-family: 'Inter', sans-serif;
      pointer-events: none;
    }
    #slide-toolbar > * { pointer-events: auto; }
    .tb-left, .tb-right {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .tb-btn {
      background: rgba(0,0,0,0.72);
      color: #fff;
      border: none;
      padding: 10px 16px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      text-decoration: none;
      transition: background 0.15s;
      line-height: 1;
    }
    .tb-btn:hover { background: rgba(0,0,0,0.9); }
    .tb-arrow { padding: 10px 14px; font-size: 16px; }
    .tb-disabled { opacity: 0.25; pointer-events: none; }
    .tb-counter {
      color: rgba(0,0,0,0.45);
      font-size: 13px;
      font-weight: 500;
      margin-left: 8px;
    }
    .tb-status {
      color: rgba(0,0,0,0.5);
      font-size: 13px;
    }

    /* PNG preview overlay */
    #png-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.85);
      z-index: 10000;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 16px;
    }
    #png-overlay img {
      max-width: 90vw;
      max-height: 75vh;
      border: 3px solid #fff;
      border-radius: 8px;
      box-shadow: 0 8px 40px rgba(0,0,0,0.5);
    }
    #png-overlay .overlay-bar {
      display: flex;
      gap: 12px;
      align-items: center;
    }
    #png-overlay .overlay-btn {
      background: rgba(255,255,255,0.15);
      color: #fff;
      border: 1px solid rgba(255,255,255,0.3);
      padding: 10px 20px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      font-family: 'Inter', sans-serif;
    }
    #png-overlay .overlay-btn:hover { background: rgba(255,255,255,0.25); }
    #png-overlay .overlay-btn.primary { background: #0078d4; border-color: #0078d4; }
    #png-overlay .overlay-btn.primary:hover { background: #106ebe; }
    #png-overlay .overlay-info {
      color: rgba(255,255,255,0.6);
      font-size: 13px;
      font-family: 'Inter', sans-serif;
    }
  `;

  document.head.appendChild(style);
  document.body.appendChild(toolbar);

  // Keyboard nav: left/right arrows
  document.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    if (document.getElementById('png-overlay')) return;
    if (e.key === 'ArrowLeft' && prevSlide) location.href = prevSlide.slug + '.html';
    if (e.key === 'ArrowRight' && nextSlide) location.href = nextSlide.slug + '.html';
  });

  // Load html2canvas on demand
  function loadH2C() {
    return new Promise((resolve, reject) => {
      if (window.html2canvas) return resolve(window.html2canvas);
      const s = document.createElement('script');
      s.src = 'https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js';
      s.onload = () => resolve(window.html2canvas);
      s.onerror = () => reject(new Error('Failed to load html2canvas'));
      document.head.appendChild(s);
    });
  }

  document.getElementById('tb-export-btn').addEventListener('click', async () => {
    const status = document.getElementById('tb-status');
    const btn = document.getElementById('tb-export-btn');
    btn.disabled = true;
    status.textContent = 'Rendering...';

    toolbar.style.display = 'none';

    try {
      const h2c = await loadH2C();
      const canvas = await h2c(document.body, {
        width: 1920,
        height: 1080,
        scale: 1,
        useCORS: true,
        backgroundColor: '#ffffff',
        logging: false,
      });

      toolbar.style.display = 'flex';
      status.textContent = '';
      btn.disabled = false;

      const dataUrl = canvas.toDataURL('image/png');
      showOverlay(dataUrl);
    } catch (err) {
      toolbar.style.display = 'flex';
      status.textContent = 'Export failed: ' + err.message;
      btn.disabled = false;
    }
  });

  function showOverlay(dataUrl) {
    const overlay = document.createElement('div');
    overlay.id = 'png-overlay';
    const slug = location.pathname.split('/').pop().replace('.html', '');

    overlay.innerHTML = `
      <img src="${dataUrl}" alt="Exported PNG preview">
      <div class="overlay-bar">
        <button class="overlay-btn primary" id="ol-download">Download PNG</button>
        <button class="overlay-btn" id="ol-close">Close</button>
      </div>
      <div class="overlay-info">1920 &times; 1080 &mdash; Check for gray backgrounds or rendering issues</div>
    `;

    document.body.appendChild(overlay);

    overlay.querySelector('#ol-close').onclick = () => overlay.remove();
    overlay.querySelector('#ol-download').onclick = () => {
      const a = document.createElement('a');
      a.href = dataUrl;
      a.download = slug + '.png';
      a.click();
    };

    const esc = (e) => { if (e.key === 'Escape') { overlay.remove(); document.removeEventListener('keydown', esc); } };
    document.addEventListener('keydown', esc);
  }
})();
