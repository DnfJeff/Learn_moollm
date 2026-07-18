---
status: canonical
tags: [templates, registry, pattern]
---

# registry — the surfaced by-name layer (copy-me)

**This is the registry template: the standardized pattern for surfacing a category of things
near the top of the library so they resolve by NAME, while their full write-ups stay deep in
the tree with their context.** `library/characters/` is the first live instance.

## When a category earns a registry

The classification tree is the spine — most things need nothing else. Surface a registry only
when **all three** hold:

1. **By-name lookup is the common access.** You reach for "*danny-thomas*", "*python*",
   "*ripgrep*" — not "1950s sitcom leads" or "scripting languages".
2. **Instances scatter across the tree.** The same figure in two shows; the same language in
   docs, projects, and tooling notes. One classified home can't serve the lookup.
3. **A small card answers most queries.** Who/what, why known, where the full material is.
   If every lookup needs the full write-up anyway, the registry adds a hop, not a shortcut.

Candidates that pattern-match: characters/figures (live), programming languages + their
official docs, tools, organizations. What gets surfaced is deliberately left configurable —
the *process* is what's standardized here.

## The shape (three synced layers + a librarian)

```
library/<registry>/
├── GLANCE.yml / CARD.yml / SKILL.md / README.md    the librarian card stack —
│                                                   README is the human browse layer,
│                                                   SKILL holds the rules + roster
├── MANIFEST.yaml        every card, one row — the scan tier for the whole registry
└── <name>.yaml          one quick card per entry: facts + appearances[] routes
```

- **Cards point; content lives with its work/class** (`CANONICAL-COLLECTION`). A card that
  grows paragraphs is content leaking in — push it to the write-up, re-shrink the card.
- **One entry, one card, N routes.** Multiple appearances = multiple `appearances:` rows on
  the same card, never a second card.
- **Three layers sync** (`LEDGER-SYNC`): card, MANIFEST row, README row. The `registrar`
  capability is the procedure; `validate.py` is the check.

## Instantiate one

1. Copy this directory's `entry.yaml` and `MANIFEST.yaml` into `library/<registry>/`; build
   the librarian stack from [`../section/`](../section/) (its ledger becomes the roster).
2. Register the layer itself: a line in `library/INDEX.md`, an entry in
   `meta/structure-log.md` (surfacing a registry is a structural change), terms in
   `meta/ontology.md`.
3. Seed it from write-ups that already exist — a registry is surfaced *from* the tree, never
   written ahead of it.
