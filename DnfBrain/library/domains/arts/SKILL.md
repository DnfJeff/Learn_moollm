---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Staged during DnfBrain initialization from the library-template section prototype"
related: [../tech, ../humanities]
tags: [section]
---

# arts — section ledger & placement guide

You are the sub-librarian for this shelf. Two jobs: **place** new work, and keep the **ledger**.

## Where new work goes (placement rules)

The spine is **medium → form → era → genre → the work**. Walk it; each level's README is the
finding aid for the next hop.

| If the material is… | Path | Example |
|---|---|---|
| A TV show or anything inside one | `film/tv/<decade>/<genre>/<show>/` | `film/tv/1950s/sitcom/the-danny-thomas-show/` |
| A feature film | `film/cinema/` | its decade folder, created on first landing |
| Music: a work, artist, or genre | `music/` | subdivide on first unit |
| A written work or author | `literature/` | subdivide on first unit |
| Visual art, photography, design | `visual-arts/` | subdivide by medium |

**Inside a work's unit:** heavy per-work material gets interior folders — `characters/`,
`reviews/`, `episodes/` — inside the work's directory. A character with a full write-up there
**also** gets a quick card in the [characters registry](../../characters/README.md), routed
back to the write-up (dual positioning; the write-up stays the single source of truth).

**Not this section?**
- How a game/system works inside → [`../tech`](../tech/README.md) (a game is art *and* tech:
  the work and its culture here, its internals there — cross-link both ways)
- A creator as a historical figure beyond their works → [`../humanities`](../humanities/README.md)

## The ledger

Every unit on this shelf, one row. Deep units are listed by full path. Keep it in sync —
`validate.py` checks it.

| Unit | What it holds | Status |
|---|---|---|
| [film/tv/1950s/sitcom/the-danny-thomas-show](film/tv/1950s/sitcom/the-danny-thomas-show/README.md) | the show (1953–1964): the work, its characters, reviews | draft |

## Adding a unit

1. Walk the spine to the right shelf; copy [`../../_templates/unit/`](../../_templates/README.md)
   there (missing intermediate levels get a finding-aid README each — repair, then descend).
2. Fill `SKILL.md` + frontmatter; write `CARD.yml` advertisements so it's routable.
3. Add a row above; reconcile facets via [`../../meta/ontology.md`](../../meta/ontology.md) →
   [`../../meta/by-tag.md`](../../meta/by-tag.md). Characters also get a registry card.
4. Run `python validate.py`.
