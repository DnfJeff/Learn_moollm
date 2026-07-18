---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Staged during DnfBrain initialization from the library-template section prototype"
related: [../arts, ../science, ../practices]
tags: [section]
---

# tech — section ledger & placement guide

You are the sub-librarian for this shelf. Two jobs: **place** new work, and keep the **ledger**.

## Where new work goes (placement rules)

The spine is **platform → domain → subject → concern**. Walk it; each level's README is the
finding aid for the next hop.

| If the material is… | Path | Example |
|---|---|---|
| A game's technical side | `pc/gaming/<genre>/<franchise>/<title>/technical/` | `pc/gaming/simulation/the-sims/the-sims-1/technical/dev/tools/` |
| PC hardware or platform | `pc/hardware/` | a build's rationale, a component class |
| A programming language | `programming/languages/<lang>/` | idioms, gotchas, official-doc pointers |
| Dev tooling (editors, build, CLI) | `programming/tools/` | behavior and config worth keeping |
| Running models locally | `ai/local-models/` | runtime comparisons, quantization, serving |
| Agent harnesses and patterns | `ai/agents/` | tool-use discipline, context management |
| Web platform | `web/` | subdivide on first unit |

**Not this section?**
- A game or film as a *work* — its story, reception, characters →
  [`../arts`](../arts/README.md) (cross-link both ways: one subject, two shelves, two concerns)
- Theory of computation, math → [`../science`](../science/README.md)
- A repeatable method not tied to one system → [`../practices`](../practices/README.md)

## The ledger

Every unit on this shelf, one row. Deep units are listed by full path. Keep it in sync —
`validate.py` checks it.

| Unit | What it holds | Status |
|---|---|---|
| [pc/gaming/.../dev/tools/sim-obliterator-suite-depr](pc/gaming/simulation/the-sims/the-sims-1/technical/dev/tools/sim-obliterator-suite-depr/README.md) | exemplar: a deprecated Sims 1 tool suite, fully carded at depth | draft |

## Adding a unit

1. Walk the spine to the right shelf; copy [`../../_templates/unit/`](../../_templates/README.md)
   there (missing intermediate levels get a finding-aid README each — repair, then descend).
2. Fill `SKILL.md` + frontmatter; write `CARD.yml` advertisements so it's routable.
3. Add a row above; reconcile facets via [`../../meta/ontology.md`](../../meta/ontology.md) →
   [`../../meta/by-tag.md`](../../meta/by-tag.md).
4. Run `python validate.py`.
