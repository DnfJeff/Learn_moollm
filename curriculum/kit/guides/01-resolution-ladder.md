# Guide 1 · Resolution ladder

> **Tier:** Practitioner · deeper: [spec/MECHANISMS.md#m1](../../spec/MECHANISMS.md#m1--resolution-ladder) · plainer: [onramp/THE-TEN-IDEAS.md#m1](../../onramp/THE-TEN-IDEAS.md#m1--resolution-ladder)

**The symptom.** Your agent reads whole files — often whole directories — to answer
questions a table of contents could have answered. Long sessions start with a minute of
file-dumping. Your library of prompts and procedures has grown past what you can paste in,
so the agent either gets all of it (bloat) or none of it (amnesia).

**What you build.** Each capability written at multiple sizes, plus an index above them all,
plus one reading rule.

## The files

Per capability, cheapest first — each answers **one** question:

| File | ~Tokens | Question | Reader should |
|---|---:|---|---|
| `INDEX.yml` entry | 35 | Does it exist? | consider it |
| `GLANCE.yml` | 400 | Is it relevant *right now*? | descend or drop |
| `CARD.yml` | 1,400 | How do I call it? | **use it — stop here** |
| `SKILL.md` | 2,800 | How does it work inside? | implement / debug |
| `README.md` | 1,200 | Why is it like this? | modify / extend |

The rule, verbatim in your boot file:

> **Read the cheapest tier that answers your question. Never load a tier without first
> loading the tier above it.**

And the discipline that makes the whole thing worth building:

> **Each tier is a rewrite, not a truncation.** A GLANCE is not the first 40 lines of the
> SKILL — it's a different document answering a different question. Its `key_insight:` line
> should be something *no truncation would surface*. Do not auto-generate these files; a
> generated summary is a truncation with extra steps, and it drops exactly the one line that
> mattered. (This is principle P3, and it's the part that can't be delegated.)

Start from the annotated skeleton: `capabilities/example-capability/` in the
[template](../../../template/capabilities/example-capability/).

## Why this is worth the writing

Measured on the origin corpus: 141 capabilities ≈ 790K tokens — unloadable. The index is
~5K tokens (**155× smaller**) and sufficient to *choose*. A working session (index + five
capabilities at full depth) costs ~33K tokens: 4% of the corpus, and that fraction barely
moves as the library grows, because you still only descend into five. Choosing is cheap;
only the chosen pay.

## Verify it's working

1. Fresh session. Ask something one capability should answer.
2. Watch the reads: INDEX → one or two GLANCEs → one CARD → **stop**.
3. Ask a "how does it work inside" question; *now* it should read SKILL.md — and not before.
4. Run `python validate.py` — tier presence, tier budgets, and index count are checked
   mechanically.

## The traps

- **Ladder collapse** — the model "just reads SKILL.md." Cause: the rule isn't in the boot
  file, or your CARDs are incomplete so readers *must* descend. Fix the CARD, not the model.
- **Glance inflation** — GLANCEs growing until they're CARDs. The validator's size budgets
  exist for this; respect the warning.
- **Tier drift** — four files per unit is four places to desync. The origin drifted (index
  claimed 133 units; 141 existed). The fix costs one second: `validate.py` in CI.
- **Building it too early** — under ~10 capabilities, the index answers nothing the
  directory listing didn't. Skip the ladder until choosing is actually hard.
