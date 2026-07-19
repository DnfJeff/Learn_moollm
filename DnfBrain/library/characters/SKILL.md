---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Staged during DnfBrain initialization; first instance of the registry pattern (library/_templates/registry/)"
related: [../domains/arts/SKILL.md, ../_templates/registry/README.md]
tags: [registry, character]
---

# characters — registry rules & roster

You are the registry librarian. The registry answers one question — **"where is <name>?"** —
without the reader knowing which work, era, or section holds the write-up.

## The contract (what keeps this from becoming a second home)

1. **Cards point; write-ups live with their works.** A card carries quick facts (who, why
   known) and `appearances:` routes. The full write-up stays inside its work
   (`.../the-danny-thomas-show/characters/danny-thomas.md`) — the single source of truth
   (`CANONICAL-COLLECTION`). A card that grows paragraphs is content leaking in; move the
   material to the write-up and re-shrink the card.
2. **Dual (or more) positioning.** A figure with write-ups in several works gets **one card**
   with several `appearances:` entries — never two cards, never a copied write-up.
3. **Three layers stay in sync** (`LEDGER-SYNC`): the card (`<name>.yaml`), its
   [`MANIFEST.yaml`](MANIFEST.yaml) row, and its row in the browsable [`README.md`](README.md).
   The `registrar` capability (`../../capabilities/registrar/`) is the procedure.
4. **Names are addresses.** Card file = `<lowercase-kebab-name>.yaml`. Aliases (stage names,
   character names) go in the card's `aka:` so by-name resolution catches them.

## The roster

| Figure | Card | Write-ups |
|---|---|---|
| Danny Thomas (Danny Williams) | [danny-thomas.yaml](danny-thomas.yaml) | [the-danny-thomas-show](../domains/arts/film/tv/1950s/sitcom/the-danny-thomas-show/characters/danny-thomas.md) |

## Adding a figure

1. The full write-up lands first, inside its work (the arts librarian places it).
2. Copy [`../_templates/registry/entry.yaml`](../_templates/registry/entry.yaml) to
   `<name>.yaml`; fill quick facts + `appearances:` routes.
3. Add the `MANIFEST.yaml` row and the README + roster rows here.
4. `python validate.py`.

## Registry history
- 2026-07-18 — Registry created as the first instance of the registry pattern; seeded with
  danny-thomas. Logged in [`../meta/structure-log.md`](../meta/structure-log.md).
