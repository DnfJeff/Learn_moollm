---
status: canonical
tags: [section, overview]
---

# technical — section overview

**This is the technical-domain README. What lives here, how it's organized, and notable changes
are noted here.**

Durable, reusable knowledge about **how specific systems, tools, protocols, and formats work** —
the kind of thing you reverse-engineer or look up once and want kept for years.

## Subclasses
- `formats/` — file formats and binary layouts
- `systems/` — architecture of specific systems and services
- `tools/` — tool and protocol behavior kept for reuse

*(Subclass folders are created when their first unit lands — flat-to-structured, never empty
ceremony.)*

## How to use this section
- **Browsing:** read this file, then `SKILL.md` for the full ledger of units.
- **Routing (agent):** `CARD.yml` decides whether new work belongs here.
- **Filing:** copy `../../_templates/unit/`, fill it, register it in the ledger.

## Section history
- (date) — Section created from the quickstart. Empty but for the `plain-text-durability` demo
  unit. Rename the section to your real domain when ready and log it in
  [`../../meta/structure-log.md`](../../meta/structure-log.md).
