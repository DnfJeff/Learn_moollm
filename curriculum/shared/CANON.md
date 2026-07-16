# CANON — Source of Truth for the Document Series

Every document in `spec/`, `kit/`, and `onramp/` uses the names, numbers, and definitions on
this page exactly. A rename happens here first, then propagates. Nothing on this page is
explained — that's what the tiers are for; this page only *fixes* terms.

Primary source of truth: [MOOLLM on GitHub](https://github.com/SimHacker/moollm) (read-only).
Evidence lens: [`../../study/`](../../study/) (corrected as needed).

---

## The paradigm name

**Spec name (Set A):** **the Legible Workspace** — a file-native architecture for context
orchestration. Usage: "the Legible Workspace pattern"; the discipline it belongs to is
*context engineering* (an established term the spec should attach to, not compete with).

**Why this name:** legibility — every piece of the agent's knowledge, attention, policy, and
routing is plain text a human can open — is the one property all ten mechanisms serve, and
"legible" is a word already dense in the model's and readers' vocabulary. Novel jargon is
the documented anti-pattern (M9); this name is made of prepaid words.

**Tier phrasings** (recorded so paraphrase doesn't drift):

| Tier | Allowed phrasing |
|---|---|
| Set A | the Legible Workspace; file-native context orchestration |
| Set B | the Legible Workspace; "the workspace pattern" after first use |
| Set C | "the workspace approach"; "everything on paper" as the informal hook |

**Runners-up** (recorded for the provenance doc; do not use as the name):
Context-Resident Orchestration, Filesystem-Native Orchestration, Resolution-Ladder
Orchestration.

**Provenance sentence** (must appear in every set's opening doc, adapted to register): the
mechanisms originate in **MOOLLM** by **Don Hopkins** (SimHacker/moollm); this series is a
domain-neutral presentation of them, with credit, not a replacement.

---

## The ten mechanisms

Canonical order = teaching order. Every tier covers all ten, in this order, under these
names. "MOOLLM name" is for the provenance/glossary docs; series prose uses the canonical
name only.

| # | Canonical name | One-line definition | MOOLLM name | Set C analogy |
|---|---|---|---|---|
| **M1** | **Resolution ladder** | Every unit is written at several sizes; read the cheapest tier that answers your question, and never load a tier without the one above it. | Semantic Image Pyramid / MOO-Maps (GLANCE → CARD → SKILL → README) | A book: cover → table of contents → chapter → appendix. You don't read the appendix to find out what the book is about. |
| **M2** | **Declarative routing** | Each capability announces its own activation conditions and relevance score; selection is collect-score-pick, with no central router to maintain. | Advertisements (The Sims) | Shops on a street hang their own signs; nobody maintains a mall directory kiosk. A new shop just hangs a sign. |
| **M3** | **Host drivers** | One portable policy plus per-host adapter files that map abstract operations onto whatever tools the environment has, with declared fallbacks. | Drivers (kernel/drivers/) | A universal travel adapter: the appliance doesn't care which country's wall it's plugged into. |
| **M4** | **Externalized state** | The agent's memory *and attention* are small plain files — focus, keep-loaded, evicted, log, output — so sessions resume, humans audit, and attention itself is editable. | Files-as-State; hot/cold/working-set | A shared project binder on the table vs. "it's all in Dave's head." Anyone can open the binder, and Dave can be sick. |
| **M5** | **Standing constraints** | Always-on behavioral rules that shape every response without being invoked or re-argued, each naming the failure mode it forbids. | Ambient Skills; the no-ai-* suite | House rules posted on the wall: nobody re-negotiates "no shoes inside" every time a guest arrives. |
| **M6** | **Boot compilation** | Compile what every session actually needs into the file the host auto-loads, and refine it each cycle: work → introspect → compile → boot. | cursor-mirror OPTIMIZE; bootstrap (PROBE → DETECT-DRIVER → SETUP → WARM-CONTEXT → STARTUP) | Mise en place: the chef preps tonight's station from what last night's service actually used. |
| **M7** | **In-context ensemble** | Simulate several perspectives, turns, or roles inside one model call instead of paying a lossy, slow serialization boundary between separate calls. | Speed of Light (vs. Carrier Pigeon) | A panel discussion in one room vs. mailing letters between experts and waiting weeks per exchange. |
| **M8** | **Directory-as-object** | A capability's identity is its path; its interfaces are marker files; discovery is listing the directory; units are prototypes that instantiate stateful copies. | Selfish COM; DIRECTORY-AS-OBJECT; prototypes (Self) | One labeled folder per client: the folder *is* the record, and its tabs tell you every role it plays. |
| **M9** | **Names as addresses** | The right name activates knowledge the model already has, for one token; novel jargon is a cache miss billed on every call, forever. | K-lines (Minsky); PROTOCOLS.yml | Telling a session band "play it Motown" — one word summons a whole tradition no sheet music could spell out. |
| **M10** | **Tolerant interpretation** | Accept sloppy, partial, or malformed input; emit clean output; treat missing state as something to repair, never a reason to crash. | POSTEL; robust-first; self-healing protocol; repair demons | A good waiter: accepts "the, uh… chicken thing," sends a precise ticket to the kitchen. |

---

## Cross-cutting principles

Not mechanisms — properties that span them. Same rule: these names, everywhere.

| # | Canonical name | One-line definition | Set C analogy |
|---|---|---|---|
| **P1** | **The dual-mode contract** | Every control file works under two runtimes: *operational* (an orchestrator parses and enforces it) or *advisory* (the model reads it and self-manages). Same files; enforcement is an upgrade, not a prerequisite. | Directions that work as GPS turn-by-turn when the car supports it, and as a printed map when it doesn't. |
| **P2** | **The determinism split** | Everything mechanical and repeatable goes in scripts; the model is reserved for judgment, creativity, and language. | The spreadsheet adds the columns; the accountant decides what the numbers mean. |
| **P3** | **Rewrite, not truncate** | Each ladder tier is an editorial judgment about what a reader needs at that depth — never the first N lines of the tier below. Auto-truncation destroys the value. | A movie trailer is not the first two minutes of the film. |

---

## The capability-unit anatomy

The construction standard for one unit (spec reference: study
[analysis/06-capability-anatomy.md](../../study/analysis/06-capability-anatomy.md);
normative version to be written into Set A's MECHANISMS doc under M1/M8):

- Four-file contract: `GLANCE` / `CARD` / `SKILL` / `README` (A1)
- 50-line sniff contract for every file, scripts included (A2)
- Card sections: identity, files-index, k-lines, invoke_when, methods (signatures only),
  advertisements, drivers, warming priorities, resolution hints (A3)
- Always-on = an advertisement with `condition: always` + `scope` + `resolution` (A3)
- Prose index with the reading protocol printed at its top; declared load order (A4)
- Instance libraries + path/fragment refs + the promotion pattern (A5)
- Instantiation modes: mentioned → modeled → embedded → instantiated (A6)
- Typed precondition gates: hidden / visible-but-blocked / available, with reason types (A7)

---

## Count reconciliation

Older documents compress the list. For the record: the study README's "six" = M1–M5 + M7;
the study framework's "seven requirements" table groups M8 into discovery and P1 into
correctability. **The series always says ten mechanisms, three principles.** When citing the
study, cite the inventory (ten), not the compressions.

---

## Glossary seeds (canonical ↔ MOOLLM ↔ plain)

Full tables live in `kit/GLOSSARY.md` and `onramp/PLAIN-GLOSSARY.md`; this is the seed both
must agree with:

| Canonical | MOOLLM | Plain (Set C) |
|---|---|---|
| capability unit | skill | a how-to the assistant can pick up |
| unit catalog | skills/INDEX.md | the table of contents |
| glance / card / skill / readme | GLANCE.yml / CARD.yml / SKILL.md / README.md | blurb / menu / manual / backstory |
| attention files | .moollm/ (hot, cold, working-set) | the assistant's desk: what's out, what's filed |
| session log / output | session-log.md / output.md | the lab notebook / the deliverable |
| driver | kernel/drivers/*.yml | the travel adapter |
| standing constraint | ambient skill (no-ai-*) | house rule |
| advertisement | advertisement | the sign a shop hangs |
| boot file | .cursorrules / CLAUDE.md / AGENT.md | the morning briefing |
