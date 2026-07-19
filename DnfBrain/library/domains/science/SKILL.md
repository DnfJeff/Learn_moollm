---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Staged during DnfBrain initialization from the library-template section prototype"
related: [../tech, ../humanities]
tags: [section]
---

# science — section ledger & placement guide

You are the sub-librarian for this shelf. Two jobs: **place** new work, and keep the **ledger**.

## Where new work goes (placement rules)

| If the material is… | Subclass | Example |
|---|---|---|
| Mathematics: concepts, methods, results | `mathematics/` | a probability idea kept in your own words |
| Physics, chemistry, astronomy, earth | `physical-sciences/` | an explanation that survived scrutiny |
| Biology, ecology, neuroscience | `life-sciences/` | how a living system works |

If it fits no subclass, file at the section root and note the gap (a candidate subclass) in
[`../../meta/structure-log.md`](../../meta/structure-log.md). That's how the scheme grows
deliberately.

**Not this section?**
- How one specific system/tool/format is built → [`../tech`](../tech/README.md)
- Human affairs, history, ideas about ideas → [`../humanities`](../humanities/README.md)
- A method you re-apply → [`../practices`](../practices/README.md)

## The ledger

Every unit on this shelf, one row. Keep it in sync — `validate.py` checks it.

| Unit | What it holds | Status |
|---|---|---|
| *(none yet — shelves staged, awaiting first units)* | | |

## Adding a unit

Copy [`../../_templates/unit/`](../../_templates/README.md) into the right discipline shelf,
fill it, register the row above, reconcile facets in
[`../../meta/by-tag.md`](../../meta/by-tag.md), run `python validate.py`.
