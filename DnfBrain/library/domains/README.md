---
status: canonical
tags: [domains, overview]
---

# domains — permanent knowledge

**This is the domains README: the reusable, long-lived side of the library, and the place where
changes to the section scheme are noted.**

`domains/` holds knowledge that outlives any single project — **prototypes**, in the library's
terms. It is organized as a classified tree: six **sections** (top-level classes), each a card
stack with a **librarian** (`SKILL.md`) that knows what belongs on its shelf, and below them
staged **class shelves** whose finding-aid READMEs map each level. The principle throughout:
**the path carries the classification** — every future note already has a route to a unique
address, and the address carries the backstory.

The counterpart is [`../projects`](../projects/README.md), which holds time-bound **instances**.
When a project yields something reusable, it graduates here (promotion).

## The sections

| Section | Holds | The test |
|---|---|---|
| [arts](arts/README.md) | creative works and their makers | *about a work or its world?* |
| [tech](tech/README.md) | computing, down to internals | *about how a computing thing works?* |
| [science](science/README.md) | the natural and formal worlds | *true regardless of any one system?* |
| [humanities](humanities/README.md) | human affairs: history, philosophy, language | *about what people did or thought?* |
| [life](life/README.md) | practical living, for future-you | *needed to run a life again?* |
| [practices](practices/README.md) | repeatable ways of working | *a reusable way of doing something?* |

Figures looked up by name resolve through the [characters registry](../characters/README.md)
regardless of which section holds their write-up.

## Adding a section

Copy [`../_templates/section/`](../_templates/README.md) to `domains/<name>/`, fill its
placement rules and ledger, add it to [`../INDEX.md`](../INDEX.md) and
[`../meta/by-domain.md`](../meta/by-domain.md), and log it in
[`../meta/structure-log.md`](../meta/structure-log.md). A new shelf hangs its own sign; the
central catalog just gains one line. Intermediate class shelves are cheaper: a finding-aid
README each, staged ahead of need or created on first landing (repair-not-fatal).

## Section history
- 2026-07-18 — Six-section spread staged in the DnfBrain initialization, replacing the
  template's three neutral placeholders; two exemplar paths built to full depth. See
  [`../meta/structure-log.md`](../meta/structure-log.md) for the reasons.
