---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Staged during DnfBrain initialization from the library-template section prototype"
related: [../practices]
tags: [section]
---

# life — section ledger & placement guide

You are the sub-librarian for this shelf. Two jobs: **place** new work, and keep the **ledger**.

## Where new work goes (placement rules)

| If the material is… | Subclass | Example |
|---|---|---|
| Body and mind, maintained | `health/` | sleep, fitness, medical reference |
| Money, understood | `finance/` | a concept, or a decision with rationale |
| The physical world you maintain | `home/` | a repair worth remembering, a system's quirks |
| Cooking and eating | `food/` | a technique, a recipe that earned its place |

If it fits no subclass, file at the section root and note the gap (a candidate subclass) in
[`../../meta/structure-log.md`](../../meta/structure-log.md).

**Not this section?**
- A method that isn't life-specific → [`../practices`](../practices/README.md)
- A device's internals (vs. just maintaining it) → [`../tech`](../tech/README.md)

## The ledger

Every unit on this shelf, one row. Keep it in sync — `validate.py` checks it.

| Unit | What it holds | Status |
|---|---|---|
| *(none yet — shelves staged, awaiting first units)* | | |

## Adding a unit

Copy [`../../_templates/unit/`](../../_templates/README.md) into the right shelf, fill it,
register the row above, reconcile facets in [`../../meta/by-tag.md`](../../meta/by-tag.md),
run `python validate.py`.
