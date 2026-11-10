# AGENTS.md — MidnightRider_Website

## Project intent
- Treat `README.md` as the canonical summary of the site's purpose and current boundaries.
- This is MRLP's personal web hub, not the Riderverse store or Acadie.sol community site. Keep its identity and content distinct.
- The public address is `https://MidnightRider.sol.site`; keep implementation portable across domains and hosts.

## Working rules
- The Notecore project at `~/Documents/Notes/notecore/projects/websites/MidnightRider/` is the private capture inbox. Preserve its raw notes there; do not copy them into this public repository by default.
- Promote only deliberate, public-safe decisions from Notecore into project docs or implementation.
- Keep changes small and understandable. Do not add frameworks, animation, pages, or design infrastructure without a demonstrated need.
- Responsive behavior, readability, performance, and accessible interaction matter from the first real page.
- Keep `logs/` append-only. Put implementation checklists and durable handoffs in `todo/`.
- Put project-specific helpers in `scripts/`; add tests or reproducible checks for behavior that merits them.
- Never commit secrets, wallet seed/private-key material, credentials, or private captures. Inspect staged files before commits.
- Do not commit or push without the user's explicit approval.

## Starting work
1. Read `README.md`, `todo/README.md`, and relevant project notes.
2. Check `git status` and inspect existing code before editing.
3. Make the smallest change that serves a stated need.
4. Run relevant checks and inspect the diff before reporting completion.

## Current state
- This repository is intentionally a fresh content/code base with folder scaffolding only. There is no starter homepage or inherited LP64 theme; decide the visual system with the project owner before implementing the site.
