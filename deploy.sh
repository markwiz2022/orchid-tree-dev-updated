#!/usr/bin/env bash
# Orchid Tree — one-command deploy to Vercel.
# Project: "orchid"  ·  Production alias: https://orchid-sigma.vercel.app
#
# Syncs the current production files into .deploy/ (the linked Vercel folder),
# sets "/" to the latest home page, then ships to production.
# Usage:  ./deploy.sh
set -euo pipefail
cd "$(dirname "$0")"

# The pages that go live (wireframes and the .zip are intentionally excluded).
PAGES=(
  home.html guest.html admin.html book-packages.html faq.html
  experiences.html corporate.html about.html restaurant.html
  weddings.html host-with-us.html privacy-policy.html stays.html
  plan-your-dining.html restaurant-dashboard.html
  brand.html brand-components.html brand-voice.html
  blog.html blog-weekend-getaways-near-bangalore.html
  blog-farm-to-table-dining-near-bangalore.html blog-intimate-wedding-venues-near-bangalore.html
)

echo "→ syncing production files into .deploy/"
cp -f "${PAGES[@]}" .deploy/
cp -f shared/*.js .deploy/shared/
cp -f images/* .deploy/images/ 2>/dev/null || true
# The owner's videos and the room reels, once they exist. shared/media.js points
# at these paths; until a file is dropped in, the manifest entry stays null and
# nothing here is copied.
if compgen -G "videos/**/*.mp4" > /dev/null 2>&1 || compgen -G "videos/*/*" > /dev/null 2>&1; then
  mkdir -p .deploy/videos/owner .deploy/videos/rooms
  cp -f videos/owner/* .deploy/videos/owner/ 2>/dev/null || true
  cp -f videos/rooms/* .deploy/videos/rooms/ 2>/dev/null || true
fi
# home.html and index.html are the same page: index.html is the working copy and
# home.html is what the site's own nav links to. Keep them in lockstep.
cp -f index.html home.html
cp -f home.html .deploy/index.html      # "/" serves the latest home page
# Note: the hero video (ORCHID_WEBISTE_9febd4b485.mov) already lives in .deploy/
# and is left untouched so it isn't re-uploaded on every deploy.

echo "→ deploying to Vercel (production)"
cd .deploy
vercel --prod --yes

echo "✓ done — https://orchid-sigma.vercel.app"
