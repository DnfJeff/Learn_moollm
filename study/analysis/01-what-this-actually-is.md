# What MOOLLM Actually Is

A plain description, with the whimsy set aside. Not because the whimsy is worthless — see
[03-metaphor-vs-mechanism.md](03-metaphor-vs-mechanism.md) — but because you cannot evaluate
a thing while it is winking at you.

## The elevator description

MOOLLM is **a set of file conventions that let an LLM navigate a corpus far larger than its
context window, and a body of policy text that shapes how it behaves while doing so.**

That's it. That is the whole system.

It is not a program. Nothing executes. There is no server, no daemon, no runtime loop. The
repository contains three Python/shell scripts total, and none of them are the system — they
are utilities beside it. When MOOLLM says "kernel," it means *a directory of Markdown and
YAML documents that an LLM is expected to read and voluntarily obey.*

This is stated openly in the source. From `kernel/ARCHITECTURE.md`:

> The kernel provides **infrastructure**, not **semantics**.

And from `kernel/memory-management-protocol.md`, the line that most honestly describes the
whole architecture:

> *Memory is infrastructure, not cognition.*
> *The model advises. The orchestrator decides.*

The catch, examined in [05-honest-assessment.md](05-honest-assessment.md), is that on every
orchestrator MOOLLM actually supports today, **there is no orchestrator making decisions.**
The model advises, and then the model also decides, because nothing else is there. The
architecture describes a two-party system and ships as a one-party discipline.

## What's in the box

```
moollm/
├── kernel/       30 files   The actual architecture. Policy + protocols + host adapters.
├── skills/       2,067 files 141 units of capability. The library.
├── designs/      225 files  Essays, rationale, lineage.
├── examples/     2,090 files One large adventure world. Demo content.
├── schemas/      6 files    YAML shapes.
├── indexes/      9 files    Curated lists.
├── scripts/      3 files    Git hooks. Not load-bearing.
└── .moollm/      47 files   Runtime state (gitignored). Currently: a Mayberry adventure.
```

The proportion is the first useful fact: **kernel is 0.7% of the file count.** Roughly 4,150
of the 4,489 files are content — a demo world and a skill library — not architecture. The
architecture is small. It is buried in a warehouse.

That ratio is why the system reads as impenetrable. Nothing is hidden; it's just that the
signal is 30 files and the noise is 4,459, and the noise is charming enough that you keep
reading it.

## The three layers, as claimed

From `kernel/ARCHITECTURE.md`:

| Layer | Contents | Claim |
|---|---|---|
| Userland | `skills/` | Semantics, application logic |
| Kernel | `kernel/` | Infrastructure, plumbing, adaptation |
| Hardware | LLM + orchestrator | Stateless token predictor + context management |

This is a real and useful separation, and it mostly holds. The kernel genuinely doesn't know
what a "room" is. You could delete `examples/` and every game-flavored skill and the kernel
would still stand. That's the property that makes extraction possible at all.

## The five things the kernel actually specifies

Stripped of framing, `kernel/` says five things:

**1. Read at the cheapest resolution that answers your question.**
Four tiers per skill — `GLANCE.yml` (~1.7 KB) → `CARD.yml` (~5.4 KB) → `SKILL.md` (~11 KB) →
`README.md` (~4.7 KB) — plus a rule from `.cursorrules`: *"Never load a lower level without
first loading the level above."* This is the single most important mechanism in the system.

**2. Identity is location; interfaces are marker files.**
A directory *is* an object. Its path is its identity. An UPPERCASE file inside it is an
interface: `CARD.yml` means dispatchable, `SKILL.md` means it teaches a protocol,
`ROOM.yml`/`CHARACTER.yml` mean domain interfaces. Asking "is this a skill?" is `os.path.exists`.
No registry, no manifest, no build step. `kernel/DIRECTORY-AS-OBJECT.md` traces this to the
Densmore–Rosenthal patent (US5187786A, Sun, 1991), which is a real and correct citation.

**3. Units declare when they're relevant; nothing central routes them.**
Every capability carries `advertisements:` — a name, a condition, a score. Selection is
"collect all advertisements in scope, score against current context, take the top." The
router doesn't know what exists. The things that exist know when they matter.

**4. State lives in files, not in memory.**
`working-set.yml` (current focus), `hot.yml` (keep loaded), `cold.yml` (evicted breadcrumbs),
`session-log.md` and `output.md` (append-only). No hidden state. If it isn't in a file, it
didn't happen.

**5. Adapt to the host; never crash.**
`kernel/drivers/*.yml` map abstract operations onto concrete tools per environment (Cursor,
Claude Code, generic), declare capability tiers 0–6, and specify fallbacks for every missing
feature. Paired with POSTEL ("accept messy input, emit clean output") and robust-first
("a crashed system is infinitely wrong").

Those five, plus the in-context-ensemble idea from `speed-of-light`, are the entire portable
architecture. Everything else in 4,489 files is either an application of them or a story
about them.

## What the skills library actually contains

141 skill directories, and they are not one kind of thing. Sorting them by what they *do*
rather than what they're *called*:

| Kind | Count (approx) | Examples | Portable? |
|---|---|---|---|
| Behavioral constraints | ~12 | `no-ai-slop`, `no-ai-hedging`, `no-ai-sycophancy`, `postel` | **Directly.** Best-in-class. |
| Core mechanisms | ~15 | `card`, `advertisement`, `skill`, `prototype`, `context`, `scoring`, `k-lines` | **Yes**, after renaming. |
| Process/method | ~20 | `plan-then-execute`, `play-learn-lift`, `code-review`, `research-notebook`, `rubric` | **Yes**, mostly. |
| Deliberation | ~6 | `adversarial-committee`, `debate`, `evaluator`, `roberts-rules` | **Yes.** Underrated. |
| Game/world content | ~50 | `room`, `character`, `adventure`, `bartender`, `cat`, `pub` | No. This is the demo. |
| Domain-specific | ~20 | `postgres`, `datasette`, `micropolis`, `emacs`, `sqlite` | Irrelevant to the framework. |
| Lore/philosophy | ~18 | `society-of-mind`, `constructionism`, `mythic`, `soul-chat` | Rationale, not mechanism. |

The `no-ai-*` family deserves special notice and gets it in
[guide/05-standing-constraints.md](../guide/05-standing-constraints.md). It is the most
immediately stealable thing in the repository and has nothing to do with adventure games.

## The one paragraph that explains the whole design

From `no-ai-humansplaining`, inlined into `.cursorrules`:

> **"Latent knowledge is prepaid; respelled knowledge is billed per call, forever. Novel
> jargon is a cache miss that never fills."**
> Constitutional directive: **LEAN INTO the training data.**

This is the load-bearing insight of the entire architecture, and it is stated in one of the
141 skills rather than in the kernel, which tells you something about how the repository is
organized.

Everything else follows from it. Why rooms? Because the model already knows rooms. Why The
Sims? Because the model already knows The Sims. Why cite Minsky, Ungar, Wright, Postel,
Ackley, Papert by name? Because those names are dense pointers into pretrained weights, and a
name costs one token while an explanation costs a paragraph on every call forever.

MOOLLM is, at its core, **a system for addressing pretrained knowledge by name instead of
re-teaching it.** The adventure game is the address space.

Which is elegant, correct, and the exact reason you're reading this study instead of just
reading MOOLLM.

## Where to go next

[02-mechanism-inventory.md](02-mechanism-inventory.md) names each mechanism precisely and
rates it for portability. If you'd rather have the argument than the catalogue, skip to
[03-metaphor-vs-mechanism.md](03-metaphor-vs-mechanism.md).
