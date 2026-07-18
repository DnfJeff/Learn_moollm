---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Shipped with the library-template quickstart"
related: [../../library/INDEX.md]
tags: [capability, library-ops]
---

# curator — how filing actually works

Read this to change the filing procedure. To *run* it, `CARD.yml` is enough.

The premise: **you don't need to know where everything goes.** The library is organized so that
each level knows the next hop. A patron asks the front desk, the front desk names a section, the
section's librarian knows the exact shelf. You just walk the chain.

## LOCATE — where does this belong?

1. **Ask the chief librarian.** Read `library/INDEX.md`. Match the material to a *section* by
   what it is: about how a specific thing works → `technical`; durable subject understanding →
   `knowledge`; a repeatable way of working → `practices`. (Your real sections after you rename.)
2. **Ask the section librarian.** Read that section's `CARD.yml` — do the advertisements confirm
   it belongs here? Then read its `SKILL.md` — the **placement rules** table says *which
   subclass*, and the **ledger** shows what's already there (avoid duplicating; prefer extending).
3. **Decide the target:**
   - Fits an existing unit → extend that unit.
   - New concept, clear home → `new unit` at that path.
   - Doesn't fit any subclass → file at the section root and note the gap (a candidate new
     subclass) in `meta/structure-log.md`.
   - **Genuinely unsure → `inbox/`.** Uncertainty is not a reason to guess into `domains/`
     (`CLASSIFY-LAST`).

## CAPTURE — get it in the door

Drop it in `library/inbox/` as a single file with a breadcrumb: what it is, where it came from,
the date. No classification, no card stack, no ceremony. The point is that capture never stalls.

## TRIAGE — empty the inbox on a rhythm

For each `inbox/` item:

1. **Atomize** — split a mixed dump into one-concept pieces (`ATOMIC-OR-STAGED`).
2. **LOCATE** each piece (above).
3. **Create the unit** — copy `library/_templates/unit/` to the target path (or the single-file
   `note.md` for the cheap rung). Fill `SKILL.md` and its frontmatter, including `provenance`
   from the breadcrumb (`PROVENANCE-OR-IT-DIDNT-HAPPEN`). Write `CARD.yml` advertisements so the
   unit is routable.
4. **Register** — add a row to the section's ledger (`SKILL.md`), and if it introduces a facet,
   add it to `meta/ontology.md` first, then `meta/by-tag.md` (`LEDGER-SYNC`).
5. **Remove** the item from `inbox/`.
6. **Validate** — `python validate.py`. Fix drift before moving on.

## PROMOTE — projects feed domains

When a project (`projects/<name>/`) turns up something reusable beyond that project, create a
domain unit for it (LOCATE + create), and link the project artifact to it. The instance
graduates its reusable state into the prototype. Do this *before* archiving the project, or the
knowledge dies with it.

## ARCHIVE — retire, don't delete

A superseded unit: set its frontmatter `status: superseded`, add a forward link to its
replacement, and move it to `library/archives/`. Deletion destroys provenance; archiving keeps
the audit trail and clears the active shelf. Log the move in `meta/structure-log.md`.

## Failure modes (named, so they're checkable)

- **`HEAP`** — capturing without ever triaging. The inbox is a queue, not a landfill. Triage on
  a rhythm or it becomes the thing the library was supposed to prevent.
- **`GUESS-FILING`** — dropping an uncertain item into a domain to feel finished. Gate: are you
  sure? No → inbox.
- **`GHOST-UNIT`** — a unit created but never registered in the ledger. Invisible to the next
  reader. Gate: does `validate.py` pass?
- **`TAG-SPRAWL`** — coining a tag at filing time. Gate: is it in `meta/ontology.md`? If not, add
  it there deliberately first, or reuse an existing one.
- **`ORPHAN-KNOWLEDGE`** — archiving a project without promoting its reusable findings. Gate: did
  anything here deserve a domain unit?
