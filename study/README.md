# General Use Study

An extraction of the orchestration architecture inside [MOOLLM](https://github.com/SimHacker/moollm), separated from
the adventure-game world it ships in, and rewritten as a general project-orchestration
template you can teach and reuse.

MOOLLM is not modified by anything in here. This directory only reads it.

## Why this study exists

MOOLLM works. Reading it, you can feel that something real is happening — an LLM navigates a
4,489-file repository without drowning, and the mechanism is clearly deliberate rather than
lucky. But the working parts are fused to a metaphor about pubs, monkeys, and dungeon rooms,
and the two are genuinely hard to pull apart.

The hard part isn't that the metaphor is decoration you can scrape off. It's that **the
metaphor is doing real work** — just not the work it looks like it's doing. Understanding
*which* work is the whole study.

## The one-paragraph answer

MOOLLM's efficiency comes from six mechanisms that have nothing to do with adventure games:
a **resolution ladder** that lets an LLM sample a 790,000-token corpus for ~5,000 tokens;
**capability declarations** that let each unit announce its own activation conditions instead
of a central router knowing about all of them; a **host driver layer** that maps abstract
operations onto whatever tools the current environment has; **externalized state** in files
so nothing depends on hidden memory; **standing constraints** that shape every response
without being re-argued; and **in-context ensembles** that simulate multiple perspectives in
one call instead of paying network round-trips. The adventure metaphor is a **compression
scheme** layered on top: it names these mechanisms using concepts the model already knows
deeply, which makes the naming nearly free. That compression is real, and it's also exactly
what makes the architecture hard to read — because the codebook is a game, and your project
isn't.

Six is the headline count; the full inventory in
[analysis/02-mechanism-inventory.md](analysis/02-mechanism-inventory.md) itemizes **ten**
(adding boot compilation, directory-as-object, names-as-addresses, and tolerant
interpretation), and [analysis/06-capability-anatomy.md](analysis/06-capability-anatomy.md)
documents the construction standard of the capability units themselves. The canonical
numbering for all downstream documents lives in
[../curriculum/shared/CANON.md](../curriculum/shared/CANON.md).

**The framework is: keep the mechanisms, swap the codebook.**

## How to read this

Start at the top and go down. Each section assumes the one before it.

| Order | Path | What it gives you |
|---|---|---|
| 1 | [analysis/01-what-this-actually-is.md](analysis/01-what-this-actually-is.md) | A plain-language description of MOOLLM with the whimsy removed |
| 2 | [analysis/02-mechanism-inventory.md](analysis/02-mechanism-inventory.md) | Every orchestration mechanism, named and rated for portability |
| 3 | [analysis/03-metaphor-vs-mechanism.md](analysis/03-metaphor-vs-mechanism.md) | The central argument: why separation is hard, and how to do it |
| 4 | [analysis/04-token-economics.md](analysis/04-token-economics.md) | Measured numbers behind the efficiency claim |
| 5 | [analysis/05-honest-assessment.md](analysis/05-honest-assessment.md) | What's real, what's aspirational, what's broken |
| 6 | [analysis/06-capability-anatomy.md](analysis/06-capability-anatomy.md) | How a capability unit is built — the construction standard of all 141 skills |
| 7 | [framework/01-the-pattern.md](framework/01-the-pattern.md) | The distilled, domain-neutral architecture |
| 7 | [framework/02-principles.md](framework/02-principles.md) | The portable principles, stated without metaphor |
| 8 | [framework/03-glossary.md](framework/03-glossary.md) | MOOLLM term → general term translation table |
| 9 | [guide/](guide/) | Six teaching docs, one per mechanism |
| 10 | [template/](../template/) | A runnable, domain-neutral starting point |

[evidence/](evidence/) holds the measurement script and its output. Every number in the
analysis comes from `python evidence/measure.py` and you can re-run it.

## The shortest version

If you read only one thing, read
[analysis/03-metaphor-vs-mechanism.md](analysis/03-metaphor-vs-mechanism.md). It contains the
insight the rest of the study is built on:

> A metaphor that is dense in the model's latent space is free compression. "Room" costs one
> token and delivers containment, adjacency, entry/exit, and contents. Your novel jargon
> costs a paragraph of explanation on every single call, forever. MOOLLM chose adventure
> games because that codebook is enormous and free. That was correct — and it's the reason
> the architecture is nearly unreadable to a human who wants the framework instead of the
> game.
