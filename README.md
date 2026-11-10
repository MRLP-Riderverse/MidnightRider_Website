# MidnightRider_Website

Creation date: 2026-11-10

Author signature: MidnightRider.sol

The source for MidnightRider’s personal website: a welcoming web hub where newcomers and returning people can find MRLP, explore the story and work at their own pace, and follow connections across the wider online presence. The site should represent both the Midnight Rider identity and its Solana identity transparently, without making the project dependent on one domain or platform.

**Canonical public address:** https://MidnightRider.sol.site

**GitHub repository:** https://github.com/MRLP-Riderverse/MidnightRider_Website

## Project direction

- Treat this as a personal portfolio and connection hub, distinct from the Riderverse storefront and Acadie.sol community project.
- Keep content and navigation easy to understand; let visitors choose how deeply to explore.
- Favor a fast, readable, responsive site over heavy effects. A brief LP-logo splash is an idea to evaluate, not a requirement to build before the core experience works.
- Purple, green, and sable are early palette directions, not finalized design tokens. Avoid borrowing Acadie branding.
- Keep the code and domain configuration portable so the site can move to another host or domain if needed.
- The Notecore project at `~/Documents/Notes/notecore/projects/websites/MidnightRider/` is the private capture and planning home. Keep raw thoughts there; add only deliberate, public-safe decisions or implementation docs to this repository.

## Structure

- `index.html` — homepage entry point (to be designed)
- `pages/` — additional public pages when their purpose is clear
- `css/`, `js/` — site styles and behavior
- `assets/` — images, icons, fonts, and other static media
- `data/` — small structured content, where useful
- `docs/` — public-safe architecture and decision notes
- `todo/` — project-local implementation checklists and handoffs
- `logs/` — append-only operational project logs
- `scripts/`, `tests/` — project-specific helpers and verification

Empty directories are intentional scaffolding. No design system, framework, or page structure is prescribed yet.

## Local preview

From this directory, serve the site over HTTP once an `index.html` exists:

```bash
python3 -m http.server 5173
```

Then open `http://localhost:5173/`.

## Git and privacy

This repository is the website code and public-safe project documentation, not the personal thought inbox. Do not add the Notecore capture files, private identity details, credentials, wallet secret material, or unreviewed personal notes here. Review staged files before every commit and keep changes focused.
