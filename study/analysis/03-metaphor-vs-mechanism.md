# Metaphor vs. Mechanism

The central argument. Why MOOLLM resists extraction, why that resistance is a *feature* of its
design rather than sloppiness, and how to separate the two anyway.

## The problem, stated

You read MOOLLM. You can tell something real is there. But every time you reach for the
architecture, you come back holding a monkey.

The natural conclusion is that someone built a good system and then buried it in whimsy —
that there's a clean framework under the jokes, and extraction means deleting the jokes.

**That conclusion is wrong, and getting it wrong is why extraction fails.**

## The metaphor is load-bearing

Here is the sentence that reframes everything, from `skills/no-ai-humansplaining`:

> **"Latent knowledge is prepaid; respelled knowledge is billed per call, forever.**
> **Novel jargon is a cache miss that never fills."**

Think about what "room" costs.

You write `ROOM.yml`. One token. In return, the model brings: containment, adjacency,
entry and exit, contents, occupancy, the idea that you're *somewhere* and could be
*elsewhere*, that things are *in here* and other things are *out there*, and that moving
between rooms is a discrete event worth logging.

Now write that specification yourself. It's a paragraph. And you pay for that paragraph on
**every single call, forever**, because the model doesn't remember your last conversation.

`ROOM.yml` costs one token and delivers the paragraph. Every call. Free.

That's not whimsy. That's **compression against a codebook the model already has**.

Now run the same calculation on the rest of it:

| MOOLLM writes | Model already knows | What you'd pay to respell it |
|---|---|---|
| `ROOM.yml` | Containment, adjacency, exits, contents | A paragraph, every call |
| `advertisements:` | The Sims: objects score themselves by need | A page, every call |
| `parents:` | Self/prototypes: delegation, cloning | A page, every call |
| "POSTEL" | RFC 761, be liberal in what you accept | A sentence, every call |
| "Society of Mind" | Minsky: intelligence from simple agents | A book, every call |
| "K-line" | Minsky: names activate constellations | A chapter, every call |
| "robust-first" | Ackley: survive > correct | A paper, every call |
| `CARD.yml` | HyperCard + TypeLib + Actor + trading card | Several pages, every call |

Every one of those is a pointer into pretrained weights. The names aren't decoration on the
architecture. **The names are the architecture's compression scheme.**

MOOLLM isn't a system that happens to be themed as an adventure game. It's a system that
**addresses pretrained knowledge by name**, and the adventure game is the address space it
chose — because that region of latent space is enormous, coherent, and universally present in
any model trained on the public internet.

That was a correct engineering decision.

## And that is exactly why you can't read it

Here's the trap, and it's symmetric.

**The model has the codebook pretrained. You don't. Your team doesn't. Your docs can't
assume it.**

Every K-line that's free for the LLM is a **lookup** for the human:

- The model reads `advertisements:` and knows SimAntics. You read it and think "ads?"
- The model reads `parents:` and knows Self. You read it and think "inheritance? like classes?"
- The model reads `CARD.yml` and gets HyperCard + OLE TypeLib + Actor + Smalltalk + trading
  card, simultaneously, as a coherent pun. You read it and think "…cards?"
- The model reads "the pub remembers who sat where" and gets persistent entity state across
  sessions. You read it and think this is a toy.

**The compression is asymmetric.** It's free in one direction and expensive in the other.
MOOLLM is optimized for the reader that has the codebook, and you are not that reader.

This is not a flaw in MOOLLM. **It's the cost of the thing that makes MOOLLM work.**

You are experiencing a system tuned for a different audience, and the difficulty you feel is
the tuning, not a defect.

## The resolution

If the metaphor is a compression scheme, the question isn't "how do I remove it?"

It's: **"what's the codebook, and can I swap it?"**

You can. That's the whole framework.

The mechanisms are codebook-independent. "Read cheap, then descend" doesn't care whether the
thing you're reading is a room or a service. "Units declare their own activation conditions"
doesn't care whether the unit is a bartender or a deploy script. "Identity is location" works
the same for `pub/` and `services/auth/`.

What the codebook has to be is **dense in the model's latent space and legible to your team.**

Adventure games satisfy the first and fail the second. That's the mismatch. Not wrongness —
mismatch.

So pick a codebook that satisfies both:

| Mechanism | MOOLLM's codebook | A software project's codebook |
|---|---|---|
| Unit of capability | Skill, character, object | **Component, service, module** |
| Container / scope | Room | **Package, directory, subsystem** |
| Identity | Path in the world | **Path in the repo** |
| Interface declaration | `CARD.yml` | **`CARD.yml`** (or `INTERFACE.yml`) |
| Activation conditions | Advertisement, need score | **Trigger conditions, relevance** |
| Persistent state | The pub remembers | **Session state, working set** |
| Multi-perspective | Characters debating in the pub | **Reviewer roles: security, perf, API** |
| Host adaptation | Driver | **Driver** (already neutral) |
| Standing constraints | Ambient skill | **House rules, always-on policy** |

Every right-hand term is *also* dense in latent space. The model knows what a service is, what
a package is, what a code reviewer looks for, what a session is. Those K-lines are just as
prepaid as "room" — the software-engineering region of latent space is at least as large as
the adventure-game region.

**You lose nothing and gain legibility.** That's the trade, and it's free.

## The test for whether something is mechanism or metaphor

Ask: **if I rename it, does it still work?**

- Rename `ROOM.yml` → `MODULE.yml`. Everything works. → **metaphor**
- Rename `advertisements:` → `triggers:`. Everything works. → **metaphor**
- Remove the resolution ladder and load everything at full depth. **It stops working** — you
  blow the context window at skill #15 of 141. → **mechanism**
- Remove tiering but keep the word "room." Works exactly as badly. → confirms the ladder is
  the mechanism and the word is the costume.

Apply it across the board:

| Thing | Rename test | Verdict |
|---|---|---|
| Four-tier GLANCE/CARD/SKILL/README | Remove it → context blows up | **Mechanism** |
| The word "GLANCE" | Rename to `SUMMARY.yml` → fine | Metaphor |
| Units declaring activation conditions | Remove → need a central router that knows all 141 | **Mechanism** |
| Calling them "advertisements" | Rename to `triggers` → fine | Metaphor |
| Directory = identity, marker file = interface | Remove → need a registry, a manifest, a build step | **Mechanism** |
| Calling it "Selfish COM" | Rename to "convention-based discovery" → fine | Metaphor |
| Files hold all state | Remove → can't resume, can't audit, can't correct | **Mechanism** |
| Calling `hot.yml` "hot" | Rename to `priority.yml` → fine | Metaphor |
| Always-on behavioral constraints | Remove → model reverts to default slop | **Mechanism** |
| Calling them "ambient" | Rename to "house rules" → fine | Metaphor |
| Host capability mapping + fallbacks | Remove → policy forks per host | **Mechanism** |
| Naming things the model already knows | Remove → pay respelling cost on every call | **Mechanism** ⚠️ |
| Naming them *adventure-game* things specifically | Rename to software things → fine, **and clearer** | Metaphor |

Note the last two. **"Use dense names" is mechanism. "Use *these* dense names" is metaphor.**
That distinction is the whole study in two lines. Everyone who tries to extract MOOLLM either
keeps both (and ships a framework about monkeys) or drops both (and ships a framework that
respells everything and is expensive forever).

Keep the mechanism. Swap the codebook.

## Why nobody notices

The mechanisms are boring and the metaphor is delightful.

"Read a summary before reading the whole document" is not an insight. Everyone nods. Nobody
implements it, because it sounds too obvious to be load-bearing.

But look at what it actually buys: **155×**. `INDEX.yml` is ~5,100 tokens and lets you choose
correctly among 141 skills whose full text is ~790,000 tokens. The obvious idea, applied with
discipline, is the difference between a corpus that fits and one that doesn't. It's not
clever. It's just *done consistently*, 140 times, by hand, with editorial judgment at each
tier.

That's the actual lesson and it's unglamorous: **MOOLLM's efficiency isn't a trick. It's the
obvious thing, done rigorously, at scale, without exceptions.**

The pub is what makes you keep reading long enough to notice.

Which — and this is worth sitting with — may also be deliberate. A framework nobody reads has
no users. The monkey is doing marketing work that a document titled *"Hierarchical Context
Loading Conventions for Large Language Model Agent Systems"* would not do. Don Hopkins has
been building playable systems since SimCity and pie menus; the play is the on-ramp, not the
accident.

But you are past the on-ramp. You want the machine.

## The extraction procedure

1. **Find the rename test failures.** Those are your mechanisms. There are ten
   ([02-mechanism-inventory.md](02-mechanism-inventory.md)).
2. **List every K-line the mechanism depends on.** Not the names — the *knowledge* the names
   point at. "Containment + adjacency + exits," not "room."
3. **Find a name in your domain that points at the same knowledge and is dense in latent
   space.** "Module" gives containment. "Service" gives boundaries and interfaces. "Session"
   gives temporal scope and state.
4. **Verify density.** Would a model with no context understand the term? "Service" yes.
   "Widget" no. "FooBarProcessor" absolutely not — that's a cache miss that never fills.
5. **Write the mechanism using the new codebook.** Never explain the codebook. If you have to
   explain it, it wasn't dense, and you've reintroduced the respelling cost you were avoiding.

Steps 3–5 are [framework/03-glossary.md](../framework/03-glossary.md), already done for you.

## The one thing not to take

MOOLLM's tolerance is total. `.cursorrules` is invalid YAML — two ambient skills fell out of
the map at line 208 — and nothing noticed, because nothing parses it. POSTEL says interpret
charitably; robust-first says never crash; so a structural error sits in the boot file
indefinitely, silently.

That's the flip side of "the LLM is the parser." The bug *proves the architecture works* —
the file still functions — and it *proves the architecture has no floor*. Both. At once. From
one file.

For a game, that's correct engineering: a malformed room description is better than a crash.
For a project orchestration system that touches your code, silent misinterpretation is worse
than a crash, because a crash tells you.

**Take POSTEL for input. Do not take it for your own config.** Validate the files you author.
Be liberal in what you accept from users and conservative about what you accept from
yourself. The template in [template/](../../template/) ships with a validator for exactly this
reason — the one place where the study deliberately departs from MOOLLM's design.

## Summary

- The metaphor is a **compression scheme against pretrained knowledge**, not decoration.
- It's **free for the model and expensive for you** — the asymmetry is the difficulty you felt.
- The mechanisms are **codebook-independent**. The codebook is swappable.
- **"Use dense names" is mechanism. "Use adventure-game names" is metaphor.**
- Swap in a software-domain codebook: equally dense, legible to your team, free.
- Keep tolerance for input. Add a floor under your own configuration.

Next: [04-token-economics.md](04-token-economics.md) puts numbers on the efficiency claim, or
skip to [framework/01-the-pattern.md](../framework/01-the-pattern.md) for the distilled result.
