# TODO and handoff notes

This folder holds actionable, project-local website work and durable handoffs. It is not the raw idea inbox; capture and exploration stay in the Notecore project outside this repository.

Start new sessions with [`PROJECT_BRIEF.md`](PROJECT_BRIEF.md) for the distilled intent, design decisions, open questions, privacy boundary, and resumption workflow. Update it only when decisions change; keep transient task status in checklists or handoff notes.

## Active
- [ ] Shape a public-safe content outline for a future identity/about page and a “what MRLP does” page; keep real name, birth details, hometown/family history, and lore specifics out until the owner chooses what to publish.
- [x] Create the initial Home → Socials path with the supplied Instagram profile and consistent home links.
- [x] Add Discord, X, and Telegram as non-clickable “Coming soon” placeholders; add no invented usernames or URLs.
- [x] Use `LP_EYE.jpg` as the current PFP: small borderless circle (128 px desktop / 96 px mobile); do not use the older Strays PFPs as the current image.
- [x] Generate the favicon, Apple touch icon, and standard/maskable PWA icons from `LP_EYE.jpg`; link them through `site.webmanifest` on both pages.
- [x] Remove the repeated “More, coming soon” label and duplicate Socials CTA from the homepage section; remove the Socials intro sentence.
- [x] Keep the same sitewide footer content **“Created in 2026”** on both current pages, with shared styling; the static markup is repeated per page.
- [x] Change the homepage tab title to **“MRLP - MidnightRider.sol”** and keep that identity on the Socials tab title.
- [x] Keep the unused older Strays PFP copies local-only by ignoring them in `.gitignore`; leave deletion/archive as the owner's choice.
- [x] Verify both pages at phone (390 px), tablet (768 px), and desktop (1440 px): local links and icons resolve, image loads, footer and titles are consistent, no horizontal overflow; keyboard focus is visible and ordered; sticky header remains at the viewport top.
- [ ] Review the exact public-safe file set and deployment after explicit commit/push approval; confirm the domain and fallback path separately.


## Deferred
- [ ] LP-logo splash: skip for now; wait until the owner provides the asset. Do not invent a substitute.

## Notes
- Keep raw notes in `~/Documents/Notes/notecore/projects/websites/MidnightRider/`.
- Convert these broad prompts into focused checklists or handoffs as decisions are made.
- Mark review and implementation status separately; do not imply an idea is completed because it has been discussed.
