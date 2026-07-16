# Capability-Unit Anatomy

The [mechanism inventory](02-mechanism-inventory.md) names what MOOLLM's architecture *does*.
This document names how a capability unit is *built* — the construction standard shared by all
141 skill directories. The inventory treated the skills as a corpus to be measured; this
treats one skill as an artifact to be reverse-engineered.

Primary sources, in authority order: `skills/skill/SKILL.md` (the meta-skill — the skill that
defines skills), `skills/INDEX.md` (the catalog and its reading protocol),
`kernel/ARCHITECTURE.md` (§ Ambient Skills, § Agents All The Way Down),
`skills/bootstrap/CARD.yml` (a well-formed card to imitate), `kernel/INTEREST-GATES.yml`
(precondition gating).

Portability ratings as in the inventory: 🟢 direct, 🟡 adapt, 🔴 local.

---

## A1 · The four-file contract 🟢

Every unit is a directory with the same four files, which are the four rungs of the
resolution ladder (M1) *instantiated per unit*:

| File | Required | Role | Audience |
|---|---|---|---|
| `GLANCE.yml` | effectively¹ | "Is this relevant?" | LLM, scanning many |
| `CARD.yml` | ✓ | Interface: methods, advertisements, k-lines, file index | LLM, deciding to activate |
| `SKILL.md` | ✓ | Full protocol with YAML frontmatter | LLM, executing |
| `README.md` | ✓ | History, rationale, discovery | Humans browsing |

¹ The meta-skill lists GLANCE as part of the pyramid but not the required trio; in practice
the INDEX entry can serve as the glance. The rule from `skills/INDEX.md`: *"If you have CARD
or SKILL, you do not need GLANCE."*

MOOLLM explicitly keeps `README.md` **against Anthropic's recommendation**, because the two
files serve different audiences: README is for humans discovering (GitHub renders it), SKILL
is for models executing. This is a deliberate, argued deviation, not sloppiness.

Optional members, added only when needed (**flat-to-structured growth** — the meta-skill
prescribes starting flat and adding `scripts/`, `templates/`, `references/`, `examples/`
directories only when a second file of that kind appears):

| Member | Purpose |
|---|---|
| `*.tmpl` | Templates the unit instantiates from (see A5) |
| `*.py` | "Sister scripts" — deterministic automation |
| `examples/` | Curated examples; also the raw material for boot compilation (M6) |
| `plugins/` | Loadable extensions |
| instance library dir | Catalog of pre-made instances (see A5) |

**One structural rule worth stealing verbatim:** *"Top-level SKILL.md references ALL files,
regardless of nesting. No hierarchical hunting."* The unit's root doc is a complete manifest.

---

## A2 · Frontmatter and the 50-line contract 🟢

`SKILL.md` opens with YAML frontmatter. The core fields (`name`, `description`) are
Anthropic-skill compatible; MOOLLM extends with `allowed-tools`, `permissions`, `related`,
`license`, `tags`, `credits`.

The deeper convention is **front-matter sniffing**: the first ~50 lines of any file — skill,
script, or document — must be sufficient to decide whether to keep reading. For skills that
means frontmatter + one-liner + purpose + file map inside the sniff window. For Python it's
the `sniffable-python` pattern: docstring, imports, constants, CLI structure first;
implementation below the fold. The same artifact serves humans (`--help`) and models (first
50 lines) without duplicate documentation.

This generalizes the resolution ladder from directories down into single files: **every file
has its own glance, and it's the top of the file.**

---

## A3 · CARD.yml: the interface in full 🟢

The study's inventory covered advertisements (M2). A real card carries more, and the extra
sections are load-bearing. From `skills/bootstrap/CARD.yml`, the complete anatomy:

| Section | What it declares | Why it matters |
|---|---|---|
| `card:` | id, name, type tags, aliases, tagline, `reach` (permission scope) | Identity + one-line pitch |
| `files:` | **Index of every file in the unit, grouped** | "One activation can load skill + resources for next iteration" — a paging manifest |
| `k-lines:` | `activates:` (symbols this unit answers to) + `related:` (refs with named relations) | The unit's vocabulary entry (M9) |
| `invoke_when:` | Plain-language trigger conditions | Human-readable routing |
| `methods:` | **Signatures only** — full sequences live in SKILL.md | Interface/implementation split; CARD is not repeated in SKILL |
| `advertisements:` | Scored, conditioned activation offers (M2) | Machine routing |
| `drivers:` | Per-host adaptation table (tier, degradation mode) | The unit knows its own fallbacks (M3) |
| `warming_priorities:` | What to preload at which priority | Boot integration (M6) |

Two details the study previously missed:

**Resolution hints.** A card can declare how deeply it should be paged in:
`activation_only → summary → interface → implementation → full`. The ladder isn't only
something the reader climbs; the unit itself states which rung suffices for a given use.

**AMBIENT is an advertisement type, not a separate mechanism.** MOOLLM considered a dedicated
`AMBIENT.yml` file and explicitly rejected it: the advertisement system already has scores,
conditions, and priorities, so always-on presence is expressed as an ad with
`condition: always` plus two extra fields — `scope` (session/conversation/room) and
`resolution` (how much of the unit stays loaded). Standing constraints (M5) are therefore not
special-cased anywhere: one routing mechanism handles on-demand *and* always-on. That's a
genuinely elegant unification and the template should reflect it.

---

## A4 · Aggregation: how 141 units stay navigable 🟢

The catalog layer above the units has its own construction standard:

**The prose index.** `skills/INDEX.md` is a *narrative* index — flowing paragraphs where
**every bold term is simultaneously a k-line and a skill directory name, spelled exactly**,
and bold is used for nothing else. Skills are introduced in dependency groups (Foundation,
Philosophy, Format, …) so reading the index top to bottom is also a load order. MOOLLM claims
the markdown form beats the YAML form (`INDEX.yml`, same content) by ~46% fewer tokens while
carrying *more* relational meaning, because prose encodes relationships that repeated YAML
keys cannot. (Claimed in `designs/`; consistent with the file sizes — 10.1 KB vs 19.9 KB —
but not independently re-measured here.)

**The reading protocol is printed at the top of the index.** Resolution order, when to skip
GLANCE, the instruction to load CARD + SKILL together on activation, and the note that CARDs
list the *next* files to page in. The catalog teaches you how to read the catalog.

**Declared load order.** Foundation (moollm → skill → k-lines → bootstrap) → Format → Quality
→ Ethics → Core → everything else on demand. A dependency-ordered boot sequence, stated as
six lines of text.

**Aliases are explicit.** `k-lines ↔ protocol` — same unit, two names, declared in the index
rather than discovered by accident.

---

## A5 · Factories and instance libraries 🟢

The meta-skill's first claim: skills are **prototypes that create instances**, not static
documentation. Behavior lives in the prototype; state lives in instances. The skill directory
carries `*.tmpl` templates; instantiation produces a directory elsewhere that inherits from
the prototype and accumulates its own state.

Mature units grow an **instance library** — a catalog of pre-made instances inside the skill,
in three interchangeable styles:

| Style | When | Example |
|---|---|---|
| Directory per instance | Complex, has assets | `buffs/fire-resistance/BUFF.yml` |
| Single file | Simple, standalone | `buffs/haste.yml` |
| `INDEX.yml` bundle | Many small related | 20 buffs in one file |

Instances are referenced by path, with fragment addressing into bundles:
`ref: skills/buff/buffs/INDEX.yml#haste`. The same addressing works into logs — objects
embedded in append-only narrative files (`LOG.md#session-artifact`) are readable in place,
and the **promotion pattern** says: the moment you need to *edit* one, promote it to its own
`.yml` file. Read-only history stays append-only; mutable state graduates out of it.

Domain-neutral restatement: **a capability ships with a starter catalog, and users reference,
copy, or extend catalog entries by path.** This is the part of the "Vite feeling" the
template can actually deliver — scaffolding is instantiation from a prototype's templates.

---

## A6 · Instantiation modes: the cost dial 🟢

Not every use of a unit creates files. The meta-skill defines four modes, cheapest first:

| Mode | Files created | When |
|---|---|---|
| **Mentioned** | none | "Apply POSTEL here" — pure k-line invocation |
| **Modeled** | none | Guided use within the conversation only |
| **Embedded** | inside another doc | Design discussion, literate programming |
| **Instantiated** | full directory | A running instance with persistent state |

*"Start light, instantiate when needed."* This resolves a question the study's template left
implicit: activation is not binary. A unit can shape one response for zero tokens of state,
or become a permanent stateful subdirectory, and the levels in between are legitimate.

---

## A7 · Precondition gates 🟡

`kernel/INTEREST-GATES.yml` defines a three-stage gate hierarchy for any interactable thing:
**visibility** (do you even see the option?) → **activation** (can you start it?) →
**execution** (can you complete it?), with structured failure feedback at each stage
("too far" vs "blocked" vs "missing requirement").

The vocabulary is proximity-based (rooms, meters, routing slots) — that part is 🔴 Sims/MUD
theater. The portable kernel is: **advertisements carry preconditions evaluated *before* the
option is shown, and gate failures are typed, not generic.** A capability that can't run in
this host/context shouldn't appear in the routing set at all — and when something is shown
but unavailable, the reason has a category. The study's template currently treats an
advertisement's `condition` as one opaque string; a gate taxonomy (available / visible-but-
blocked / hidden, with reason types) is the graduated version.

---

## A8 · The dual-mode contract 🟢 (cross-cutting — promote to framework)

The single most under-reported finding of this pass. From `kernel/ARCHITECTURE.md`:

Every control file is written to work under **two runtimes**:

| Runtime | `hot.yml` / ads / working-set are… | Who acts on them |
|---|---|---|
| **Operational** (a smart orchestrator exists) | Commands — parsed, enforced, injected | The orchestrator |
| **Advisory** (generic host: Cursor, Claude Code) | Conventions — the model reads them and self-manages | The LLM itself |

Same files, no changes, graceful degradation of *authority* rather than of function. And on
generic hosts the files can run **in reverse** — generated as *mirrors* documenting what the
host actually loaded, rather than commands for what it should load.

This explains what the study's honest assessment flagged as "documentation of an aspiration"
(M3's fallbacks, M4's nothing-decides). It is not an unfinished implementation; it is the
contract's designed floor. The files are the API; enforcement is an upgrade, not a
prerequisite. The framework docs should state this as a first-class principle instead of a
caveat.

---

## A9 · The determinism split 🟢 (cross-cutting — promote to framework)

Stated by Don Hopkins directly (Leela demo transcript, §4): *"Factor work into deterministic
and non-deterministic components. Put everything possible into Python for deterministic, fast
execution. Reserve the LLM for tasks that require judgment, creativity, or natural language
understanding."*

In unit anatomy this is the sister-script rule: when Play-Learn-Lift discovers a consistent,
mechanical sub-procedure inside a skill, it gets **lifted out of prose and into a script**.
The skill doc shrinks to judgment; the script owns repetition. The study's template has
`validate.py` but never states the principle that produced it.

---

## A10 · What's declared but not built 🔴→file under honest assessment

For completeness, the meta-skill contains a designed-but-unimplemented **skill compiler**
(dead k-line elimination, README absorption, tiered output targeting a host/domain) and a
publishing/permissions model (MOOAM). Treat both as the same category as M6's aspiration:
the direction is coherent, the artifact doesn't exist. The *requirement it implies* is real,
though — units must be **self-contained** (SKILL.md works alone, without CARD or README),
which is stated policy and is portable today.

---

## Summary: what this adds to the template

| Finding | Template implication |
|---|---|
| A1 four-file contract + root-doc-as-manifest | Already present; add the "SKILL references all files" rule |
| A2 50-line sniff contract | State it in policy; applies to scripts too |
| A3 full card anatomy (files index, k-lines, drivers, warming, resolution hints) | Template cards carry only ads + methods — extend |
| A3 AMBIENT-as-advertisement | Template's standing constraints should use the unified ad form |
| A4 prose index + printed reading protocol + load order | Template `INDEX.yml` is bare YAML — add the narrative index with the protocol at top |
| A5 instance libraries + promotion pattern | Absent from template; this is the scaffold story |
| A6 instantiation modes | Document the cost dial in the pattern doc |
| A7 typed gates | Optional; graduate `condition:` when needed |
| A8 dual-mode contract | Promote to framework principle; reframe honest-assessment caveats |
| A9 determinism split | Promote to framework principle |

These are template *checks*, to be applied at the end of the series drafting pass (per the
working agreement: MOOLLM is the source of truth; this study is a lens that gets corrected).
