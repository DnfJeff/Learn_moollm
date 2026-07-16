# Document Series Plan: The Orchestration Paradigm at Three Resolutions

**Status:** Phases 0–3 complete — canon + naming locked 2026-07-15; Set A (spec, 4 docs)
2026-07-15; Set B (kit, 15 docs) 2026-07-16; Set C (onramp, 4 docs) + cross-tier link pass
2026-07-16. Remaining: the end-of-series template check (apply
`study/analysis/06-capability-anatomy.md` §Summary A1–A9 to the template) and
audience read-throughs.
**Inputs:** [`../moollm/`](https://github.com/SimHacker/moollm) (read-only **primary source of truth**) and
[`../study/`](../study/) (the extraction — a lens, corrected during doc
runs whenever primary sources contradict it; template re-checked at the end of the series).
**Goal:** Publishable materials that teach the paradigm to three audiences, so it can be applied to any AI orchestration work — not just re-read as a study of MOOLLM.

---

## 1. What this series is (and is not)

The `study` proved the thesis: MOOLLM's efficiency comes from six domain-neutral
mechanisms, and the adventure metaphor is a compression codebook layered on top. The study is
an *autopsy* — written for the person doing the extraction.

This series is the *product* of that autopsy: the nervous system presented on its own terms,
as a general orchestration paradigm. Think of the relationship the way Vite relates to a
bundler research paper: the study explains why it works; the series lets people **adopt** it.

Non-goals:

- Not a rewrite or fork of MOOLLM. MOOLLM stays untouched and fully credited.
- Not personality-stripping for its own sake. The study already established that metaphor is
  functional compression; the series *says so* where relevant instead of pretending whimsy
  was noise.
- Not framework marketing. The word "framework" is avoided in titles; "paradigm" or
  "pattern language" until a real name is chosen (§6).

## 2. The organizing principle: the series is itself a resolution ladder

The paradigm's first mechanism is the resolution ladder (GLANCE → CARD → SKILL → README:
never load detail without first loading the summary above it). The series uses the same
shape:

| Ladder level | Series tier | Audience question answered |
|---|---|---|
| GLANCE | **Set C — The Onramp** | "Is this relevant to me? What is it, in human terms?" |
| CARD | **Set B — The Practitioner's Kit** | "What can I do with it? How do I start?" |
| SKILL | **Set A — The Specification** | "How does it work, exactly? Prove it." |

This is not cosmetic. It is the strongest possible demo: a reader climbs the tiers and
experiences progressive disclosure firsthand. Every tier covers the **same ten mechanisms and
three cross-cutting principles, in the same order, under the same canonical names**, so
moving between tiers never requires re-mapping vocabulary.

The canonical list lives in [shared/CANON.md](shared/CANON.md) (M1–M10 + P1–P3, locked after
the skills-system excavation of 2026-07-15, which also produced
[analysis/06-capability-anatomy.md](../study/analysis/06-capability-anatomy.md) in
the study). Short form: M1 resolution ladder, M2 declarative routing, M3 host drivers, M4
externalized state, M5 standing constraints, M6 boot compilation, M7 in-context ensemble,
M8 directory-as-object, M9 names as addresses, M10 tolerant interpretation; P1 the dual-mode
contract, P2 the determinism split, P3 rewrite-not-truncate.

## 3. The three sets

### Set A — The Specification (technical white paper tier)

**Audience:** AI engineers, framework authors, researchers, informed skeptics.
**Register:** Formal, evidence-first, adversarial-reader-proof. Claims are either measured,
cited, or explicitly marked speculative. No analogies except where they are load-bearing and
flagged as such.
**Directory:** `spec/`

| # | Document | Contents | Primary source material |
|---|---|---|---|
| A1 | `WHITEPAPER.md` | The paradigm in one paper: problem statement (round-trip orchestration cost, context churn, opaque agent state), the six mechanisms as claims, measured results, comparison to tool-call/agent-swarm architectures, limits and failure modes, honest-assessment section carried forward intact | `analysis/01`, `analysis/03`, `analysis/04`, `analysis/05`, `framework/01` |
| A2 | `MECHANISMS.md` (or six files `mechanisms/01–06`) | Normative reference per mechanism: definition, file contract (exact filenames, size budgets, schemas), MUST/SHOULD/MAY rules, interaction with the other five, known degenerate cases | `framework/01`, `framework/02`, `guide/01–06`, `template/` |
| A3 | `EVIDENCE.md` | Methodology and numbers: token accounting of the 790k-token corpus sampled at ~5k tokens, how `measure.py` works, how to reproduce, what the numbers do and don't show | `evidence/measure.py`, `evidence/RESULTS.txt`, `analysis/04` |
| A4 | `PROVENANCE.md` | Prior art and credit: MOOLLM and Don Hopkins as origin, the Minsky (K-lines, Society of Mind) / Drescher (schemas) / Wright (advertisements) / Ungar (prototypes) lineage stated as citations; the metaphor-as-compression finding presented as a result, not an apology | `analysis/03`, MOOLLM manifesto + designs |

Definition of done for Set A: a senior engineer with no MOOLLM exposure can (a) implement
the pattern from A2 + the template alone, and (b) argue with the claims using A3's numbers
rather than vibes.

### Set B — The Practitioner's Kit (hobby-dev tier)

**Audience:** Technically capable builders using Claude Code / Cursor / similar daily, who
are not AI-engineering professionals. (This is the author's own tier — B is written to be
*used*, and the author is its first test reader.)
**Register:** Direct, recipe-shaped, copy-paste-honest. Every doc ends with "how you verify
it's working." Analogies allowed as one-line asides, never as the explanation itself.
**Directory:** `kit/`

| # | Document | Contents | Primary source material |
|---|---|---|---|
| B1 | `START-HERE.md` | The paradigm in ten minutes: what problem it solves, what you get, what it costs to adopt, **when not to use it** (small projects, one-shot tasks) | `framework/01`, README of study |
| B2 | `SCAFFOLD.md` | The Vite moment: initialize a fresh workspace from `template/`, walk through every generated file, create your first capability, run your first session, watch the agent use the ladder. Ends with the workspace as a living checklist | `template/` (verbatim, kept in sync) |
| B3–B12 | `guides/01–10` | One guide per mechanism M1–M10, in recipe form: *symptom you have → what you build → the files → the verification step*. Guides 1–6 rewrite the study's `guide/`; guides 7–10 (boot compilation, directory-as-object, names-as-addresses, tolerant interpretation) are new, from primary sources. P1–P3 woven in where they bind (P1→drivers/state guides, P2→every guide's "what goes in a script" box, P3→ladder guide) | `guide/01–06`, `analysis/02`, `analysis/06`, moollm kernel |
| B13 | `RETROFIT.md` | Applying this to an **existing** project or AI workflow — the motivating use case of the whole series. Prescribes an adoption order: externalized state first (cheapest, highest immediate value), then resolution ladder over existing docs, then declarative routing, then the rest as needed. Explicitly permits partial adoption | `framework/02`, new writing |
| B14 | `FAQ.md` | Failure smells and fixes: agent reads the whole corpus anyway (ladder discipline broken), capability index turning into a router (declarations centralizing), state drifting from reality (write-back discipline), constraint files bloating | `analysis/05`, new writing |
| B15 | `GLOSSARY.md` | Canonical term → one-line definition → MOOLLM original term. Direct descendant of `framework/03`, seeded from CANON's glossary table | `framework/03`, `shared/CANON.md` |

Definition of done for Set B: a reader can go from zero to a working orchestrated workspace
in one sitting using B1 + B2, and retrofit one existing project using B13, without opening
Set A.

### Set C — The Onramp (casual / business tier)

**Audience:** Non-developers: managers, founders, curious professionals, anyone evaluating
whether "AI orchestration" is real or hype.
**Register:** Analogy-first, zero code, zero YAML, zero filenames. Hard rule: if a sentence
requires knowing what a file is, it belongs in Set B. Short — the entire set should read in
under 30 minutes.
**Directory:** `onramp/`

| # | Document | Contents |
|---|---|---|
| C1 | `WHY-YOUR-AI-FORGETS.md` | The hook. The lived problem in plain terms: assistants that re-learn everything each session, teams paying for the same context over and over, no way to see what the AI "knows." Ends by naming the six ideas |
| C2 | `THE-TEN-IDEAS.md` | One section per mechanism M1–M10, each built on the single sustained analogy fixed in CANON, each ending with one real sentence about what it looks like in practice; P1–P3 as three short closing vignettes |
| C3 | `WHAT-IT-MEANS-FOR-A-TEAM.md` | The business one-pager: cost (fewer model calls), speed (fewer round-trips), auditability (everything on paper), continuity (work survives sessions and personnel). No numbers without a pointer to A3 |
| C4 | `PLAIN-GLOSSARY.md` | The same canonical terms as B11, defined for a non-technical reader, analogy included |

The analogies are **owned by [shared/CANON.md](shared/CANON.md)** (one per mechanism and
principle) — C2 elaborates them but may not substitute new ones without changing CANON
first. Each must survive the drafting test: *does the analogy predict the right behavior?*

Definition of done for Set C: a non-technical reader can explain to a colleague, in their own
words, why this approach is cheaper and more trustworthy than "just chatting with the AI" —
and knows Set B exists if they want hands-on.

## 4. The shared spine (drift prevention)

One small directory, `shared/`, that all three sets are written against:

- **`shared/CANON.md`** — the single source of truth: for each of the six mechanisms, its
  canonical name, one-line definition, its Set C analogy, its MOOLLM-original name, and links
  to its A/B/C treatments. Every series doc must use these names exactly. When a name
  changes, it changes here first.
- **`shared/CROSS-TIER-NAV.md`** — the header/footer convention: every document links one
  tier up ("want the proof?") and one tier down ("want the plain-language version?").

This is the series' own externalized state: the canon file plays the role a `GLANCE.yml`
plays in the paradigm itself.

## 5. Production order and phases

| Phase | Work | Why this order |
|---|---|---|
| 0 ✅ | Naming pass (§6) + write `shared/CANON.md` — **done 2026-07-15**, preceded by the MOOLLM skills-system excavation (study `analysis/06`) | Everything downstream uses these names; renaming after drafting is the expensive path |
| 1 | Set A (spec) | It is closest to done — `framework/` and `analysis/` are ~70% of the content. A becomes the source of truth B and C compress |
| 2 | Set B (kit) | Largest practical payoff, and the author dogfoods it immediately on their own orchestration work — which feeds real corrections back before C is written |
| 3 | Set C (onramp) | Written last, when names and claims are stable; analogies are cheap to write and expensive to rewrite |
| 4 | Cross-tier link pass + read-through at each tier by its actual audience type | The definition-of-done checks in §3 |

Estimated scope: ~23 documents (4 + 15 + 4) plus 2 spine files. Sets A and B are largely
transformations of existing study + primary-source material; C, B13 (`RETROFIT.md`), and
guides 7–10 are the substantially new writing.

## 6. Naming — DECIDED (Phase 0, 2026-07-15)

**The Legible Workspace** — a file-native architecture for context orchestration. Rationale,
tier phrasings, and runners-up are recorded in [shared/CANON.md](shared/CANON.md), which owns
the name from here on. The constraint that drove the choice: the name must be made of words
already dense in the model's (and readers') vocabulary — novel jargon is the anti-pattern the
paradigm itself documents (M9) — and legibility is the one property all ten mechanisms serve.
It coexists with "MOOLLM" via the provenance sentence required in every set's opening doc.

## 7. Directory layout when built

```
paradigm-docs/
├── SERIES-PLAN.md        ← this file
├── shared/
│   ├── CANON.md
│   └── CROSS-TIER-NAV.md
├── spec/                 ← Set A
├── kit/                  ← Set B
│   └── guides/
└── onramp/               ← Set C
```

`study/` remains frozen as the evidence base; the series links into it rather than
copying from it wherever a claim needs its receipt.
