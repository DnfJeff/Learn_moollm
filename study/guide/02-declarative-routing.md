# Guide 2 · Declarative Routing

**Each unit declares when it's relevant. Nothing central knows the catalogue.**

MOOLLM calls these Advertisements, from The Sims. It's the mechanism that makes the library
extensible.

## The problem

You have a growing library. Something must decide which capability applies to a request.

The obvious answer is a router:

```python
def route(request):
    if "review" in request:      return code_review
    elif "deploy" in request:    return deploy
    elif "test" in request:      return run_tests
    # ... 138 more
```

This fails in a specific, predictable way: **the router must know everything.** Every new
capability edits the router. The router becomes the bottleneck, the merge conflict, and the
thing nobody wants to touch. Knowledge that belongs to a capability lives somewhere else.

## The solution

Invert it. Each capability declares its own activation conditions:

```yaml
# capabilities/code-review/CARD.yml
triggers:
  REVIEW-DIFF:
    score: 90
    when: "User asks for review, or a nontrivial diff exists"
    method: REVIEW

  REVIEW-SECURITY:
    score: 95
    when: "Diff touches auth, crypto, or input parsing"
    method: REVIEW
    params: { focus: security }
```

Selection becomes: **collect all triggers in scope, score against context, take the top.**

The router knows nothing. The things that exist know when they matter.

## Why this is the right shape

This is the architecture that let The Sims ship expansion packs and let players build objects
the developers never imagined. `skills/advertisement/SKILL.md` names it exactly:

> - **User-created objects** — anyone could make new furniture, appliances, characters
> - **Expansion packs** — just drop in new objects with their advertisements
> - **No code changes** — objects self-describe their behaviors

A refrigerator knows it offers food. A bed knows it offers sleep. The Sim chooses from what's
advertised nearby. **No central AI knows the catalogue** — which is why the catalogue can grow
forever.

| | Central router | Declarative triggers |
|---|---|---|
| Add a capability | Edit the router | Add a directory |
| Knowledge location | One file knows all | Each unit knows itself |
| Merge conflicts | Constant | None |
| Third-party extension | Fork the router | Drop in a directory |
| Complexity | O(n) in one place | O(1) per unit |

## The anatomy of a trigger

```yaml
TRIGGER-NAME:            # A K-line. Verb-first, kebab-case, describes the situation.
  score: 90              # Base relevance, 0-100.
  when: "condition"      # Prose. The model evaluates it.
  method: METHOD         # What to invoke.
  params: {}             # Optional bound arguments.
```

**On `score`:** it's a *base* relevance, adjusted by context. Rough bands that work:

| Score | Meaning |
|---|---:|
| 90–100 | Almost certainly what the user wants |
| 70–89 | Strong candidate |
| 40–69 | Plausible; offer it |
| 1–39 | Long shot; mention only if nothing better |

Don't over-tune these. The model reads them as hints, not as arithmetic. Which brings us to the
limit.

## The honest limit

**Nothing evaluates `when:`.** There is no engine, no predicate parser, no expression
evaluator. The model reads prose and forms a judgment.

```yaml
when: "Diff touches auth, crypto, or input parsing"   # This is a suggestion.
```

That means:

- ✅ Great for **soft routing** — "which of these 20 things is probably relevant?"
- ✅ Great for **discovery** — "what could I do here?"
- ❌ Wrong for **correctness** — "must this security check run?"
- ❌ Wrong for **ties that matter** — nothing deterministically resolves two 90s

**The rule:** if the wrong choice is merely inefficient, declarative routing is perfect. If the
wrong choice is *incorrect*, put a real check in the code path. Don't ask a relevance score to
enforce an invariant.

MOOLLM never states this boundary. It's the most important caveat on the mechanism.

## Writing good triggers

**Name the situation, not the capability.**

```yaml
# Bad — restates the name
CODE-REVIEW:
  when: "when code review is needed"

# Good — describes the world
REVIEW-BEFORE-MERGE:
  when: "A PR is open and hasn't been reviewed"
```

The trigger name is a K-line. `REVIEW-BEFORE-MERGE` activates a situation the model recognizes.
`CODE-REVIEW` activates nothing beyond the noun.

**Be specific in `when:`.** The model is reading it to make a judgment. Give it something to
judge.

```yaml
when: "when relevant"                                    # ❌ useless
when: "Diff touches auth, crypto, or input parsing"      # ✅ judgeable
```

**One trigger per situation, not per method.** Triggers answer "when might I want this?" —
methods answer "what can it do?" A capability with six methods might have two triggers.

## Ambient triggers

A trigger with `when: always` is a standing constraint — it's always active, shaping every
response:

```yaml
AMBIENT:
  score: 100
  when: always
  scope: session
  resolution: card-only    # how much to keep loaded
```

`resolution` matters: it declares how *much* of the capability to keep in context. Always-on at
full depth would eat your budget. See
[05-standing-constraints.md](05-standing-constraints.md).

## Applying it

**Don't build this for six capabilities.** With six, the model reads the index and picks
correctly with no help. Triggers are overhead until choosing is actually hard.

**Build it when:** your index is long enough that the model starts picking wrong, or you want
third parties to extend the library without touching your code.

**The migration:** start with an index and taglines only. When you notice the model
consistently missing a capability, add a trigger to *that* capability. Let triggers grow where
they're earned, rather than writing 141 of them upfront.

## Checklist

- [ ] Triggers live on the capability, never in a central router
- [ ] Trigger names describe *situations*, not capability names
- [ ] `when:` is specific enough to be judged
- [ ] Scores are rough bands, not tuned numbers
- [ ] Correctness-critical decisions have a **real check**, not a trigger
- [ ] Ambient triggers declare a `resolution` so they don't eat the budget
- [ ] Adding a capability requires touching exactly one directory

Next: [03-host-drivers.md](03-host-drivers.md)
