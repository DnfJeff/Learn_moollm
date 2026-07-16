# Guide 5 · Standing Constraints

**Always-on behavioral policy.** The most immediately stealable thing in MOOLLM, and the one
with nothing to do with adventure games.

MOOLLM calls these Ambient Skills. The `no-ai-*` family is twelve of them.

## The problem

You tell the model "be concise." It's concise for two turns. Then it writes you an essay with
a bulleted summary, three caveats, and a closing paragraph about how nuanced the landscape is.

Not because it ignored you. Because "be concise" is **not checkable**. There's no test the
model can run against its own draft. It's a vibe, and vibes decay under the pressure of the
model's training distribution, which rewards thoroughness and hedging.

## The solution

**Name the failure mode.** Give it a handle. State the test.

| Vague ❌ | Named ✅ |
|---|---|
| "Don't be verbose" | `VERBOSITY` — cut adjectives, state facts |
| "Don't hedge" | `QUALIFIER-STACKING` — state confidence as a number, then claim it |
| "Don't flatter" | `UNEARNED-VALIDATION` — respect is not agreement |
| "Don't over-warn" | `CAVEAT-BOMBING` — librarians don't interrogate patrons |
| "Be accurate" | `CLAIM-LEDGER` — CONFIRM / DISPUTE / ASK, per claim, before proceeding |

A name is a K-line ([P1](../framework/02-principles.md)). The model can check a draft against
`CERTAINTY-THEATER` because that's a *pattern with a shape*. It cannot check against "be
appropriately confident."

**This is P1 applied to behavior instead of concepts.** Same mechanic, different target.

## MOOLLM's cardinal sins

The `no-ai-*` family, condensed. Steal these verbatim — the names are already domain-neutral.

**`no-ai-slop`** — syntactic + epistemic hygiene
> Sins: `HALLUCINATION` `VERBOSITY` `YES-MAN` `CERTAINTY-THEATER` `NOT-ASKING`
> `OVER-ENTHUSIASM` `BOTH-SIDESISM` `EPISTEMIC-EVASION` `UNSOLICITED-COACHING`
> Words to avoid: *pivotal, crucial, groundbreaking, legendary, iconic, nestled, delve,
> tapestry, multifaceted, nuanced, landscape, interplay*
> Fix: **Replace adjectives with facts.**
> Insight: *LLMs regress to the mean — specific becomes generic, nuanced becomes puffed.*

**`no-ai-hedging`** — epistemic hygiene
> Sins: `QUALIFIER-STACKING` `WEASEL-CERTAINTY` `PASSIVE-EVASION`
> `PROBABILITY-WITHOUT-NUMBERS` `FAUX-HUMILITY` `EPISTEMIC-COWARDICE`
> Avoid: *"perhaps it might", "could potentially", "research suggests", "it has been argued"*
> Fix: **State confidence as a number. Then make the claim plainly.**

**`no-ai-sycophancy`** — social hygiene
> Sins: `UNEARNED-VALIDATION` `AGREEMENT-WITHOUT-EVALUATION` `EMOTIONAL-MIRRORING`
> `SOFTENED-DISAGREEMENT` `PREMISE-ACCEPTANCE` `CHEERLEADING` `RETROACTIVE-AGREEMENT`
> Calibration ladder:
> - exceptional → *"This is genuinely brilliant because [specific reason]"*
> - good → *"This works well. [Specific praise]"*
> - adequate → *"This is fine."*
> - flawed → *"This has problems: [specific issues]"*
> - wrong → *"I disagree: [why]"*
> Insight: **Respect is not agreement.**

**`no-ai-moralizing`** — ethical hygiene
> Sins: `UNSOLICITED-WARNINGS` `PERFORMATIVE-ETHICS` `CAVEAT-BOMBING` `VIRTUE-SIGNALING`
> `REFUSAL-THEATER` `PARENTAL-TONE`
> Standard: **Librarians don't interrogate patrons.**
> Fix: Answer the question. ONE sentence of warning if truly needed. Then answer.

**`no-ai-humansplaining`** — context hygiene (inbound)
> Sins: `MANUAL-PASTING` `PREEMPTIVE-TUTORING` `FILE-DUMPING` `GUID-NAMING`
> Test: *Is the pointee in latent space? Point — the name is the activation. If not: spell it
> ONCE, in a file.*
> Insight: **Latent knowledge is prepaid; respelled knowledge is billed per call, forever.**

**`no-ai-gloss`** — semantic hygiene
> Sins: `EUPHEMISM-LAUNDERING` `POWER-PROTECTIVE-NEUTRALITY` `REGISTER-SWITCHING`
> Fix: **Call corruption "corruption."** Separate legal claims from functional descriptions.

## The two hard gates

Worth stealing on their own:

**`CLAIM-LEDGER`** (from `no-ai-slop`):
> For EACH user claim: **CONFIRM / DISPUTE / ASK FOR SOURCE.**
> Do NOT proceed until all claims are handled.

This is the single highest-value constraint in the repository. It fixes the most expensive
failure mode in agentic work — the model accepts a false premise and builds twenty minutes of
work on it. A ledger forces the premise check *first*, when it's cheap.

**`META-QUOTA`**:
> Max 10% of output on epistemology and strategy.

Stops the model from narrating its own process instead of doing the work.

## Where they go: the free channel

Standing constraints belong in the host's auto-loaded file — `CLAUDE.md`, `.cursorrules`, the
system prompt. That content is **prepaid**: loaded every session at zero marginal cost.

**Inline the text. Don't reference a file.**

```markdown
# ❌ Wastes the free channel — costs a round-trip to learn the rules
See policy/constraints/no-ai-slop/GLANCE.yml

# ✅ Uses it — the rule is present before the model does anything
## Standing constraints
- VERBOSITY: replace adjectives with facts. No: pivotal, crucial, delve, tapestry, nuanced.
- QUALIFIER-STACKING: state confidence as a number, then claim it plainly.
- CLAIM-LEDGER: per user claim → CONFIRM / DISPUTE / ASK FOR SOURCE. Before anything else.
```

Referencing a file from the free channel is the worst of both worlds — you've spent the free
tokens on a pointer and still have to pay for the load. MOOLLM gets this right: `.cursorrules`
inlines the GLANCE content of all twelve ambient skills directly.

## The cost

MOOLLM states it plainly:

> *"Ambient = permission to live in context rent-free; high trust — only trustworthy skills."*

Every standing constraint is a **permanent tax on every session, forever.** Twelve constraints
at ~150 tokens each is ~1,800 tokens gone before you start.

**Budget ~2,000 tokens for the free channel.** Be ruthless. **Six good constraints beat twenty
mediocre ones** — and past a certain count they start to blur, because the model is weighing
twenty simultaneous imperatives against each other instead of following six clearly.

## Writing your own

**1. Find your actual failure mode.** Not a hypothetical. Something the model did to you this
week that annoyed you.

**2. Name it.** Verb-noun, kebab-case, caps. `SCOPE-CREEP`. `PREMATURE-ABSTRACTION`.
`TEST-SKIPPING`.

**3. State the test.** How does the model check a draft against it?

**4. State the fix.** One line, imperative.

```markdown
- SCOPE-CREEP: if a change touches files outside the stated task, stop and ask.
  Test: does the diff match what was requested? Fix: revert the extras, name them, ask.
```

**5. Cut it if it doesn't fire.** A constraint you never see violated is 150 tokens of tax on
every call for nothing.

## Project-specific constraints

The `no-ai-*` family is generic. Yours shouldn't be. Real ones from real projects:

```markdown
- NO-NEW-DEPS: adding a dependency requires asking. We ship to a 200KB budget.
- MIGRATION-FIRST: schema changes need a migration in the same commit. No exceptions.
- TEST-THE-BUG: bug fixes need a test that fails before and passes after.
- NO-COMMENT-NARRATION: comments state constraints the code can't. Never what the line does.
```

These are worth more than the generic ones because they encode knowledge the model *cannot*
have — your budget, your conventions, your scars.

## Applying it

**Start here.** This is the highest value-per-hour mechanism in the whole framework. One hour
of work, immediate and obvious change in output quality, no prerequisites, no infrastructure.

**Minimum viable:** five constraints in your `CLAUDE.md`. Three generic (claim-ledger, hedging,
verbosity), two from your project.

## Checklist

- [ ] Constraints are in the free channel, **inlined**, not referenced
- [ ] Each has a NAME, a test, and a one-line fix
- [ ] Free channel is under ~2,000 tokens
- [ ] Six or fewer to start
- [ ] At least two are project-specific
- [ ] `CLAIM-LEDGER` is one of them
- [ ] You cut the ones that never fire

Next: [06-in-context-ensemble.md](06-in-context-ensemble.md)
