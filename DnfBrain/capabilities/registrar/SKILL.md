---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Authored during DnfBrain initialization, alongside the first registry (library/characters/)"
related: [../curator/SKILL.md, ../../library/_templates/registry/README.md]
tags: [capability, library-ops]
---

# registrar — how registry maintenance actually works

Read this to change how registries behave. To *run* the procedures, `CARD.yml` is enough.

The premise: the classification tree answers "where does this *belong*?"; a registry answers
"where is ***<name>***?" Those are different questions, and the second one deserves a surfaced
layer only when the [three criteria](../../library/_templates/registry/README.md) hold. The
registrar owns that layer's integrity.

## ADD-CARD — a write-up landed; give it a card

1. Confirm the write-up exists and lives with its work (the curator files content; if there's
   no write-up yet, this is a curator job first — cards never precede content).
2. Copy `library/_templates/registry/entry.yaml` → `library/<registry>/<name>.yaml`
   (lowercase-kebab). Fill `quick:` (small — facts, not paragraphs), `aka:`, one
   `appearances:` row routing to the write-up, `k-lines`.
3. Add the row in `MANIFEST.yaml` (bump `count:`), the browse row in the registry `README.md`,
   and the roster row in its `SKILL.md`.
4. Cross-link back: the write-up's frontmatter `related:` gains the card's path.
5. `python validate.py`.

## ADD-APPEARANCE — same figure, new work

Append an `appearances:` row to the **existing** card; update the manifest row's appearance
count and, if the "known for" line changed, the manifest/browse lines. **Never** create a
second card for the same figure (`ONE-CARD-PER-ENTITY`, below).

## SURFACE — does this category earn a registry?

Run the three criteria (by-name access · scattered instances · card-answers-most). All three →
instantiate from `_templates/registry/`, seed it **from existing write-ups only**, add the
`library/INDEX.md` line, the `meta/ontology.md` terms, and the `meta/structure-log.md` entry.
Any criterion fails → say so and stop; the tree plus `by-*` finding aids already serve it.

## SYNC — reconcile drift

Diff cards ↔ `MANIFEST.yaml` ↔ README table ↔ SKILL roster. Cards missing rows get rows;
rows without cards are removed with a note; `count:` is corrected. Then `validate.py`.

## Failure modes (named, so they're checkable)

- **`CONTENT-IN-CARD`** — a card growing paragraphs. Cards route; write-ups hold. Push the
  material to the write-up, re-shrink the card.
- **`ONE-CARD-PER-ENTITY`** (violated) — two cards for one figure because they appear in two
  works. The whole point of the registry is one card, N routes.
- **`GHOST-CARD`** — a card whose write-up doesn't exist (or a write-up with no card once its
  category is registry-tracked). Cards never precede content; content in a tracked category
  never goes uncarded.
- **`PREMATURE-REGISTRY`** — surfacing a layer for a category with two entries and no by-name
  habit. Registries are earned, like card stacks.
