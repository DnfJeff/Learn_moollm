---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Staged during DnfBrain initialization from the library-template section prototype"
related: [../tech, ../life]
tags: [section]
---

# practices — section ledger & placement guide

You are the sub-librarian for this shelf. Two jobs: **place** new work, and keep the **ledger**.

## Where new work goes (placement rules)

| If the material is… | Where | Example |
|---|---|---|
| A method or workflow | section root, one unit each | how this library files things |
| A pattern (reusable solution shape) | section root, `pattern`-tagged | the registry pattern |
| A checklist or standard you run | section root, `checklist`-tagged | a release checklist |

Subclasses (`workflows/`, `patterns/`, `checklists/`) are created when enough units force
them; until then the shelf stays flat. Note candidate subclasses in
[`../../meta/structure-log.md`](../../meta/structure-log.md).

**Not this section?**
- Tied to one specific system → [`../tech`](../tech/README.md)
- Understanding rather than a way of working → [`../science`](../science/README.md) /
  [`../humanities`](../humanities/README.md)

## The ledger

Every unit on this shelf, one row. Keep it in sync — `validate.py` checks it.

| Unit | What it holds | Status |
|---|---|---|
| [plain-text-durability](plain-text-durability/README.md) | why versioned plain text outlives app-specific formats | canonical |

## Adding a unit

Copy [`../../_templates/unit/`](../../_templates/README.md) → here, fill it, register the row
above, reconcile facets in [`../../meta/by-tag.md`](../../meta/by-tag.md), run
`python validate.py`.
