# curator — why the librarian chain

**This is the curator capability's backstory: why filing is a chain of librarians rather than one
big classifier, and what changes are noted here.**

## The idea

A real research library scales because no single person holds the whole catalog in their head.
The front desk knows the *sections*. Each section's librarian knows their *shelves* and keeps a
*ledger* of what's on them. A patron with a vague question gets routed: desk → section →
shelf → item. Nobody had to know everything; the structure carried the knowledge.

This capability is that chain, made executable. `library/INDEX.md` is the front desk. Each
section's `CARD.yml`/`SKILL.md` is its librarian. The `curator` walks between them.

## Why a chain beats a flat classifier

- **It scales.** Adding a section adds a librarian; it doesn't grow a central rulebook everyone
  must edit (declarative routing — a new shelf hangs its own sign).
- **It degrades gracefully.** If a section's placement rules are thin, filing still works at the
  section root, and the gap gets logged as a candidate subclass — the scheme grows from real use.
- **It's legible.** Every routing decision traces to a card a human can open and correct.

## Why filing enforces provenance and atomicity *now*

Cleanup-later never comes. A unit filed without its source, or a five-topic dump filed as one
note, is debt that compounds as the collection grows. The cheapest moment to get it right is at
filing time, which is why `CANONICAL-COLLECTION`, `PROVENANCE-OR-IT-DIDNT-HAPPEN`, and
`ATOMIC-OR-STAGED` are checked here and not deferred.

## Changes
- (date) — Capability shipped with the library-template quickstart.
