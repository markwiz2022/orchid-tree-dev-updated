/* ============================================================================
   Orchid Tree — Video card + lightbox player
   ----------------------------------------------------------------------------
   One component, used by every page. Handles the mixed-orientation problem:
   the owner's pieces and the room reels are PORTRAIT (9:16), the estate
   photography is LANDSCAPE. The player sizes itself to whichever it is showing,
   so nothing is letterboxed and nothing is cropped.

   Usage
   -----
     <script src="shared/media.js"></script>
     <script src="shared/video.js"></script>

     OrchidVideo.card(entry, { ratio:'portrait'|'cover', badge:'Owner' })
       → HTML string for a thumbnail card. Drop it into any grid or carousel.
     OrchidVideo.bind(rootEl)
       → wires up every card inside rootEl (call after injecting HTML).
     OrchidVideo.open(items, index)
       → opens the lightbox on a set of { kind, src, poster, portrait, label }.

   The CSS injects itself, and reads the host page's design tokens (--gold,
   --green, --ink, --serif, --sans) with sane fallbacks, so it looks native on
   the cream pages and on the dark ones.
   ========================================================================== */
(function () {
  if (window.OrchidVideo) return;

  /* ── styles ─────────────────────────────────────────────────────────────── */
  var CSS = [
    /* --- the thumbnail card ------------------------------------------------ */
    '.ovcard{position:relative;display:block;width:100%;border:0;padding:0;overflow:hidden;',
    '  border-radius:var(--radius,12px);background:#8c8275;cursor:pointer;font-family:inherit;',
    '  box-shadow:0 4px 20px rgba(67,56,43,.10);transition:box-shadow .3s ease,transform .3s ease;}',
    '.ovcard:hover{box-shadow:0 18px 44px rgba(67,56,43,.20);transform:translateY(-3px);}',
    '.ovcard:focus-visible{outline:2px solid var(--gold,#c9a23c);outline-offset:3px;}',
    '.ovcard.is-portrait{aspect-ratio:9/16;}',
    '.ovcard.is-cover{height:100%;}',
    '.ovcard .ov-poster,.ovcard .ov-prev{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;',
    '  transition:transform .7s ease,opacity .45s ease;}',
    '.ovcard .ov-prev{opacity:0;}',
    '.ovcard.playing .ov-prev{opacity:1;}',
    '.ovcard:hover .ov-poster,.ovcard:hover .ov-prev{transform:scale(1.05);}',
    /* soft top + bottom scrim so the play button and the label always read */
    '.ovcard .ov-scrim{position:absolute;inset:0;background:linear-gradient(to top,rgba(28,24,19,.80),rgba(28,24,19,.06) 46%,rgba(28,24,19,.34));}',

    /* --- the play button: gold ring, glass fill --------------------------- */
    '.ov-play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:3;',
    '  width:68px;height:68px;border-radius:50%;display:flex;align-items:center;justify-content:center;',
    '  background:rgba(255,255,255,.16);border:1.5px solid rgba(255,255,255,.72);',
    '  -webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);',
    '  box-shadow:0 6px 26px rgba(0,0,0,.30);transition:background .25s ease,border-color .25s ease,transform .25s ease;}',
    '.ov-play svg{width:22px;height:22px;fill:#fff;margin-left:3px;transition:fill .25s ease;}',
    '.ovcard:hover .ov-play{background:var(--gold,#c9a23c);border-color:var(--gold,#c9a23c);transform:translate(-50%,-50%) scale(1.06);}',
    '.ovcard:hover .ov-play svg{fill:#fff;}',
    '.ovcard.playing .ov-play{opacity:0;transform:translate(-50%,-50%) scale(.85);}',
    /* a soft breathing halo, so the card reads as "video" at a glance */
    '.ov-play::after{content:"";position:absolute;inset:-9px;border-radius:50%;border:1px solid rgba(255,255,255,.34);animation:ovpulse 2.8s ease-out infinite;}',
    '@keyframes ovpulse{0%{transform:scale(.9);opacity:.85}70%{transform:scale(1.22);opacity:0}100%{opacity:0}}',

    /* --- badges + label --------------------------------------------------- */
    '.ov-badge{position:absolute;top:14px;left:14px;z-index:3;display:inline-flex;align-items:center;gap:6px;',
    '  background:rgba(255,255,255,.94);color:var(--ink,#43382b);font-size:9.5px;font-weight:700;',
    '  letter-spacing:2px;text-transform:uppercase;padding:6px 11px;border-radius:20px;',
    '  box-shadow:0 2px 10px rgba(0,0,0,.18);}',
    '.ov-badge .dot{width:5px;height:5px;border-radius:50%;background:var(--gold,#c9a23c);}',
    '.ov-soon{position:absolute;top:14px;right:14px;z-index:3;background:rgba(20,16,12,.55);color:#fff;',
    '  font-size:9px;font-weight:700;letter-spacing:1.6px;text-transform:uppercase;padding:5px 10px;border-radius:20px;}',
    '.ov-cap{position:absolute;left:0;right:0;bottom:0;z-index:3;padding:22px;text-align:left;color:#fff;}',
    '.ov-cap .ov-eyebrow{font-size:9.5px;letter-spacing:3px;text-transform:uppercase;color:var(--gold,#c9a23c);font-weight:700;margin-bottom:7px;}',
    '.ov-cap .ov-title{font-family:var(--serif,Georgia,serif);font-size:23px;line-height:1.2;font-weight:600;color:#fff;text-shadow:0 1px 12px rgba(0,0,0,.5);}',
    '.ov-cap .ov-blurb{font-size:13px;line-height:1.5;color:rgba(255,255,255,.86);margin-top:8px;max-width:34ch;}',

    /* --- the lightbox ----------------------------------------------------- */
    '.ovlb{position:fixed;inset:0;z-index:120;display:none;align-items:center;justify-content:center;',
    '  background:rgba(18,15,11,.93);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);padding:28px;}',
    '.ovlb.open{display:flex;}',
    '.ovlb-stage{position:relative;display:flex;align-items:center;justify-content:center;max-width:100%;max-height:100%;}',
    '.ovlb-media{border-radius:14px;overflow:hidden;background:#000;box-shadow:0 30px 90px rgba(0,0,0,.6);',
    '  max-height:86vh;max-width:min(100%,1180px);display:block;}',
    '.ovlb-media.portrait{aspect-ratio:9/16;height:86vh;width:auto;}',
    '.ovlb-media.landscape{aspect-ratio:16/9;width:min(94vw,1180px);height:auto;}',
    '.ovlb-media video,.ovlb-media img{width:100%;height:100%;object-fit:contain;display:block;background:#000;}',
    '.ovlb-close{position:fixed;top:22px;right:24px;z-index:4;width:44px;height:44px;border-radius:50%;',
    '  border:1px solid rgba(255,255,255,.35);background:rgba(255,255,255,.10);color:#fff;font-size:22px;line-height:1;',
    '  cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .18s,border-color .18s;}',
    '.ovlb-close:hover{background:#fff;color:#1c1813;border-color:#fff;}',
    '.ovlb-nav{position:fixed;top:50%;transform:translateY(-50%);z-index:4;width:52px;height:52px;border-radius:50%;',
    '  border:1px solid rgba(255,255,255,.3);background:rgba(255,255,255,.10);color:#fff;font-size:26px;line-height:1;',
    '  cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .18s;}',
    '.ovlb-nav:hover{background:rgba(255,255,255,.26);}',
    '.ovlb-nav.prev{left:22px;} .ovlb-nav.next{right:22px;}',
    '.ovlb-nav[hidden]{display:none;}',
    '.ovlb-cap{position:fixed;left:0;right:0;bottom:20px;z-index:4;text-align:center;color:rgba(255,255,255,.82);',
    '  font-size:12px;letter-spacing:2.4px;text-transform:uppercase;font-weight:600;padding:0 24px;}',
    '.ovlb-soon{color:rgba(255,255,255,.9);font-family:var(--serif,Georgia,serif);font-style:italic;font-size:19px;',
    '  text-align:center;padding:40px 32px;letter-spacing:0;text-transform:none;}',

    /* --- the full-width owner band (stays page + anywhere else) ------------ */
    '.ownerband{position:relative;background:#1c1813;color:#fff;padding:clamp(76px,11vh,132px) 0;overflow:hidden;}',
    '.ownerband::before{content:"";position:absolute;inset:0;pointer-events:none;',
    '  background:radial-gradient(68% 55% at 76% 32%,rgba(201,162,60,.15),transparent 62%);}',
    '.ownerband .ob-inner{position:relative;display:flex;gap:clamp(32px,5vw,72px);align-items:center;}',
    '.ownerband .ob-vid{flex:0 0 clamp(250px,25vw,330px);position:relative;}',
    '.ownerband .ob-vid::before{content:"";position:absolute;inset:-14px -14px 14px 14px;',
    '  border:1px solid rgba(201,162,60,.42);border-radius:6px;pointer-events:none;}',
    '.ownerband .ob-vid .ovcard{box-shadow:0 26px 62px rgba(0,0,0,.5);}',
    '.ownerband .eyebrow{color:var(--gold,#c9a23c);margin-bottom:20px;}',
    '.ownerband h2{color:#fff;font-family:var(--serif,Georgia,serif);font-weight:400;',
    '  font-size:clamp(30px,4.1vw,54px);line-height:1.07;letter-spacing:-.5px;}',
    '.ownerband .muted{color:rgba(255,255,255,.72);font-size:16px;line-height:1.8;max-width:54ch;margin-top:14px;}',
    '.ownerband .ob-txt{flex:1;min-width:0;}',
    '.ownerband .ob-txt h2{margin-bottom:16px;}',
    '.ownerband .ob-quote{font-family:var(--serif,Georgia,serif);font-style:italic;font-size:clamp(19px,2.1vw,24px);',
    '  line-height:1.5;color:rgba(255,255,255,.9);margin-top:22px;}',
    '.ownerband .ob-sig{font-family:var(--script,cursive);font-size:38px;color:var(--gold,#c9a23c);line-height:1;margin-top:30px;}',
    '.ownerband .ob-who{font-size:10.5px;letter-spacing:2.6px;text-transform:uppercase;font-weight:700;color:rgba(255,255,255,.5);margin-top:7px;}',

    '@media(max-width:820px){',
    '  .ownerband .ob-inner{flex-direction:column;align-items:stretch;}',
    '  .ownerband .ob-vid{flex:none;max-width:320px;width:100%;margin:0 auto;}',
    '  .ovlb-media.portrait{height:auto;width:min(92vw,420px);}',
    '  .ovlb-nav{width:42px;height:42px;} .ovlb-nav.prev{left:10px;} .ovlb-nav.next{right:10px;}',
    '  .ov-cap .ov-title{font-size:20px;}',
    '}',
    '@media(prefers-reduced-motion:reduce){',
    '  .ov-play::after{animation:none;}',
    '  .ovcard,.ovcard .ov-poster,.ovcard .ov-prev,.ov-play{transition:none;}',
    '}',
  ].join("\n");

  var style = document.createElement("style");
  style.setAttribute("data-orchid-video", "");
  style.textContent = CSS;
  document.head.appendChild(style);

  /* ── helpers ────────────────────────────────────────────────────────────── */
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  var PLAY_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>';

  /* registry so a card can carry a whole media set through a data attribute */
  var SETS = {};
  var seq = 0;
  function stash(items) { var k = "ovs" + (++seq); SETS[k] = items; return k; }

  /* ── card ───────────────────────────────────────────────────────────────── */
  /**
   * @param {object} entry  { src, poster, portrait, eyebrow, label, blurb }
   * @param {object} [opts] { ratio:'portrait'|'cover', badge:string,
   *                          items:[], index:number, showBlurb:boolean }
   */
  function card(entry, opts) {
    opts = opts || {};
    if (!entry) return "";
    var ratio = opts.ratio === "cover" ? "is-cover" : "is-portrait";
    var playable = !!entry.src;
    var key = stash(opts.items && opts.items.length ? opts.items : [{
      kind: "video", src: entry.src, poster: entry.poster,
      portrait: entry.portrait !== false, label: entry.label, ready: playable,
    }]);

    var h = '<button type="button" class="ovcard ' + ratio + '"' +
      ' data-ovid="' + key + '" data-ovi="' + (opts.index || 0) + '"' +
      ' aria-label="Play video: ' + esc(entry.label || "Orchid Tree") + '">';
    h += '<img class="ov-poster" src="' + esc(entry.poster || "") + '" alt="" loading="lazy" decoding="async">';
    if (playable) {
      h += '<video class="ov-prev" src="' + esc(entry.src) + '" muted loop playsinline preload="none"></video>';
    }
    h += '<div class="ov-scrim"></div>';
    if (opts.badge) h += '<span class="ov-badge"><i class="dot"></i>' + esc(opts.badge) + "</span>";
    if (!playable) h += '<span class="ov-soon">Video coming soon</span>';
    h += '<span class="ov-play">' + PLAY_SVG + "</span>";
    if (entry.eyebrow || entry.label) {
      h += '<span class="ov-cap">';
      if (entry.eyebrow) h += '<span class="ov-eyebrow">' + esc(entry.eyebrow) + "</span>";
      if (entry.label) h += '<span class="ov-title">' + esc(entry.label) + "</span>";
      if (opts.showBlurb && entry.blurb) h += '<span class="ov-blurb">' + esc(entry.blurb) + "</span>";
      h += "</span>";
    }
    return h + "</button>";
  }

  /* ── lightbox ───────────────────────────────────────────────────────────── */
  var lb, lbMedia, lbCap, lbPrev, lbNext;
  var LB = { items: [], i: 0 };

  function buildLb() {
    if (lb) return;
    lb = document.createElement("div");
    lb.className = "ovlb";
    lb.setAttribute("role", "dialog");
    lb.setAttribute("aria-modal", "true");
    lb.innerHTML =
      '<button class="ovlb-close" aria-label="Close video">&times;</button>' +
      '<button class="ovlb-nav prev" aria-label="Previous">&lsaquo;</button>' +
      '<div class="ovlb-stage"><div class="ovlb-media" id="ovlbMedia"></div></div>' +
      '<button class="ovlb-nav next" aria-label="Next">&rsaquo;</button>' +
      '<div class="ovlb-cap"></div>';
    document.body.appendChild(lb);
    lbMedia = lb.querySelector(".ovlb-media");
    lbCap = lb.querySelector(".ovlb-cap");
    lbPrev = lb.querySelector(".ovlb-nav.prev");
    lbNext = lb.querySelector(".ovlb-nav.next");
    lb.querySelector(".ovlb-close").addEventListener("click", close);
    lbPrev.addEventListener("click", function () { go(LB.i - 1); });
    lbNext.addEventListener("click", function () { go(LB.i + 1); });
    lb.addEventListener("click", function (ev) { if (ev.target === lb || ev.target.classList.contains("ovlb-stage")) close(); });
    document.addEventListener("keydown", function (ev) {
      if (!lb.classList.contains("open")) return;
      if (ev.key === "Escape") close();
      if (ev.key === "ArrowLeft") go(LB.i - 1);
      if (ev.key === "ArrowRight") go(LB.i + 1);
    });
  }

  function go(target) {
    var n = LB.items.length; if (!n) return;
    LB.i = (target + n) % n;
    var it = LB.items[LB.i];
    var portrait = it.kind === "video" ? it.portrait !== false : false;
    lbMedia.className = "ovlb-media " + (portrait ? "portrait" : "landscape");
    lbMedia.style.position = "";

    if (it.kind === "video" && it.src) {
      lbMedia.innerHTML = '<video src="' + esc(it.src) + '" poster="' + esc(it.poster || "") +
        '" controls autoplay playsinline preload="metadata"></video>';
    } else if (it.kind === "video") {
      // placeholder state — the file hasn't been uploaded yet
      lbMedia.innerHTML = '<img src="' + esc(it.poster || "") + '" alt="">' +
        '<div class="ovlb-soon" style="position:absolute;inset:auto 0 0 0;background:rgba(18,15,11,.82);">' +
        "This video hasn&rsquo;t been uploaded yet.</div>";
      lbMedia.style.position = "relative";
    } else {
      lbMedia.innerHTML = '<img src="' + esc(it.src) + '" alt="' + esc(it.label || "") + '">';
    }

    lbCap.textContent = it.label || "";
    var multi = n > 1;
    lbPrev.hidden = !multi; lbNext.hidden = !multi;
  }

  function open(items, index) {
    buildLb();
    LB.items = (items || []).slice();
    if (!LB.items.length) return;
    lb.classList.add("open");
    document.body.style.overflow = "hidden";
    go(index || 0);
  }

  function close() {
    if (!lb) return;
    lb.classList.remove("open");
    lbMedia.innerHTML = "";
    document.body.style.overflow = "";
  }

  /* ── bind ───────────────────────────────────────────────────────────────── */
  function bind(root) {
    root = root || document;
    Array.prototype.forEach.call(root.querySelectorAll(".ovcard[data-ovid]"), function (c) {
      if (c._ovBound) return;
      c._ovBound = true;
      var items = SETS[c.getAttribute("data-ovid")] || [];
      var start = parseInt(c.getAttribute("data-ovi"), 10) || 0;
      c.addEventListener("click", function () { open(items, start); });

      // hover: a silent looping preview, so the card feels alive before the click
      var v = c.querySelector("video.ov-prev");
      if (!v) return;
      if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
      c.addEventListener("mouseenter", function () {
        c.classList.add("playing");
        try { v.currentTime = 0; v.play(); } catch (e) {}
      });
      c.addEventListener("mouseleave", function () {
        c.classList.remove("playing");
        try { v.pause(); } catch (e) {}
      });
    });
  }

  /* ── band ───────────────────────────────────────────────────────────────
     The whole "owner talks about this page" section, rendered into a host
     element. Pages that don't need a bespoke layout use this:

       <section class="ownerband" id="ownerBand"></section>
       OrchidVideo.band('restaurant', document.getElementById('ownerBand'));

     Removes the host entirely if there's no video to show, so a page never
     carries an empty band.                                                   */
  function band(page, host, opts) {
    opts = opts || {};
    if (!host) return;
    var M = window.OrchidMedia;
    var v = M && M.owner(page);
    if (!v) { host.remove(); return; }

    host.innerHTML =
      '<div class="wrap ob-inner">' +
        '<div class="ob-vid"></div>' +
        '<div class="ob-txt">' +
          '<div class="eyebrow">' + esc(v.eyebrow || "From the owner") + "</div>" +
          "<h2>" + esc(opts.heading || v.label) + "</h2>" +
          '<div class="ob-quote">' + esc(opts.quote || v.blurb || "") + "</div>" +
          (opts.body ? '<p class="muted">' + esc(opts.body) + "</p>" : "") +
          '<div class="ob-sig">Orchid Tree</div>' +
          '<div class="ob-who">' + (M.ownerName ? esc(M.ownerName) + " &middot; " : "") +
            (M.ownerRole || "") + "</div>" +
        "</div>" +
      "</div>";

    var slot = host.querySelector(".ob-vid");
    slot.innerHTML = card(v, {
      ratio: v.portrait === false ? "cover" : "portrait",
      badge: "The owner",
    });
    if (v.portrait === false) slot.querySelector(".ovcard").style.aspectRatio = "16/9";
    bind(slot);
  }

  window.OrchidVideo = { card: card, band: band, bind: bind, open: open, close: close, esc: esc, PLAY_SVG: PLAY_SVG };
})();
