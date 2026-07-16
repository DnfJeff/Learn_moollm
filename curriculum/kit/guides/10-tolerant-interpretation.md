# Guide 10 · Tolerant interpretation

> **Tier:** Practitioner · deeper: [spec/MECHANISMS.md#m10](../../spec/MECHANISMS.md#m10--tolerant-interpretation) · plainer: [onramp/THE-TEN-IDEAS.md#m10](../../onramp/THE-TEN-IDEAS.md#m10--tolerant-interpretation)

**The symptom.** Your agent setup is brittle: a missing state file derails the session, a
typo'd command gets a lecture instead of the obvious interpretation, a half-filled YAML
field crashes a procedure. You're writing input validation for a reader that doesn't need
it — and skipping validation where you *do* need it.

**What you build.** An asymmetric policy — extremely tolerant inbound, strict outbound,
self-repairing in the middle — plus the one validator script that keeps tolerance from
becoming blindness.

## The three rules

**1. Liberal in.** The model is a robust parser; let it be one. Typos, missing fields,
approximate commands, "the auth thing" — interpret intent and proceed. Ask only when the
ambiguity is *worth* resolving (the interpretations genuinely diverge and the action is
consequential). You do not need to write a parser; you need to stop writing lectures.

**2. Conservative out.** Everything the agent emits — YAML, code, reports — is strictly
well-formed. Tolerance is for *other people's* input, never for your own output.

**3. Repair, don't crash.** Missing state file → create the minimal stub, log the repair,
continue. Priority order under any failure: **survive → heal → function → optimize.**
Declare the stubs in your boot file so repair is deterministic:

```yaml
# Minimal stubs — create if missing, log the repair in session-log.md
working-set.yml: |
  focus: { task: "(unknown — repaired; ask the user)" }
  active_files: []
hot.yml: |
  keep: []
session-log.md: |
  # Session log (recreated by repair — prior log missing)
```

## The line the origin didn't draw (don't skip this)

Tolerant interpretation has a failure mode, and the origin system is the proof: its boot
file was **structurally invalid YAML for an unknown period** — two standing constraints had
silently fallen out of the config — and nothing noticed, *because* the only reader was a
model that charitably absorbed the error. Tolerance for input is a feature. Tolerance for
**your own config** is an absence of tests.

So draw the line explicitly:

| What | Policy |
|---|---|
| User input, chat commands, other people's files | Interpret charitably; proceed |
| Missing optional state | Repair with a stub; log it; proceed |
| **Config you authored** (boot file, CARDs, index) | **Validate mechanically. Malformed → stop and say so.** |
| Money, auth, deletion, anything irreversible | Deterministic checks in the code path — never model judgment (P2) |

`validate.py` (ships with the [template](../../../template/)) is that line,
implemented: YAML validity, tier presence and budgets, index-count drift, boot-file budget.
Run it in CI. It exists *because of* the incident above.

## Verify it's working

1. Delete `.agent/working-set.yml`; start a session. Expected: stub created, repair logged,
   session proceeds, agent asks about the unknown task. No drama.
2. Type a sloppy command ("run the revew on teh diff"). Expected: it runs the review. No
   meta-commentary about the typo.
3. Break a CARD's YAML on purpose. Expected: `validate.py` fails loudly in CI — and if the
   agent reads the broken file mid-session, it *says so* instead of silently absorbing it.
4. Confirm test 3's failure was loud and test 1's wasn't. The asymmetry is the mechanism.

## The traps

- **Silent absorption** — the model papering over corruption you needed to see. The
  validator is the countermeasure; there is no prompt-side fix.
- **Repair loops** — regenerating a stub some other process keeps deleting. Repair logs
  exist so the loop becomes visible; read them.
- **Charity toward yourself** — quoting Postel to excuse unvalidated config. Postel's law
  is about protocol peers, not about skipping your own tests.
