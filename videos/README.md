# Videos

Drop the owner's files here, then point `shared/media.js` at them. Nothing else
on the site needs to change — every card, carousel and modal reads from that
one manifest.

## Where things go

```
videos/
  owner/
    owner-welcome.mp4      → home page      (OWNER.home)
    owner-rooms.mp4        → stays page     (OWNER.stays)
    owner-day.mp4          → experiences    (OWNER.experiences)
  rooms/
    couple-pool.mp4        → the 4 Couple Rooms by the Pool
    family-pool.mp4        → the 4 Family Rooms by the Pool
    couple-garden.mp4      → Hattimara + Bodhi Tree
    family-garden.mp4      → Chandana
```

A single room can override its type's reel — add an entry to `BY_ROOM` in
`shared/media.js` keyed by room id (`"bodhi-tree"`, `"chandana"`, …).

## Turning a video on

In `shared/media.js`, find the entry and replace the `null`:

```js
home: {
  src: 'videos/owner/owner-welcome.mp4',   // was: null
  poster: 'videos/owner/owner-welcome.jpg',
  portrait: true,
  ...
}
```

Give it a `poster` too — a still frame exported from the video. The poster is
what the card thumbnail shows before playback, so it does a lot of work.

## Preview mode

`shared/media.js` opens with:

```js
var PREVIEW = true;
```

While it's `true`, video cards with no file still render — poster, play button,
and a small "Video coming soon" tag — so the layout can be reviewed before the
owner's files land. **Set it to `false` before launch** and any still-empty card
disappears cleanly, with the page falling back to photography.

## Encoding

The owner's pieces and the room reels are **portrait, 9:16**. The estate
photography is landscape — the player handles both, so don't crop the reels to
match the photos.

```bash
# portrait reel → web (H.264, ~2.5 Mbps, no audio track lost)
ffmpeg -i input.mov -vf "scale=1080:-2" -c:v libx264 -profile:v main \
       -crf 24 -preset slow -movflags +faststart -c:a aac -b:a 128k \
       videos/owner/owner-welcome.mp4

# poster still, 2 seconds in
ffmpeg -i input.mov -ss 00:00:02 -vframes 1 -q:v 3 \
       videos/owner/owner-welcome.jpg
```

Keep each file **under ~8 MB**. These autoplay muted on hover, so weight is felt
immediately. `-movflags +faststart` matters — without it the video won't begin
until the whole file has downloaded.
