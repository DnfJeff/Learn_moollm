# The Legible Library — a quickstart vault

A shareable, domain-neutral starting point for a **long-term "everything" knowledge library**
you keep for years: every finding, spec, decision, and reference, classified, browsable in
Obsidian, and navigable by an AI agent. It is the [Legible Workspace](https://github.com/SimHacker/moollm)
pattern — extracted from **MOOLLM** by **Don Hopkins** — with a durable collection layer built on
top and **pre-staged** so the shelves exist before you have anything to put on them.

Nothing here is personalized. Rename the sections, keep the structure.

## Why it comes pre-staged

A library only stays usable at scale if it is organized *before* it is full. So this template
ships the **higher-level layers already built as card stacks** — the predictable part. Each
classification section carries a "librarian": a card stack that already knows what belongs on
its shelf and can tell an agent *"work like this goes here"* before a single note exists. You
add leaves; the tree is already standing.

The card stack is the standard that keeps it usable. Every shelf and every note is written at
the same four sizes — GLANCE → CARD → SKILL → README — so a reader loads the cheapest one that
answers the question and never reads the whole library to file one note.

## What's here

```
library-template/
├── HOME.md               The front desk. Open this in Obsidian first.
├── AGENT.md              Boot file. Copy to CLAUDE.md / .cursorrules. Always loaded.
├── validate.py          Checks the card stacks and ledgers stay in sync. Run in CI.
├── .obsidian/           Minimal vault config, so the graph opens with something to see.
├── .agent/              Session state (disposable). Not the library.
├── policy/              Standing rules + host drivers (incl. obsidian.yml).
├── capabilities/        Executable how-tos. Ships `curator/` — the filing skill.
└── library/             THE COLLECTION — permanent, versioned, the brain space.
    ├── INDEX.md           The chief librarian: prose master catalog + reading protocol.
    ├── meta/              The ontology (controlled vocabulary) + finding aids + change log.
    ├── domains/           Permanent knowledge, as classified sections with librarians.
    │   ├── technical/       how specific systems, tools, formats work
    │   ├── knowledge/       durable subject understanding, not tied to one system
    │   └── practices/       repeatable methods, patterns, checklists
    ├── projects/          Time-bound work (instances). Feeds domains when it yields reuse.
    ├── inbox/             Drop anything here. Classify later. Never a gate at the door.
    ├── archives/          Superseded, not deleted. Provenance preserved.
    └── _templates/        Copy-me card stacks: a section, a unit, a note, a project.
```

## Use it

```bash
cp -r library-template/ /path/to/your-library/
cd /path/to/your-library
cp AGENT.md CLAUDE.md              # or .cursorrules
python validate.py                 # should pass: 0 errors
```

Then **open the folder as a vault in Obsidian** and start at `HOME.md`. The graph view will
already show the front desk linked to every section.

## First moves

1. **Read `HOME.md`, then `library/INDEX.md`.** That's the front desk and the directory.
2. **Rename the three sections** under `library/domains/` to your real domains — keep the
   librarian card stack, replace the labels and placement rules. Log the change in
   `library/meta/structure-log.md`.
3. **Drop things in `library/inbox/`** from day one. Triage on a rhythm; don't file at the door.
4. **When you (or the agent) start real work**, the `curator` capability walks the librarian
   chain — chief librarian → section librarian → the shelf — so new material lands in the
   right place instead of a heap.

## What this is not

- **Not a runtime.** Nothing executes. The files are conventions a model reads and applies, or
  an orchestrator enforces — same files either way. Enforcement is an upgrade, not a prerequisite.
- **Not enforcement.** Append-only logs and ledger sync are conventions; `validate.py` is the
  only thing that actually checks, so run it.
- **Not personalized.** The sections are neutral placeholders. The value is the shape.

The mechanisms originate in [MOOLLM](https://github.com/SimHacker/moollm) by Don Hopkins; this
is a domain-neutral presentation of them at library scale, with credit.
