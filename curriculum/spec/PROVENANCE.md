# Provenance and Prior Art

> **Tier:** Specification · argument: [WHITEPAPER.md](WHITEPAPER.md) · rules: [MECHANISMS.md](MECHANISMS.md)

Nothing in this series is presented as newly invented here. The pattern has one immediate
origin and a deep, checkable lineage; this page records both, so that credit lands where it
belongs and so readers can follow any mechanism to its source literature.

## Immediate origin: MOOLLM

The ten mechanisms and three principles are extracted from **MOOLLM** — *Microworld
Operating System for LLMs* — by **Don Hopkins** (github.com/SimHacker/moollm, 2024–present),
with collaborators including Henry Minsky and the Leela AI team, where the same architecture
runs against industrial computer-vision work rather than game worlds.

What this series changes, and does not:

| | MOOLLM | This series |
|---|---|---|
| Mechanisms | ten, embedded in a text-adventure microworld | the same ten, domain-neutral names |
| Codebook | adventure games, The Sims, MOO tradition | offices, libraries, Unix — reader-owned metaphors |
| Register | manifesto, demonstration, play | specification, measurement, limits |
| Floor | conventions the model follows (P1 advisory mode) | same, plus a required validator and stated open questions |
| Credit | cites its lineage carefully | cites MOOLLM the same way |

MOOLLM's own presentation — the whimsy included — is respected as the origin form, and the
study underlying this series found the whimsy to be *functional*: a compression codebook
dense in the model's latent space (M9, whitepaper §7). Readers who want the mechanisms in
their native habitat should read MOOLLM itself, starting at its manifesto and
`kernel/ARCHITECTURE.md`.

## The lineage, mechanism by mechanism

Every load-bearing idea has a named source, and the citations check out:

| Mechanism / principle | Source tradition | The specific inheritance |
|---|---|---|
| M1 Resolution ladder | Computer-graphics mipmaps; library card catalogs | Multi-resolution representations read cheapest-first (MOOLLM: "semantic image pyramid") |
| M2 Declarative routing | **Will Wright, The Sims (2000)** — advertisements, needs, dithering | Objects broadcast scored actions; selection = collect, score, pick from top-N; extensibility without central edits (why expansion packs worked) |
| M3 Host drivers | Operating-system device drivers | One policy, N adapters, declared fallbacks, capability tiers |
| M4 Externalized state | Unix "everything is a file"; CPU cache hierarchies | Hot/warm/cold context tiers as files; attention as an artifact |
| M5 Standing constraints | Minsky's censors/suppressors (*Society of Mind*); checklists | Always-on negative constraints; naming the failure mode as most of the fix |
| M6 Boot compilation | JIT compilation and profile-guided optimization; **Ungar & Smith's Self** implementation lineage | Watch what runs, compile the hot path into the cheap channel (MOOLLM: cursor-mirror OPTIMIZE) |
| M7 In-context ensemble | **Minsky, Society of Mind (1985)**; ensemble inference; MOOLLM's own "Speed of Light vs Carrier Pigeon" analysis | Many agents in one substrate; the boundary-tax critique of call-per-agent architectures is MOOLLM-original |
| M8 Directory-as-object | **Densmore & Rosenthal, US Patent 5,187,786 (Sun Microsystems, filed 1991)** — OOP in a hierarchical filesystem; **Self (Ungar & Smith, 1987)** — prototypes, clone-don't-instantiate; COM's QueryInterface; **Pavel Curtis, LambdaMOO (1990)** — persistent objects in navigable space | Identity = path; interface = marker file; prototypes instantiate stateful copies |
| M9 Names as addresses | **Marvin Minsky, "K-lines: A Theory of Memory" (1980)** | A name reactivates the mental state present when it was learned; MOOLLM's contribution is the *economics* — latent knowledge is prepaid, novel jargon is a cache miss billed forever |
| M10 Tolerant interpretation | **Jon Postel, RFC 761 (1980)** — liberal in, conservative out; **Dave Ackley** — robust-first computing, the Movable Feast Machine | Repair-not-crash; survive → heal → function → optimize; "a crashed system is infinitely wrong" |
| P1 Dual-mode contract | NeWS magic dictionaries (Hopkins' own lineage): data structures backed by a live system, or not, transparently | Same files, advisory or operational runtime |
| P2 Determinism split | Standard engineering judgment, stated crisply by Hopkins in the Leela demo: deterministic → scripts, judgment → the model | |
| P3 Rewrite-not-truncate | Editorial practice; the study's inspection result | The tier boundary is a human judgment about what a reader needs at that depth |

Deeper background woven through the origin: **Piaget** (knowledge constructed through
interaction) → **Papert** (constructionism, microworlds) → **Minsky** (agents, K-lines) →
**Drescher** (*Made-Up Minds*, 1991 — schema mechanism: context → action → result, the
play-learn-lift loop's ancestor); **Alan Kay** (the workspace-as-medium sensibility);
**Ken Kahn's ToonTalk** (making message-passing concurrency visible — the origin's
carrier-pigeon metaphor used honestly, as pedagogy).

## What is MOOLLM-original, as best this study can determine

Beyond the synthesis itself (which is the main contribution): the **latent-knowledge
economics** stated as a design rule (M9's "prepaid vs. billed-per-call, forever"); the
**boundary-tax critique** in its sharp form ("tokenization destroys precision; delay
tokenization"); **AMBIENT-as-advertisement** (always-on behavior unified into the routing
mechanism rather than special-cased); the **four-tier per-unit ladder** as a written
discipline with a stated reading rule; and the **dual-mode contract** as an explicit design
stance rather than an accident of missing tooling.

## Naming record

The series name **"the Legible Workspace"** was chosen (Phase 0, 2026-07-15) over
*Context-Resident Orchestration*, *Filesystem-Native Orchestration*, and
*Resolution-Ladder Orchestration*, for the reasons recorded in
[shared/CANON.md](../shared/CANON.md): legibility is the invariant all ten mechanisms serve,
and the name is built from prepaid words — the paradigm's own M9 applied to itself. "MOOLLM"
remains the name of the origin system and is never treated as a legacy term.
