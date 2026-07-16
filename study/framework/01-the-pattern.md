# The Pattern

The distilled architecture. Domain-neutral, no adventure games, no monkeys.

This is what MOOLLM is, once you've done the extraction in
[analysis/](../analysis/). Read this if you want the framework and trust the analysis.

## The problem it solves

> **An LLM agent needs access to more capability than fits in its context window, must behave
> consistently across sessions and hosts, and must be correctable by a human who wasn't
> watching.**

Every part of that sentence generates a mechanism:

| Requirement | Mechanism |
|---|---|
| More capability than fits | **Resolution ladder** — sample cheap, descend on demand |
| Find the right one | **Declarative routing** — units announce when they're relevant |
| Without a registry | **Convention discovery** — identity is path, interface is a marker file |
| Across sessions | **Externalized state** — attention and memory are files |
| Consistently | **Standing constraints** — always-on policy in the free channel |
| Across hosts | **Driver layer** — one policy, N adapters |
| Correctable by a human | **Everything is text a person can open and edit** |

Seven requirements, seven mechanisms. That's the architecture.

## The shape

```
project/
├── AGENT.md              Entry point. The free channel. Always loaded.
│                         Standing constraints inline. Pointers only.
│
├── .agent/               Runtime state. Gitignored. The agent's attention.
│   ├── working-set.yml     What I'm focused on now
│   ├── hot.yml             Keep these loaded
│   ├── cold.yml            Evicted, with breadcrumbs
│   ├── session-log.md      What happened (append-only)
│   └── output.md           Results for the human (append-only)
│
├── policy/               Portable rules. Host-independent.
│   ├── core.md             Universal principles
│   └── drivers/            Host adapters
│       ├── claude-code.yml
│       ├── cursor.yml
│       └── generic.yml
│
└── capabilities/         The library. One directory per unit.
    ├── INDEX.yml           All units, one line each. THE ENTRY POINT.
    └── <name>/
        ├── GLANCE.yml      ~400 tokens  "Is this relevant?"
        ├── CARD.yml        ~1,400       "What can it do? How do I call it?"
        ├── SKILL.md        ~2,800       "How does it work?"    (optional)
        └── README.md       ~1,200       "Why is it like this?" (optional)
```

Four directories. That's the whole system.

## The seven mechanisms

### 1. Resolution ladder

Write each capability at multiple sizes. Read the cheapest tier that answers your question.

```
INDEX.yml    ~35 tokens/entry    Does it exist?        → consider
GLANCE.yml   ~400               Is it relevant?        → descend or drop
CARD.yml     ~1,400             How do I call it?      → USE IT (stop here)
SKILL.md     ~2,800             How does it work?      → implement/debug
README.md    ~1,200             Why is it like this?   → modify/extend
```

**The rule:** *never load a tier without first loading the tier above.*

**Why it works:** a 790K-token library is navigable from a 5K-token index — 155×. Most reads
stop at CARD. Library size becomes nearly free.

**The discipline that makes it work:** each tier is *rewritten*, not truncated. A GLANCE is an
editorial judgment about what a reader needs at that depth, not the first N lines of the
SKILL. Do not auto-generate them.

→ [guide/01-progressive-disclosure.md](../guide/01-progressive-disclosure.md)

### 2. Declarative routing

Each unit declares its own activation conditions. No central dispatcher.

```yaml
triggers:
  REVIEW-SECURITY:
    score: 90
    when: "diff touches auth, crypto, or input parsing"
    method: REVIEW
```

**Why it works:** adding a capability = adding a directory. Nothing else changes. The router
doesn't know what exists; the things that exist know when they matter.

**The honest limit:** the LLM scores these, not an engine. `when:` is a suggestion, not a
predicate. Good for soft routing. Never for anything requiring determinism.

→ [guide/02-declarative-routing.md](../guide/02-declarative-routing.md)

### 3. Convention discovery

- **Identity is path.** `capabilities/deploy/` *is* the deploy capability.
- **Interface is a marker file.** `CARD.yml` present → dispatchable. `SKILL.md` present → it
  teaches a protocol.
- **Discovery is `ls`.** No registry, no manifest, no build step.
- **Git is your database.** Text files: diff, merge, history, blame, review — free.

**The check:** "is this a capability?" is `os.path.exists(dir/CARD.yml)`.

### 4. Externalized state

No hidden memory. Everything the agent knows is a file a human can open and edit.

| File | Mode | Holds |
|---|---|---|
| `working-set.yml` | read/write | Current focus |
| `hot.yml` | read/write | Keep-loaded, with priority |
| `cold.yml` | read/write | Evicted, with breadcrumbs for recovery |
| `session-log.md` | append-only | What happened |
| `output.md` | append-only | Results for the human |

**Three wins, commonly conflated:**
1. **Resumption** — a new session reads five small files, not a replayed history.
2. **Auditability** — you can see what the agent is attending to.
3. **Attention as artifact** — "what am I focused on" becomes a document you can diff and fix.

The third is the underrated one. Most frameworks treat context as something that happens *to*
the agent. Here it's writable.

→ [guide/04-externalized-state.md](../guide/04-externalized-state.md)

### 5. Standing constraints

Always-on behavioral policy, inlined into the host's free channel.

```markdown
## Standing constraints  (in AGENT.md — loaded every session, free)

- CLAIM-LEDGER: for each user claim → CONFIRM / DISPUTE / ASK FOR SOURCE. Before anything else.
- NO-HEDGING: state confidence as a number, then claim it plainly.
- NO-SYCOPHANCY: respect is not agreement.
- META-QUOTA: ≤10% of output on process talk.
```

**Why it works:** naming a failure mode is most of the fix. "Don't be verbose" is unusable.
`VERBOSITY` as a named sin with a stated test is actionable.

**The cost:** every standing constraint is a permanent context tax. Keep it under ~2,000
tokens. Inline the text; don't reference files.

→ [guide/05-standing-constraints.md](../guide/05-standing-constraints.md)

### 6. Driver layer

One policy document, N host adapters.

```yaml
driver:
  name: claude-code
  tier: 5
capabilities:
  file_read: true
  semantic_search: false
tools:
  read_file:  { tool: Read }
  write_file: { tool: Write }
fallbacks:
  semantic_search: "use Grep with a regex approximation"
```

**Why it works:** policy stops forking per host. New host = new adapter, not a new fork.
Declare a fallback for every capability you don't have.

→ [guide/03-host-drivers.md](../guide/03-host-drivers.md)

### 7. Tolerant input, validated self

> *"Be conservative in what you send, be liberal in what you accept."* — Postel, RFC 761

Accept messy input; emit clean output; never crash. **And validate your own configuration.**

This is the one place the framework deliberately departs from MOOLLM. MOOLLM's tolerance is
total, which is why its boot file has been invalid YAML for an unknown length of time with no
signal ([analysis/05](../analysis/05-honest-assessment.md)).

**The split:**
- Input from humans → liberal. Fix typos, infer intent, never crash.
- Config you authored → strict. Parse it. Check it. Fail loudly.

→ `template/validate.py`

## The free channel

Every host auto-loads something: `CLAUDE.md`, `.cursorrules`, the system prompt. That content
is **prepaid** — you pay for it whether you use it or not.

**The rule:**

| Need it | Put it |
|---|---|
| Every session | **Free channel** (`AGENT.md`) — inline the text |
| Sometimes | **Ladder** (`capabilities/`) — load on demand |
| Never, but it explains why | **README** — a human will read it, the model won't |

Confusing these is the most common context-budget mistake. Standing constraints go in the free
channel. Capability details go in the ladder. Rationale goes where the model won't trip over
it.

## Optional: in-context ensembles

When you need multiple perspectives, simulate them **in one call** rather than N API
round-trips.

> INSIDE the model: high-dimensional vectors, precise, instant.
> AT the boundary: serial tokens, lossy, slow.
> **Delay tokenization.**

**The tradeoff, which MOOLLM names and doesn't resolve:** personas in one forward pass share
activations. You save latency and lose independence.

| Use | Choose |
|---|---|
| Brainstorming, drafting, exploring a space | **In-context** — cheaper, coherent, fast |
| Red-teaming, adversarial review, catching blind spots | **Separate calls**, ideally separate models |

The blind spot you're hunting is exactly the one a shared forward pass shares.

→ [guide/06-in-context-ensemble.md](../guide/06-in-context-ensemble.md)

## What this is not

Be honest about it, because MOOLLM isn't:

- **Not a runtime.** Nothing executes. These are conventions an LLM reads and usually follows.
- **Not enforcement.** `hot.yml` is a hint. Append-only is a promise. If you need a guarantee,
  use a hook.
- **Not deterministic.** Scores are read by a model, not evaluated by an engine.
- **Not free.** Four tiers per unit = 4× write amplification and four places to drift. The
  validator exists because of this.

**It is:** a way to organize files so an LLM can navigate more capability than it can hold,
behave consistently, and be corrected by a human — for the cost of writing things down at
several sizes and running a checker.

That's a real, modest, useful thing. Which is what MOOLLM is, underneath the pub.

## Adoption order

Don't build all seven. In order of value per hour:

1. **Standing constraints** (`AGENT.md`) — one hour, immediate quality change. Start here.
2. **Externalized state** (`.agent/`) — one hour, unlocks resumption and auditing.
3. **Resolution ladder** — the big one, but only once you have ~10+ capabilities. Below that,
   just write them out; the ladder is overhead.
4. **Declarative routing** — once the index gets long enough that choosing is hard.
5. **Driver layer** — only when you actually have a second host. Not before.
6. **Boot compilation** — once you know what's genuinely hot. Requires data.
7. **In-context ensembles** — a technique, not infrastructure. Adopt per task.

**The trap:** building the ladder for four capabilities. The mechanism costs more than it
saves until the library is big enough to be unreadable. MOOLLM has 141 units and needs it. You
probably have six and don't.

Next: [02-principles.md](02-principles.md), or jump to [template/](../../template/) to start.
