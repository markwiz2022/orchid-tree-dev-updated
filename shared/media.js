/* ============================================================================
   Orchid Tree — Video Manifest
   ----------------------------------------------------------------------------
   Single source of truth for every video on the site: the owner's pieces to
   camera, and the per-room reels.

   HOW TO ADD A VIDEO
   ------------------
   1. Drop the file into  videos/owner/  or  videos/rooms/  (see videos/README.md
      for the naming convention and the encode settings).
   2. Find its entry below and replace  src: null  with the path.
   3. Give it a `poster` (a still frame, or any estate photo). The poster is what
      renders before playback and is what the card thumbnail shows.

   Nothing else needs editing. Every card, carousel and modal on the site reads
   from here, and falls back to photos wherever a video is still null.

   ORIENTATION
   -----------
   The owner's reels are PORTRAIT (9:16). Room reels are PORTRAIT too. Estate
   photography is LANDSCAPE. Declare it with `portrait: true/false` — the player
   and the card sizing both key off that flag, so a mixed set never letterboxes.
   ========================================================================== */
(function () {
  var U = "https://orchidtree.in/uploads/";

  /* ── PREVIEW ────────────────────────────────────────────────────────────────
     true  → cards for not-yet-uploaded videos still render (poster + play), so
             the layout can be reviewed before the owner's files land.
     false → those cards are hidden entirely and the page falls back to photos.
     FLIP THIS TO false BEFORE LAUNCH IF ANY src IS STILL null.
     ──────────────────────────────────────────────────────────────────────── */
  var PREVIEW = true;

  /* The owner. Named here once so every page credits him identically. */
  var OWNER_NAME = "Pradeep Kuppa Swamy";
  var OWNER_ROLE = "Landscape architect &middot; founder";
  var OWNER_PORTRAIT = U + "pradip_aboutus_a82dd2aa16.jpg";

  /* ── The owner, to camera ─────────────────────────────────────────────────
     One entry per page. Same person, different subject — so each page opens
     with the owner talking about that page's thing.                          */
  var OWNER = {
    home: {
      id: "owner-home",
      src: null,                      // → 'videos/owner/owner-welcome.mp4'
      poster: U + "Experience_section_jpg_afb1c77479.webp",
      portrait: true,
      eyebrow: "From the owner",
      label: "Why we left the forest standing",
      blurb: "A minute with the person who built this place, on what Orchid Tree is and what it isn't.",
    },
    stays: {
      id: "owner-stays",
      src: null,                      // → 'videos/owner/owner-rooms.mp4'
      poster: U + "Bodhi_Tree_03_1_35a5ef31e4.webp",
      portrait: true,
      eyebrow: "From the owner",
      label: "Eleven rooms, and how to pick yours",
      blurb: "Which room suits which kind of trip — poolside or deep in the trees — from the person who built each one.",
    },
    experiences: {
      id: "owner-experiences",
      src: null,                      // → 'videos/owner/owner-day.mp4'
      poster: U + "Image8_scaled_jpg_ec00384f49.webp",
      portrait: true,
      eyebrow: "From the owner",
      label: "A day here, in the owner's words",
      blurb: "Before the sun comes up and long after it goes down — what the hours actually feel like.",
    },
    /* The weddings page already had a founder-film slot. It is a LANDSCAPE
       16:9 film, not a portrait reel — hence portrait:false. */
    weddings: {
      id: "owner-weddings",
      src: null,                      // → 'videos/owner/owner-weddings.mp4'
      poster: OWNER_PORTRAIT,
      portrait: false,
      eyebrow: "Founder film",
      label: "A note from Pradeep",
      blurb: "Celebration without visual pollution, and why the landscape should never disappear under decor.",
    },
    corporate: {
      id: "owner-corporate",
      src: null,                      // → 'videos/owner/owner-corporate.mp4'
      poster: "images/corporate-offsite-prayer-flags.jpg",
      portrait: true,
      eyebrow: "From the owner",
      label: "Why teams think differently here",
      blurb: "What happens to a team when you take the meeting room away and give them four acres instead.",
    },
    restaurant: {
      id: "owner-restaurant",
      src: null,                      // → 'videos/owner/owner-restaurant.mp4'
      poster: U + "Copy_of_Barbeque_03_cf30f0f667.jpg",
      portrait: true,
      eyebrow: "From the owner",
      label: "The farm is forty steps away",
      blurb: "No buffet, no standing menu — what gets cooked depends on what came out of the ground that morning.",
    },
    about: {
      id: "owner-about",
      src: null,                      // → 'videos/owner/owner-about.mp4'
      poster: OWNER_PORTRAIT,
      portrait: true,
      eyebrow: "From the owner",
      label: "Why we left the trees standing",
      blurb: "A landscape architect explains the one decision the whole estate was built around.",
    },
  };

  /* ── Room reels ───────────────────────────────────────────────────────────
     Keyed by room TYPE first (all four Couple Rooms by the Pool share a reel).
     Add a per-room entry to BY_ROOM to override the type for one room.        */
  var BY_TYPE = {
    "Couple Room by the Pool": {
      id: "room-couple-pool",
      src: null,                      // → 'videos/rooms/couple-pool.mp4'
      poster: U + "bael_1_2b4731913c.png",
      portrait: true,
      label: "Inside a Couple Room",
    },
    "Family Room by the Pool": {
      id: "room-family-pool",
      src: null,                      // → 'videos/rooms/family-pool.mp4'
      poster: U + "spatika_1_5f0d445b7b.png",
      portrait: true,
      label: "Inside a Family Room",
    },
    "Couple Garden Cottage": {
      id: "room-couple-garden",
      src: null,                      // → 'videos/rooms/couple-garden.mp4'
      poster: U + "bodhi_tree_5c9ce0f7ce.webp",
      portrait: true,
      label: "Inside the Couple Cottage",
    },
    "Family Garden Cottage": {
      id: "room-family-garden",
      src: null,                      // → 'videos/rooms/family-garden.mp4'
      poster: U + "chandana_1_07f1342c80.png",
      portrait: true,
      label: "Inside Chandana",
    },
  };

  /* Per-room overrides. e.g. "bodhi-tree": { src:'videos/rooms/bodhi-tree.mp4', … } */
  var BY_ROOM = {};

  /* ── helpers ───────────────────────────────────────────────────────────── */

  /** A video entry is playable once it has a src. */
  function ready(v) { return !!(v && v.src); }

  /** Should this entry render at all? Playable, or PREVIEW is on and it has a poster. */
  function usable(v) { return !!(v && (v.src || (PREVIEW && v.poster))); }

  /** The owner's video for a page key ('home' | 'stays' | 'experiences'). */
  function owner(page) {
    var v = OWNER[page];
    return usable(v) ? v : null;
  }

  /** The reel for a room record (per-room override, else its type). */
  function roomVideo(room) {
    if (!room) return null;
    var v = BY_ROOM[room.id] || BY_TYPE[room.category];
    return usable(v) ? v : null;
  }

  /**
   * The full ordered media set for a room, exactly as the brief asks:
   *   1. the room's own reel   2. the owner's video   3. the photographs
   * Returns [{ kind:'video'|'image', src, poster, portrait, label }]
   */
  function roomMedia(room, ownerPage) {
    var out = [];
    var rv = roomVideo(room);
    if (rv) out.push({ kind: "video", src: rv.src, poster: rv.poster, portrait: rv.portrait !== false, label: rv.label || "Room tour", ready: ready(rv) });
    var ov = owner(ownerPage || "stays");
    if (ov) out.push({ kind: "video", src: ov.src, poster: ov.poster, portrait: ov.portrait !== false, label: ov.label, owner: true, ready: ready(ov) });
    (room && room.imageUrls || []).forEach(function (u) {
      out.push({ kind: "image", src: u, poster: u, portrait: false, ready: true });
    });
    return out;
  }

  window.OrchidMedia = {
    PREVIEW: PREVIEW,
    ownerName: OWNER_NAME,
    ownerRole: OWNER_ROLE,
    ownerPortrait: OWNER_PORTRAIT,
    owner: owner,
    roomVideo: roomVideo,
    roomMedia: roomMedia,
    ready: ready,
    usable: usable,
    types: BY_TYPE,
    ownerAll: OWNER,
  };
})();
