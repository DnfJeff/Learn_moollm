# example-capability

**TIER 3 of the ladder.** Budget ~2,800 tokens. Answers: *"How does it actually work?"*

Read when implementing, debugging, or extending — **not** when merely using. If you're just
calling it, `CARD.yml` was enough and you should have stopped there.

This tier is optional. Write it when `CARD.yml` readers keep asking "but how?"

---

## The protocol

Describe the actual procedure. Steps, in order, with the reasoning that isn't obvious from the
step list.

1. **Read the target.** Prefer the working set if no target is given.
2. **Do the thing.** Explain the non-obvious part — the reason someone reimplementing this
   would get it wrong on the first try.
3. **Report.** Most severe first. Never pad to reach a count.

## Edge cases

Where it gets hard. This is the section that earns the tier — anyone can guess step 1.

| Case | Behavior |
|---|---|
| Target doesn't exist | Note it, continue with the working set. Don't crash (P9). |
| Target is empty | Return nothing. Say nothing. Don't invent findings to seem useful. |
| Ambiguous target | Ask. Don't guess when the guess is expensive. |

## Failure modes

What goes wrong, named so it's checkable:

- **`PADDING`** — inventing low-value findings to hit a count. If there's one finding, report
  one.
- **`SCOPE-DRIFT`** — reviewing things nobody asked about. Stay in the diff.

## Why it's built this way

Short rationale, or point at `README.md` if it's long. If you have nothing to say here, delete
the section — an empty "why" is worse than no "why."

## If this capability produces instances

Some capabilities are **factories**: they ship a template (`INSTANCE.md.tmpl`) and a small
starter catalog of worked instances (`examples/`). Instantiation copies the template *out*
— behavior stays here in the prototype; state lives in the copies. Don't accumulate live
instances inside the capability; the catalog holds curated examples only.

And remember the cost dial before creating files at all: *mention* the capability by name →
use it in-conversation → embed its output in an existing doc → full instantiation. Start
cheap.

## The manifest rule

This file references **every** file in the unit, regardless of nesting — scripts,
templates, examples, all of it. A reader of SKILL.md never hunts the directory tree to
discover what exists.

## Related

- [code-review](../code-review/) — the worked example
