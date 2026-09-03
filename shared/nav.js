/* ============================================================================
   Orchid Tree — Mobile navigation
   ----------------------------------------------------------------------------
   Every page hides `.nav .links` below 820px and nothing replaced it, so the
   site had no navigation at all on a phone. This adds the missing piece.

   Drop `<script src="shared/nav.js" defer></script>` on any page that has a
   `nav.nav` with a `.links` block. The drawer is built from the links already
   in the markup, so each page keeps its own menu and there is nothing to
   duplicate or keep in sync.

   Styles are injected from here for the same reason: fourteen pages carry
   their own inline stylesheet, and one source beats fourteen copies.
   ========================================================================== */
(function () {
  var BREAKPOINT = 820;   // matches the `.nav .links{display:none}` query
  var CSS = [
    /* burger button — hidden on desktop, 44px touch target on mobile */
    '.nav-burger{display:none;position:relative;z-index:120;width:44px;height:44px;margin:-10px -8px -10px 0;padding:0;border:0;background:none;cursor:pointer;color:#fff;-webkit-tap-highlight-color:transparent;}',
    '.nav-burger span{position:absolute;left:11px;width:22px;height:1.5px;background:currentColor;border-radius:2px;transition:transform .3s ease,opacity .2s ease;}',
    '.nav-burger span:nth-child(1){top:16px;}',
    '.nav-burger span:nth-child(2){top:21.5px;}',
    '.nav-burger span:nth-child(3){top:27px;}',
    '.nav.solid .nav-burger{color:var(--ink,#43382b);}',
    /* open state: burger becomes a cross, and always reads on the dark sheet */
    'body.nav-open .nav-burger,body.nav-open .nav.solid .nav-burger{color:#fff;}',
    'body.nav-open .nav-burger span:nth-child(1){transform:translateY(5.5px) rotate(45deg);}',
    'body.nav-open .nav-burger span:nth-child(2){opacity:0;}',
    'body.nav-open .nav-burger span:nth-child(3){transform:translateY(-5.5px) rotate(-45deg);}',

    /* scroll lock: position:fixed is the only form iOS Safari respects */
    'body.nav-open{position:fixed;left:0;right:0;width:100%;overflow:hidden;}',

    /* drawer */
    '.nav-drawer{position:fixed;inset:0;z-index:110;display:flex;flex-direction:column;justify-content:center;padding:96px 32px 48px;background:rgba(20,16,12,.97);backdrop-filter:blur(10px);opacity:0;visibility:hidden;transition:opacity .32s ease,visibility .32s ease;overflow-y:auto;overscroll-behavior:contain;}',
    'body.nav-open .nav-drawer{opacity:1;visibility:visible;}',
    '.nav-drawer a{display:block;padding:14px 0;color:rgba(255,255,255,.92);text-decoration:none;font-family:var(--serif,Georgia,serif);font-size:30px;line-height:1.15;letter-spacing:.2px;border-bottom:1px solid rgba(255,255,255,.1);opacity:0;transform:translateY(14px);transition:opacity .4s ease,transform .4s ease;}',
    'body.nav-open .nav-drawer a{opacity:1;transform:none;}',
    '.nav-drawer a[aria-current="page"]{color:var(--gold,#e0a23c);}',
    /* the WhatsApp CTA keeps its emphasis, as a button at the foot of the sheet */
    '.nav-drawer a.reserve{margin-top:28px;border:1px solid rgba(255,255,255,.55);border-radius:var(--radius,12px);padding:16px 22px;text-align:center;font-family:var(--sans,system-ui,sans-serif);font-size:12px;letter-spacing:2.5px;text-transform:uppercase;font-weight:600;}',

    '@media (prefers-reduced-motion:reduce){.nav-burger span,.nav-drawer,.nav-drawer a{transition:none;}}',
    /* nav sitting on a light bar (faq) needs ink, not white */
    '.nav-burger.on-light{color:var(--ink,#43382b);}',
    /* most pages already hide `.links` here; faq.html never did, so own the rule */
    '@media (max-width:' + BREAKPOINT + 'px){.nav-burger{display:block;}.nav .links{display:none;}}',
    /* desktop must never keep a stale open drawer (e.g. phone rotated to tablet) */
    '@media (min-width:' + (BREAKPOINT + 1) + 'px){.nav-drawer{display:none;}}',
  ].join('\n');

  function init() {
    // some pages use `<nav class="nav">`, others `<div class="nav">`; match the
    // first `.nav` that actually carries a `.links` block
    var nav = null, links = null;
    var candidates = document.querySelectorAll('.nav');
    for (var i = 0; i < candidates.length; i++) {
      var l = candidates[i].querySelector('.links');
      if (l) { nav = candidates[i]; links = l; break; }
    }
    if (!nav || nav.querySelector('.nav-burger')) return;

    var style = document.createElement('style');
    style.textContent = CSS;
    document.head.appendChild(style);

    // drawer mirrors the page's own links, so each page keeps its own menu
    var drawer = document.createElement('div');
    drawer.className = 'nav-drawer';
    drawer.id = 'navDrawer';
    drawer.hidden = false;
    Array.prototype.forEach.call(links.querySelectorAll('a'), function (a) {
      var clone = a.cloneNode(true);
      clone.removeAttribute('id');
      drawer.appendChild(clone);
    });

    var burger = document.createElement('button');
    burger.type = 'button';
    burger.className = 'nav-burger';
    burger.setAttribute('aria-label', 'Open menu');
    burger.setAttribute('aria-expanded', 'false');
    burger.setAttribute('aria-controls', 'navDrawer');
    burger.innerHTML = '<span></span><span></span><span></span>';

    // pages whose bar is a dark gradient report a transparent background-color
    // and want a white burger; faq.html paints an opaque cream bar and wants ink
    var bg = getComputedStyle(nav).backgroundColor || '';
    var rgb = bg.match(/[\d.]+/g);
    if (rgb && rgb.length >= 3) {
      var alpha = rgb.length > 3 ? parseFloat(rgb[3]) : 1;
      var lum = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]) / 255;
      if (alpha > 0.5 && lum > 0.6) burger.classList.add('on-light');
    }

    nav.appendChild(burger);
    document.body.appendChild(drawer);

    // staggered reveal, so the sheet doesn't land as one flat block
    Array.prototype.forEach.call(drawer.children, function (a, i) {
      a.style.transitionDelay = (0.05 + i * 0.035) + 's';
    });

    var scrollY = 0;
    function setOpen(open) {
      if (open) {
        // position:fixed on body is the only lock iOS Safari honours
        scrollY = window.pageYOffset;
        document.body.style.top = -scrollY + 'px';
        document.body.classList.add('nav-open');
      } else {
        document.body.classList.remove('nav-open');
        document.body.style.top = '';
        window.scrollTo(0, scrollY);
      }
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      burger.setAttribute('aria-expanded', String(open));
    }
    function isOpen() { return document.body.classList.contains('nav-open'); }

    burger.addEventListener('click', function () { setOpen(!isOpen()); });
    drawer.addEventListener('click', function (e) {
      // close on any link tap, and on the backdrop around the links
      if (e.target === drawer || e.target.closest('a')) setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen()) { setOpen(false); burger.focus(); }
    });
    window.addEventListener('resize', function () {
      if (isOpen() && window.innerWidth > BREAKPOINT) setOpen(false);
    });
  }

  // body must exist before the drawer is appended
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
