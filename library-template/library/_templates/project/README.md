---
status: draft
tags: [project, overview]
---

# <project-name> — project overview

**This is the project README: goal, scope, and status of a time-bound initiative. This is an
instance, not permanent knowledge — when it yields something reusable, promote that into a
domain.**

- **Goal:** <what done looks like>
- **Status:** <not started | in progress | done | archived>
- **Draws on:** <links into the domain sections this project uses — see `references/`>

## Workflow stages
Copy this whole directory to `library/projects/<name>/`. Fill the stages as you go; not every
project needs every stage, but the order is the spine:

| Stage | Folder | Holds |
|---|---|---|
| Research | `research/` | raw inputs, sources, open questions |
| Content mapping | `content-maps/` | what exists / what's needed |
| Roadmapping | `roadmaps/` | scope, sequence, dependencies |
| Job cards | `job-cards/` | discrete units of work ([template](job-cards/_TEMPLATE.md)) |
| Execution | `execution-logs/` | append-only record of what happened |
| Specs | `specs/` | the concrete deliverable definitions |
| References | `references/` | links into the domains this draws on |

## On finishing
**Promote first, then archive.** Move this project's reusable findings into `domains/` (the
`curator` PROMOTE), then mark it done or move it to `archives/`. Log it in
`../../meta/structure-log.md`. A project that's archived without promoting its yield threw the
knowledge away (`ORPHAN-KNOWLEDGE`).

## History
- (date) — Project started from `_templates/project/`.
