---
status: canonical
tags: [archives, preservation]
---

# archives — superseded, not deleted

**This is the archives README: what moves here, why, and how it's kept.**

Material that is superseded, purely historical, or no longer actively referenced moves here
rather than being deleted. This preserves provenance — the record of what you once believed and
why — while keeping the active shelves in `domains/` clean.

## What goes here
- A unit whose `status` has become `superseded` (replaced by a newer canonical unit).
- A finished project you want out of the active `projects/` view but not gone.
- Old versions of the classification scheme, once reworked.

## The rules
- **Set `status: superseded`** in the unit's frontmatter and **add a forward link** to whatever
  replaced it, so a reader who lands here is sent onward.
- **Deletion is not archiving.** Deleting destroys provenance; archiving keeps the audit trail.
  Git history is the finer-grained backstop beneath this.
- **Promote first.** Before archiving a project, promote its reusable findings to `domains/`
  (`ORPHAN-KNOWLEDGE` is the failure mode). Archive the husk, keep the yield.
- **Log the move** in [`../meta/structure-log.md`](../meta/structure-log.md).

## History
- (date) — Zone created from the quickstart. Empty.
