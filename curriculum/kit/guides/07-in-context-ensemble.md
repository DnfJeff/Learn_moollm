# Guide 7 · In-context ensemble

> **Tier:** Practitioner · deeper: [spec/MECHANISMS.md#m7](../../spec/MECHANISMS.md#m7--in-context-ensemble) · plainer: [onramp/THE-TEN-IDEAS.md#m7](../../onramp/THE-TEN-IDEAS.md#m7--in-context-ensemble)

**The symptom.** You want multiple perspectives on a decision — security review, performance
review, a devil's advocate — so you either run N separate agent calls (slow, expensive, each
one re-fed the whole context) or you ask once and get the averaged, hedged, single-voice
answer that satisfies nobody.

**What you build.** One call that *simulates the panel*: declared perspectives debating in
the same context. And one bright line for when you must **not** do this.

## Why one call beats N calls (usually)

Every boundary between LLM calls serializes rich internal state into tokens, ships it, and
re-tokenizes it — paying latency, cost, and precision every hop. Five "agents" that are
really five API calls to the same model paid that tax four times to simulate a separation
one context could have held — with *better* coherence, because one forward pass sees all
the personas at once. (The origin's demos run 33 game turns across 8 personas, and 210
character-turns, in one call each.)

There's a second, subtler payoff: a single-voice answer is the *centroid* of possible
opinions — the statistical middle, which tells you nothing about the shape of the
disagreement. A declared ensemble recovers the shape: where the perspectives clash is
exactly the information the averaged answer destroyed.

## The files

Declare the panel; don't improvise it per-turn or the voices collapse into one:

```yaml
# capabilities/design-review/panel.yml
perspectives:
  security:
    optimizes_for: "abuse cases, blast radius"
    disposition: "assumes hostile input; hates implicit trust"
  performance:
    optimizes_for: "hot-path cost, allocation"
    disposition: "suspicious of abstraction layers"
  maintainer:
    optimizes_for: "the person on-call in six months"
    disposition: "votes against cleverness"
protocol:
  rounds: 2                    # position → rebuttal
  output: "disagreements first, then agreements, then each holdout's price to concur"
```

The output rule matters most: **disagreements first.** If the ensemble's report reads like
consensus, you bought a committee and received a press release.

## The bright line (this part is normative)

Personas in one forward pass **share activations** — they are correlated minds, not
independent ones. So:

| Task | Architecture |
|---|---|
| Explore the shape of an opinion space; brainstorm; stress a design from declared angles | **In-context ensemble** — fast, cheap, coherent |
| Independent verification: red-teaming, second opinions, "would someone else catch this?" | **Separate calls — ideally separate models.** Pay the tax; independence *is* the product |

An in-context "red team" has the same blind spots as the blue team, delivered in a scarier
voice. When correlated failure is the thing you're hunting, the boundary cost is not waste.

## Verify it's working

1. Run a decision through the panel. Count genuine disagreements in the output. Zero
   disagreements on a non-trivial decision = persona theater; sharpen `optimizes_for` until
   the perspectives actually want different things.
2. Ask the same question single-voice. If the ensemble's answer isn't materially different
   from the centroid answer, the panel isn't earning its tokens.
3. Check the transcript: does each perspective ever *concede*? Real deliberation includes
   updates, not just restated positions.

## The traps

- **Herd behavior sold as consensus** — the correlation problem above, unhandled.
- **Persona theater** — five names, one opinion. Cause: perspectives declared as job titles
  instead of *what they optimize for and what they hate*.
- **Ensemble where a script should decide** — "which linter rule applies" is not a debate
  (P2). Panels are for judgment under trade-offs, not lookups.
