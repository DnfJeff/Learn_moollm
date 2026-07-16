# Guide 1 · Progressive Disclosure

**The resolution ladder.** How to make a library bigger than the context window navigable.

MOOLLM calls this the Semantic Image Pyramid. It's the most valuable mechanism in the system.

## The problem

You have 141 capabilities. Their full documentation is 790,000 tokens. Your context window is
200,000. Even if it were 2,000,000, filling it would be wrong — you'd pay for everything on
every call and the model's attention would be spread across 140 irrelevant documents.

**The model needs to find the right capability without reading them all.**

## The solution

Write each capability at several sizes. Read the cheapest one that answers your current
question. Descend only when the question demands it.

```
INDEX.yml       ~35 tokens/entry     Does it exist?
GLANCE.yml      ~400 tokens          Is it relevant?
CARD.yml        ~1,400 tokens        What can it do? How do I call it?
SKILL.md        ~2,800 tokens        How does it actually work?
README.md       ~1,200 tokens        Why is it built this way?
```

**The rule:** *never load a tier without first loading the tier above.*

That rule is the whole thing. Without it the ladder collapses into "just read SKILL.md," which
is where every such system drifts.

## Why it works

| Strategy | Tokens | % of corpus |
|---|---:|---:|
| Read everything | 790,000 | 100% |
| Read every GLANCE | 58,600 | 7.4% |
| **Read INDEX, then descend into 5** | **33,100** | **4.2%** |

The index is **155× smaller than the corpus and sufficient to choose.** Choosing is cheap; only
the chosen pay.

The scaling property is the real prize: **grow the library to 1,000 capabilities and
per-session cost barely moves.** The index grows linearly (still small); you still descend into
five. Library size becomes nearly free.

## The rule that makes or breaks it

**Each tier is a rewrite, not a truncation.**

This is the part people get wrong, and getting it wrong silently destroys the mechanism.

A GLANCE is **not** the first 40 lines of the SKILL. It answers a *different question*, so it's
a *different document*. Compare — `skills/card/SKILL.md` is 25,102 bytes; here is the entire
GLANCE:

```yaml
# GLANCE.yml — card
what: |
  Meta-skill for cards. Trading cards, playing cards,
  Magic cards, Tarot, business cards, key cards.
key_insight: "Cards are ACTIVATION TRIGGERS, not handlers."
methods:
  CREATE: "CREATE [name] TYPE [types]"
  PLAY: "PLAY [card] (IN [room])"
```

`key_insight` is the payload. *Cards trigger, they don't handle.* That's the one thing you must
know before deciding whether to descend — and **no truncation of the SKILL surfaces it**,
because it isn't a summary. It's a judgment about what a reader needs at that depth.

> **Do not auto-generate your GLANCE files.** A generated summary is a truncation with extra
> steps. It will fail exactly where it matters: at the point where the reader needed the one
> insight a summarizer wouldn't rank highly. The editorial pass *is* the mechanism.

## What goes in each tier

### INDEX entry (~35 tokens)

One line. Name, tagline, why.

```yaml
- id: code-review
  tagline: "Find bugs before the human does"
  why: "Use before any PR; catches correctness and reuse issues"
```

**Test:** can the model decide whether to open the GLANCE? That's all it needs to do.

### GLANCE (~400 tokens)

```yaml
# GLANCE.yml — code-review
what: |
  Reviews a diff for correctness bugs and simplification.
  Not a linter — it reasons about intent.
why: |
  - Catches logic errors static analysis misses
  - Flags reuse opportunities across the codebase
when:
  - '"review this PR" → REVIEW'
  - '"is this correct?" → REVIEW --focus correctness'
key_insight: "Review the diff against intent, not against style rules."
methods:
  REVIEW: "REVIEW [path] [--focus correctness|reuse]"
  EXPLAIN: "EXPLAIN [finding-id]"
```

**Test:** can the model decide "yes, this is the one" or "no, keep looking"? Include a
`key_insight` — the one non-obvious thing. That line earns the whole file.

### CARD (~1,400 tokens)

The interface. **Most reads should stop here.** Methods with signatures, parameters, triggers,
state shape, related capabilities.

```yaml
card:
  name: code-review
  invoke_when: ["Before a PR", "After nontrivial changes"]
tools:
  required: [read_file, grep]
methods:
  REVIEW:
    description: "Review a diff for bugs"
    parameters:
      path: "File or directory; defaults to working diff"
      focus: "correctness | reuse | all (default: all)"
    output: "Findings, most severe first"
triggers:
  REVIEW-DIFF:
    score: 90
    when: "User asks for review, or a nontrivial diff exists"
    method: REVIEW
```

**Test:** can the model *use* it correctly from this alone? If not, the CARD is incomplete —
don't make the reader descend for basics.

### SKILL (~2,800 tokens)

How it works. The protocol, the algorithm, edge cases, failure modes. Read when implementing,
debugging, or extending.

**Test:** could someone reimplement it from this?

### README (~1,200 tokens) — optional

Why it's like this. Rationale, alternatives rejected, history. **A human reads this. The model
mostly shouldn't.** MOOLLM ships 10 skills with no README and they're fine.

## Applying it

**Don't build this for six capabilities.** The ladder costs 4× write amplification and four
places to drift. Below ~10 units, just write them out — the mechanism costs more than it saves.

MOOLLM has 141 and needs it. You probably have six and don't.

**Build it when:** your INDEX gets long enough that reading it is itself a chore, or your
capability docs collectively exceed ~30% of your context budget.

**Start at two tiers.** GLANCE + CARD gets you most of the value. Add SKILL when a capability
grows complex enough that CARD readers keep asking "but how?". Add README when someone asks
"why is it like this?" twice.

## The cost, stated plainly

| Cost | Mitigation |
|---|---|
| 4× write amplification | Start with 2 tiers |
| 4 places to drift per unit | **Ship a validator** |
| Editorial judgment per tier | Non-negotiable — it's the mechanism |
| Index rot | Validator again |

MOOLLM's index claims 133 skills; there are 141. It drifted because nothing checks. A checker
is ~40 lines — see `template/validate.py`. There is no excuse for shipping without one.

## Checklist

- [ ] `INDEX.yml` lists every capability, one line each
- [ ] Every capability has `GLANCE.yml` with a `key_insight`
- [ ] Every capability has `CARD.yml` sufficient to *use* it
- [ ] The rule is written down: *never load a tier without the tier above*
- [ ] Tiers are rewritten, not truncated
- [ ] A validator checks conformance and index drift
- [ ] `README.md` only where someone actually asked "why?"

Next: [02-declarative-routing.md](02-declarative-routing.md)
