# Index

Every **bold term** is a path in this repository, spelled exactly. No other bold is used.

## Reading protocol

Read in resolution order; stop when you have enough. **GLANCE.yml** (this repo at a
glance, ~30 lines) → this index → the shelf that matches your question → deeper shelves
only as needed. Never open a deeper document without having read the tier above it. Every
curriculum document carries a tier bar linking one level *deeper* and one *plainer* for
the same content.

## The shelves

**curriculum/onramp/** is the ground floor — plain language, one everyday analogy per
idea, zero code. Start at **curriculum/onramp/WHY-YOUR-AI-FORGETS.md**; the ten ideas
live in **curriculum/onramp/THE-TEN-IDEAS.md**; the decision-maker's page is
**curriculum/onramp/WHAT-IT-MEANS-FOR-A-TEAM.md**.

**curriculum/kit/** is the practitioner shelf — recipes with verification steps. Entry at
**curriculum/kit/START-HERE.md**, hands-on from **curriculum/kit/SCAFFOLD.md**, one guide
per mechanism in **curriculum/kit/guides/**, incremental adoption in
**curriculum/kit/RETROFIT.md**, failure smells in **curriculum/kit/FAQ.md**.

**curriculum/spec/** is the top shelf — normative rules in
**curriculum/spec/MECHANISMS.md**, the argument in **curriculum/spec/WHITEPAPER.md**,
numbers in **curriculum/spec/EVIDENCE.md**, credit and lineage in
**curriculum/spec/PROVENANCE.md**. A durable-collection layer built on the ten mechanisms —
the long-term "everything" brain space, classified and Obsidian-browsable — is specified in
**curriculum/spec/THE-LEGIBLE-LIBRARY.md**.

**curriculum/shared/CANON.md** is the source of truth for every name, definition, and
analogy — when any document disagrees with it, the canon wins.

## The tooling

**template/** is the irreducible-but-complete starting point: a boot file, a session zone,
portable policy with host drivers, a two-capability library, and **template/validate.py**
— the mechanical check the origin system never had. Copy it out; don't work inside it.

**library-template/** is the durable-collection layer of
**curriculum/spec/THE-LEGIBLE-LIBRARY.md**, shipped ready to copy: a long-term knowledge
library pre-staged with classified sections, each carrying a "librarian" card stack, plus an
Obsidian vault config so the graph opens with something to see, the `curator` filing capability,
and **library-template/validate.py** extended to check card-stack completeness and ledger sync.

## The evidence

**study/** is the extraction that produced all of this: the mechanism inventory in
**study/analysis/02-mechanism-inventory.md**, the capability construction standard in
**study/analysis/06-capability-anatomy.md**, the honest assessment in
**study/analysis/05-honest-assessment.md**, and the measurement harness in
**study/evidence/measure.py** (to re-run it, clone MOOLLM into this repo root as
`moollm/` — it's gitignored).

## Housekeeping

**AGENT.md** is the boot file for anyone — human or model — *working on* this repo.
**.agent/** is the live session zone. **curriculum/SERIES-PLAN.md** is the production
history, kept as provenance.

## Load order

New reader: glance → this index → your shelf. New contributor: **AGENT.md** →
**curriculum/shared/CANON.md** → the shelf you're editing.
