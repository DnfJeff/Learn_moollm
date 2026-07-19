---
status: draft
created: YYYY-MM-DD
reviewed: YYYY-MM-DD
provenance: "Instantiated from _templates/section/"
related: []
tags: [section]
---

# <section-name> — section ledger & placement guide

You are the sub-librarian for this shelf. Two jobs: **place** new work, and keep the **ledger**.

## Where new work goes (placement rules)

| If the material is… | Subclass | Example |
|---|---|---|
| <criterion> | `<subclass>/` | <example> |
| <criterion> | `<subclass>/` | <example> |

If it fits no subclass, file at the section root and note the gap (a candidate subclass) in
`../../meta/structure-log.md`. That's how the scheme grows deliberately.

**Not this section?** Point onward:
- <neighbor test> → `../<other-section>`

## The ledger

Every unit on this shelf, one row. Keep it in sync — `validate.py` checks it.

| Unit | What it holds | Status |
|---|---|---|
| *(none yet)* | | |

## Adding a unit
Copy `../../_templates/unit/` → here, fill it, register the row above, reconcile facets in
`../../meta/by-tag.md`, run `python validate.py`.
