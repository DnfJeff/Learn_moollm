# Honest Assessment

What's real, what's aspirational, what's broken. Written in the spirit of MOOLLM's own
`no-ai-sycophancy`: *"Respect is not agreement."*

MOOLLM is a serious piece of work by someone with a thirty-year track record of building
systems people actually play with. That's exactly why it deserves a real critique rather than
a tour.

## The biggest thing: it's a discipline, not a runtime

**MOOLLM describes a two-party system and ships as a one-party discipline.**

The architecture is built on this split, stated repeatedly:

> *The model advises. The orchestrator decides.*
> — `kernel/memory-management-protocol.md`

The model writes `hot.yml` saying what it wants kept. The orchestrator reads it and manages
context. The model advertises; the orchestrator injects. Clean separation. Good design.

**On every host MOOLLM supports today, the orchestrator does none of this.**

Cursor does not read `hot.yml`. Claude Code does not parse `CARD.yml`. Nothing injects ambient
skills. Nothing enforces append-only. Nothing evaluates `score_if`. Nothing assembles context
from `working-set.yml`.

MOOLLM knows. `kernel/drivers/cursor.yml` is explicit — everything is "advisory." The
architecture doc has a whole table for it:

| Feature | Generic (Advisory) | Smart (Operational) |
|---|---|---|
| `hot.yml` | Documentation of what SHOULD be prioritized | Actually loaded into context |
| `cold.yml` | Breadcrumbs for archaeology | Actually evicted |
| Ambient skills | LLM must manually load | Injected invisibly |
| CARD advertisements | Read on demand | Parsed and activated |

The right column is **MOOCO** — the smart orchestrator. It is referenced throughout the
repository. It does not exist here. `kernel/ARCHITECTURE.md`'s see-also table points to it as
"(see orchestrator docs)." There are no orchestrator docs.

So the honest description:

> **MOOLLM is a set of conventions an LLM reads and voluntarily follows, plus a detailed
> specification of the runtime that would enforce them, which is not included.**

The `advertisement` skill's own design notes concede this, and the concession is the most
clear-eyed paragraph in the repository:

> **rejected-because:**
> - "Requires smart orchestrator we don't control (Cursor, Claude Code)"
> - "Adds complexity without current runtime support"
>
> **pragmatic-solution:** *"Throw down the gauntlet" architecture: ... 4. **Trust the LLM** —
> once CARD is in context, constraints apply.*

"Trust the LLM" is the enforcement model. That's it. That's the whole thing.

**Is that fatal?** No — and this is important. The conventions genuinely work, because modern
models genuinely do follow well-structured instructions in context. The efficiency in
[04-token-economics.md](04-token-economics.md) is real and doesn't depend on a runtime; a
ladder works because the *reader* climbs it. But you must not confuse "the model usually does
this" with "the system does this." One is a tendency. The other is a guarantee. MOOLLM
documents guarantees and delivers tendencies.

**For your project:** decide per mechanism whether a tendency is enough. For "read the summary
first" — fine, tendencies are fine. For "never write to this file" — get a real hook.

## The bug that proves both cases

`.cursorrules` does not parse as YAML.

```
.cursorrules parses as YAML: NO -> line 208, column 2
```

Lines 208–221 (`yaml-jazz`, `copy-that`) are indented one space instead of two. They break out
of the `ambient_skills:` mapping. In any YAML-consuming system this file is a hard error.

It has been sitting there working fine, because **nothing parses it.** An LLM reads it, sees
two more entries in an obvious list, and carries on. POSTEL in action: charitable
interpretation, no crash.

This single file demonstrates the architecture's central bet **and** its central risk:

- ✅ **The bet pays off.** The LLM is a robust parser. Structure can be approximate. The system
  survives errors that would halt a conventional pipeline.
- ❌ **The floor is missing.** A structural error lived in the boot file indefinitely, silently,
  with no signal. Nobody knows how long. Nothing will ever tell you.

Both are true. From one file. It's the most instructive artifact in the repository, and it's
an accident.

**The lesson:** tolerance for *input* is a feature. Tolerance for *your own configuration* is
an absence of tests. MOOLLM doesn't distinguish. Your framework should — see
[template/](../../template/), which ships a validator specifically because of this file.

## Drift

The system has no mechanism to detect its own inconsistency, and it is inconsistent.

| Claim | Location | Reality |
|---|---|---|
| "117 skills and counting" | `README.md` | 141 directories |
| `skill_count: 133` | `skills/INDEX.yml` | 141 directories |
| "~80 skills" | `QUICKSTART.md` | 141 directories |
| "132 Skills" | `skills/INDEX.yml` header comment | 141 directories, and it contradicts `skill_count: 133` two lines below |

Four numbers, four values, none correct. The index header disagrees with the index body.

This is what the resolution ladder costs: **four tiers per skill means four places to drift,
and 141 skills means 564 documents in hand-maintained sync.** There is no build step, no
validation, no CI. `scripts/` contains three files, all git hooks, none of which check this.

It's the predictable failure of "no build step" as a virtue. The build step is what catches
this. MOOLLM traded it away for zero-ceremony authoring, and the bill is drift.

**For your framework:** you can keep zero-ceremony authoring *and* have a checker. They're not
opposed. `evidence/measure.py` in this study detects the drift in under a second. That's the
entire cost of not having this problem.

## What's genuinely excellent

Criticism is cheap. Here's what I'd take without hesitation:

**1. The `no-ai-*` family.** Twelve behavioral constraints, each naming its failure modes as
K-lines with one-line fixes. `CERTAINTY-THEATER`, `EUPHEMISM-LAUNDERING`, `QUALIFIER-STACKING`,
`EPISTEMIC-EXHAUSTION`. Naming a failure mode is most of the fix — "don't be verbose" is
unusable, `VERBOSITY` as a named sin with a stated test is actionable. `CLAIM-LEDGER` (for
each user claim: CONFIRM / DISPUTE / ASK FOR SOURCE, before proceeding) is worth the price of
admission alone. This is the most immediately stealable content in the repository and it has
nothing to do with adventure games.

**2. The latent-knowledge economics.** *"Latent knowledge is prepaid; respelled knowledge is
billed per call, forever. Novel jargon is a cache miss that never fills."* This is the
sharpest single insight about prompt engineering I've encountered, it's stated in one line,
and it's buried in skill #58 of 141 rather than in the kernel.

**3. The Carrier Pigeon critique.** *"Tokenization destroys precision. Detokenization adds
noise. Delay tokenization."* A real, load-bearing critique of the dominant multi-agent
architecture, delivered in three lines.

**4. The resolution ladder itself.** Obvious in concept, rare in execution, 155× in effect.

**5. Intellectual honesty in the source.** The `advertisement` CARD's design-decision block —
recording what was considered, what was rejected, and why — is better engineering documentation
than most production codebases contain. It argues against its own preferred design and says so.

**6. The lineage is real.** The Densmore–Rosenthal patent (US5187786A) genuinely describes
directories-as-objects in 1991. Self, SimAntics, HyperCard, NeWS, RFC 761 — these citations are
accurate, not name-dropping. MOOLLM says *"we're not inventing — we're combining"* and that's
an honest self-description.

## What's overclaimed

**"117 skills"** — 141 directories exist, but count what's *general*: ~15 mechanisms, ~12
constraints, ~20 process, ~6 deliberation. Call it 50. The rest is a demo world, domain
one-offs (`emacs`, `micropolis`, `postgres`), and philosophy essays. "141 skills" measures
directories, not capability.

**"Microworld Operating System"** — it's a document set. Calling `kernel/` a kernel invites a
comparison it loses: no scheduler, no isolation, no resource management, no enforcement. The
metaphor is doing marketing work here rather than compression work, and it's the one place the
naming misleads rather than compresses.

**"Skills are programs. The LLM is `eval()`."** — evocative and roughly right, but `eval()`
has *semantics*. Skills are prose an LLM interprets probabilistically. It's closer to "skills
are documentation the LLM usually follows," which is less quotable and more true.

**Tier 6 / MOOCO** — referenced throughout as though it exists. It doesn't. The capability
table lists it as a shipping tier alongside Cursor and Claude Code.

## What's missing

| Gap | Why it matters |
|---|---|
| **Evals** | Nothing measures whether the model picks the right skill from the index. That's the load-bearing question and it's untested. |
| **Validation** | No check for pyramid conformance, index drift, or YAML validity. All three are currently broken. |
| **The orchestrator** | The right column of every capability table. |
| **Comparison to embeddings** | The ladder is hand-maintained. Vector search might beat it on cost and accuracy and requires no maintenance. Unexamined. |
| **Multi-agent guidance** | `speed-of-light` flags herd-behavior risk in one line and drops it. When is the boundary tax worth paying? Never answered. |
| **A "just the framework" entry point** | The reason this study exists. |

## The verdict

**Take:** the resolution ladder (M1), declarative routing (M2), driver layer (M3), externalized
state (M4), standing constraints (M5), the latent-knowledge economics (M9), tolerant input
handling (M10). Seven of ten mechanisms, directly, after renaming.

**Adapt:** boot compilation (M6) — the concept is general, `cursor-mirror` is not. In-context
ensembles (M7) — powerful, but decide the herd-behavior question yourself. Directory-as-object
(M8) — take "identity = path, interface = marker file," leave the prototype resolver.

**Leave:** the adventure world, the domain one-offs, the philosophy essays, and every
occurrence of the word "kernel."

**Add what MOOLLM lacks:** a validator, and an eval for retrieval quality. Two things it never
built, both cheap, both fixing its two worst problems — silent drift and unproven selection.

**The honest summary:** MOOLLM is a well-designed set of conventions with an unusually good
compression scheme, an excellent behavioral-constraint library, a real efficiency result, no
enforcement, no tests, and a hard dependency on a runtime that doesn't exist. It works anyway,
because modern LLMs are forgiving readers — which is simultaneously the thesis it's proving
and the reason it can't tell when it's broken.

It is worth studying. It is not worth copying wholesale. Take the ten mechanisms, swap the
codebook, add a floor.

That's [framework/01-the-pattern.md](../framework/01-the-pattern.md).
