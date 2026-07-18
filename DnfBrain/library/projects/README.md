---
status: canonical
tags: [projects, overview]
---

# projects — time-bound work

**This is the projects README: the instance side of the library, where active initiatives live
and where changes to project structure are noted.**

`projects/` holds **instances** — time-bound work with a start and an end — as against
[`../domains`](../domains/README.md), which holds permanent **prototypes** (reusable knowledge).
The distinction is the library's version of prototype-vs-instance: behavior and durable knowledge
live in domains; a project carries its own state and is instantiated from a template.

## Each project mirrors the workflow stages

Copy [`../_templates/project/`](../_templates/README.md) to `projects/<name>/`. A project has:

```
projects/<name>/
├── research/         raw inputs, sources, open questions
├── content-maps/     what exists / what's needed, mapped
├── roadmaps/         scope, sequence, dependencies
├── job-cards/        discrete units of work
├── execution-logs/   append-only record of what happened
├── specs/            the concrete deliverable definitions
└── references/       links into the domains this project draws on
```

## The rule that makes projects worth it: promotion

When a project turns up something reusable beyond itself — a finding, a spec, a pattern —
**promote it into a domain unit** (the `curator` capability's PROMOTE). Do this *before* the
project is archived, or the reusable knowledge dies with the instance. Projects are how domains
grow.

## Finishing a project
Promote its reusable yield to domains, then archive the project (or leave it in place, marked
done). Log significant structure changes in [`../meta/structure-log.md`](../meta/structure-log.md).

## History
- (date) — Zone created from the quickstart. No projects yet; instantiate from `_templates/project/`.
