# Mechanism Inventory

Every orchestration mechanism in MOOLLM, named precisely, with what it does, why it's
efficient, what it costs, and how portable it is.

**Portability ratings:**

- 🟢 **Direct** — take it as-is, only rename things
- 🟡 **Adapt** — the idea is portable, the implementation is MOOLLM-shaped
- 🔴 **Local** — inseparable from the adventure-game domain; do not port

---

## M1 · Resolution Ladder 🟢

**MOOLLM calls it:** Semantic Image Pyramid.
**Where:** `.cursorrules` (`skill-reading-order`), every `skills/*/GLANCE.yml`, `constitution-core.md` §14.

Every capability is written four times at four sizes. You read the cheapest tier that answers
your question and stop.

| Tier | File | Mean size | ~Tokens | Answers |
|---|---|---|---|---|
| 👁️ Glance | `GLANCE.yml` | 1.7 KB | ~420 | "Is this even relevant?" |
| 📇 Card | `CARD.yml` | 5.4 KB | ~1,360 | "What can it do? How do I call it?" |
| 📜 Skill | `SKILL.md` | 11.0 KB | ~2,760 | "How does it actually work?" |
| 📚 Readme | `README.md` | 4.7 KB | ~1,190 | "Why is it like this?" |

Above all four sits `INDEX.yml` (19.9 KB, ~5,100 tokens) listing all 141 skills with a
tagline each.

**The rule that makes it work** (`.cursorrules`):

> *"Never load a lower level without first loading the level above."*

**Why it's efficient:** The full skill corpus is ~790,000 tokens. No context window holds it.
The index is ~5,100 tokens — **155× smaller** — and it is sufficient to *choose*. Once you've
chosen, loading five skills at full depth costs ~28,000 tokens: 3.5% of the corpus. The
ladder converts "read everything" into "sample, then descend."

**The real insight:** this is not compression. Each tier is *rewritten*, not truncated. A
`GLANCE.yml` is not the first 40 lines of `SKILL.md` — it's an editorial judgment about what
matters. That's why it works and why auto-generating these tiers would destroy the value.
The tier boundary is a human deciding what a reader needs at that depth.

**Cost:** 4× write amplification, and four places to drift out of sync. MOOLLM has drifted:
`INDEX.yml` claims 133 skills; there are 141.

**Port it as:** [guide/01-progressive-disclosure.md](../guide/01-progressive-disclosure.md)

---

## M2 · Declarative Capability Routing 🟢

**MOOLLM calls it:** Advertisements (from The Sims).
**Where:** `skills/advertisement/`, 115 of 140 `CARD.yml` files.

Instead of a dispatcher that knows every capability, each capability declares its own
activation conditions and a relevance score. Selection = collect, score against context, take
the top.

```yaml
advertisements:
  DISCOVER-ACTIONS:
    score: 90
    condition: "New room or unsure what to do"
    effect: "Scan and list ads with scores"
    delegate:
      method: SCAN
```

**Why it's efficient:** it inverts the dependency. A central router is O(n) knowledge in one
place that must change whenever anything is added. Advertisements are O(1) local knowledge
per unit — you add a capability by adding a directory, and nothing else changes. This is
exactly why The Sims could ship expansion packs and why players could build objects: *the
object carries its own behavior*. `skills/advertisement/SKILL.md` names this correctly as the
reason for the game's extensibility.

**The genuinely good part:** advertisements aren't restricted to skills. Any directory, file,
or YAML section can advertise. `kernel/ARCHITECTURE.md` frames this as "agents all the way
down," which is theatrical but structurally accurate — an advertisement is a lexically scoped
handler bound to its directory.

**The catch:** scoring is done by the LLM reading YAML, not by an engine evaluating
expressions. `score_if: "has_materials AND has_skill"` is a *suggestion*. There is no
evaluator. Consistency comes from the model, not from arithmetic. This is fine for soft
routing and unacceptable for anything requiring determinism.

**Port it as:** [guide/02-declarative-routing.md](../guide/02-declarative-routing.md)

---

## M3 · Host Driver Layer 🟢

**MOOLLM calls it:** Drivers.
**Where:** `kernel/drivers/{cursor,claude-code,antigravity,generic,custom}.yml`.

One policy document, N host adapters. Each driver declares detection, capabilities, abstract
operation → concrete tool mapping, paths, fallbacks, and limits.

```yaml
capabilities:
  file_read: true
  semantic_search: false
  why_parameter: "via_mcp"
tools:
  read_file: { tool: "View" }
  write_file: { tool: "Edit" }
```

Plus capability tiers 0–6, and a fallback for every unsupported feature:

| Feature | Full support | Fallback |
|---|---|---|
| `why` parameter | Include in tool call | Document intent in prose |
| Append-only | Enforced by orchestrator | Convention only |
| Vector search | `SemanticSearch` | Grep |

**Why it matters:** this is the mechanism that makes the whole thing portable across Cursor,
Claude Code, and unknown future hosts without forking the policy. It's ordinary, correct
engineering — the same reason OS drivers exist — and it's the least glamorous and most
reusable idea in the repository.

**The honest read:** the fallback for nearly everything is "convention only," which means the
driver layer is currently *documentation of an aspiration* on every real host. See
[05-honest-assessment.md](05-honest-assessment.md).

**Port it as:** [guide/03-host-drivers.md](../guide/03-host-drivers.md)

---

## M4 · Externalized State 🟢

**MOOLLM calls it:** Files-as-State.
**Where:** `constitution-core.md` §2, `.moollm/`, `kernel/memory-management-protocol.md`.

No hidden memory. Everything the agent knows is a file a human can open.

| File | Mode | Holds |
|---|---|---|
| `working-set.yml` | read/write | Current focus |
| `hot.yml` | read/write | Keep-loaded hints + priority |
| `cold.yml` | read/write | Evicted, with breadcrumbs |
| `session-log.md` | append-only | What happened |
| `output.md` | append-only | User-visible results |

The live `.moollm/` in this repo shows it working — `working-set.yml` is 607 bytes and names
five active files. That's the entire session's attention, legible at a glance.

**Why it's efficient:** three separate wins that are easy to conflate.
1. **Resumption** — a new session reads five small files instead of replaying history.
2. **Auditability** — you can see what the agent is attending to and correct it by editing a file.
3. **Attention as an artifact** — making "what am I focused on" explicit and writable turns a
   vague property of the conversation into something you can review, diff, and fix.

The third is the underrated one. Most agent frameworks treat context as something that
happens *to* the agent. Here it's a document.

**The model-advises-orchestrator-decides split** is the intended design:

> *The model advises. The orchestrator decides.*

Good separation. Currently unimplemented — nothing decides. See M4's caveat in the honest
assessment.

**Port it as:** [guide/04-externalized-state.md](../guide/04-externalized-state.md)

---

## M5 · Standing Constraints 🟢

**MOOLLM calls it:** Ambient Skills.
**Where:** `skills/no-ai-*/` (12 of them), `.cursorrules` `ambient_skills:` block, 13 CARDs declaring `AMBIENT`.

Behavioral constraints that are always in context, shaping every response without being
invoked. Declared with a wildcard advertisement:

```yaml
AMBIENT:
  score: 100
  condition: always
  scope: session
  resolution: card-only
```

The 12-member `no-ai-*` family is the best-executed thing in the repository. Each names its
failure modes as **cardinal sins** and gives a one-line fix:

| Skill | Fights | The fix |
|---|---|---|
| `no-ai-slop` | Verbosity, hallucination, certainty theater | "Replace adjectives with facts." |
| `no-ai-hedging` | Qualifier stacking, weasel certainty | "State confidence as a number. Then claim it plainly." |
| `no-ai-sycophancy` | Unearned validation, softened disagreement | "Respect is not agreement." |
| `no-ai-moralizing` | Caveat-bombing, refusal theater | "Librarians don't interrogate patrons." |
| `no-ai-humansplaining` | Re-teaching the model what it knows | "Point at latent knowledge by name." |
| `no-ai-gloss` | Euphemism laundering, power-protective neutrality | "Call corruption 'corruption'." |

**Why it works:** naming a failure mode is most of the fix. "Don't be verbose" is unusable
feedback. `CERTAINTY-THEATER` is a handle — the model can check output against a named
pattern. These are K-lines pointed at *behaviors* instead of concepts.

Two hard gates in `no-ai-slop` are worth stealing outright:
- **CLAIM-LEDGER** — for each user claim: CONFIRM / DISPUTE / ASK FOR SOURCE, before anything else.
- **META-QUOTA** — max 10% of output spent on epistemology and strategy.

**The cost, stated by MOOLLM itself:** *"Ambient = permission to live in context rent-free;
high trust — only trustworthy skills."* Every ambient skill is a permanent context tax. Twelve
of them at `card-only` resolution is real budget. The `.cursorrules` solution — inline the
GLANCE text directly — is correct and is M6.

**Port it as:** [guide/05-standing-constraints.md](../guide/05-standing-constraints.md)

---

## M6 · Boot Compilation 🟡

**MOOLLM calls it:** `cursor-mirror OPTIMIZE`, the MOOLLM Compiler.
**Where:** `.cursorrules`, `kernel/ARCHITECTURE.md` § Cursor Optimization System.

Compile the always-needed subset into whatever file the host auto-loads at session start.
Cursor reads `.cursorrules` for free; so the ambient skills' GLANCE content is *inlined* there
rather than being loaded from 12 separate files.

The loop: **Work → Introspect → Compile → Boot → Repeat.** Each cycle, the boot artifact gets
better at pre-loading what this project actually needed.

**Why it's efficient:** it exploits a free channel. Every host has some auto-loaded config
(`.cursorrules`, `CLAUDE.md`, system prompt). Content there costs nothing extra because it's
loaded regardless. Moving hot content into it converts N file reads into zero.

**Why 🟡:** the compiler is `cursor-mirror`, which reads Cursor's LevelDB conversation
history. That's Cursor-specific archaeology. The *concept* — compile hot context into the
host's free channel — is fully general. The *implementation* is not.

**The bug that proves the point:** `.cursorrules` does not parse as YAML. Lines 208–221
(`yaml-jazz`, `copy-that`) are indented one space instead of two, breaking out of the
`ambient_skills` map. Run `python evidence/measure.py` and it reports the parse error. The
system works anyway, because an LLM reads the file and doesn't care. This is simultaneously
the best demonstration of the architecture's core bet and its sharpest warning — see
[05-honest-assessment.md](05-honest-assessment.md).

---

## M7 · In-Context Ensemble 🟡

**MOOLLM calls it:** SPEED-OF-LIGHT.
**Where:** `skills/speed-of-light/`, `constitution-core.md` §0.

Simulate multiple perspectives **inside one LLM call** rather than orchestrating N agents
across N API round-trips.

The argument from `skills/speed-of-light/GLANCE.yml`, which is the sharpest technical claim in
the repository:

> INSIDE LLM: high-dimensional vectors, precise, instant
> AT BOUNDARY: serial tokens, lossy, glacial
>
> Tokenization destroys precision. Detokenization adds noise.
> Work with vectors at speed of light. **Delay tokenization.**

It names the anti-pattern **Carrier Pigeon Protocol**: multi-agent systems where agents
communicate by squeezing high-dimensional internal state through a narrow serial token
channel, over a network, repeatedly. Each hop is lossy *and* slow.

**Why it matters:** it's a real critique of the dominant multi-agent architecture. If your
five "agents" are five API calls to the same model, you paid latency and precision to
simulate a separation that a single call could have held in context — with better coherence,
because one forward pass sees all the personas at once.

**Paired with §0 of the constitution**, which explains *why* you'd want an ensemble at all:

> Traditional chat produces **the statistical center of all possible viewpoints**.
> The centroid of a cloud tells you nothing about the cloud's shape.

So: single-voice LLM output is an average. Ensembles recover the distribution. Do the
ensemble in-context to avoid paying the boundary tax.

**Why 🟡 and not 🟢** — MOOLLM states the risk itself and then doesn't resolve it:

> `security_note: "Single-model multi-agent creates herd behavior risk"`

That's the whole problem with the idea, noted in one line and dropped. Personas in a single
forward pass share activations; they are correlated in ways that separate calls are not. You
save latency and lose independence. For brainstorming, in-context wins. For genuine red-teaming
where correlated blind spots are the thing you're hunting, separate calls — ideally separate
*models* — are worth the tax. MOOLLM has the mechanism (`adversarial-committee`, `evaluator`,
`debate`, `roberts-rules`) but not the guidance on when the boundary is worth paying for.

**Port it as:** [guide/06-in-context-ensemble.md](../guide/06-in-context-ensemble.md)

---

## M8 · Directory-as-Object 🟡

**MOOLLM calls it:** Selfish COM, DIRECTORY-AS-OBJECT.
**Where:** `kernel/DIRECTORY-AS-OBJECT.md`, `kernel/SELFISH-COM-IMPLEMENTATION.md`.

The directory is the object. Its path is its identity. UPPERCASE marker files are interfaces.
`queryInterface(dir, 'room')` is `os.path.exists(dir/ROOM.yml)`.

```
don-hopkins/          ← object; identity = path
├── CHARACTER.yml     ← queryInterface('character')
├── ROOM.yml          ← queryInterface('room')
└── memories/         ← child object
```

Multi-interface, COM-style: a directory with both `CHARACTER.yml` and `ROOM.yml` is both.
Inheritance via `parents:` arrays, Self-style prototypes, resolved by walking outward.

The lineage claim checks out — `kernel/DIRECTORY-AS-OBJECT.md` cites **US Patent 5187786A**
(Densmore & Rosenthal, Sun Microsystems, filed 1991): OOP in a hierarchical filesystem,
directories as classes, PATH files as inheritance chains. This is not a new idea and MOOLLM
correctly says so.

**Why it's efficient:** discovery is `ls`. No registry to maintain, no manifest to sync, no
build step. Add a directory, the capability exists. Git handles versioning, diffing, merging,
and history for free because everything is text.

**Why 🟡:** the *pattern* is portable and good. The *ceremony* — four marker files per unit,
prototype chains, multi-interface dispatch — is a lot of structure for a project that just
wants an agent to be useful. Take "identity = path, interface = marker file, discovery = ls."
Leave the prototype-inheritance resolver until you have a demonstrated need.

---

## M9 · Names as Addresses 🟢

**MOOLLM calls it:** K-lines (Minsky).
**Where:** `skills/k-lines/`, `kernel/naming/`, `PROTOCOLS.yml`, `no-ai-humansplaining`.

A name is a pointer into pretrained weights. Using the right name activates a whole
constellation of knowledge for the cost of one token.

The economics, stated exactly:

> **"Latent knowledge is prepaid; respelled knowledge is billed per call, forever.**
> **Novel jargon is a cache miss that never fills."**
> The test: *Is the pointee in latent space? Point — the name is the activation. If not: spell it ONCE, in a file.*
> Constitutional directive: **LEAN INTO the training data.**

**Why this is the keystone:** it justifies everything else. Why "room"? Free. Why "The Sims"?
Free. Why cite Postel, Minsky, Ungar, Ackley, Wright, Papert? Each name is a compressed
library the model already has. `PROTOCOLS.yml` is a 106 KB index of ~200 such names, each
mapping a symbol to a meaning and an invocation condition.

**Why it's also the trap:** the same mechanism that makes MOOLLM cheap for the LLM makes it
expensive for you. Your team does not have MOOLLM's codebook pretrained. Every K-line that's
free for the model is a lookup for the human. This is the core tension and it gets its own
document: [03-metaphor-vs-mechanism.md](03-metaphor-vs-mechanism.md).

---

## M10 · Tolerant Interpretation 🟢

**MOOLLM calls it:** POSTEL, robust-first, self-healing.
**Where:** `constitution-core.md` §5 and §7, `skills/postel/`, `skills/robust-first/`, `kernel/self-healing-protocol.md`.

> *"Be conservative in what you send, be liberal in what you accept."* — Jon Postel, RFC 761

Accept misspellings, missing fields, format variants, natural-language approximations. Emit
clean, well-formed output. Never crash — degrade, log, repair, continue.

From `robust-first`: *"A crashed system is infinitely wrong."* Priority order: **survive →
heal → function → optimize → adapt → reproduce.**

**Why it's efficient:** it eliminates the entire class of work that is input validation and
error paths, which in an LLM system is work the model does natively and for free. `SING-PRASES`
resolves to `SING-PRAISES` because the model reads intent, not syntax. You don't write the
parser.

**And this is exactly how `.cursorrules` survives being invalid YAML.** The bug is not caught
because nothing parses; nothing parses because the design says the LLM interprets. The
tolerance is real and load-bearing — and it means malformed state is silent. Both facts are
true at once.

---

## The domain layer 🔴

Not portable. Listed so you can recognize it and leave it behind: `room`, `adventure`,
`character`, `incarnation`, `pub`, `bartender`, `budtender`, `cat`, `dog`, `animal`, `party`,
`inventory`, `exit`, `buff`, `needs`, `economy`, `groceries`, `soul-chat`, `mythic`,
`trekify`, `showboat`, `worm`, `stone`, plus all of `examples/adventure-4/` (2,090 files) and
`.moollm/mayberry/`.

Some are near-misses worth noting. `needs` and `scoring` are general (priority arithmetic
wearing a Sims costume). `inventory` is general (holding state). `buff` is general (temporary
modifiers). If you want them, rename them before you port them, or the costume comes along.

---

## Summary

| # | Mechanism | MOOLLM name | Port |
|---|---|---|---|
| M1 | Resolution ladder | Semantic Image Pyramid | 🟢 |
| M2 | Declarative capability routing | Advertisements | 🟢 |
| M3 | Host driver layer | Drivers | 🟢 |
| M4 | Externalized state | Files-as-State | 🟢 |
| M5 | Standing constraints | Ambient Skills | 🟢 |
| M6 | Boot compilation | cursor-mirror OPTIMIZE | 🟡 |
| M7 | In-context ensemble | SPEED-OF-LIGHT | 🟡 |
| M8 | Directory-as-object | Selfish COM | 🟡 |
| M9 | Names as addresses | K-lines | 🟢 |
| M10 | Tolerant interpretation | POSTEL / robust-first | 🟢 |

Ten mechanisms. Seven take directly. Three need adaptation. Everything else in 4,489 files is
application, demonstration, or story.

That's the extraction. [03-metaphor-vs-mechanism.md](03-metaphor-vs-mechanism.md) explains why
it took this much work.
