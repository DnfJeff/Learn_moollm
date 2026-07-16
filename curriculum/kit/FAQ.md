# FAQ — failure smells and fixes

> **Tier:** Practitioner · deeper: [spec/WHITEPAPER.md#5-limits--carried-forward-intact](../spec/WHITEPAPER.md) · plainer: [onramp/THE-TEN-IDEAS.md](../onramp/THE-TEN-IDEAS.md)

Symptoms first, because that's how you'll arrive here. Each smell names the broken
mechanism and the fix.

## Smell 1 · "The agent reads everything anyway"

The ladder exists but the model globs directories or jumps straight to `SKILL.md`.

**Causes, in observed order:** (a) the reading rule isn't in the boot file — it's in a file
the model has to *choose* to read, which defeats it; (b) your CARDs are incomplete, so
readers *must* descend for basics — fix the CARD, not the model; (c) the index entries are
too vague to choose from ("misc helpers" chooses nothing).
**Check:** [guide 1](guides/01-resolution-ladder.md) verification steps.

## Smell 2 · "It picked the wrong capability" / "it never picks the new one"

**Causes:** `when:` describes a topic, not a situation; score inflation flattened the
rankings; the index line's tagline doesn't match how you actually ask. Remember the honest
limit: this is soft routing by a model reading prose — if a wrong route is *costly*, the
route belongs in code (P2), not in a better-worded trigger.
**Check:** [guide 2](guides/02-declarative-routing.md), rules 1–2.

## Smell 3 · "The working set describes last Tuesday"

State drift — the most common failure in practice, and the one that makes everything else
lie. **Fix:** the boot file rule is "update at task boundaries," but the durable fix is
habit-shaped: you glance at `working-set.yml` when you'd glance at a whiteboard. A stale
working set is worse than none; if you won't maintain it, shrink it (task line only) rather
than let it rot at 30 lines.

## Smell 4 · "My boot file is 6,000 tokens and growing"

Boot bloat. Everything there is taxed on every call. **Fix:** the free-channel rule —
inline only what *every* session needs; pointers for the rest; evict on the recompile pass
([guide 6](guides/06-boot-compilation.md)). `validate.py` warns past budget.

## Smell 5 · "It keeps violating a constraint that's right there in the file"

**Causes, in order:** the constraint is phrased as a virtue ("be careful with scope")
instead of NAME · rule · test; the boot file is so bloated the constraint is drowning
(smell 4); the behavior needs a guarantee, not a tendency — some rules simply need a hook
or a code check, and no phrasing fixes that (P1).
**Check:** [guide 5](guides/05-standing-constraints.md).

## Smell 6 · "The panel agreed with itself five times"

Persona theater / herd behavior. **Fix:** perspectives declared as *what they optimize for
and what they hate*, not job titles; output format "disagreements first"; and if the task
was independent verification, no prompt fixes it — that's the separate-calls case
([guide 7](guides/07-in-context-ensemble.md), the bright line).

## Smell 7 · "Something was broken for weeks and nothing noticed"

The tolerance trap: the model absorbed your malformed config silently. This is the
signature failure of the whole paradigm, and the origin system shipped it (invalid boot
YAML, two constraints silently dropped, duration unknown). **Fix:** `validate.py` in CI,
today. Tolerance is for input; strictness is for what you authored
([guide 10](guides/10-tolerant-interpretation.md)).

## Smell 8 · "Maintaining the tiers is becoming a job"

Either you built the ladder before ~10 capabilities (tear it down; that's a supported
move — see [RETROFIT](RETROFIT.md) level guidance), or your deep tiers are bloating.
The origin's SKILL tier grew to 49% of its corpus because the ladder hides depth cost so
well — **a good mechanism subsidizes bad discipline.** The validator's budgets are the
tripwire; essays go in README or nowhere.

## Smell 9 · "New teammates ask what our terms mean"

You've grown a private codebook — the exact disease the origin has, where the mechanisms
hide behind pub-and-monkey vocabulary. **Fix:** the glossary test in
[guide 9](guides/09-names-as-addresses.md): every term is standard, or defined once in
`GLOSSARY.yml`, or renamed to something prepaid.

## Honest questions

**Is any of this enforced?** No. On a generic host every rule here is a convention the
model reads and (reliably, not perfectly) follows — that's the designed floor (P1). Hooks
and scripts provide guarantees where you need them. Decide per rule; don't discover the
difference in an incident.

**Why not just RAG the capability library?** Maybe! Nobody has run the comparison
(stated plainly in [EVIDENCE](../spec/EVIDENCE.md)). What the ladder gives you that
embeddings don't: you can *read* the index and *fix* a bad entry with an editor. The two
also compose — nothing stops you retrieving over well-laddered files.

**Does this lock me into one vendor or tool?** The opposite — it's plain files plus one
optional Python script. The driver layer exists precisely so the same workspace moves
between hosts. Worst case, you delete `.agent/` and `capabilities/` and you've lost
nothing but the files themselves.

**Where did this come from?** [MOOLLM](https://github.com/SimHacker/moollm), by Don Hopkins — see
[PROVENANCE](../spec/PROVENANCE.md). The origin ships these mechanisms inside a
text-adventure world; the kit is the same nervous system without the costume.
