# registrar — why registries get their own librarian

**This is the registrar capability's backstory: why the surfaced by-name layer needs a keeper
distinct from the curator, and where changes are noted.**

## The idea

The curator answers "where does this belong?" by walking the classification chain. But some
things are reached by *name*, not by class — you think "danny-thomas", not "1950s sitcom
leads". The registry layer (first instance: `library/characters/`) serves that access path
with small quick cards near the top of the library, each routing to the full write-ups deep
in the tree — including to *multiple* works when a figure earns write-ups in more than one.

That layer is three files that must agree (card, manifest row, browse row) times every entry.
Agreement doesn't maintain itself; the registrar is the procedure that maintains it, and
`validate.py` is the check that it did.

## Division of labor

- **curator** — files *content*: the write-up lands with its work, provenance and all.
- **registrar** — files *routes*: the card, the manifest row, the browse row, the cross-link.

Content first, card second, always: a card pointing at nothing is worse than no card.

## Changes
- 2026-07-18 — Capability authored during DnfBrain initialization, alongside the characters
  registry and the `_templates/registry/` pattern.
