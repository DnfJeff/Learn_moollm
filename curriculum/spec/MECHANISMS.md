# The Legible Workspace — Mechanism Reference

> **Tier:** Specification · plainer: [kit/guides/](../kit/guides/) · evidence: [study/](../../study/)

This is the normative reference for the Legible Workspace pattern: ten mechanisms and three
cross-cutting principles, as fixed in [shared/CANON.md](../shared/CANON.md). Each section
states what the mechanism is, the rules that make it work (**MUST** / **SHOULD** / **MAY**,
used in the RFC-2119 sense), its file contract, how it interacts with the others, and its
known degenerate cases.

The mechanisms originate in **MOOLLM** by **Don Hopkins** (SimHacker/moollm); this document
presents them domain-neutrally, with credit. Where a rule's effectiveness has been measured,
the number lives in [EVIDENCE.md](EVIDENCE.md); where a rule is aspiration rather than
practice even in the origin system, that is said in place.

---

## The workspace shape

A conforming workspace has four zones. Names below are the reference names; the driver layer
(M3) may map them onto host conventions.

```
project/
├── AGENT.md               The boot file — whatever this host auto-loads (M6).
│                          Standing constraints inline (M5). Pointers, not copies.
├── .agent/                Attention and session state (M4). Typically gitignored.
│   ├── working-set.yml      Current focus
│   ├── hot.yml              Keep loaded
│   ├── cold.yml             Evicted, with breadcrumbs
│   ├── session-log.md       What happened (append-only)
│   └── output.md            Results for the human (append-only)
├── policy/                Portable rules (M5) + host adapters (M3).
│   ├── core.md
│   └── drivers/<host>.yml
└── capabilities/          The unit library (M1, M2, M8).
    ├── INDEX.md             Prose catalog; reading protocol printed at top
    └── <unit>/              One directory per capability unit
        ├── GLANCE.yml       ~400 tokens   "Is this relevant?"
        ├── CARD.yml         ~1,400        "What can it do? How do I call it?"
        ├── SKILL.md         ~2,800        "How does it work?"     (optional)
        └── README.md        ~1,200        "Why is it like this?"  (optional)
```

Everything in all four zones **MUST** be plain text a human can open, diff, and edit. That
property — legibility — is not one mechanism among the ten; it is the invariant the ten
exist to preserve.

---

## M1 · Resolution ladder

Every capability unit is written at several sizes; a reader loads the cheapest tier that
answers the current question.

**Rules**

1. A unit **MUST** provide at least two tiers: a catalog entry (one line to one paragraph)
   and an interface (`CARD`). It **SHOULD** provide all four: glance, card, skill, readme.
2. A reader **MUST NOT** load a tier without having loaded the tier above it. (The single
   discipline the whole mechanism rests on.)
3. Each tier **MUST** be *rewritten* for its depth, never truncated from the tier below
   (**P3**). Auto-generated summaries defeat the mechanism: the tier boundary is an
   editorial judgment about what a reader needs at that depth.
4. Tiers answer fixed questions, in order: *does it exist? → is it relevant? → how do I call
   it? → how does it work? → why is it like this?* Most reads **SHOULD** stop at the card.
5. Every file, not just units, **SHOULD** obey the 50-line sniff contract: its first ~50
   lines (frontmatter, purpose, file map — or for scripts: docstring, imports, constants,
   CLI surface) suffice to decide whether to keep reading.

**Why it works:** a corpus far larger than any context window becomes navigable from an
index two orders of magnitude smaller, because choosing and using need different depths.
Measured on the origin corpus: ~790K tokens navigable from a ~5K-token index (see
EVIDENCE.md).

**Degenerate cases:** tier drift (counts and content falling out of sync across tiers —
observed in the origin repo); glance inflation (glances growing until they are cards);
truncation masquerading as rewriting.

---

## M2 · Declarative routing

Each capability announces its own activation conditions and relevance score; selection is
collect → score against context → take the top. There is no central router.

**Rules**

1. A unit's card **MUST** carry an `advertisements:` block: named offers, each with a
   `score` (0–100 baseline relevance) and a `condition` (plain-language trigger).
2. Adding a capability **MUST NOT** require editing any other file except the catalog entry.
   The router-knowledge is O(1) per unit, never O(n) in one place.
3. Advertisements **MAY** appear on anything — a directory, a file, a section of a data
   file — not only on units.
4. Always-on behavior is declared as an advertisement, not a separate mechanism: an ad with
   `condition: always` plus `scope` (how long it persists) and `resolution` (how much of the
   unit stays loaded). See M5.
5. Conditions **SHOULD** state preconditions that gate *visibility*, not only desirability;
   an option that cannot run in this host or context **SHOULD NOT** enter the routing set,
   and a shown-but-unavailable option **SHOULD** carry a typed reason (blocked / missing
   requirement) rather than a generic failure.

**Honest limit:** in the reference implementation the "scoring engine" is the model reading
YAML. Conditions are suggestions interpreted in context, not expressions evaluated by an
engine. This is adequate for soft routing and **MUST NOT** be relied on where routing needs
determinism — that case belongs in a script (**P2**).

**Degenerate cases:** index-as-router (the catalog accreting per-unit dispatch logic until
it is a central router again); score inflation (every unit claiming 95+).

---

## M3 · Host drivers

One portable policy; per-host adapter files map abstract operations onto whatever tools the
environment actually has.

**Rules**

1. A driver file **MUST** declare: detection (how to recognize this host), capabilities
   (booleans/enums for what works here), tool mappings (abstract op → concrete tool name),
   paths (where session files live on this host), and adaptations (a fallback for every
   capability it lacks).
2. Policy documents **MUST NOT** name concrete host tools; they name abstract operations
   that drivers resolve.
3. Every unsupported feature **MUST** have a declared fallback, even if the fallback is
   "by convention only." A conventions-only fallback is a valid floor, not a defect — see
   **P1**.
4. A `generic` driver **MUST** exist and assume nothing beyond read/write/list.
5. Drivers **SHOULD** declare host tiers (from minimal to full-control) so units can adapt
   behavior by tier rather than by host name.

**Degenerate cases:** policy leaking hostisms; driver files growing host-specific *policy*
(they carry mappings, not rules).

---

## M4 · Externalized state

The agent's memory *and its attention* are small plain files. Nothing the agent knows,
wants, or is focused on lives only in the conversation.

**Rules**

1. The session zone **MUST** contain, at minimum: a working set (current focus), a log
   (append-only record of what happened), and an output file (append-only, user-facing).
   It **SHOULD** also contain hot (keep-loaded hints) and cold (evicted items, each with a
   breadcrumb sufficient to re-find it).
2. `session-log.md` and `output.md` are **append-only**. History is never rewritten;
   corrections are new entries.
3. Mutable state lives in editable files; narrative lives in append-only files. An object
   embedded in a log **MAY** be read in place (fragment addressing), but the moment it needs
   *editing* it **MUST** be promoted to its own state file (the promotion pattern).
4. A new session **MUST** be able to resume from the session zone alone, without replaying
   conversation history.
5. The human may edit any of these files at any time; the agent **MUST** treat the files,
   not its recollection, as authoritative.

**The underrated consequence:** attention becomes an artifact. "What is the agent focused
on" stops being a vague property of a conversation and becomes a 600-byte file you can read,
diff, and fix.

**Degenerate cases:** state drift (files describing a focus the session no longer has —
write-back discipline is the cost of the mechanism); log-as-state (mutable data trapped in
append-only files because promotion never happens).

---

## M5 · Standing constraints

Always-on behavioral rules that shape every response without being invoked, each one naming
the failure mode it forbids.

**Rules**

1. A standing constraint is a unit like any other, declared always-on via the unified ad
   form (M2 rule 4): `condition: always`, plus `scope` and `resolution`.
2. Each constraint **MUST** name its target failure modes as short, checkable handles
   (e.g. CERTAINTY-THEATER, EUPHEMISM-LAUNDERING) and give the one-line corrective. Naming
   the failure is most of the fix: a named pattern is something output can be checked
   against; "be concise" is not.
3. Constraints are a permanent context tax. The active set **MUST** be budgeted (each
   declares its `resolution` — how much of it stays resident), and the always-on subset
   **SHOULD** be compiled into the boot file (M6) rather than loaded from N files.
4. Constraints **MUST** be stated as behavioral rules, not values essays. One page maximum
   at resident resolution.

**Degenerate cases:** constraint bloat (the rent-free set growing until it crowds out
work); vague constraints (unfalsifiable virtues instead of named failure modes).

---

## M6 · Boot compilation

Compile what every session actually needs into the file the host auto-loads, and refine the
compilation each cycle.

**Rules**

1. Every host has a free channel — a file loaded at session start regardless
   (`.cursorrules`, `CLAUDE.md`, `AGENT.md`, a system prompt). The always-needed subset
   (standing constraints at resident resolution, the reading protocol, pointers to the
   catalog and session zone) **SHOULD** live *inlined* there, converting N reads into zero.
2. The boot file carries **pointers, not copies**, for everything below the always-needed
   bar.
3. Session start **SHOULD** follow a declared sequence: probe the environment → detect the
   driver (M3) → repair the session zone if damaged (M10) → warm the context in declared
   priority order (critical → high → medium) → begin.
4. The loop is **work → introspect → compile → boot**: periodically review what recent
   sessions actually loaded and re-compile the boot file accordingly. The introspection step
   **MAY** be manual; the origin system's automated introspector is host-specific.
5. Compiled content **MUST** remain human-readable. The boot file is part of the workspace,
   not a build artifact exempt from legibility.

**Degenerate cases:** boot bloat (the free channel isn't free past the model's attention
budget — compile *out* as well as in); stale compilation (the boot file preloading last
quarter's project).

---

## M7 · In-context ensemble

Simulate several perspectives, roles, or turns inside one model call rather than paying a
serialization boundary between separate calls.

**Rules**

1. Work that fits one context **SHOULD** stay in one call: multi-perspective review, debate,
   role-played turns, tightly-coupled pipelines. Each avoided boundary saves latency, cost,
   and the precision lost to detokenize→retokenize round-trips.
2. Split into separate calls (cells) when: the work genuinely exceeds one context;
   independent streams don't converse; fault isolation or parallelism is worth the tax.
   Between cells, messages **MUST** be serialized once at the boundary — files, not chatter
   — and each cell runs in-context internally.
3. An ensemble **MUST** declare its perspectives (who is present, what each optimizes for)
   in state files rather than improvising them per turn, or the perspectives collapse into
   one voice.
4. **The independence caveat is normative:** personas in one forward pass share activations
   and are correlated in ways separate calls are not. For brainstorming and shape-of-the-
   opinion-space work, in-context wins. Where *independent* failure detection is the goal
   (red-teaming, second opinions), separate calls — ideally separate models — **MUST** be
   used despite the cost. In-context committees find the shape of a distribution; they do
   not simulate independent judges.

**Degenerate cases:** herd behavior mistaken for consensus; theater (many named voices, one
opinion); using ensemble where a script should decide (**P2**).

---

## M8 · Directory-as-object

A capability's identity is its path; its interfaces are marker files; discovery is listing
the directory.

**Rules**

1. One unit = one directory. The path is the unit's identity and its reference address.
2. Marker files are interfaces: a directory *is* whatever its marker files say
   (`CARD.yml` = routable capability; additional markers = additional interfaces). Interface
   query is a file-existence check.
3. Discovery **MUST** be `ls`-shaped: no registry, no manifest to sync, no build step.
   Adding a directory creates the capability; the catalog entry is the only other touch
   (M2 rule 2).
4. Units are **prototypes**: they may ship templates and an instance library (pre-made
   instances as subdirectory / single file / bundled index), and instantiation copies a
   template into a new directory that carries its own state. Behavior stays in the
   prototype; state lives in instances.
5. Instances and catalog entries are referenced by path, with fragment addressing into
   bundles (`path/INDEX.yml#entry`).
6. Instantiation has a cost dial, cheapest first — *mentioned* (name only, no files) →
   *modeled* (in-conversation only) → *embedded* (inside another document) → *instantiated*
   (full stateful directory) — and use **SHOULD** start at the cheap end.
7. Prototype-chain inheritance (`parents:` resolution) **MAY** be implemented but **SHOULD**
   be deferred until a demonstrated need; identity-path + marker-interface + `ls`-discovery
   is the load-bearing 80%.

**Degenerate cases:** ceremony creep (four files and an inheritance chain for a two-line
helper); registry regression (a generated manifest becoming load-bearing).

---

## M9 · Names as addresses

The right name activates knowledge the model already has, for approximately one token.
Novel jargon is a cache miss billed on every call, forever.

**Rules**

1. Prefer names that are already dense in the model's training distribution. The test:
   *is the pointee in latent space?* If yes, point — the name is the activation. If no,
   spell it out **once, in a file**, and thereafter use the name you gave it.
2. The workspace **SHOULD** maintain a symbol index: name → one-line meaning → where it's
   defined → when to invoke it. This is the project's controlled vocabulary.
3. Catalog and file names are part of the addressing system: a directory listing is an
   index, so names **MUST** be written to be read in listings (most-significant component
   first, so related files sort together and side-car files cluster with their subject).
4. The catalog **SHOULD** be prose, not tables: a narrative index whose marked terms are
   exactly the unit names, grouped so that reading order is dependency order. Prose carries
   relationships that repeated keys cannot, at lower token cost.
5. Do not re-teach the model what a name already activates (the humansplaining
   anti-pattern). One name beats a paragraph that paraphrases the name badly.

**The tension, stated honestly:** the same mechanism that makes names free for the model
makes them expensive for humans who lack the codebook. Every coined term **MUST** clear a
higher bar than every borrowed one — this is why the origin system's game vocabulary reads
as noise to outsiders while costing the model nothing.

**Degenerate cases:** private jargon accretion; codebook capture (the metaphor layer doing
real work nobody can name anymore — the original motivation for this entire series).

---

## M10 · Tolerant interpretation

Accept sloppy, partial, or malformed input; emit clean, well-formed output; treat missing
or damaged state as something to repair, never a reason to crash.

**Rules**

1. Inbound: interpret intent, not syntax. Misspellings, missing fields, format variants,
   and natural-language approximations of commands **MUST** be accepted where intent is
   recoverable; ambiguity worth resolving **SHOULD** be asked about, not guessed silently
   on consequential actions.
2. Outbound: emit strictly well-formed artifacts. Tolerance is asymmetric — liberal in,
   conservative out.
3. Missing canonical files are repaired, not fatal: session start and error paths **MUST**
   create minimal stubs for absent session-zone files (declared per file: what a minimal
   valid stub is). Repair actions **MUST** be logged.
4. Priority order under failure: survive → heal → function → optimize. A crashed system is
   infinitely wrong.
5. **The flip side is normative:** where the model is the parser, malformed state is
   *silent*. Anything whose malformation must be *detected* rather than absorbed — money,
   auth, irreversible actions, counts you report to humans — **MUST** be validated by a
   script (**P2**), because tolerant interpretation will paper over exactly the corruption
   you needed to see.

**Degenerate cases:** silent absorption of meaningful corruption (the origin repo shipped a
broken YAML boot file for months *because* everything tolerated it); repair loops
(regenerating stubs that something else keeps deleting).

---

## P1 · The dual-mode contract

Every control file in the workspace works under two runtimes:

| Mode | The files are | Acted on by |
|---|---|---|
| **Operational** | Commands — parsed, enforced, injected | An orchestrator that understands them |
| **Advisory** | Conventions — read and self-applied | The model itself |

**Rules**

1. Control files **MUST** be written to function in advisory mode, because that is the floor
   every generic host provides. Enforcement is an upgrade, not a prerequisite.
2. A document **MUST NOT** describe advisory-mode operation as "unimplemented." The
   designed floor of the contract is not a missing feature.
3. In advisory mode, control files **MAY** run in reverse — generated as *mirrors* of what
   the host actually loaded rather than commands for what it should load. A mirror is a
   valid conforming use.

## P2 · The determinism split

Everything mechanical and repeatable goes in scripts; the model is reserved for judgment,
creativity, and language.

**Rules**

1. When a consistent, mechanical sub-procedure emerges inside a capability, it **MUST** be
   lifted out of prose into a script the unit ships. The doc shrinks to judgment.
2. Validation of anything that must be *correct* rather than *plausible* — counts, money,
   schemas, irreversible steps — belongs to scripts (see M10 rule 5, M2's determinism
   limit).
3. Scripts obey the same legibility rules as documents: sniffable structure, self-describing
   help, first-50-lines contract.

## P3 · Rewrite, not truncate

Each resolution-ladder tier is an editorial judgment about what a reader needs at that
depth. Stated as its own principle because it is the most tempting corner to cut and the
one that silently destroys M1: a truncated card is not a card, it is the top of a skill.
Anything that auto-generates tiers **MUST** be treated as producing drafts for editing, not
artifacts for shipping.

---

## Conformance levels

Adoption is incremental by design (this ordering is also the retrofit order, Set B B13):

| Level | Requires | You get |
|---|---|---|
| **1 — Legible state** | M4 + M10 (session zone, append-only logs, stub repair) | Resumable, auditable sessions |
| **2 — Legible library** | + M1, M8, M9 (units, ladder, catalog, naming) | A capability corpus larger than context |
| **3 — Self-routing** | + M2, M5 (advertisements, standing constraints) | Extension without central edits; stable behavior |
| **4 — Portable & tuned** | + M3, M6 (drivers, boot compilation) | Same workspace across hosts; cheap session starts |
| **5 — Ensemble-aware** | + M7 (with its independence caveat) | Multi-perspective work priced correctly |

P1–P3 apply at every level.

---

*Next in Set A:* [WHITEPAPER.md](WHITEPAPER.md) (the argument), [EVIDENCE.md](EVIDENCE.md)
(the numbers), [PROVENANCE.md](PROVENANCE.md) (the credit).
