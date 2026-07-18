---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Shipped with the library-template quickstart"
related: [../technical, ../practices]
tags: [section]
---

# knowledge — section ledger & placement guide

Sub-librarian for this shelf. **Place** new work, keep the **ledger**.

## Where new work goes (placement rules)

| If the material is… | Subclass | Example |
|---|---|---|
| A concept or definition you return to | `concepts/` | "what eventual consistency means" |
| Synthesized research on a field | `research/` | a literature synthesis, a survey note |
| A way to think about something | `models/` | a mental model, a framework |

Fits none? File at the section root and log a candidate subclass in
[`../../meta/structure-log.md`](../../meta/structure-log.md).

**Not this section?**
- How one concrete thing works → [`../technical`](../technical/README.md)
- A repeatable way of working → [`../practices`](../practices/README.md)

## The ledger

| Unit | What it holds | Status |
|---|---|---|
| *(none yet — add your first unit)* | | |

## Adding a unit
Copy [`../../_templates/unit/`](../../_templates/README.md) → `knowledge/<name>/`, fill it,
register the row above, reconcile facets in [`../../meta/by-tag.md`](../../meta/by-tag.md), and
run `python validate.py`.
