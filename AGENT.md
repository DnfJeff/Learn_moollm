# Agent Policy — working ON this repository

This file is for anyone — human or model — editing Learn_moollm itself. (If you're here to
*learn*, you want [INDEX.md](INDEX.md) instead.) Auto-load it: copy to `CLAUDE.md` or
`.cursorrules` when working in this repo.

## Standing constraints

**`CANON-WINS`** — [curriculum/shared/CANON.md](curriculum/shared/CANON.md) owns every
mechanism name, definition, and analogy. A rename happens there first, then propagates.
Test: grep the term you're about to change; if CANON has it, edit CANON first.

**`TIER-VOICE`** — Each shelf keeps its register. Onramp: zero code, zero filenames, zero
YAML in prose. Kit: recipes ending in a verification step. Spec: MUST/SHOULD, measured or
labeled speculative. Test: could this paragraph move shelves unchanged? Then it's on the
wrong shelf.

**`REWRITE-NOT-TRUNCATE`** — Every summary tier (GLANCE.yml, index entries, tier bars) is
written fresh for its depth, never cut from a longer document. This repo teaches P3; it
must not violate P3.

**`CREDIT-STANDS`** — The provenance sentence (mechanisms originate in MOOLLM by Don
Hopkins) stays in every set's opening document and in README.md. Not negotiable, not
movable to a footnote.

**`CLAIM-LEDGER`** — Numbers are *measured* (traceable to study/evidence/) or *reported*
(origin transcripts) and labeled as such. A new claim without a label doesn't ship.

**`VERBOSITY`** — Replace adjectives with facts. Test: does every sentence carry
information the reader didn't have?

## Reading protocol

[GLANCE.yml](GLANCE.yml) → [INDEX.md](INDEX.md) → the shelf you're editing. Read the
cheapest tier that answers your question; never skip a tier downward.

## State

Session state lives in `.agent/` — working-set (current focus, under 30 lines, updated at
task boundaries), session-log (decisions and why, append-only), output (results,
append-only). If the conversation and the files disagree, the files win.

## Structure invariants

- Cross-tier links use the tier-bar convention in
  [curriculum/shared/CROSS-TIER-NAV.md](curriculum/shared/CROSS-TIER-NAV.md); anchors are
  `#mN--name` from the canonical headings.
- `template/` is copied out by users; it must stay self-contained (no links back into
  curriculum/ or study/) and `python template/validate.py` must exit clean after any edit
  to it.
- `library-template/` is likewise copied out and must stay self-contained (no links back into
  curriculum/, study/, or template/); `python library-template/validate.py` must exit clean
  after any edit. It is the implementation of
  [curriculum/spec/THE-LEGIBLE-LIBRARY.md](curriculum/spec/THE-LEGIBLE-LIBRARY.md) — when the
  layer spec and the template disagree, reconcile them in the same change.
- `study/` is frozen evidence; correct it only when a primary source (MOOLLM itself)
  contradicts it, and log the correction in the session log.
- External pointer for the origin: https://github.com/SimHacker/moollm — cloned locally
  into `moollm/` (gitignored) when re-running `study/evidence/measure.py`.
