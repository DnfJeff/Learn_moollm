---
status: canonical
tags: [catalog, front-desk]
---

# The Directory — chief librarian

The master catalog for the whole collection. This is the front desk: it tells you **which
section** holds what you need, so you never search the whole library to file or find one thing.

## Reading protocol

Read the cheapest level that answers your question; never open a deeper level without the one
above it.

```
this directory        which section?        → pick a section below
  domains/<s>/GLANCE   is this the shelf?    → descend, or try another section
    CARD.yml           routing + interface   → file here / route on
      SKILL.md         the ledger / the note → read the knowledge, or place the unit
        README.md      history + why
```

Bold terms below are section paths, spelled exactly. Reading order is also dependency order.

## The sections (permanent knowledge — `domains/`)

Each section is a **librarian**: a card stack whose `SKILL.md` holds the ledger of everything on
its shelf and the rules for what belongs there. Route by *what the material is*:

**[domains/technical](domains/technical/README.md)** holds knowledge about **how a specific
thing works** — a system's architecture, a file format's layout, a tool or protocol's behavior.
Reverse-engineering findings and specs live here. The test: *is this about one concrete thing?*

**[domains/knowledge](domains/knowledge/README.md)** holds **durable understanding of a subject**
that isn't tied to any one system — concepts, theory, research notes, mental models, facts you
want kept. The test: *is this true across many systems, about a field rather than a thing?*

**[domains/practices](domains/practices/README.md)** holds **repeatable ways of working** —
methods, patterns, checklists, standards, workflows you re-apply. The test: *is this a way of
doing something, reusable next time?*

When something could fit two sections, prefer the one you'd look in *first* next year, and cross-
link from the other. When it fits none cleanly, put it in **[inbox](inbox/README.md)** and let
triage decide.

## Work in progress (`projects/`)

**[projects](projects/README.md)** holds time-bound initiatives — instances, mirroring the
workflow stages. Projects draw on the sections and, when they yield something reusable, feed a
new unit back into a section (promotion). A finished project is archived; its reusable knowledge
is promoted first.

## Intake and retirement

- **[inbox](inbox/README.md)** — drop anything unsorted here. Classification is a later triage
  step, never a gate at the door.
- **[archives](archives/README.md)** — superseded material, kept for provenance, linked forward
  to whatever replaced it.

## Keeping the catalog honest

- **[meta/ontology.md](meta/ontology.md)** — the controlled vocabulary. Every tag and k-line
  comes from here.
- **[meta/by-domain.md](meta/by-domain.md)** · **[meta/by-tag.md](meta/by-tag.md)** — alternate
  ladders into the same units (finding aids, not copies).
- **[meta/structure-log.md](meta/structure-log.md)** — every structural change, with its reason.
  Append-only.
- Access paths by project and by workflow stage (`meta/by-project.md`, `meta/by-stage.md`) come
  online once you have projects; add them then.

Run `python validate.py` after any change — it checks that ledgers, counts, and links stay in
sync, which is the one thing the model won't reliably do on its own.
