# TODO and handoff notes

This folder holds actionable, project-local website work and durable handoffs. It is not the raw idea inbox; capture and exploration stay in the Notecore project outside this repository.

Start new sessions with [`PROJECT_BRIEF.md`](PROJECT_BRIEF.md) for the distilled intent, design decisions, open questions, privacy boundary, and resumption workflow. Update it only when decisions change; keep transient task status in checklists or handoff notes.

## Active
- [x] Add `strays_pfp_LP.png` as supporting WIP-section artwork: right column on wide screens, below copy on mobile; keep `strays_pfp_LP2.png` ignored and do not replace the current portrait. **Done locally:** image loads at 1500 px source size; layout switches from two columns at 1440 px to a stacked 343 px content column at 390 px, with no horizontal overflow.
- [x] Add one shared top divider to `.site-footer` and verify its appearance on Home and Socials. **Done locally:** shared CSS adds a 1 px `var(--line)` top border; verified on both pages at 390 px and 1440 px widths, with no horizontal overflow; owner reviewed the viewport visuals as good.
- [x] Review the owner's first visual/copy pass; preserve the revised personal voice, confirm the X profile link as owner-approved, and keep Projects paused/unlinked.
- [ ] Shape a public-safe content outline for a future identity/about page and a “what MRLP does” page; keep real name, birth details, hometown/family history, and lore specifics out until the owner chooses what to publish.
- [x] Create the initial Home → Socials path with the supplied Instagram profile and consistent home links.
- [x] Keep Discord and Telegram as non-clickable “Coming soon” placeholders; the owner supplied/confirmed the X profile link.
- [x] Use `LP_EYE.jpg` as the current PFP: small borderless circle (128 px desktop / 96 px mobile); do not use the older Strays PFPs as the current image.
- [x] Generate the favicon, Apple touch icon, and standard/maskable PWA icons from `LP_EYE.jpg`; link them through `site.webmanifest` on both pages.
- [x] Remove the repeated “More, coming soon” label and duplicate Socials CTA from the homepage section; remove the Socials intro sentence.
- [x] Keep the shared footer structure/styling consistent on current pages; footer wording is currently under owner-led exploration.
- [x] Use the homepage tab title **“MRLP - MidnightRider.sol”**; Socials keeps page context with MRLP identity.
- [x] Keep the intentionally paused Projects draft local-only and unlinked until its content is ready; exclude it from public commits/deployment.
- [x] Keep the unused older Strays PFP copies local-only by ignoring them in `.gitignore`; leave deletion/archive as the owner's choice.
- [x] Verify both pages at phone (390 px), tablet (768 px), and desktop (1440 px): local links and icons resolve, image loads, footer and titles are consistent, no horizontal overflow; keyboard focus is visible and ordered; sticky header remains at the viewport top.
- [x] Review the exact public-safe file set and verify the approved commit/push deployment; commit `39746ea` was published and served at the canonical domain after the Pages build completed.
- [ ] Confirm the domain and fallback path separately.
- [x] Check the day's MidnightRider Notecore entries against the TODO board; preserve the owner's original capture and track actionable follow-ups here.
- [ ] Refine the expanded-name headline: test letter spacing/legibility across narrow and wide screens; later prototype a tap-to-reveal full-name interaction (avoid hover-only behavior).

## Deferred
- [ ] LP-logo splash: skip for now; wait until the owner provides the asset. Do not invent a substitute.

## Notes
- Keep raw notes in `~/Documents/Notes/notecore/projects/websites/MidnightRider/`.
- Convert these broad prompts into focused checklists or handoffs as decisions are made.
- Mark review and implementation status separately; do not imply an idea is completed because it has been discussed.
