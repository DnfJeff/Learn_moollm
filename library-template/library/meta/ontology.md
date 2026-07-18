---
status: canonical
tags: [meta, ontology]
---

# Ontology — the controlled vocabulary

**This is the ontology: the authority list of preferred terms for the whole library. Its history
and additions are noted here.** Every tag and every card `k-line` is drawn from this file. New
terminology is introduced *here first*, deliberately, then used — that is what keeps the
vocabulary meaningful instead of a fog of near-synonyms.

Format per term: `name` — one-line meaning — when to apply it.

## Sections (top-level classes)

- `technical` — knowledge about how a specific system, tool, format, or protocol works.
- `knowledge` — durable understanding of a subject, not tied to one system.
- `practices` — repeatable ways of working: methods, patterns, checklists.

## Unit types

- `section` — a classification shelf; its `SKILL.md` is a ledger + placement rules.
- `unit` — one atomic knowledge item as a card stack.
- `note` — the cheap rung: a single-file unit that hasn't earned a full stack.
- `project` — a time-bound instance mirroring the workflow stages.

## Status values

- `draft` — captured, not yet trusted. Visible, flagged.
- `canonical` — the authoritative statement on its subject.
- `superseded` — retired; lives in `archives/`, links forward to its replacement.

## Facets (cross-cutting tags — extend deliberately)

Seed set. Add a facet here **before** tagging with it. Prefer names already meaningful to a
domain expert; every private coinage is a term the next reader must learn.

- `reference` — look-it-up material you expect to reuse.
- `finding` — something discovered through investigation or reverse engineering.
- `decision` — a choice made, with its rationale (an ADR-style record).
- `pattern` — a reusable shape of a solution.
- `checklist` — a repeatable sequence to run.
- `open-question` — a known unknown, parked deliberately.

## Change log
- (date) — Ontology seeded by the library-template quickstart. Replace the section terms when
  you rename `domains/`.
