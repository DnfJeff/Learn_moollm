# Guide 6 · In-Context Ensembles

**Simulate multiple perspectives in one call instead of N API round-trips.**

MOOLLM calls this SPEED-OF-LIGHT. It contains the sharpest technical claim in the repository
and an unresolved caveat you have to resolve yourself.

## The problem, part one: single-voice output is an average

From `constitution-core.md` §0, which is the best thing in the kernel:

> Traditional chat (one user ↔ one assistant) produces **the statistical center of all possible
> viewpoints**.
>
> When asked a complex question, a single-voice LLM gives you the most *likely* answer:
> hedged and cautious, genre-conventional, hidden assumptions invisible, outlier perspectives
> smoothed away.
>
> **The centroid of a cloud tells you nothing about the cloud's shape.**

That's the case for ensembles in three lines. One voice gives you the mean. You often want the
distribution — especially for decisions, where the outlier objection is the whole value.

## The problem, part two: the boundary is expensive

The obvious way to get an ensemble is five agents, five API calls, orchestrated. MOOLLM's
critique of this, from `skills/speed-of-light/GLANCE.yml`:

> INSIDE LLM: high-dimensional vectors, precise, instant
> AT BOUNDARY: serial tokens, lossy, glacial
>
> Tokenization destroys precision. Detokenization adds noise.
> Work with vectors at speed of light. **Delay tokenization.**

It names the anti-pattern: **Carrier Pigeon Protocol.**

> *Writing on toilet paper with crayon, sending by pigeon, when you could navigate idea-space
> at speed of light.*

The point is real. When agent A "tells" agent B something, A's rich internal state is squeezed
into a serial token stream, shipped over a network, and re-expanded by B into *different*
internal state. Every hop is lossy **and** slow. If A and B are the same model, you paid twice
— latency and precision — to simulate a separation that never needed to exist.

## The solution

Do the ensemble **inside one call**.

```markdown
Convene a review of this migration plan. Simulate four roles, each arguing its own priority:

- SECURITY: what breaks confidentiality or integrity?
- PERFORMANCE: what gets slower, and by how much?
- MAINTAINER: what will hurt in six months?
- SKEPTIC: what is the strongest case for not doing this at all?

Let them disagree explicitly. Where two roles conflict, state the conflict rather than
splitting the difference. Then, as an independent evaluator, score each objection for
severity and give a recommendation.
```

One call. Four perspectives. No network. Full coherence — the model holds all four at once and
knows what each said, exactly, because it's all one forward pass.

MOOLLM's framing:

```yaml
characters_simulated: 5
debate_rounds: 4
perspectives: [paranoid, idealist, evidence-based, systemic, historical]
output: ensemble_wisdom  # Not the statistical center!
```

## The caveat MOOLLM names and drops

One line, in `speed-of-light/GLANCE.yml`:

```yaml
security_note: "Single-model multi-agent creates herd behavior risk"
```

That's the entire treatment of the biggest problem with the idea. So here it is properly.

**Personas in a single forward pass share activations.** They are not independent. They're four
samples from one distribution, conditioned on one context, computed by one set of weights in
one pass. If the model has a blind spot, **all four roles have it**, and they will agree with
each other about it, confidently, which reads exactly like corroboration.

That's worse than one voice, because now you have four voices agreeing and a false sense of
having checked.

Separate calls don't fully fix this — same weights, same blind spots — but they help: different
sampling, no shared activations, no conversational momentum pulling later roles toward earlier
ones. **Separate *models* fix it much better**, because the blind spots differ.

## When to use which

| Situation | Choose | Why |
|---|---|---|
| Brainstorming, exploring a space | **In-context** | Cheap, fast, coherent; independence doesn't matter |
| Drafting from multiple angles | **In-context** | Same |
| Surfacing obvious objections | **In-context** | Good enough, 10× cheaper |
| Design review with real stakes | **Separate calls** | Correlation starts to cost |
| Red-teaming, adversarial review | **Separate calls, separate models** | The shared blind spot is the target |
| Anything where "they all agreed" would be your evidence | **Separate models** | Agreement from one model is not evidence |

**The rule:** *the more the value depends on the perspectives being genuinely independent, the
more the boundary tax is worth paying.*

If you're using the ensemble to **generate** options — in-context, always. If you're using it
to **validate** — the correlation is exactly what you're trying to defeat, so pay the tax.

## Making it work

**Give roles real, conflicting priorities.**

```markdown
# ❌ These are the same person in four hats
- Reviewer A: check the code
- Reviewer B: look for issues

# ✅ These want incompatible things
- SECURITY: assume the input is hostile. Nothing else matters.
- PERFORMANCE: this runs 10k times a second. Allocation is a bug.
- MAINTAINER: I inherit this. Clever is a defect.
```

Roles that want incompatible things produce real disagreement. Roles that want "good code"
produce four paraphrases and a false consensus.

**Force explicit disagreement.**

> *Where two roles conflict, state the conflict. Do not split the difference.*

Without this the model resolves tension automatically — it's trained to be agreeable — and you
get a smooth synthesis that has quietly discarded the objection you most needed.

**Use a separate evaluator.**

MOOLLM has `skills/evaluator/` and `skills/rubric/` for exactly this: after the debate, an
independent pass scores against explicit criteria. The debaters advocate; the evaluator judges.
Different jobs, and collapsing them means the advocate grades their own argument.

**Structure helps.** `skills/roberts-rules/` applies parliamentary procedure — motions,
seconds, amendments, votes. Sounds like a joke; isn't. Structure prevents the debate from
collapsing into agreement, because the *form* requires opposition.

## The honest limit

You are not getting five agents. **You are getting one model doing an impression of five
agents.** That's genuinely useful — impressions surface objections a single voice smooths away
— but it is not independent verification, and the failure mode is that it *feels* like
verification.

Five in-context roles agreeing tells you: *one model, in one pass, found no objection.* That is
roughly as much evidence as one voice saying "looks fine."

**Never let in-context agreement be your evidence.** Use it to find objections, not to confirm
their absence.

## Applying it

**This is a technique, not infrastructure.** Nothing to build. Adopt it per task.

**Start:** next time you'd ask for a review, ask for three roles with conflicting priorities
and an explicit statement of where they disagree. Compare to what one voice gave you. The
difference is usually obvious immediately.

## Checklist

- [ ] Roles want **incompatible** things, not the same thing in different hats
- [ ] The prompt forces explicit disagreement, forbids splitting the difference
- [ ] An independent evaluator scores after the debate
- [ ] You chose in-context vs. separate calls **deliberately**, based on whether independence matters
- [ ] For anything adversarial: separate calls, ideally separate models
- [ ] You are not treating in-context agreement as verification

---

That's all six mechanisms. Next: [template/](../../template/) — a working starting point.
