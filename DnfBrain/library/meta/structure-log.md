---
status: canonical
tags: [meta, changelog]
---

# Structure log — how the library's shape has changed

**This is the append-only record of every structural change to the library: new sections,
renamed facets, classification revisions — each with its reason.** History is never rewritten;
corrections are new entries. This is the library's own provenance, and the first place to look
to understand *why* it's shaped the way it is.

## Entries (newest first)

- **2026-07-18 — Characters registry surfaced; registry pattern standardized.**
  First instance of a surfaced by-name layer: `library/characters/` (librarian stack +
  `MANIFEST.yaml` + one card per figure), seeded with `danny-thomas` routing to the write-up
  inside its show. The pattern generalized into `_templates/registry/` with three earn-it
  criteria (by-name access, scattered instances, card-answers-most) — languages and tools are
  named candidates, deliberately not surfaced yet. New capabilities: `registrar` (registry
  sync), `project-intake` (the new-project flow). *Reason: people are looked up by name, not
  by walking medium → era → genre → show; one card routes to N write-ups without duplicating
  content.*

- **2026-07-18 — Full domain spread staged; naming convention fixed.**
  The template's three neutral sections (`technical`, `knowledge`, `practices`) replaced by a
  six-section spread: `arts`, `tech`, `science`, `humanities`, `life`, `practices` — each a
  librarian card stack — with 34 intermediate class shelves staged as finding-aid READMEs.
  Two exemplar paths built to full depth:
  `arts/film/tv/1950s/sitcom/the-danny-thomas-show/` (with `characters/` + `reviews/`
  interior) and
  `tech/pc/gaming/simulation/the-sims/the-sims-1/technical/dev/tools/sim-obliterator-suite-depr/`.
  The `plain-text-durability` demo unit reshelved from `technical/` to `practices/`.
  **Naming convention:** all path segments are lowercase-kebab (`the-danny-thomas-show`, not
  `TheDannyThomasShow`); decades are written in full (`1950s`, not `50s`); deprecated tools
  carry `-depr`. *Reason: a library is organized before it is full — the shelves exist so
  everything not yet known already has a route to a unique address, and the address carries
  the backstory.*

- **2026-07-18 — DnfBrain initialized from the library-template quickstart.**
  Full template instantiated as a staging workspace, to be transplanted into its own repo.
  Ontology and finding aids reseeded to match the spread (see entries above).
