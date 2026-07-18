---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Shipped with the library-template quickstart"
related: [../knowledge, ../practices]
tags: [section]
---

# technical — section ledger & placement guide

You are the sub-librarian for this shelf. Two jobs: **place** new work, and keep the **ledger**.

## Where new work goes (placement rules)

| If the material is… | Subclass | Example |
|---|---|---|
| How a file format or binary layout works | `formats/` | a spec you reverse-engineered |
| How a system or service is built | `systems/` | an architecture teardown |
| How a tool or protocol behaves | `tools/` | flags, quirks, gotchas kept for reuse |

If it fits none of these, file it at the section root as its own unit and note the gap in
[`../../meta/structure-log.md`](../../meta/structure-log.md) — a candidate new subclass. That's
how the scheme grows deliberately instead of sprawling.

**Not this section?**
- Subject theory not tied to one system → [`../knowledge`](../knowledge/README.md)
- A repeatable way of working → [`../practices`](../practices/README.md)

## The ledger

Every unit on this shelf, one row. Keep it in sync — `validate.py` checks it.

| Unit | What it holds | Status |
|---|---|---|
| [plain-text-durability](plain-text-durability/README.md) | why versioned plain text outlives app-specific formats | canonical |

## Adding a unit

1. Copy [`../../_templates/unit/`](../../_templates/README.md) to `technical/<name>/` (or into a
   subclass).
2. Fill `SKILL.md` (the knowledge) + its frontmatter; write `CARD.yml` advertisements so it's
   routable.
3. Add a row above; add a facet to [`../../meta/by-tag.md`](../../meta/by-tag.md) if it
   introduces one (from the [ontology](../../meta/ontology.md) first).
4. Run `python validate.py`.
