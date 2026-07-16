# Retrofit — applying this to a project you already have

> **Tier:** Practitioner · deeper: [spec/MECHANISMS.md#conformance-levels](../spec/MECHANISMS.md#conformance-levels) · plainer: [onramp/WHAT-IT-MEANS-FOR-A-TEAM.md](../onramp/WHAT-IT-MEANS-FOR-A-TEAM.md)

The scaffold assumes a clean slate. Real life is an existing repo, existing habits, maybe an
existing `CLAUDE.md` with three months of accumulated notes. This guide adopts the pattern
**incrementally, in value order, with a stopping point after every level.** Partial adoption
is not a compromise — for most projects it's the correct end state.

The levels below are the spec's conformance levels, turned into afternoons.

## Level 1 — Legible state *(one afternoon; do this one regardless)*

**Mechanisms:** externalized state (M4) + tolerant interpretation (M10).

1. Create `.agent/` with the four files from the [template](../../template/.agent/):
   `working-set.yml`, `hot.yml`, `session-log.md`, `output.md`. Gitignore it.
2. Add the state table + the "update at task boundaries" rule + the repair-stub block to
   your existing boot file (`CLAUDE.md` / `.cursorrules`). Don't rewrite what's there; append.
3. Fill `working-set.yml` with your actual current task, by hand, once.

**You get:** sessions that resume ("where were we?" answered from files), an editable
attention record, an audit trail. **Stop here happily if:** you're solo and the pain was
session amnesia — this level fixes it and nothing below is required.

## Level 2 — Constraints and the free channel *(one hour, highest value-per-hour of anything in this kit)*

**Mechanisms:** standing constraints (M5) + boot compilation (M6).

1. Mine your chat history for corrections you've issued twice. Each becomes a named
   constraint: **NAME · rule · test** ([guide 5](guides/05-standing-constraints.md)).
2. Take the template's six generic constraints verbatim; add your project ones.
3. Apply the free-channel rule to your existing boot file: inline what every session needs,
   convert everything else to pointers, evict what nothing uses. Most legacy `CLAUDE.md`
   files shrink and improve simultaneously.
4. Adopt `validate.py` now even if you have no library yet — it checks the boot file.

**Stop here happily if:** you have fewer than ~10 reusable procedures. Most personal
projects should stop here.

## Level 3 — The library *(days, spread out; only past ~10 capabilities)*

**Mechanisms:** resolution ladder (M1) + directory-as-object (M8) + names (M9).

1. Inventory what you actually re-explain to the agent: prompts you re-paste, procedures
   in your head, snippets in a notes app. Each is a capability candidate.
2. `capabilities/` + `INDEX.yml` + one directory per unit, built CARD-first
   ([SCAFFOLD.md §4](SCAFFOLD.md) has the order). **Migrate the three most-used first**;
   the long tail can stay unmigrated forever.
3. Start `GLOSSARY.yml` the first time you catch two names for one thing
   ([guide 9](guides/09-names-as-addresses.md)).
4. Add the reading rule to the boot file. `validate.py` in CI becomes non-negotiable here —
   this is the level where drift starts.

## Level 4 — Routing and portability *(hours, when the specific pain arrives)*

**Mechanisms:** declarative routing (M2) + host drivers (M3).

- Add `triggers:` to CARDs when choosing from the index gets hard — that pain, not the
  calendar, is the signal ([guide 2](guides/02-declarative-routing.md)).
- Split `policy/core.md` from a driver file the day a **second host actually exists** —
  not the day you imagine one ([guide 3](guides/03-host-drivers.md)).

## Level 5 — Ensembles *(per-decision, not an installation)*

Use in-context panels for judgment-under-trade-offs decisions; pay for separate calls when
you need genuinely independent verification ([guide 7](guides/07-in-context-ensemble.md)
has the bright line). There's nothing to install — this level is a habit.

## Retrofitting *around* an existing mess

- **A bloated `CLAUDE.md`:** don't rewrite it in one heroic pass. Levels 1–2 are additive;
  the free-channel eviction in level 2 shrinks it organically.
- **An existing prompt library** (snippets folder, Notion page): that's a pre-ladder
  library. Level 3 is its migration path; the index can point at unmigrated snippets in
  the meantime — a one-line entry with `tagline` + path beats leaving them invisible.
- **Existing automation** (hooks, CI, scripts): already conformant — that's P2. The
  retrofit just documents them as capabilities so the agent knows they exist.

## The one thing not to do

Don't install Level 3–4 machinery on day one because it looks like the "real" version.
The origin system needs a ladder because it has 141 capabilities; the study's template
warns you off it below ten, and it's right. **Every level you skip is a level you can add
the week it starts hurting** — that property is the point of the ordering.
