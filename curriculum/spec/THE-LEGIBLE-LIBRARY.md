# The Legible Library — a durable collection layer for the Legible Workspace

> **Tier:** Specification (layer) · substrate: [MECHANISMS.md](MECHANISMS.md) · adapts: the Knowledge Library System overview (v1.0, 2026-07-18)

The [Legible Workspace](MECHANISMS.md) is a *desk*: a session-scoped set of capabilities and
attention files an agent works from and clears away. This document specifies a *library* built
on the same desk — a permanent, classified, cross-project collection meant to be the reliable
long-term "everything" brain space: every finding, specification, decision, and reference,
kept for years, browsable by a human, and navigable by an agent that will never fit it in one
context window.

The claim of this layer is deliberately small. **It introduces no new mechanism.** A durable
knowledge library is the ten mechanisms of the Legible Workspace applied at *collection* scale
instead of *session* scale, plus one thing the base pattern leaves to the user: a predefined,
opinionated scaffold — a classification scheme, a controlled vocabulary, finding aids, and
intake rules — shipped ready to copy. The library-grade rigor is the goal; the mechanisms are
how it stays legible instead of collapsing into a folder swamp.

The mechanisms originate in **MOOLLM** by **Don Hopkins** (SimHacker/moollm); this layer
presents them at archive scale, with credit. The library discipline it adapts — classification,
controlled vocabulary, finding aids, provenance, collocation, and preservation — comes from the
**Knowledge Library System overview (v1.0)**, re-expressed here in Legible Workspace terms
rather than added alongside them. Where the two traditions name the same move, the workspace
name wins and the library term becomes a gloss.

**The name.** *The Legible Library* is made of prepaid words (M9): parallel to *the Legible
Workspace*, and saying exactly what it is — a large collection whose every part is plain text a
human can open. It names a **layer**, not a mechanism; it redefines nothing in
[CANON.md](../shared/CANON.md). Rule numbers below use the **L** namespace (Library) so they
never collide with the canonical **M**/**P** numbers they draw on.

---

## The shape

The library is a second zone beside the workspace's four. It is **permanent and versioned**,
where `.agent/` is disposable session state — the two must not be confused.

```
project/
├── AGENT.md               Boot file (M6). Gains a pointer to the library catalog.
├── .agent/                Session attention (M4). Disposable. NOT the library.
├── policy/                Rules (M5) + host drivers (M3), incl. the Obsidian driver (L9).
├── capabilities/          Executable units — the workspace's how-to corpus.
└── library/               THE COLLECTION — permanent, git-tracked, the brain space.
    ├── INDEX.md             Prose master catalog; reading protocol printed at top (L4).
    ├── meta/                Finding aids + the ontology + the evolution log.
    │   ├── ontology.md        Controlled vocabulary = the symbol index (L4)
    │   ├── by-domain.md       ·
    │   ├── by-project.md      ·  Curated access paths — alternate ladders into the
    │   ├── by-tag.md          ·  same units (L4)
    │   ├── by-stage.md        ·
    │   └── structure-log.md   Append-only record of every structural change (L6)
    ├── domains/             PROTOTYPES — permanent, reusable, cross-project knowledge (L3)
    │   └── <class>/           A classification class; its README is a finding aid (L2)
    │       └── <unit>.md      One atomic note: glance frontmatter → body (L1, L2)
    ├── projects/            INSTANCES — time-bound work, instantiated from templates (L3)
    │   └── <project>/         research/ content-maps/ roadmaps/ job-cards/
    │                          execution-logs/ specs/ references/
    ├── inbox/               Liberal intake. No classification required at the door (L5)
    └── archives/            Superseded, not deleted. Provenance preserved (L6)
```

Everything in `library/` **MUST** be plain text — Markdown with YAML frontmatter — for the same
reason the workspace is: legibility is the invariant the mechanisms exist to preserve, and a
brain space you can only read through one tool is not a brain space you own.

---

## The reframe: a library is the ten mechanisms at collection scale

Every rule of a professional knowledge library maps onto a mechanism the Legible Workspace
already has. The library layer is the mapping made concrete, not a parallel rulebook.

| Library discipline (from the KLS overview) | Is this Legible Workspace mechanism, at collection scale |
|---|---|
| Single source of truth + version control | **M4** externalized state; the legibility invariant; git as the audit trail |
| Atomicity with explicit relationships | **M8** directory-as-object (one unit = one addressable thing) + **M1** links between tiers |
| Projects vs Domains separation | **M8** prototype/instance dial — domains are prototypes, projects are instances (**L3**) |
| Library-grade classification (DDC/LCC-style) | **M1** resolution ladder applied to the *collection*: class → subclass → unit (**L2**) |
| Controlled vocabulary & ontology | **M9** names as addresses — the ontology *is* the symbol index (**L4**) |
| Finding aids, master indexes, multiple access paths | **M1** + the prose catalog (**M9**); one collection, many ladders into it (**L4**) |
| Low-friction intake (`inbox/`), incremental adoption | **M10** tolerant interpretation — liberal in, classify later (**L5**) + conformance levels |
| Preservation & provenance mindset | **M4** append-only logs + git + frontmatter provenance (**L6**) |
| Human oversight with AI augmentation | **P2** determinism split + **P1** dual-mode + **M5** standing constraints (**L7**, **L8**) |
| Evolvable but deliberate structure | **M6** boot/compile loop + an append-only `structure-log.md` (**L6**, **L8**) |
| No fragmentation; hybridize by synthesis | **M5** a standing constraint: one canonical collection (**L7**) |

The rest of this document states the nine library rules (**L1–L9**) that fall out of that
mapping, then ships the predefined scaffold that makes them usable on day one.

---

## L1 · The collection is permanent state, not session state

A knowledge unit is a small, focused file — one finding, one specification, one decision, one
reference — that outlives every session that touches it.

**Rules**

1. `library/` **MUST** be git-tracked and **MUST NOT** be gitignored. It is the opposite of
   `.agent/`: the session zone is disposable working memory (**M4**); the library is the
   preserved record. A file that belongs in both is promoted from the log to the library (the
   promotion pattern, **M4** rule 3), never left only in session state.
2. A unit **SHOULD** hold one concept. Monolithic documents are legitimate only as an explicit
   `inbox/` staging item or a top-level overview, and carry that status in frontmatter (**L6**).
3. Relationships are **explicit links between units**, not implied by folder proximity alone.
   Collocation (**L2**) and linking are complementary: the folder says what class a unit is in;
   the links say what else it touches.
4. History is **append-only** where it is narrative (`structure-log.md`, execution logs) and
   **editable** where it is state (a unit under active revision). Never both in one file.

**Why it works:** the same discipline that lets a session resume from `.agent/` alone lets the
library be trusted as the source of truth — the record is on paper, not in anyone's head or any
one conversation.

---

## L2 · Classes are ladders, not folders

Library classification (Dewey, Library of Congress) and the resolution ladder (**M1**) are the
same move seen from two traditions: broad class → narrower subclass → the item, each level
readable before you descend. The library layer builds classification *as* the ladder.

**Rules**

1. `domains/` **MUST** be organized as a hierarchy of classes (broad) and subclasses (narrow).
   The primary organization is this hierarchy; it is the collection's spine (**M1**).
2. Every non-trivial class directory **MUST** carry a `README.md` that is a **finding aid**: a
   collection-level glance — what lives in this class, how it's subdivided, the entry points.
   A class README is to its shelf what a `GLANCE.yml` is to a unit. Reading it **MUST** be
   sufficient to decide whether to descend.
3. Each finding aid is **rewritten for its level, never truncated** from the units below it
   (**P3**). A class README is a curated map, not the concatenated first lines of its files.
4. When a unit could sit in a project or a domain, it **SHOULD** default to `domains/` — the
   permanent, reusable side — for longevity (see **L3**).
5. Classification is **secondary-indexed** by facets (**L4**), not only by the primary tree: a
   unit lives in one class but is reachable by many tags. One home, many doors.

**The scaling property:** M1 is usually stated for one unit at four sizes. L2 is M1 for the
*whole collection* at nested sizes — catalog → class finding aid → subclass finding aid → unit
glance → unit body. A library of thousands of units stays navigable from a catalog two orders
of magnitude smaller, for the same reason a 790K-token corpus is navigable from a ~5K-token
index (measured on the origin corpus; see [EVIDENCE.md](EVIDENCE.md)).

**Degenerate cases:** class explosion (classes multiplying until the catalog is a router again
— see **L4**); orphan units (files with no class and no `inbox/` status); finding-aid rot (a
class README describing last quarter's shelf).

---

## L3 · Domains are prototypes; projects are instances

The Knowledge Library System's central split — reusable **Domains** vs time-bound **Projects** —
is not a new idea in this vocabulary. It is exactly **M8**'s prototype/instance distinction:

| KLS term | Legible Workspace term | Holds | Lifespan |
|---|---|---|---|
| **Domain** | **prototype** | Reusable, cross-project knowledge and reference | Permanent |
| **Project** | **instance** | Time-bound work instantiated from workflow templates | Bounded; then archived |

**Rules**

1. `domains/` **MUST** hold only material that outlives any single initiative: format
   reverse-engineering, architectural patterns, security techniques, reference specs. Behavior
   and durable knowledge live in the prototype (**M8** rule 4).
2. `projects/` **MUST** hold initiative-scoped work, each project a directory mirroring the
   workflow stages (research/ content-maps/ roadmaps/ job-cards/ execution-logs/ specs/
   references/). Projects are **instances**: they carry their own state and are instantiated
   from the workflow templates (**L8**, the predefined scaffold).
3. A discovery made *inside* a project that proves reusable **MUST** be promoted into a domain
   unit — the instance graduates state into the prototype. This is the same graduation as
   **M8**'s promotion pattern, applied to knowledge: projects feed domains.
4. Instantiation obeys the cost dial (**M8** rule 6), cheapest first: a topic can be *mentioned*
   in a note, *modeled* in a project's research log, *embedded* in a spec, or *instantiated* as
   its own domain unit. Start light; instantiate a standalone unit when the concept earns it.
5. A completed project **SHOULD** be archived (**L6**), not deleted — but its reusable yield
   **MUST** already have been promoted to domains first, or the knowledge dies with the instance.

**Why this matters:** the split that a librarian defends on grounds of reuse and a MOOLLM defends
on grounds of prototypes-vs-instances is the *same split*. Naming it with the mechanism the
workspace already has means the library needs no second rulebook to explain it.

---

## L4 · The catalog is prose; the ontology is the symbol index

A library's controlled vocabulary and its finding aids are, in this vocabulary, **M9** (names as
addresses) and the prose catalog. The library ships them as first-class files under `meta/`.

**Rules**

1. `library/INDEX.md` **MUST** be a **prose** master catalog: flowing paragraphs where every
   bold term is exactly a class or unit name, spelled as its path, and bold is used for nothing
   else. Prose carries relationships repeated YAML keys cannot, at lower token cost (**M9** rule
   4). The **reading protocol MUST be printed at its top**: resolution order, when to stop, how
   the finding aids relate. The catalog teaches how to read the catalog.
2. `meta/ontology.md` **MUST** be the **controlled vocabulary**: the project's authority list of
   preferred terms — each a name → one-line meaning → where it is defined → when to apply it.
   This file *is* the symbol index of **M9**. New terminology is introduced deliberately, here,
   once; thereafter the name is the address.
3. Secondary access paths (`by-domain.md`, `by-project.md`, `by-tag.md`, `by-stage.md`) are
   **alternate ladders into the same units** — curated finding aids, not copies. A unit is
   written once and reached many ways; no access path may hold content that isn't a pointer.
4. Facet tags **MUST** be drawn from the ontology, not coined ad hoc at filing time. A tag that
   isn't in `ontology.md` isn't a facet yet — it's a candidate to be added there deliberately.
5. Coined terms clear a higher bar than borrowed ones (**M9**): prefer names already dense in
   both the model's and a domain expert's vocabulary. Every private tag is a cache miss for the
   model *and* a codebook the next human has to learn.

**Degenerate cases:** ontology drift (tags proliferating uncontrolled until the vocabulary means
nothing — **M9**'s private-jargon accretion at collection scale); index-as-router (finding aids
accreting per-unit dispatch logic until the catalog is a central router, **M2**'s degenerate
case); catalog truncation (a master index that is the first lines of each class rather than a
written map — **P3** violation).

---

## L5 · Intake is tolerant; classification is deferred

The single most important rule for a library that actually grows: **capture must never wait on
classification.** This is **M10** (tolerant interpretation) at the scale of a collection.

**Rules**

1. New material of any kind — a link, a screenshot, a half-formed note, a snippet — **MUST** be
   accepted into `inbox/` with no required classification, schema, or naming ceremony. Liberal
   in (**M10** rule 1).
2. Triage happens on a human rhythm (daily/weekly), not at the door. Each `inbox/` item is
   **synthesized** — split into atomic units, classified into a domain or project, linked,
   indexed, and its facets reconciled against the ontology (**L4**) — then removed from `inbox/`.
3. Output of triage is **strictly well-formed** (**M10** rule 2): a classified, frontmattered,
   linked unit with provenance. Tolerance is asymmetric — sloppy in, clean out.
4. Missing or damaged structure is **repaired, not fatal** (**M10** rule 3): if a class README,
   an index, or the ontology is absent when it's needed, a minimal stub is created and the
   repair is logged in `structure-log.md`. A library never refuses an item because a shelf isn't
   built yet.
5. Anything whose correctness must be *verified* rather than *plausibly interpreted* — counts in
   an index, a claimed provenance date, whether a link resolves — **MUST** be checked by a script
   (**P2**, **M10** rule 5), because tolerant reading papers over exactly the drift you needed to
   catch. `validate.py` (from the base template) extends to the library: index counts, dangling
   links, units missing required frontmatter.

**Why it works:** perfect filing upfront is the failure mode that kills knowledge systems. The
inbox is the release valve that lets the collection improve through use instead of demanding
complete organization before the first note lands.

---

## L6 · Every unit carries provenance and status

Preservation is **M4**'s append-only discipline plus a frontmatter contract that makes each
unit self-describing about where it came from and how far it can be trusted.

**Rules**

1. Every significant unit **MUST** open with YAML frontmatter carrying at least:
   `status` (one of `draft` / `canonical` / `superseded`), `created`, `reviewed`,
   `provenance` (source + date of capture + any transformation applied), and `related` (links to
   adjacent units). The first ~50 lines — frontmatter + purpose — **MUST** suffice to decide
   whether to read on (the sniff contract, **M1** rule 5).
2. `status` is the trust dial. A `draft` unit is visible but flagged; a `canonical` unit is the
   authoritative statement; a `superseded` unit is kept for provenance, links forward to its
   replacement, and moves to `archives/`.
3. `structure-log.md` **MUST** be append-only and **MUST** record every structural change to the
   library — a new class, a renamed facet, a classification revision — with its rationale.
   Corrections are new entries; history is never rewritten (**M4** rule 2). This is the library's
   own changelog and the primary account of how the scheme evolved.
4. Superseded and purely historical material **MUST** move to `archives/`, not be deleted.
   Deletion destroys provenance; archiving preserves the audit trail while keeping active shelves
   clean. Git history is the finer-grained backstop.
5. Imported or synthesized external material **MUST** note its original source, capture date, and
   any transformation, in `provenance`. An unsourced claim in a canonical unit is a defect.

---

## L7 · One canonical collection (standing constraints)

The library's governance rules are **M5** standing constraints: always-on, each naming the
failure mode it forbids, declared as advertisements with `condition: always`. They belong in the
boot file (**M6**) at resident resolution so every session inherits them.

| Constraint | Forbids | The rule |
|---|---|---|
| **CANONICAL-COLLECTION** | Parallel truths / fragmentation | This library is the definitive home for synthesized, high-value knowledge. Valuable material living elsewhere is **migrated or synthesized in**, never mirrored. Other tools may hold scratch capture; they do not hold second copies of the truth. |
| **PROVENANCE-OR-IT-DIDNT-HAPPEN** | Orphaned, untraceable claims | A unit imported or synthesized from outside carries source, date, and transformation, or it stays in `inbox/`. |
| **ATOMIC-OR-STAGED** | Monolith creep | A unit is one concept, or it is explicitly `status: staging` in `inbox/`. No silent kitchen-sink documents in `domains/`. |
| **CLASSIFY-LAST** | Capture friction | Intake never blocks on classification (**L5**). Filing is a triage step, not a gate at the door. |

**Rules**

1. These constraints **MUST** be stated as checkable behavioral rules with named failure handles,
   not as values essays (**M5** rule 2, rule 4). "CANONICAL-COLLECTION" is something a session can
   check its output against; "keep things tidy" is not.
2. Hybridization with other note systems is **welcomed by synthesis, forbidden by duplication**:
   the practice when good material exists elsewhere is to migrate the canonical version here, not
   to maintain the same knowledge in two places (**CANONICAL-COLLECTION**).
3. The active constraint set is a context tax and **MUST** be budgeted (**M5** rule 3): compiled
   into the boot file, not loaded from four files each session.

---

## L8 · The workflow is the boot-compile loop

The Knowledge Library System's development cycle — Research → Documentation / Content-Mapping →
Roadmapping → Job-Card Creation → Execution → Review — is **M6**'s introspect-and-compile loop
with domain-specific stage names, and **P2**'s determinism split deciding what is a template
versus what is judgment.

**Rules**

1. Each workflow stage **MUST** have a template under the predefined scaffold
   (`workflows/templates/`, below), and a project instance (**L3**) is built by instantiating
   those templates. The mechanical shape of a roadmap or job card is a template (**P2**); its
   content is judgment.
2. The **Review** stage **MUST** write back into the library: update the affected finding aids,
   the ontology if new terms appeared, and `structure-log.md`. This closes the loop — work
   produces knowledge, and the knowledge is compiled back into the navigable structure (**M6**
   rule 4: work → introspect → compile → boot).
3. Job cards and content maps **SHOULD** reference the domain units they draw on by path
   (**M8**), so the workflow is wired to the collection rather than re-deriving it.
4. What recurs mechanically across projects — a checklist, a validation step, an index
   regeneration — **MUST** be lifted out of prose into a script the library ships (**P2** rule 1),
   and the stage doc shrinks to judgment.

---

## L9 · Obsidian is a driver, not the format

"Obsidian-browsable" is a host adaptation (**M3**), not a storage decision. Obsidian is one host
among several; the collection stays plain Markdown so it is equally legible in VS Code, on
GitHub, through ripgrep, or by an agent with only read/write/list.

**Rules**

1. The library **MUST** remain plain Markdown + YAML frontmatter with **relative-path links** as
   its portable floor. A `policy/drivers/obsidian.yml` driver maps the abstract navigation
   operations — link, backlink, list-a-class, facet-by-tag, graph-view — onto Obsidian's
   features, exactly as any host driver maps abstract ops onto concrete tools (**M3** rule 1).
2. Obsidian's `[[wikilink]]` resolution is **M9 made operational**: a link by *name* that
   resolves regardless of path is names-as-addresses enforced by the tool. Where the Obsidian
   driver is active, wikilinks **MAY** be used and Obsidian's backlink pane and graph view become
   live, generated finding aids — a **mirror** of the collection's structure (**P1** rule 3),
   read for free instead of hand-maintained.
3. On a generic host the same collection **MUST** stay fully usable through relative links and
   full-text search — Obsidian's graph and backlinks are an **upgrade of navigation authority,
   not a prerequisite** (**P1** rule 1). A brain space that only opens in one app is not legible.
4. The driver **MUST** declare a fallback for every Obsidian-specific feature it uses (**M3**
   rule 3): backlinks → `grep` for the unit name; graph view → the prose catalog and `by-*`
   finding aids; Dataview queries → a `validate.py`-generated static index. Convention-only
   fallbacks are a valid floor, not a defect.

**Degenerate cases:** wikilink lock-in (a collection that only resolves inside Obsidian — a
legibility violation and a portability trap); plugin dependence (finding aids that exist only as
live Dataview queries, unreadable when the plugin is absent — generate a static mirror).

---

## The predefined support — the shipped scaffold

The point of this layer is that the library-grade structure arrives **predefined**. You copy a
scaffold, not design one. In MOOLLM terms the scaffold is a **prototype with an instance library**
(anatomy A5): opinionated starter content you reference, copy, or extend by path — the same way
the base template ships a two-capability library to copy from.

The scaffold `library/` contains, ready to instantiate:

**1 · The collection skeleton** — the directory shape from *The shape* above, with `inbox/`,
`archives/`, `domains/`, `projects/`, and `meta/` present and each carrying a stub finding aid so
**L5** rule 4 (repair-not-fatal) never triggers on a fresh copy.

**2 · A concrete classification scheme** — an opinionated default set of top-level domain classes,
provided so classification starts populated rather than blank. This starter reflects the source
overview's own domains and is meant to be edited, not obeyed:

```
domains/
├── sims-1/                        Classic-game reverse engineering: formats, rendering,
│                                  asset pipeline, modding ecosystem, preservation strategy
├── web-platforms/                 Architecture, frontend, backend/database, storage/CDN,
│                                  security/sandboxing, deployment
├── ai-assisted-development/       Structured AI collaboration, prompt patterns, tool
│                                  comparisons, human-oversight checkpoints
├── reverse-engineering-general/   Techniques and tools beyond any single domain
└── archive-and-security-practices/ Complex-archive handling, upload/processing security,
                                    defensive design
```

Each ships a `README.md` finding-aid stub (**L2** rule 2) and a subclass sketch. Adding, renaming,
or removing a class is a `structure-log.md` entry (**L6** rule 3) — the scheme is a versioned
artifact, deliberately evolved.

**3 · An ontology skeleton** (`meta/ontology.md`) — a seeded controlled vocabulary (**L4** rule 2)
with the starter facets `reverse-engineering`, `security-pattern`, `deduplication`,
`format-parsing`, `community-insight`, `performance`, `preservation`, each with its one-line
meaning and when-to-apply. New facets are added here first, then used.

**4 · The finding-aid set** (`meta/by-domain.md`, `by-project.md`, `by-tag.md`, `by-stage.md`) —
the alternate ladders of **L4** rule 3, as stubs that fill in as units land.

**5 · The unit frontmatter template** — the **L6** rule 1 schema, as a `unit.md.tmpl` an agent or
human instantiates for each new note:

```yaml
---
status: draft            # draft | canonical | superseded
created: 2026-07-18
reviewed: 2026-07-18
provenance: "source + capture date + transformation applied"
related: []              # relative links / [[wikilinks]] to adjacent units
tags: []                 # facets, drawn from meta/ontology.md only
---
```

**6 · The workflow-stage templates** (`workflows/templates/`) — one template per **L8** stage:
`research.md.tmpl`, `content-map.md.tmpl`, `roadmap.md.tmpl`, `job-card.md.tmpl`,
`execution-log.md.tmpl`, `spec.md.tmpl`. A new project is instantiated from these (**L3** rule 2).

**7 · The intake protocol** — `inbox/README.md` states the **L5** loop (drop anything → triage on
a rhythm → atomize, classify, link, index, reconcile facets → remove from inbox), so the release
valve is documented at the point of use.

**8 · Boot and validation wiring** — a boot-file fragment (**M6**) that inlines the **L7** standing
constraints and points to `library/INDEX.md`; and `validate.py` extensions (**L5** rule 5) that
check index counts, dangling links, and units missing required frontmatter — the mechanical checks
a controlled vocabulary needs and the model cannot be trusted to perform silently (**P2**).

---

## Conformance levels

Adoption is incremental, mirroring the base pattern's conformance ladder (**MECHANISMS.md**
§ Conformance levels) and the source overview's migration path. Each level is independently useful;
stop at any of them.

| Level | Requires | You get |
|---|---|---|
| **L·1 — Legible collection** | `library/` git-tracked + `inbox/` + append-only `structure-log.md` (**L1**, **L5**, **L6**) | A durable, capturable, auditable home for knowledge |
| **L·2 — Classified** | + `domains/` class hierarchy with finding-aid READMEs (**L2**) + the domain/project split (**L3**) | A collection navigable by class, larger than any context window |
| **L·3 — Catalogued** | + prose `INDEX.md` with reading protocol + `meta/ontology.md` + `by-*` finding aids (**L4**) | Multiple curated access paths; a controlled vocabulary |
| **L·4 — Workflow-wired** | + `projects/` instances from workflow templates + review write-back (**L8**) | Work that feeds the collection instead of bypassing it |
| **L·5 — Browsable & tuned** | + the Obsidian driver (**L9**) + boot compilation of the standing constraints and hot references (**M6**, **L7**) | Live graph/backlink navigation on top of a still-portable corpus |

The library becomes valuable at **L·1** — the moment new work flows through `inbox/` cleanly and
old material is synthesized in. Full classification is earned as the collection grows, not
required before the first note.

---

## Degenerate cases (collected)

- **Classification paralysis** — refusing to capture until the perfect class exists. The inbox
  (**L5**) is the fix; **CLASSIFY-LAST** (**L7**) is the rule that forbids the gate.
- **Class explosion / domain sprawl** — top-level classes multiplying until the catalog is a
  router again (**M2**/**M9** degenerate). Evolve the scheme deliberately through
  `structure-log.md`; prune and merge on the maintenance cadence.
- **Ontology drift** — facet tags proliferating uncontrolled until the vocabulary is noise
  (**M9** private-jargon accretion). Tags come from `ontology.md` first, coined deliberately.
- **Parallel truths** — the same knowledge maintained in Obsidian *and* here *and* in a wiki.
  **CANONICAL-COLLECTION** (**L7**): migrate and synthesize, never mirror.
- **Archive-as-graveyard** — moving units to `archives/` to avoid the harder call of promoting
  their reusable yield to `domains/` first (**L3** rule 5). Archive after promotion, not instead.
- **Monolith staging that never atomizes** — inbox items parked as one giant document and never
  split (**M4**'s log-as-state, at collection scale). Triage means atomize (**L5** rule 2).
- **Wikilink lock-in** — a collection that only resolves inside Obsidian (**L9**). The plain-
  Markdown floor is the invariant; the driver is the upgrade.
- **Finding-aid rot** — class READMEs and `by-*` indexes describing a shelf that has moved on.
  Review write-back (**L8** rule 2) is the discipline; `validate.py` catches the count drift.

---

## Provenance & credit

The ten mechanisms and three principles this layer stands on originate in **MOOLLM** by **Don
Hopkins** (SimHacker/moollm), with the lineage documented in [PROVENANCE.md](PROVENANCE.md). This
document adds no mechanism to that set; it applies them at collection scale and names the result
*the Legible Library*.

The library discipline — hierarchical classification adapted from Dewey Decimal and Library of
Congress practice, controlled vocabularies, finding aids, provenance, collocation, and
preservation — is adapted from the **Knowledge Library System overview (v1.0, 2026-07-18)**
supplied as source material. That overview stood as a parallel system; this layer folds its rules
into the Legible Workspace so there is one pattern, not two. Where the librarian's term and the
workspace's term named the same move, the workspace term was kept and the librarian's became a
gloss — because the goal here was never a second rulebook, but library-grade rigor expressed in
the mechanisms already proven to keep a large corpus legible.

---

*Substrate:* [MECHANISMS.md](MECHANISMS.md) (the ten mechanisms) · [CANON.md](../shared/CANON.md)
(the fixed names) · [EVIDENCE.md](EVIDENCE.md) (the measured ratio this layer scales).
