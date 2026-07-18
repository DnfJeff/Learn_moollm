# Core policy — portable, host-independent

The rules that govern the library regardless of where it runs. `AGENT.md` inlines the always-on
subset into the free channel; this file is the fuller reference. Host-specific mappings live in
`drivers/`; this file names abstract operations only.

## The two zones

- **`library/`** — permanent, versioned collection. The source of truth. Git-tracked.
- **`.agent/`** — disposable session state (focus, log, output). Not the library.

A finding born in the session log is **promoted** into a library unit; it is never left to live
only in session state.

## The card stack (every shelf and every note)

One unit = one directory, written at four sizes:

| Tier | Question it answers | Who reads it |
|---|---|---|
| `GLANCE.yml` | Is this relevant? | agent, scanning many |
| `CARD.yml` | Where does it route / how do I use it? | agent, deciding |
| `SKILL.md` | The knowledge itself (or, for a section, the ledger) | agent + human |
| `README.md` | History and why | human, browsing |

Each tier is **rewritten** for its depth, never truncated from the one below. A note that hasn't
earned a full stack may be a single frontmattered `<name>.md` — the cheap rung — and graduates
to a directory when it becomes reference-grade or routable.

## Classification

- `domains/` holds **permanent, reusable** knowledge (prototypes), organized as classified
  **sections**. Each section is a card stack whose `SKILL.md` is its ledger + placement rules.
- `projects/` holds **time-bound** work (instances), each mirroring the workflow stages.
- When material could fit both, default to `domains/` for longevity.
- Classification is the primary spine; facet **tags** (from `meta/ontology.md`) are the secondary
  access path. One home, many doors.

## Intake

`inbox/` accepts anything with no required classification (**CLASSIFY-LAST**). Triage on a rhythm:
atomize → classify → link → register in the ledger → reconcile tags → remove from inbox.

## Provenance & preservation

Every unit's `SKILL.md` opens with `status` (draft | canonical | superseded), `created`,
`reviewed`, `provenance`, `related`. Superseded material moves to `archives/` (not deleted) and
links forward to its replacement. Structural changes are logged in `meta/structure-log.md`
(append-only).

## Determinism split

Anything that must be *correct* rather than *plausible* — ledger/index counts, dangling links,
required frontmatter — is checked by `validate.py`, not by the model reading YAML. Advertisements
and placement are soft routing; verification is a script's job.
