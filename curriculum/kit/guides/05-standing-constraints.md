# Guide 5 · Standing constraints

> **Tier:** Practitioner · deeper: [spec/MECHANISMS.md#m5](../../spec/MECHANISMS.md#m5--standing-constraints) · plainer: [onramp/THE-TEN-IDEAS.md#m5](../../onramp/THE-TEN-IDEAS.md#m5--standing-constraints)

**The symptom.** You correct the same behaviors every session: padding, hedge-stacking,
agreeing with your bad ideas, lecturing before answering, touching files outside the task.
The corrections work — until the next session forgets them.

**What you build.** A short set of always-active rules in your boot file, each one **naming
the failure mode** it forbids. This is the highest value-per-hour mechanism in the kit: one
hour, permanent effect.

## Why naming is the mechanism

"Don't be verbose" is unusable feedback — the model already believes it's being concise.
`VERBOSITY` as a *named pattern with a test* is checkable:

> **`VERBOSITY`** — Replace adjectives with facts. Never: *pivotal, crucial, groundbreaking,
> delve, tapestry*. Test: does every sentence carry information the reader didn't have?

The name gives the model (and you) a handle. "That's `CAVEAT-BOMBING`" lands in three words;
a paragraph of "please be more direct" doesn't. Every constraint therefore has three parts:
**NAME · rule · test.**

## The files

The template's `AGENT.md` ships six generic constraints worth keeping verbatim —
`CLAIM-LEDGER` (for each user claim: confirm, dispute, or ask for a source — *before*
building on it), `VERBOSITY`, `QUALIFIER-STACKING`, `UNEARNED-VALIDATION`, `CAVEAT-BOMBING`,
and `META-QUOTA` (max 10% of output on process narration).

Then the section that matters more — **yours**:

```markdown
## Project constraints

**`NO-NEW-DEPS`** — Adding a dependency requires asking first. State size and what it replaces.

**`SCOPE-CREEP`** — A change touching files outside the stated task stops and asks.
Test: does the diff match what was requested?

**`TEST-THE-BUG`** — A bug fix ships with a test that fails before and passes after.
```

Project constraints beat generic ones because they encode what the model cannot know: your
budget, your conventions, your scars. When you correct the agent for the second time about
the same thing — that's a constraint announcing itself. Name it and move it in.

Two placement rules:

1. **Always-on lives in the boot file, inlined** — not in twelve separate files the agent
   must remember to load. (That's [guide 6](06-boot-compilation.md).) In library form, an
   always-on trigger is just `when: always` plus a `resolution:` saying how much stays
   loaded — same routing mechanism as everything else, no special case.
2. **Budget the set.** Every constraint is a permanent tax on every call. The template's
   boot-file budget is ~2,000 tokens total; the validator warns when you blow it. A
   constraint that stopped earning its rent gets evicted like anything else.

## Verify it's working

1. Bait each constraint once. Make a claim that's wrong (`CLAIM-LEDGER` should dispute it,
   not build on it). Propose something mediocre ("`UNEARNED-VALIDATION`" should get you
   "this is fine," not "great idea!"). Ask for a risky-sounding but legitimate task
   (`CAVEAT-BOMBING`: one warning sentence max, then the answer).
2. The stronger test is silence: a week later, are you still re-issuing any correction? If
   yes, that correction isn't a constraint yet — or it's phrased as a virtue instead of a
   named, testable rule.

## The traps

- **Constraint bloat** — the set grows until it crowds out work. Rent is due every call.
- **Values essays** — "be rigorous and thoughtful" is not a constraint; it has no test.
- **Guarantee confusion** — these create strong tendencies, not enforcement. `SCOPE-CREEP`
  makes out-of-scope edits rare; a `PreToolUse` hook makes them impossible. Know which one
  each rule needs (P1).
