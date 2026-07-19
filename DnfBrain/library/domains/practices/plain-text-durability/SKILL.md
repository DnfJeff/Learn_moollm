---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Written as the demo unit for the library-template quickstart; a worked example of the card stack, not imported source material."
related: [../../../INDEX.md, ../README.md]
tags: [reference]
---

# Why versioned plain text outlives app-specific formats

A knowledge library is a bet measured in decades. The single decision that most determines
whether the bet pays off is the storage format — because tools change far faster than knowledge
does, and a format you can only open with one tool dies when that tool does.

## The argument

1. **Plain text survives tool churn.** Markdown and YAML are readable in any editor, on any OS,
   with no runtime. The app that renders them prettily is replaceable; the files don't care.
2. **Plain text is diffable and versionable.** Git gives you history, provenance, and blame on
   every line. A binary blob or an app database gives you, at best, opaque snapshots.
3. **Plain text is greppable.** Retrieval never depends on one app's index being intact. `grep`
   and any future tool can read the whole collection.
4. **Structure lives in convention, not lock-in.** The card stack (GLANCE/CARD/SKILL/README) and
   YAML frontmatter give machines structure to route on, while staying human-readable. You get
   database-like addressing without a database's captivity.

## The cost, stated honestly

Plain text does less *on its own*. No live backlinks, no graph, no queries — until you add a tool
that provides them. The discipline is directional: **tools go on top, never underneath.** Obsidian
reads these files and adds a graph; it does not become the format. If Obsidian vanished tomorrow,
the library would be untouched. If the library lived *inside* Obsidian's database, it wouldn't.

## Consequence for this library

- Canonical storage: Markdown + YAML, in git. Always.
- App features (Obsidian graph/backlinks, editor plugins) are conveniences layered on, declared
  as a host driver ([`policy/drivers/obsidian.yml`](../../../../policy/drivers/obsidian.yml)),
  each with a plain-text fallback.
- Anything an app generates that you want to keep (a useful index, a map) gets a static,
  plain-text mirror in `meta/`, so it survives the app.
