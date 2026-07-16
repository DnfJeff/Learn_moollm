# code-review

How reviewing actually works. Read this to change the protocol, not to run it — `CARD.yml` is
sufficient to run it.

## The protocol

### 1. Establish intent, before reading the diff

This is the step that separates a review from a lint, and it's the step people skip.

Read, in order:
- The PR description or the user's stated goal
- The tests — they encode intended behavior more honestly than prose
- The surrounding code — what conventions does this file already follow?

**Without intent you cannot find correctness bugs.** A correctness bug is code that does
something other than what it's meant to do. No intent, no "meant to," no bug — just style
opinions wearing a badge.

### 2. Read the diff against that intent

For each hunk:
- Does it do what the intent says?
- What inputs make it do something else?
- What does it assume that the caller doesn't guarantee?
- Does this already exist elsewhere in the repo? (`search` before claiming novelty)

### 3. Verify each finding before reporting it

For every candidate finding, write the failure scenario: **concrete inputs or state → wrong
output or crash.**

If you can't write that scenario, **it isn't a finding.** It's a preference. Drop it.

This single gate is what keeps a review from degenerating into noise.

### 4. Report, most severe first

Each finding: `file:line`, one-sentence summary, the failure scenario.

**Never pad.** One real bug beats six nits. Six nits teach the reader to skim you, and then
they miss the seventh, which was real.

## Edge cases

| Case | Behavior |
|---|---|
| No diff | Say so. Don't review the whole repo uninvited (`SCOPE-DRIFT`). |
| Diff is only tests/docs | Say so and stop — nothing to exercise. |
| Intent unclear | **Ask.** Reviewing against a guessed intent produces confident nonsense. |
| Tests exist and fail | Report that first. It outranks everything you'd find by reading. |
| No `terminal` tool | Read the tests instead of running them. Say you didn't run them. |
| Huge diff | Review the highest-risk files, say which you skipped. Never pretend coverage. |

## Failure modes

Named, so they're checkable:

- **`PADDING`** — inventing findings to look thorough. Gate: could you write the failure
  scenario? No → drop it.
- **`SCOPE-DRIFT`** — reviewing code outside the diff. Gate: is this line in the diff?
- **`STYLE-POLICING`** — reporting preferences as defects. Gate: does it *fail*, or do you just
  dislike it?
- **`INTENT-GUESSING`** — reviewing against an assumed goal. Gate: did you read the PR
  description? If none exists, ask.
- **`FALSE-COVERAGE`** — implying you reviewed everything when you sampled. Gate: say what you
  skipped.

## Effort levels

| Level | Behavior |
|---|---|
| `low` | Only findings you'd bet money on. Few, high confidence. |
| `medium` | Confident findings + strong suspicions, labeled as suspicions. |
| `high` | Broad. May include uncertain findings — **label them uncertain**, don't launder them. |

The label is the contract. An uncertain finding reported as certain is worse than not
reporting it, because it spends the reader's trust.

## Why it's built this way

**Why intent-first?** Because "correctness" is meaningless without a spec, and in most repos
the spec is scattered across a PR description, a test file, and the conventions of the code
around it. A reviewer who reads only the diff is a linter with extra latency.

**Why the failure-scenario gate?** It's the cheapest available filter against the model's
strongest bias in review tasks — the pull toward producing *output* rather than producing
*findings*. Requiring a concrete failure makes padding structurally impossible: you cannot
fabricate a failure scenario for a preference without noticing you're doing it.

## Related

- [example-capability](../example-capability/) — the annotated skeleton
- [guide/02-declarative-routing.md](../../../study/guide/02-declarative-routing.md) — why the security
  trigger is a hint and the security *gate* has to be CI
