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
this directory          which section?         → pick a section below
  domains/<s>/GLANCE     is this the shelf?     → descend, or try another section
    <class>/README       finding aid            → descend the tree; the path IS the classification
      CARD.yml           routing + interface    → file here / route on
        SKILL.md         the ledger / the note  → read the knowledge, or place the unit
          README.md      history + why
```

**Looking something up by NAME** (a person, later maybe a language or tool)? Skip the tree:
the registries hold quick cards that route to the full write-ups — start at
**[characters/MANIFEST.yaml](characters/MANIFEST.yaml)**.

Bold terms below are section paths, spelled exactly. Reading order is also dependency order.

## The sections (permanent knowledge — `domains/`)

Each section is a **librarian**: a card stack whose `SKILL.md` holds the ledger of everything on
its shelf and the rules for what belongs there. Below the section, the spine continues as
staged class shelves — the path itself carries the classification, so
`arts/film/tv/1950s/sitcom/the-danny-thomas-show/` reads as medium → era → genre → work before
a single file opens. Route by *what the material is*:

**[domains/arts](domains/arts/README.md)** holds **creative works and their makers** — film,
tv (by decade → genre → show), music, literature, visual art — including reviews, characters,
and everything a heavy work grows inside its own directory. The test: *is this about a work or
its world?*

**[domains/tech](domains/tech/README.md)** holds **computing knowledge down to the internals**
— the pc platform and its games (genre → franchise → title → concern), programming languages
and tools, running AI models locally and driving agents, the web. The test: *is this about how
a computing thing works?* (A game is both: its culture files in **domains/arts**, its
internals here — cross-linked.)

**[domains/science](domains/science/README.md)** holds **durable understanding of the natural
and formal worlds** — mathematics, physical sciences, life sciences. The test: *is this true
about the world, regardless of any one system?*

**[domains/humanities](domains/humanities/README.md)** holds **human affairs** — history,
philosophy, language. The test: *is this about what people did, thought, or said?* (A figure
known through a creative work files with the work in **domains/arts**; the characters registry
resolves the name either way.)

**[domains/life](domains/life/README.md)** holds **practical living** — health, finance, home,
food — written for future-you. The test: *will I need this to run my life again?*

**[domains/practices](domains/practices/README.md)** holds **repeatable ways of working** —
methods, patterns, checklists, including the library's own conventions. The test: *is this a
way of doing something, reusable next time?*

When something could fit two sections, prefer the one you'd look in *first* next year, and
cross-link from the other. When it fits none cleanly, put it in **[inbox](inbox/README.md)**
and let triage decide.

## The registries (by-name lookup — beside the tree)

**[characters](characters/README.md)** holds one quick card per character or figure, routing
to every full write-up that figure has earned inside its work(s) — the by-name door the
classified tree can't provide. Scan **[characters/MANIFEST.yaml](characters/MANIFEST.yaml)**
first. The pattern is standardized in **[_templates/registry](_templates/registry/README.md)**;
new registries (languages, tools) are surfaced deliberately via the `registrar` capability
when they earn it.

## Work in progress (`projects/`)

**[projects](projects/README.md)** holds time-bound initiatives — instances, mirroring the
workflow stages. Open one with the `project-intake` capability the moment a project is
announced; it wires `references/` into the sections the project draws on, so promotion at the
end is a walk down a list. A finished project is archived; its reusable knowledge is promoted
first.

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
  online with the first project — `project-intake` creates them.

Run `python validate.py` after any change — it checks that ledgers, counts, and links stay in
sync, which is the one thing the model won't reliably do on its own.
