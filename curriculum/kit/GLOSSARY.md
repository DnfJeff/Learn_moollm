# Glossary

> **Tier:** Practitioner · deeper: [spec/PROVENANCE.md](../spec/PROVENANCE.md) · plainer: [onramp/PLAIN-GLOSSARY.md](../onramp/PLAIN-GLOSSARY.md)

Canonical term → what it means → the MOOLLM original (for reading the origin repo). Seeded
from [shared/CANON.md](../shared/CANON.md), which is authoritative when this table and any
other document disagree.

Use it in two directions: **left column when writing your own workspace; right column when
reading MOOLLM.** If you catch yourself explaining a right-column term to a teammate,
you've re-imported the codebook this kit exists to remove.

## The mechanisms

| Canonical | One line | MOOLLM |
|---|---|---|
| Resolution ladder (M1) | Multi-size writing; read cheapest tier first; never skip up | Semantic Image Pyramid, MOO-Maps |
| Declarative routing (M2) | Capabilities announce their own relevance; no central router | Advertisements |
| Host drivers (M3) | One policy, per-host adapters with declared fallbacks | Drivers |
| Externalized state (M4) | Memory and attention as small editable files | Files-as-State, hot/cold |
| Standing constraints (M5) | Always-on named rules in the boot file | Ambient skills, `no-ai-*` |
| Boot compilation (M6) | Compile the always-needed subset into the auto-loaded file; recompile on a loop | cursor-mirror OPTIMIZE, bootstrap |
| In-context ensemble (M7) | Many perspectives, one call; separate calls only when independence is the product | Speed of Light (vs. Carrier Pigeon) |
| Directory-as-object (M8) | Identity = path; interface = marker file; discovery = `ls` | Selfish COM, prototypes |
| Names as addresses (M9) | Prepaid names over invented jargon; coin once, in a file | K-lines |
| Tolerant interpretation (M10) | Liberal in, conservative out, repair don't crash — and validate what you authored | POSTEL, robust-first, self-healing |

## The principles

| Canonical | One line | MOOLLM |
|---|---|---|
| Dual-mode contract (P1) | Control files work as enforced commands *or* as conventions the model self-applies; advisory is the designed floor | Smart vs. generic orchestrator, advisory mode |
| Determinism split (P2) | Mechanical → scripts; judgment → the model | Sister scripts; "deterministic vs non-deterministic components" |
| Rewrite, not truncate (P3) | Each tier is an editorial judgment, never an excerpt of the tier below | (implicit in MOO-Map practice) |

## The artifacts

| Canonical | What it is | MOOLLM |
|---|---|---|
| Boot file / free channel | The auto-loaded file (`CLAUDE.md`, `.cursorrules`); content there is prepaid | `.cursorrules` |
| Capability unit | One directory = one capability | Skill |
| Catalog / index | One line per unit; the entry point | `skills/INDEX.md` / `INDEX.yml` |
| Glance / card / skill / readme | The four tier files | `GLANCE.yml` / `CARD.yml` / `SKILL.md` / `README.md` |
| Trigger | A scored, conditioned activation offer in a CARD | Advertisement |
| Standing constraint | A trigger with `when: always` + a resident `resolution` | AMBIENT advertisement |
| Session zone | `.agent/` — the state files | `.moollm/` |
| Working set | Current-focus file; the agent's editable attention | `working-set.yml` (same) |
| Hot / cold | Keep-loaded and evicted-with-breadcrumbs lists | same |
| Session log / output | Append-only decisions / append-only results | same |
| Driver | Per-host adapter YAML | same |
| Instance library | Pre-made instances shipped inside a factory capability | e.g. `buffs/`, `characters/` |
| Promotion pattern | Log-embedded data graduates to its own file when it needs editing | data islands → `.yml` |
| Validator | The script that checks what you authored (`validate.py`) | (no equivalent — the gap this kit fills) |
| Named failure mode | A constraint's checkable handle (`VERBOSITY`, `CLAIM-LEDGER`) | Cardinal sins |

## MOOLLM terms you'll meet and can safely translate away

Room → directory/module · Exit → reference/dependency · Character → role/persona ·
Adventure → project/session · Incarnation → instantiation · Inventory → held state ·
Buff → temporary modifier · Needs → priority weights · Microworld → workspace ·
Kernel → policy layer · Coherence Engine → the model · YAML Jazz → commented, literate
config (the real content: *comments are semantic — the model reads them*).

## Lineage names — keep these, they're prepaid

Postel's law (RFC 761) · Minsky's Society of Mind and K-lines · Self (Ungar & Smith,
prototypes) · The Sims advertisements (Wright) · robust-first (Ackley) · Densmore–Rosenthal
US5187786A (directories as objects, 1991). Name-drop for the model; add one sentence of
gloss for the human — both readers, one line.
