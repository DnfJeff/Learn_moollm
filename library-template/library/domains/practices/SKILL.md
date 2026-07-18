---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Shipped with the library-template quickstart"
related: [../technical, ../knowledge]
tags: [section]
---

# practices — section ledger & placement guide

Sub-librarian for this shelf. **Place** new work, keep the **ledger**.

## Where new work goes (placement rules)

| If the material is… | Subclass | Example |
|---|---|---|
| A repeatable sequence to run | `checklists/` | a release checklist, a runbook |
| A reusable shape of a solution | `patterns/` | "how I structure a migration" |
| A convention you hold to | `standards/` | naming rules, a style you enforce |

Fits none? File at the section root and log a candidate subclass in
[`../../meta/structure-log.md`](../../meta/structure-log.md).

**Not this section?**
- How one concrete thing works → [`../technical`](../technical/README.md)
- What's true about a subject → [`../knowledge`](../knowledge/README.md)

## The ledger

| Unit | What it holds | Status |
|---|---|---|
| *(none yet — add your first unit)* | | |

## Adding a unit
Copy [`../../_templates/unit/`](../../_templates/README.md) → `practices/<name>/`, fill it,
register the row above, reconcile facets in [`../../meta/by-tag.md`](../../meta/by-tag.md), and
run `python validate.py`.
