# Guide 2 · Declarative routing

> **Tier:** Practitioner · deeper: [spec/MECHANISMS.md#m2](../../spec/MECHANISMS.md#m2--declarative-routing) · plainer: [onramp/THE-TEN-IDEAS.md#m2](../../onramp/THE-TEN-IDEAS.md#m2--declarative-routing)

**The symptom.** Somewhere — your boot file, a dispatcher prompt, your own head — lives a
growing list of "when the user asks X, use Y." Every new capability means editing that list.
It's O(all-knowledge-in-one-place), it drifts, and it's already wrong.

**What you build.** Nothing central. Each capability carries its own `triggers:` block; the
agent collects them, scores against the situation, picks the best. Adding a capability =
adding a directory + one index line. **Nothing else changes.** (This is why The Sims could
ship expansion packs: the object carries its own behavior.)

## The files

In each `CARD.yml`:

```yaml
triggers:
  REVIEW-DIFF:
    score: 85            # 90-100 near-certain · 70-89 strong · 40-69 plausible · <40 long shot
    when: "A diff or PR is under discussion and correctness matters"
    method: REVIEW

  EXPLAIN-FINDING:
    score: 60
    when: "User questions a previous review finding"
    method: EXPLAIN
```

Rules that keep it healthy:

1. **`when:` describes the *situation*, specifically enough for a model to judge it.**
   "User needs help" routes everything; "a diff is under discussion and correctness
   matters" routes one thing.
2. **Scores are baselines, not auctions.** If every capability claims 95, you've rebuilt
   "no routing" with extra YAML. Calibrate against the scale above; the validator can't
   check judgment, so this one's on you.
3. **Preconditions gate visibility.** If a capability can't run here (missing tool, wrong
   host), it shouldn't enter the choice at all — note required tools in the CARD and let
   the driver's capability list rule it out.
4. **A trigger with `when: always` is a standing constraint** — same mechanism, no special
   case. See [guide 5](05-standing-constraints.md).

## The honest limit (put a real check where it matters)

Nothing *evaluates* `when:`. The model reads prose and judges. That's soft routing — good
for "which of these 20 is probably right?", **wrong** for "must this security check run?"
For anything where a wrong route has real cost, put a deterministic check in the code path
(principle P2). The origin states this limit itself; don't discover it in production.

## Verify it's working

1. Add a new capability with a well-written trigger. **Touch nothing else** but the index
   line.
2. Fresh session; present the triggering situation *without naming the capability*. It
   should route there.
3. Present a near-miss situation. It should *not* route there. If it does, your `when:` is
   describing a topic, not a situation.

## The traps

- **Index-as-router regression** — per-capability dispatch logic creeping into `INDEX.yml`
  ("use this when…" paragraphs). The index says what exists; the CARD says when it applies.
- **Score inflation** — see rule 2.
- **Trigger sprawl** — a capability with nine triggers is three capabilities, or is scoped
  by topic instead of situation.
