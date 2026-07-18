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

- `arts` — creative works and their makers: film, tv, music, literature, visual art.
- `tech` — computing: platforms, games as systems, programming, AI, the web.
- `science` — durable understanding of the natural and formal worlds.
- `humanities` — human affairs: history, philosophy, language.
- `life` — practical living: health, finance, home, food.
- `practices` — repeatable ways of working: methods, patterns, checklists.

## Structural terms

- `section` — a top-level classification shelf; its `SKILL.md` is a ledger + placement rules.
- `class` — an intermediate level of the tree; carries a finding-aid `README.md`.
- `unit` — one atomic knowledge item as a card stack.
- `note` — the cheap rung: a single-file unit that hasn't earned a full stack.
- `project` — a time-bound instance mirroring the workflow stages.
- `registry` — a surfaced by-name layer of quick cards routing to write-ups in the tree
  (first instance: `characters`; pattern: `_templates/registry/`).
- `registry-card` — one entry in a registry: quick facts + `appearances:` routes; never a
  second home for content.
- `finding-aid` — any file whose job is navigation, not content: class READMEs, `by-*` maps,
  manifests.

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
- `media` — a creative work or material about one (shows, films, albums, books).
- `character` — a person or figure, real or fictional, tracked in the characters registry.
- `deprecated` — about something retired or dead; the knowledge is kept, the thing is not.
- `official-docs` — pointers into an authority's own documentation, with capture date.

## Change log
- 2026-07-18 — Reseeded for DnfBrain: section terms replaced with the six-section spread;
  structural terms `class`, `registry`, `registry-card`, `finding-aid` introduced with the
  registry pattern; facets `media`, `character`, `deprecated`, `official-docs` added for the
  staged exemplars.
- 2026-07-18 — Ontology seeded by the library-template quickstart.
