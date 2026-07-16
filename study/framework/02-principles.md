# Principles

The portable ideas, stated without metaphor. Each one names its MOOLLM origin so you can trace
it back, and states what it costs — because a principle with no cost is a slogan.

---

## P1 · Point at what the model already knows

**MOOLLM origin:** K-lines, `no-ai-humansplaining`, *"LEAN INTO the training data."*

> **Latent knowledge is prepaid. Respelled knowledge is billed per call, forever.
> Novel jargon is a cache miss that never fills.**

A name the model already understands costs one token and delivers everything it knows. A name
you invented costs a paragraph of explanation on every call, permanently, because the model
does not remember your last conversation.

**The test:** would a model with no context understand this term?

| Prepaid ✅ | Cache miss ❌ |
|---|---|
| `service`, `module`, `session` | `WidgetProc`, `FooManager` |
| "code review", "regression" | "the Vulcan process" |
| "Postel's law", "idempotent" | "our Level-3 protocol" |
| "cache", "index", "working set" | "the blue pipeline" |

**Corollary:** if you must invent a term, spell it out **once, in a file**, and then always use
the name. Never re-explain. Never use two names for one thing.

**The cost:** you're constrained to concepts that exist in the training data. Genuinely novel
ideas need genuinely novel names, and those are expensive. Pay it deliberately, rarely, and
write it down once.

---

## P2 · Read at the cheapest resolution that answers the question

**MOOLLM origin:** Semantic Image Pyramid.

Write things at several sizes. Read the smallest one that lets you decide. Descend only when
the decision requires it.

> **Never load a tier without first loading the tier above.**

**Why:** a 790K-token library is choosable from a 5K-token index. 155×. The rest is loaded only
when it's earned.

**The discipline:** each tier is a **rewrite**, not a truncation. A summary answers "is this
relevant?" — a different question than "how does this work?" — so it's a different document.
Auto-generating tiers destroys the mechanism, because a generated summary is a truncation with
extra steps.

**The cost:** N× write amplification and N places to drift. MOOLLM's index has drifted 8 skills
out of sync with no signal. Ship a checker or accept the rot.

---

## P3 · Units declare their own relevance

**MOOLLM origin:** Advertisements (The Sims).

Each capability declares when it applies. No central dispatcher knows the catalogue.

**Why:** a router is O(n) knowledge in one place that changes whenever anything is added. Local
declarations are O(1) per unit. Adding a capability = adding a directory.

This is why The Sims could ship expansion packs: the object carried its own behavior. Nothing
central had to learn about it.

**The cost:** relevance is scored by a model reading prose, not by an engine evaluating
predicates. It's soft routing. If two units both claim a request and the tie matters, nothing
resolves it deterministically. Don't use this where correctness depends on the choice.

---

## P4 · Identity is location

**MOOLLM origin:** Directory-as-Object, Selfish COM, Densmore–Rosenthal (US5187786A, 1991).

The directory *is* the thing. Its path is its name. A marker file inside it is an interface.
Discovery is `ls`.

**Why:** no registry to maintain, no manifest to sync, no build step to run. Git gives you
versioning, diffing, merging, history, and review for free, because it's all text.

**The cost:** your filesystem layout becomes your API. Renaming is refactoring. Moving a
directory breaks references. Choose the tree carefully; it's harder to change than code.

---

## P5 · State lives in files

**MOOLLM origin:** Files-as-State. *"No hidden memory."*

If the agent knows it, a human can open it. Attention, memory, focus, history — all files.

**Why, in three parts people conflate:**
1. **Resumption** — new session reads five small files instead of replaying everything.
2. **Auditability** — you can see what it's attending to.
3. **Correctability** — you can *edit* what it's attending to.

The third is the point. Attention stops being a property of the conversation and becomes a
document you can fix.

**The cost:** files drift from reality. A `working-set.yml` nobody updates is worse than none,
because it lies with authority. Write to it or delete it.

---

## P6 · The model advises; something else should decide

**MOOLLM origin:** `memory-management-protocol.md`.

The model proposes what to keep, evict, prioritize. A separate authority disposes.

**Why:** the model is inside the loop it's reasoning about. It should not be the only judge of
what it's allowed to forget.

**The honest part:** MOOLLM specifies this split and ships without the deciding party. On every
real host the model advises *and* decides, because nothing else is there.

**For you:** either build the decider (a hook, a script, a human checkpoint) or **be explicit
that you haven't.** The failure mode is documenting a guarantee and shipping a tendency —
which is exactly what MOOLLM does.

---

## P7 · Be liberal in what you accept, conservative in what you emit

**MOOLLM origin:** POSTEL, RFC 761.

Accept typos, missing fields, format variants, natural language. Emit clean, well-formed
output. Ask when genuinely ambiguous.

**Why:** the model does intent-reading natively and free. Writing a parser for user input is
work you don't have to do. `SING-PRASES` resolves to `SING-PRAISES` at no cost.

**The cost, and the exception in P8:** tolerance is why malformed things go unnoticed.

---

## P8 · Validate what you authored

**Not from MOOLLM. This is the correction.**

MOOLLM's `.cursorrules` has been invalid YAML for an unknown period. Two standing constraints
fell out of the map at line 208. Nothing noticed, because nothing parses it, because the design
says the LLM interprets.

**The split P7 doesn't make:**

| Source | Posture |
|---|---|
| Input from humans | **Liberal.** Fix typos. Infer intent. Never crash. |
| Config you wrote | **Strict.** Parse it. Check it. Fail loudly. |

Postel's law is about *protocol peers*, not about your own config files. Being liberal with
yourself isn't robustness; it's an absence of tests.

**The cost:** a build step, which is exactly what "zero ceremony" was trying to avoid. Pay it.
It's one script. `evidence/measure.py` catches MOOLLM's drift in under a second.

---

## P9 · Never crash; degrade

**MOOLLM origin:** robust-first (Ackley). *"A crashed system is infinitely wrong."*

Priority: **survive → heal → function → optimize → adapt.**

Missing file → note it, continue. Unknown host → assume the minimum, continue. Unparseable
input → best interpretation, continue.

**Why:** an agent that halts on the first anomaly is useless in the real world, which is
nothing but anomalies.

**The tension with P8, resolved:** degrade on *runtime* surprises. Fail loudly on *authoring*
errors. A missing optional file at runtime is a shrug. A malformed config at build time is a
stop. MOOLLM collapses these into one rule and gets silent breakage.

---

## P10 · Use the free channel

**MOOLLM origin:** `.cursorrules` compilation, `cursor-mirror OPTIMIZE`.

Every host auto-loads something. That content is prepaid.

| Need it | Put it |
|---|---|
| Every session | Free channel — **inline the text**, don't reference a file |
| Sometimes | The ladder — load on demand |
| Only humans need it | README — the model won't read it, and shouldn't |

**Why:** content in the free channel costs zero marginal tokens and arrives before the model
does anything. Referencing a file from there wastes the channel — you pay a round-trip to load
what you could have inlined.

**The cost:** the free channel is small and always loaded, so everything in it is a permanent
tax on every session. Budget ~2,000 tokens. Be ruthless.

---

## P11 · Name the failure mode

**MOOLLM origin:** the `no-ai-*` family, cardinal sins.

Vague guidance doesn't change behavior. Named failure modes do.

| Vague ❌ | Named ✅ |
|---|---|
| "Don't be verbose" | `VERBOSITY` — cut adjectives, state facts |
| "Don't hedge" | `QUALIFIER-STACKING` — state confidence as a number, then claim |
| "Don't flatter" | `UNEARNED-VALIDATION` — respect is not agreement |
| "Don't over-warn" | `CAVEAT-BOMBING` — librarians don't interrogate patrons |
| "Be accurate" | `CLAIM-LEDGER` — CONFIRM / DISPUTE / ASK, for each claim, first |

**Why:** a name is a K-line (P1). The model can check output against a named pattern. It can't
check against a vibe. This is P1 applied to behavior instead of concepts.

**The cost:** each named constraint is context tax forever. Six good ones beat twenty
mediocre ones.

---

## P12 · Delay tokenization

**MOOLLM origin:** SPEED-OF-LIGHT, the Carrier Pigeon critique.

> Inside the model: high-dimensional vectors, precise, instant.
> At the boundary: serial tokens, lossy, slow.

Every agent hop across an API costs latency *and* precision. If five "agents" are five calls to
one model, you paid twice to simulate a separation one call could have held.

**Why:** one forward pass holding five personas has better coherence than five passes passing
notes, and no network in between.

**The cost, which MOOLLM names in one line and drops:** shared activations mean correlated
blind spots. In-context personas are not independent. For brainstorming, that's fine. For
red-teaming, the correlation is exactly the thing you're trying to break — pay the boundary
tax, use separate calls, ideally separate models.

---

## The principles as a whole

| # | Principle | One line |
|---|---|---|
| P1 | Point at known knowledge | Latent is prepaid; jargon is billed forever |
| P2 | Cheapest useful resolution | Never load a tier without the tier above |
| P3 | Units declare relevance | Adding a capability = adding a directory |
| P4 | Identity is location | Discovery is `ls`; git is the database |
| P5 | State lives in files | Attention becomes a document you can fix |
| P6 | Model advises, other decides | Build the decider or admit you didn't |
| P7 | Liberal in, conservative out | The model reads intent for free |
| P8 | Validate what you authored | Postel is for peers, not your own config |
| P9 | Never crash, degrade | Runtime shrugs; authoring stops |
| P10 | Use the free channel | Prepaid. Inline it. Budget 2K. |
| P11 | Name the failure mode | A name is checkable; a vibe isn't |
| P12 | Delay tokenization | The boundary is lossy and slow — cross it deliberately |

P1 is the keystone. P8 is the correction. Everything else follows.

Next: [03-glossary.md](03-glossary.md) — the translation table.
