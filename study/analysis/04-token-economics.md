# Token Economics

The efficiency claim, measured. Every number here comes from `python evidence/measure.py`
against `../moollm`. Re-run it; it's read-only.

**Caveat on method:** token counts are estimated at 4 bytes/token, a reasonable average for
English prose and YAML. Real tokenizers vary roughly 3.5–4.5 bytes/token. Every absolute
figure below could be off by ±15%. The *ratios* — which are what the argument rests on — are
insensitive to this, because the same estimator applies to both sides of every fraction.

## The corpus

```
skill directories: 141

tier            n  total KB   mean B  median B    ~tokens
GLANCE.yml    140       229     1675      1483     58,615
CARD.yml      140       743     5432      3847    190,133
SKILL.md      140      1509    11037      6628    386,290
README.md     131       607     4742      2576    155,290

entire skill corpus :    3087 KB  ~  790,329 tokens
GLANCE-only sweep   :     229 KB  ~   58,615 tokens
compression ratio   :    13.5x
INDEX.yml           :    19.9 KB  ~    5,096 tokens  (155x smaller than corpus)
```

## The central fact

**The skill corpus is ~790,000 tokens. No context window holds it.**

Not 200K. Not 1M in practice — even where a million-token window exists, filling it with a
skill library is absurd: you'd pay for all of it on every call, attention would be spread
across 141 mostly-irrelevant documents, and the model would perform *worse* than if you'd
given it the five that mattered.

So the question every agent framework must answer: **how does the model find the right
capability without reading them all?**

MOOLLM's answer is the resolution ladder, and here's what it buys.

## Cost by strategy

| Strategy | Tokens | % of corpus | Verdict |
|---|---:|---:|---|
| Load everything | ~790,000 | 100% | Impossible |
| Sweep every GLANCE | ~58,615 | 7.4% | Possible, wasteful |
| **Read INDEX, then descend** | **~5,096 + selection** | **0.6% + selection** | **The design** |
| Read INDEX + 5 skills full depth | ~33,100 | 4.2% | A working session |

The index alone is **155× smaller** than the corpus and is *sufficient to choose*. That's the
entire mechanism. Choosing is cheap; only the chosen pay.

## Cost of descent

```
 1 skills ~  5,605 tokens ( 0.7% of corpus)
 3 skills ~ 16,816 tokens ( 2.1% of corpus)
 5 skills ~ 28,026 tokens ( 3.5% of corpus)
10 skills ~ 56,052 tokens ( 7.1% of corpus)
```

A realistic session — index plus five skills at full depth — is **~33,100 tokens, 4.2% of the
corpus.** That's a comfortable fraction of a 200K window, leaving room for the actual work.

Note what this implies: **a corpus 24× larger than the context window is navigable at 4% cost
per session.** Scale the library to 1,000 skills and the index grows to ~36K tokens while
per-session cost barely moves, because you still descend into five. The ladder makes library
size nearly free.

That is the efficiency. It isn't exotic. It's a card catalogue.

## Why each tier exists

The four tiers aren't arbitrary sizes. Each answers a distinct question, and the question
determines the size:

| Tier | ~Tokens | Question | Decision it enables |
|---|---:|---|---|
| INDEX entry | ~35 | "Does this exist?" | Consider it |
| GLANCE | ~420 | "Is it relevant?" | Descend or drop |
| CARD | ~1,360 | "What can it do? How do I call it?" | **Use it** |
| SKILL | ~2,760 | "How does it actually work?" | Implement/debug it |
| README | ~1,190 | "Why is it like this?" | Modify/extend it |

The critical boundary is **GLANCE → CARD**. Glance is a filter; card is an interface. Most
reads should stop at card. `.cursorrules` states the rule:

> *"Never load a lower level without first loading the level above."*

That rule is what prevents the ladder from collapsing into "just read SKILL.md," which is the
failure mode every such system drifts toward.

## The tiers are rewrites, not truncations

This is the part that can't be automated, and it's why the ladder actually works.

`skills/card/GLANCE.yml` is 2,399 bytes. `skills/card/SKILL.md` is 25,102 bytes. The GLANCE is
**not the first 10% of the SKILL.** It's a different document, written to answer a different
question:

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

`key_insight` is the payload. One line, and it's the thing you most need to know before
deciding whether to descend — *cards trigger, they don't handle*. No truncation of SKILL.md
surfaces that line, because it isn't a summary. It's a judgment about what a reader needs at
that depth.

**Implication for tooling:** don't auto-generate your GLANCE files. A generated summary is a
truncation with extra steps, and it will fail exactly where it matters — at the point where
someone needed the one insight that a summarizer wouldn't rank highly. The editorial pass *is*
the mechanism. Budget for it.

## The free channel

`.cursorrules` is 12,656 bytes (~3,160 tokens) and Cursor loads it automatically, every
session, at no marginal cost.

MOOLLM exploits this by inlining ambient-skill GLANCE content directly into it, rather than
referencing 12 separate files:

```
12 ambient skills × ~420 tokens (GLANCE each) = ~5,040 tokens + 12 file reads
inlined into .cursorrules, condensed          = ~1,800 tokens + 0 file reads
```

Roughly a **3× saving plus the elimination of 12 round-trips**, and the content arrives before
the model does anything. Every host has such a channel — `.cursorrules`, `CLAUDE.md`, the
system prompt. Content there is prepaid. Put your hot, always-needed policy in it and nothing
else.

**The rule:** if you need it every session, it goes in the free channel. If you need it
sometimes, it goes in the ladder. Confusing these is the most common context-budget mistake.

## Where the corpus is bloated

Honest accounting cuts both ways. `SKILL.md` files average 11 KB and total **386,000 tokens —
49% of the corpus.** Some are extraordinary (`skills/card/SKILL.md`, 25 KB, genuinely deep).
Many are essays where a spec would do.

The `README.md` tier adds another 155,000 tokens (20%) for "why is it like this," and 10
skills ship without one — apparently no worse for it.

A tighter corpus would be roughly:

| Tier | Current | Tightened | Change |
|---|---:|---:|---|
| GLANCE | 58,615 | 58,615 | keep |
| CARD | 190,133 | 190,133 | keep |
| SKILL | 386,290 | ~200,000 | cut essays |
| README | 155,290 | ~60,000 | merge into SKILL |
| **Total** | **790,329** | **~509,000** | **−36%** |

This doesn't change per-session cost much — you only load five skills either way — but it
matters for maintenance, drift, and the honesty of the thing. The ladder is so effective at
hiding cost that it removes the pressure to be concise at depth. **A good mechanism can
subsidize bad discipline.** Worth watching for in your own implementation.

## What the numbers don't show

Three limits on this analysis, stated plainly:

**1. No measurement of retrieval quality.** These numbers prove the ladder is *cheap*. They do
not prove the model *picks the right skill* from an index entry. That's the question that
actually matters, and answering it needs an eval harness MOOLLM doesn't have. A cheap system
that chooses wrong is worse than an expensive one that chooses right.

**2. No comparison to alternatives.** Vector search over the corpus might beat the hand-written
ladder on both cost and accuracy, and would eliminate the 4× write amplification. Nobody has
run that comparison. The ladder's real advantage may be that it's *legible and editable* — you
can fix a bad GLANCE; you can't fix an embedding — rather than that it's optimal.

**3. Estimated tokens.** ±15% on absolutes, as noted. Ratios hold.

## Summary

| Claim | Verdict |
|---|---|
| Corpus far exceeds context (790K tokens) | ✅ Measured |
| Index is 155× smaller and sufficient to choose | ✅ Measured |
| Realistic session costs ~4% of corpus | ✅ Measured |
| Ladder makes library size nearly free | ✅ Follows from the above |
| Tiers are rewrites, not truncations | ✅ Verified by inspection |
| Free channel eliminates ~12 reads/session | ✅ Measured |
| Model *chooses correctly* from the index | ❓ **Untested** |
| Ladder beats vector search | ❓ **Untested** |

The efficiency is real, measurable, and mostly it's a card catalogue applied with unusual
discipline. The unproven part is whether the catalogue's *entries* are good — and that's the
part that would decide whether to adopt this over embeddings.

Next: [05-honest-assessment.md](05-honest-assessment.md).
