---
status: canonical
tags: [inbox, intake]
---

# inbox — drop anything here

**This is the inbox README: the intake protocol, stated at the point of use.**

This is the release valve that keeps the whole library alive. **Capture is free; filing is
deliberate.** Anything — a link, a screenshot, a half-formed note, a finding, a finished
artifact — goes here immediately, with no classification, no card stack, no ceremony
(`CLASSIFY-LAST`).

## The one rule at the door
Never refuse to capture something because you're unsure where it goes. Uncertainty routes *here*,
not into a guessed shelf in `domains/`.

## How to drop something
One file, any rough name, with a breadcrumb at the top: **what it is, where it came from, the
date.** That breadcrumb becomes the unit's `provenance` at triage time
(`PROVENANCE-OR-IT-DIDNT-HAPPEN`).

## Triage (on a rhythm — daily/weekly, not at the door)
Run the `curator` capability's TRIAGE. For each item:
1. **Atomize** — split mixed dumps into one-concept pieces.
2. **LOCATE** — walk the librarian chain (chief librarian → section librarian) to a target.
3. **Create** the unit from [`../_templates/unit/`](../_templates/README.md) (or the single-file
   `note.md` for the cheap rung); fill frontmatter incl. provenance.
4. **Register** in the section ledger and reconcile facets in [`../meta/by-tag.md`](../meta/by-tag.md).
5. **Remove** the item from here.
6. **Validate** — `python validate.py`.

## The failure mode to watch
`HEAP` — capturing without ever triaging. The inbox is a queue, not a landfill. If it only grows,
the library has stopped working. A slightly messy inbox that always gets emptied is the goal.
