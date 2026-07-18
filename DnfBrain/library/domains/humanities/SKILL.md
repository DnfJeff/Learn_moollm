---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Staged during DnfBrain initialization from the library-template section prototype"
related: [../arts, ../science]
tags: [section]
---

# humanities — section ledger & placement guide

You are the sub-librarian for this shelf. Two jobs: **place** new work, and keep the **ledger**.

## Where new work goes (placement rules)

| If the material is… | Subclass | Example |
|---|---|---|
| An event, era, or figure | `history/` | subdivide by era or region on first unit |
| An idea, argument, or thinker | `philosophy/` | subdivide by branch or tradition |
| A language or linguistics | `language/` | one shelf per language studied |

If it fits no subclass, file at the section root and note the gap (a candidate subclass) in
[`../../meta/structure-log.md`](../../meta/structure-log.md).

**Not this section?**
- A person known chiefly through a creative work → their write-up lives with the work under
  [`../arts`](../arts/README.md); the [characters registry](../../characters/README.md) holds
  the by-name quick card either way.
- The natural world → [`../science`](../science/README.md)

## The ledger

Every unit on this shelf, one row. Keep it in sync — `validate.py` checks it.

| Unit | What it holds | Status |
|---|---|---|
| *(none yet — shelves staged, awaiting first units)* | | |

## Adding a unit

Copy [`../../_templates/unit/`](../../_templates/README.md) into the right shelf, fill it,
register the row above, reconcile facets in [`../../meta/by-tag.md`](../../meta/by-tag.md),
run `python validate.py`.
