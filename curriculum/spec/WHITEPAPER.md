# The Legible Workspace

## A file-native architecture for context orchestration

> **Tier:** Specification · plainer: [kit/START-HERE.md](../kit/START-HERE.md) · normative rules: [MECHANISMS.md](MECHANISMS.md) · numbers: [EVIDENCE.md](EVIDENCE.md)

**Abstract.** An LLM agent needs access to more capability than fits in its context window,
must behave consistently across sessions and hosts, and must be correctable by a human who
wasn't watching. The prevailing architectures answer with runtime machinery: retrieval
services, orchestration graphs, agent swarms coordinated over APIs. This paper describes an
architecture that answers with *files*: capability, policy, routing, memory, and attention
all live as plain text in the repository, structured so the model can navigate a corpus far
larger than its context window at ~4% of corpus cost per session, and so a human can open,
diff, and correct any part of it. We call the pattern the **Legible Workspace**. Its
mechanisms originate in **MOOLLM** (Don Hopkins, SimHacker/moollm); this paper presents them
domain-neutrally, with measurements, limits, and the conditions under which you should not
use it.

---

## 1. The problem

Three requirements define the space:

1. **Capability exceeds context.** A serious capability library is hundreds of thousands of
   tokens (the reference corpus: ~790K). No context window holds it, and even a window that
   could would perform worse for it — attention spread over 141 mostly-irrelevant documents,
   paid on every call.
2. **Consistency across sessions and hosts.** Sessions end; hosts differ (Cursor, Claude
   Code, a bare API loop). Behavior that lives only in a conversation dies with it. Behavior
   that lives in host-specific configuration forks per host.
3. **Correctability by an absent human.** If you cannot see what the agent knows, believes,
   and is attending to, you debug by guessing. Most agent frameworks make context something
   that happens *to* the agent, invisible after the fact.

And one tax that any multi-step architecture pays or avoids: **the boundary tax.** Every
hop between LLM calls serializes high-dimensional internal state into tokens, ships it,
and re-tokenizes — losing precision, adding latency, and re-billing the context. N
coordinated agents over an API pay this N times per exchange.

## 2. The claim

One invariant organizes the whole design: **everything the agent knows, wants, may do, and
is currently attending to is plain text a human can open.** Ten mechanisms preserve that
invariant while meeting the three requirements (normative statements in
[MECHANISMS.md](MECHANISMS.md); one-line forms here):

| Requirement | Mechanisms |
|---|---|
| Navigate a corpus bigger than context | **M1** resolution ladder · **M9** names as addresses |
| Find the right capability without a router | **M2** declarative routing · **M8** directory-as-object |
| Survive sessions; be auditable and correctable | **M4** externalized state · **M10** tolerant interpretation |
| Behave consistently without re-arguing | **M5** standing constraints · **M6** boot compilation |
| Run on any host | **M3** host drivers |
| Avoid the boundary tax | **M7** in-context ensemble |

Plus three cross-cutting principles: **P1** every control file works whether or not an
enforcing orchestrator exists (advisory is the designed floor, not a missing feature);
**P2** mechanical work goes to scripts, judgment to the model; **P3** every summary tier is
rewritten, never truncated.

The architecture is deliberately boring at its core: M1 is a card catalogue; M3 is device
drivers; M4 is "write things down." What is not boring is the combination — and the
discipline the measurements show it demands.

## 3. Results

Full tables and method in [EVIDENCE.md](EVIDENCE.md). The headline numbers, measured on the
origin corpus (141 units, ~790K tokens):

- **Choosing is 155× cheaper than knowing.** The catalog (~5.1K tokens) is sufficient to
  select capabilities from a ~790K-token corpus. A realistic session — catalog plus five
  units at full depth — costs ~33K tokens, **4.2% of the corpus**, and that fraction is
  nearly flat in library size: at 1,000 units you still descend into five.
- **The free channel is worth ~3× on always-on content.** Inlining the always-needed subset
  into the host's auto-loaded boot file replaced twelve per-session file reads with zero and
  cut the resident constraint set from ~5.0K to ~1.8K tokens.
- **The boundary-tax avoidance is demonstrated, not benchmarked.** The origin system's
  transcripts show 33 simulated game turns across 8+ personas, and 210 character-turns of
  parallel behavior, each within a single call — versus the 33 and 210 calls a
  call-per-agent architecture prices in. These are worked demonstrations from the origin
  repo, reported as such; no controlled comparison has been run.

## 4. Relation to prevailing architectures

**Versus tool-call orchestration (MCP and kin).** Tool calls are the right mechanism for
effects that must happen outside the model — databases, hardware, external APIs. They are
the wrong default for *reasoning*: every call stops generation, waits a round-trip, and
re-enters with a lossy serialization. The Legible Workspace default is: knowledge and
deliberation stay in-context (M1, M7); tool calls are reserved for genuine external effects
(P2 decides which is which). The origin's slogan for the anti-pattern — coordination by
"carrier pigeon" — names something real about current multi-agent practice.

**Versus vector retrieval (RAG).** The resolution ladder is hand-written, legible retrieval:
you can read the index, and you can *fix* a bad entry with an editor. An embedding you can
neither read nor fix. Whether the ladder beats vector search on selection accuracy is
**untested** (stated in the origin study and repeated here); the honest position is that the
ladder's advantage is legibility and editability, not proven retrieval superiority. Nothing
prevents using both — the ladder is also excellent grounding *for* a retriever.

**Versus framework-in-code (LangChain-style graphs).** There, policy lives in program code:
inspectable by developers, invisible to the model except as behavior, and forked per
integration. Here, policy lives in prose and YAML the model reads directly — the same
artifact the human audits. The trade is enforcement: code enforces; prose persuades. Which
brings us to the limits.

## 5. Limits — carried forward intact

This section preserves the origin study's honest assessment. Adopters should read
[the full assessment](../../study/analysis/05-honest-assessment.md); its findings
are conditions of use, not footnotes.

1. **Tendencies, not guarantees.** On every generic host, conformance is the model reading
   conventions and following them — P1's advisory floor. Modern models follow
   well-structured context reliably enough for reading discipline and routing; they are not
   an enforcement mechanism. *Decide per rule whether a tendency suffices. For "read the
   summary first," yes. For "never write to this file," get a real hook.*
2. **Tolerance hides corruption.** The origin's boot file shipped structurally invalid YAML
   for an unknown period — harmlessly, because the model absorbs malformation; silently, for
   the same reason. Tolerant interpretation (M10) plus model-as-parser means malformed state
   produces no signal. *The floor is a validator script (P2); the reference template ships
   one because of this exact incident.*
3. **The ladder's write amplification is real.** Four tiers per unit is four places to
   drift, and the origin has drifted (four different published skill-counts, none correct;
   index header contradicting index body). Zero-ceremony authoring and a drift-checker are
   not opposed; the checker runs in under a second. *Budget for the editorial pass (P3) and
   the checker, or don't build the ladder.*
4. **Selection quality is unmeasured.** The economics prove choosing is cheap, not that the
   model chooses *correctly* from an index entry. A cheap system that picks the wrong
   capability is worse than an expensive one that picks right. *An adoption at scale should
   include a small retrieval eval; none exists yet in origin or study.*
5. **In-context ensembles are correlated.** Personas in one forward pass share activations.
   For exploring the shape of an opinion space, that's acceptable and fast; for independent
   failure-hunting it is exactly wrong, and separate calls or separate models must be paid
   for (M7 rule 4 makes this normative).
6. **A good mechanism subsidizes bad discipline.** The ladder hides depth cost so well that
   the origin's deep tiers bloated (49% of the corpus is the how-it-works tier; a third of
   that is essays). The mechanism will not push back; the discipline must.

## 6. When not to use this

- **Small, short-lived projects.** Below roughly a dozen capabilities and a handful of
  sessions, the conformance levels above Level 1 are ceremony. Level 1 (a session zone and
  append-only logs) is cheap enough for almost anything; the library machinery is not.
- **Hard-guarantee domains as the primary workload.** If most rules are "never/always"
  rules with real consequences, you need enforcement-first architecture; here enforcement
  is the upgrade path, not the foundation.
- **Latency-critical single-turn work.** The workspace pays a small reading overhead every
  session for legibility. If there is no session — one prompt, one answer — there is
  nothing to amortize.

## 7. A finding about metaphor

The origin system arrives costumed as a text-adventure world — rooms, characters, a pub.
The study that produced this series established that the costume is not decoration but a
**compression codebook**: names dense in the model's training distribution ("room,"
"inventory," "The Sims") deliver whole behavioral clusters for one token each (M9). That
choice was correct *for the model* and costly *for human readers outside the codebook* —
which is precisely why this presentation exists. The general rule the finding yields: pick
the codebook your readers already own; when in doubt, borrow (Unix, libraries, offices),
don't coin. The mechanisms are codebook-independent; that is what makes them a paradigm
rather than a game.

## 8. Reading map

| You want | Read |
|---|---|
| The rules, normatively | [MECHANISMS.md](MECHANISMS.md) |
| The numbers and method | [EVIDENCE.md](EVIDENCE.md) |
| Who invented what | [PROVENANCE.md](PROVENANCE.md) |
| To build one today | [kit/START-HERE.md](../kit/START-HERE.md) → [kit/SCAFFOLD.md](../kit/SCAFFOLD.md) |
| To explain it to a non-engineer | [onramp/](../onramp/) |
| The raw extraction this rests on | [study/](../../study/) |
