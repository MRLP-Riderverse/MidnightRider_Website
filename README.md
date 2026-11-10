# MidnightRider_Website

Creation date: 2026-11-10

Author signature: MidnightRider.sol

The source for MidnightRider’s personal website: a welcoming web hub where newcomers and returning people can find MRLP, explore the story and work at their own pace, and follow connections across the wider online presence. The site should represent both the Midnight Rider identity and its Solana identity transparently, without making the project dependent on one domain or platform.

**Canonical public address:** https://MidnightRider.sol.site

**GitHub repository:** https://github.com/MRLP-Riderverse/MidnightRider_Website

## Project direction

- Treat this as a personal portfolio and connection hub, distinct from the Riderverse storefront and Acadie.sol community project.
- Keep content and navigation easy to understand; let visitors choose how deeply to explore.
- The owner has deferred the LP-logo splash until the asset is ready. Skip it for now; do not invent the logo. Once supplied, make any splash brief, accessible, and non-blocking.
- Purple, green, and sable are early palette directions, not finalized design tokens. Avoid borrowing Acadie branding.
- Keep the site lightweight, readable, and responsive; avoid heavy effects.
- Keep the code and domain configuration portable so the site can move to another host or domain if needed.
- The Notecore project at `~/Documents/Notes/notecore/projects/websites/MidnightRider/` is the private capture and planning home. Keep raw thoughts there; add only deliberate, public-safe decisions or implementation docs to this repository.

## Structure

- `index.html` — first welcome-page pass (draft; content and visual direction remain open)
- `pages/` — additional public pages when their purpose is clear; `pages/socials.html` is the first, with Instagram and Discord/X/Telegram “Coming soon” placeholders
- `assets/` — source images plus optimized favicon, Apple touch, and PWA app-icon copies generated from `LP_EYE.jpg`
- `site.webmanifest` — install metadata and PWA icon declarations
- `css/`, `js/` — shared site styles and optional client behavior
- `data/` — small structured content, where useful
- `docs/` — public-safe architecture and decision notes
- `todo/` — project-local implementation checklists and handoffs
- `logs/` — append-only operational project logs
- `scripts/`, `tests/` — project-specific helpers and verification

The remaining empty directories are intentional scaffolding. The initial page and palette are exploratory; no framework or final design system is prescribed.

## Local preview

From this directory, serve the site over HTTP:

```bash
python3 -m http.server 5173
```

Then open `http://localhost:5173/`.

Regenerate the favicon and PWA icon copies from the selected portrait with:

```bash
python3 scripts/generate_pwa_icons.py
```

This helper requires Pillow.

## Git and privacy

This repository is the website code and public-safe project documentation, not the personal thought inbox. Do not add the Notecore capture files, private identity details, credentials, wallet secret material, or unreviewed personal notes here. Review staged files before every commit and keep changes focused.
