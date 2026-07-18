---
status: canonical
tags: [domains, overview]
---

# domains — permanent knowledge

**This is the domains README: the reusable, long-lived side of the library, and the place where
changes to the section scheme are noted.**

`domains/` holds knowledge that outlives any single project — **prototypes**, in the library's
terms. It is organized into **sections** (classification classes). Each section is a card stack
with a **librarian** (`SKILL.md`) that knows what belongs on its shelf and keeps a ledger of
what's there.

The counterpart is [`../projects`](../projects/README.md), which holds time-bound **instances**.
When a project yields something reusable, it graduates here (promotion).

## The sections

| Section | Holds | The test |
|---|---|---|
| [technical](technical/README.md) | how a specific system, tool, format, or protocol works | *about one concrete thing?* |
| [knowledge](knowledge/README.md) | durable subject understanding, not tied to one system | *true across a field, not a thing?* |
| [practices](practices/README.md) | repeatable ways of working: methods, patterns, checklists | *a reusable way of doing something?* |

These three are **neutral placeholders**. Rename them to your real domains — keep each
librarian card stack, replace the labels and the placement rules in its `SKILL.md`, and log the
change in [`../meta/structure-log.md`](../meta/structure-log.md).

## Adding a section

Copy [`../_templates/section/`](../_templates/README.md) to `domains/<name>/`, fill its
placement rules and ledger, add it to [`../INDEX.md`](../INDEX.md) and
[`../meta/by-domain.md`](../meta/by-domain.md), and log it. A new shelf hangs its own sign; the
central catalog just gains one line.

## Section history
- (date) — Three starter sections created from the quickstart. Rename to taste.
