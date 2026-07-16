# Glossary

MOOLLM term → general term. The codebook swap from
[analysis/03-metaphor-vs-mechanism.md](../analysis/03-metaphor-vs-mechanism.md), done.

Use this in two directions: to **read MOOLLM** (left → right), and to **write your own
framework** (use the right column, never the left).

## Core architecture

| MOOLLM | General | Notes |
|---|---|---|
| Microworld | Project workspace | The repo the agent operates in |
| Kernel | Policy layer | It's documents, not a kernel. See [analysis/05](../analysis/05-honest-assessment.md). |
| Userland | Capability library | |
| Constitution | Policy / house rules | `constitution-core.md` → `policy/core.md` |
| Driver | Host adapter | Already neutral. Keep the word. |
| Orchestrator | Host / harness | Cursor, Claude Code, your runner |
| Coherence Engine | The model | Just say "the model" |
| Skill | Capability / component | The unit of the library |
| Card (`CARD.yml`) | Interface declaration | Keep `CARD.yml`, or use `INTERFACE.yml` |
| Advertisement | Trigger / activation condition | |
| K-line | Dense name / latent pointer | The *concept* is essential; the *word* is jargon |
| Semantic Image Pyramid | Resolution ladder | |
| Selfish COM | Convention-based discovery | |
| Speed-of-light | In-context ensemble | |
| Ambient skill | Standing constraint / house rule | |
| YAML Jazz | Commented, literate config | "Comments are semantic" is the real content |
| Files-as-state | Externalized state | |
| Working set | Working set | Already neutral |
| Hot / cold | Priority / evicted | Already neutral enough |

## The world layer — drop all of this

| MOOLLM | General | Keep? |
|---|---|---|
| Room | Package / module / directory | ❌ Drop the word, keep containment |
| Exit | Dependency / reference | ❌ |
| Character | Role / persona / reviewer | 🟡 "Reviewer role" is useful |
| Adventure | Project / session | ❌ |
| Incarnation | Instantiation | ❌ |
| Pub, bartender, budtender | — | ❌ Demo content |
| Cat, dog, animal, monkey | — | ❌ Demo content |
| Soul chat | — | ❌ |
| Inventory | Held state | 🟡 General, rename it |
| Buff | Temporary modifier | 🟡 General, rename it |
| Needs | Priority weights | 🟡 General, rename it |
| Pie menu | Ranked options | 🟡 The ranking is the idea |
| Grue, maze, treasury | — | ❌ |

The 🟡 rows are the near-misses: real mechanisms wearing a Sims costume. Rename before porting
or the costume comes with them.

## The `no-ai-*` family — take all of this

The names are already general. Steal them verbatim.

| MOOLLM | Fights | Keep the name? |
|---|---|---|
| `no-ai-slop` | Verbosity, hallucination, certainty theater | ✅ |
| `no-ai-hedging` | Qualifier stacking, weasel certainty | ✅ |
| `no-ai-sycophancy` | Unearned validation, softened disagreement | ✅ |
| `no-ai-moralizing` | Caveat-bombing, refusal theater | ✅ |
| `no-ai-humansplaining` | Re-teaching the model what it knows | ✅ |
| `no-ai-gloss` | Euphemism laundering, false neutrality | ✅ |
| `no-ai-bias`, `-ideology`, `-joking`, `-overlord`, `-soul`, `-customer-service` | assorted | 🟡 Pick what you need |

**The cardinal sins are the real payload** — each is a K-line pointed at a behavior:

`HALLUCINATION` · `VERBOSITY` · `YES-MAN` · `CERTAINTY-THEATER` · `NOT-ASKING` ·
`OVER-ENTHUSIASM` · `BOTH-SIDESISM` · `EPISTEMIC-EVASION` · `UNSOLICITED-COACHING` ·
`QUALIFIER-STACKING` · `WEASEL-CERTAINTY` · `PASSIVE-EVASION` · `FAUX-HUMILITY` ·
`EPISTEMIC-COWARDICE` · `UNEARNED-VALIDATION` · `EMOTIONAL-MIRRORING` · `SOFTENED-DISAGREEMENT` ·
`PREMISE-ACCEPTANCE` · `CHEERLEADING` · `CAVEAT-BOMBING` · `VIRTUE-SIGNALING` ·
`REFUSAL-THEATER` · `PARENTAL-TONE` · `EUPHEMISM-LAUNDERING` · `POWER-PROTECTIVE-NEUTRALITY` ·
`REGISTER-SWITCHING` · `MANUAL-PASTING` · `PREEMPTIVE-TUTORING` · `FILE-DUMPING` · `GUID-NAMING`

And the two hard gates, worth stealing outright:

- **`CLAIM-LEDGER`** — for each user claim: CONFIRM / DISPUTE / ASK FOR SOURCE. Before proceeding.
- **`META-QUOTA`** — max 10% of output on epistemology and strategy.

## Files

| MOOLLM | General | Notes |
|---|---|---|
| `.cursorrules` | `AGENT.md` / `CLAUDE.md` | The free channel |
| `.moollm/` | `.agent/` | Runtime state, gitignored |
| `MOOLLM.yml` | `PROJECT.yml` | Manifest |
| `PROTOCOLS.yml` | `GLOSSARY.yml` | The K-line index |
| `skills/INDEX.yml` | `capabilities/INDEX.yml` | **The entry point** |
| `GLANCE.yml` | `GLANCE.yml` | Neutral, keep it |
| `CARD.yml` | `CARD.yml` | Neutral enough, keep it |
| `SKILL.md` | `SKILL.md` or `PROTOCOL.md` | |
| `ROOM.yml` | `MODULE.yml` | Domain interface — name it for *your* domain |
| `CHARACTER.yml` | `ROLE.yml` | If you use reviewer roles |
| `output.md` | `output.md` | Neutral |
| `session-log.md` | `session-log.md` | Neutral |
| `hot.yml` / `cold.yml` / `working-set.yml` | same | Neutral |

## The lineage names — keep them

These are dense, prepaid, and accurate. Using them costs one token and buys a library. This is
P1 working correctly.

| Name | Points at | Use when |
|---|---|---|
| **Postel's law** | RFC 761, robustness principle | Talking about tolerant input |
| **Minsky, Society of Mind** | Intelligence from simple agents | Justifying decomposition |
| **K-line** (Minsky) | Names activate constellations | Explaining P1 — but define it once |
| **Self / prototypes** (Ungar) | Delegation, cloning, no classes | Inheritance without classes |
| **The Sims / SimAntics** (Wright) | Objects advertise, needs score | Explaining declarative routing |
| **HyperCard** (Atkinson) | Self-contained navigable units | Explaining CARD |
| **Robust-first** (Ackley) | Survivability over correctness | Justifying graceful degradation |
| **Densmore–Rosenthal** (US5187786A) | Directories as objects, 1991 | Citing prior art for P4 |
| **COM / QueryInterface** | Interface-based dispatch | Explaining marker files |

**But:** name-drop for the *model*, explain for the *human*. A doc that says "this is SimAntics"
and stops has served the LLM and abandoned the reader. One sentence of gloss costs you nothing
and is the difference between a teachable framework and MOOLLM.

## Translation, worked

MOOLLM:

> The pub advertises `enter_pub` with score 0.8 when the character's social need is high. The
> room's ROOM.yml is a K-line that wakes the constellation. The LLM is `eval()`.

General:

> The `code-review` capability declares a trigger with relevance 0.8 when the diff touches
> auth. Its `CARD.yml` declares the interface. The model reads the declaration and decides
> whether to invoke it.

Same architecture. Same mechanisms. One of them your team can act on.

## The rule

**Left column: reading MOOLLM. Right column: writing anything else.**

If you find yourself explaining a left-column term to a colleague, you've reintroduced the
respelling cost the whole architecture exists to avoid — and you're paying it in humans, who
are more expensive than tokens.
