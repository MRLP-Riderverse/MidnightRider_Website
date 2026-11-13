# Project brief — MidnightRider personal website

Last distilled: 2026-11-10. This is a concise working brief, not a replacement for the private capture notes.

## Purpose

Build a personal web hub for MidnightRider / MRLP: a clear place to send newcomers and returning people so they can find the person, work, and online projects they care about, and explore at their own pace. It is a personal portfolio and connection point—not the Riderverse storefront and not the Acadie.sol community site.

Canonical public address: `https://MidnightRider.sol.site`

Source repository: `https://github.com/MRLP-Riderverse/MidnightRider_Website`

Keep the code portable. The public address should be a replaceable configuration/deployment concern, not a hard dependency in site architecture.

## Established direction

- Display name: **MidnightRider**; familiar short name: **MRLP**. Current homepage copy uses the owner's evolving first-person voice; do not restore earlier draft wording without being asked.
- The header home link currently uses **⁜ MidnightRider.sol**. The dotted-cross glyph is temporary; replace it with the owner's logo asset when supplied, without assuming the glyph is the permanent logo.
- Purple, green, and sable are palette exploration. The first charcoal/violet/green pass was considered a decent starting point and should remain for now, not be treated as locked brand standards.
- The visitor should be able to learn who MRLP is and what MRLP does, and reach relevant online presences without being overwhelmed.
- Favor simple, quick, readable pages that adapt across phones, tablets, desktop, and orientation changes. The owner deferred the LP-logo splash until the asset is ready; skip it for now and do not invent it. Once supplied, make any splash brief, accessible, and non-blocking.
- This website may eventually identify the Solana identity alongside the persona. Be deliberate about financial links and public wallet information; do not add addresses or wallet details without explicit owner approval.
- The logo is not yet available. Do not invent or generate a replacement; the current mark is a temporary text glyph.

## Current prototype

- Homepage tab title: **MRLP - MidnightRider.sol**; socials page title keeps its page context and the same identity.
- The landing-page eyebrow is **“i am”**; the introduction is currently **“MRLP for short.”**
- The first visitor path is **Home → Socials**. Instagram `@MidnightRiderLP` and the owner-confirmed X profile are linked; Discord and Telegram are non-clickable **Coming soon** placeholders. The homepage Socials link navigates to the Socials page in the same tab.
- The selected `assets/images/LP_EYE.jpg` is the site's current PFP and PWA-icon source; do not use the older Strays PFPs as the current image. The JPEG is 2048 × 2048 (~164 KB) and is rendered as a small, borderless circle (128 px desktop / 96 px mobile).
- `site.webmanifest` references 192 px / 512 px standard and maskable icons; `scripts/generate_pwa_icons.py` creates those, the 16 px / 32 px favicons, and the 180 px Apple touch icon in `assets/images/`.
- Home and Socials use the same footer structure and shared styling; current footer wording is an owner-authored experiment. Keep it consistent sitewide as more pages are activated.
- The homepage lower section is owner-authored teaser copy. A Projects page draft is deliberately paused, unlinked, and kept local-only until the owner resumes it.
- Keep the palette and layout open to review; the project remains a draft.


## Open questions — resolve from the owner, not by guessing

1. What public-safe content belongs in “Who I am” and “What I do,” and what should stay private?
2. Which additional social profiles, projects, and contact destinations should be linked, and in what order?
3. How should the identity story be told, and what personal details should be omitted?
4. What exactly should the future logo asset replace: only the header glyph, or other uses too?
5. The owner has deferred the LP-logo splash until the asset is ready. Skip it for now; once supplied, should visitors have a skip/bypass option?
6. What is the preferred deployment/domain setup once the owner's Pages/domain pairing is complete?

## Privacy and source-of-truth boundary

- Private raw capture remains in `~/Documents/Notes/notecore/projects/websites/MidnightRider/`.
- That folder and its `.txt` / recap / session files are not part of this public repository. Do not copy raw notes into commits or public project docs.
- This brief is a deliberate public-safe distillation. When updating it, select only ideas the owner intends to carry forward; do not expose family history, precise personal details, financial information, or unreviewed lore by inference.
- Check `PROJECT_POLICY.md` and `AGENTS.md` before writing public-facing content, wallet links, contacts, or identity details.

## Working and release contract

1. Read `README.md`, this brief, `todo/README.md`, and `PROJECT_POLICY.md` before resuming.
2. Inspect current code and `git status`; preserve unrelated work.
3. Make a small, reversible change and verify it locally, including responsive behavior for visible UI changes.
4. Inspect the exact staged paths and diff for privacy/security before committing.
5. Ask for explicit approval before commit or push; verify remote/deployment separately after an approved push.

## First useful next steps

- Agree on a compact content outline before adding more sections or decorative UI.
- Identify the actual links to include after the owner chooses them.
- Keep improving the landing page in small reviewable passes; update this brief only when a decision is actually made.
- Add the real logo only when the owner provides the file and any display/cropping preference.
