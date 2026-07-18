# Learn the Legible Workspace - A moollm onramp

**A file-native architecture for orchestrating LLM agents — the curriculum, the tooling,
and the evidence, in one repo.**

### Why

Your AI assistant forgets between sessions, reads the whole project to answer
one question, drifts off your rules, and can't show you why it did what it did. Those four
problems share one root: everything the assistant knows lives in a conversation, and
conversations evaporate. The fix is old technology — **write things down** — applied with
unusual discipline: ten specific mechanisms that let an agent navigate far more capability
than fits in its context window, behave consistently across sessions and hosts, and be
corrected by a human who wasn't watching.

The mechanisms originate in **[MOOLLM](https://github.com/SimHacker/moollm)** by **Don
Hopkins**, where they ship inside a playful text-adventure microworld. This repo is the
extracted nervous system: the same architecture, domain-neutral, with measurements, limits,
and a starting point you can copy today.

## Choose your door

| You are | Start at | Time |
|---|---|---|
| Curious, non-technical, or deciding for a team | [curriculum/onramp/](curriculum/onramp/WHY-YOUR-AI-FORGETS.md) | 30 min, zero code |
| A builder using Claude Code / Cursor daily | [curriculum/kit/START-HERE.md](curriculum/kit/START-HERE.md) → [SCAFFOLD](curriculum/kit/SCAFFOLD.md) | working setup in an hour |
| Building a knowledge base to keep for years and browse in Obsidian | [curriculum/spec/THE-LEGIBLE-LIBRARY.md](curriculum/spec/THE-LEGIBLE-LIBRARY.md) → [library-template/](library-template/) | copy-out vault, ready in an hour |
| An engineer who wants rules and proof | [curriculum/spec/WHITEPAPER.md](curriculum/spec/WHITEPAPER.md) → [MECHANISMS](curriculum/spec/MECHANISMS.md) | the normative reference |

The three shelves cover the **same ten mechanisms in the same order under the same names**
— the curriculum is itself shaped like its first mechanism, a resolution ladder. Every
document links one level deeper and one plainer. Names are fixed in
[curriculum/shared/CANON.md](curriculum/shared/CANON.md).

## What's in the box

```
GLANCE.yml        this repo in 30 lines — start here if even this README is too long
INDEX.md          the prose index; reading protocol at the top
AGENT.md          boot file for working ON the repo (learners: ignore)
curriculum/       the three shelves: onramp/ · kit/ · spec/ · shared/
template/         the irreducible-but-complete starting point — copy it out
library-template/ a long-term knowledge library, pre-staged & Obsidian-ready — copy it out
study/            the extraction & evidence this is built on (measure.py, honest assessment)
.agent/           the live session zone — this repo practices what it teaches
```

## Copy one out

Two templates, one architecture, different jobs. Both are self-contained and both ship the
`validate.py` the origin system never had. Copy the one you need.

**A working-agent workspace — [`template/`](template/).** A boot file, session state, host
drivers, and a capability library for an agent working *on a project*. This is the desk.

```bash
cp -r template/ /path/to/your-project/agent/
cd /path/to/your-project/agent
cp AGENT.md ../CLAUDE.md        # or ../.cursorrules
python validate.py              # 0 errors, 0 warnings
```

Then follow [curriculum/kit/SCAFFOLD.md](curriculum/kit/SCAFFOLD.md). Existing project?
[curriculum/kit/RETROFIT.md](curriculum/kit/RETROFIT.md) adopts incrementally, with a safe
stopping point at every level.

**A long-term knowledge library — [`library-template/`](library-template/).** The same pattern
scaled to a durable, classified "everything" brain space you keep for years: pre-staged sections
that each carry a "librarian" card stack (so new work already knows where it belongs), an
Obsidian vault so the graph opens on day one, and a `curator` filing capability. This is the
archive. It is specified in [curriculum/spec/THE-LEGIBLE-LIBRARY.md](curriculum/spec/THE-LEGIBLE-LIBRARY.md).

```bash
cp -r library-template/ /path/to/your-library/
cd /path/to/your-library
cp AGENT.md CLAUDE.md           # or .cursorrules
python validate.py              # 0 errors, 0 warnings
```

Then open the folder as an Obsidian vault and start at `HOME.md`.

## Re-running the evidence

Every measured number traces to [study/evidence/measure.py](study/evidence/measure.py),
which runs read-only against the origin repo. Clone it into this repo's root first:

```bash
git clone https://github.com/SimHacker/moollm.git   # lands at ./moollm/, gitignored
cd study && python evidence/measure.py
```

## Credit

![The User Interface Flower Child — Don's Sims credits icon](media/DonHopkinsSimsCreditsIcon.jpg)

Architecture and mechanisms: [MOOLLM](https://github.com/SimHacker/moollm), Don Hopkins
(SimHacker), 2024–present — with a lineage running through Minsky, Papert, Drescher,
Wright, Ungar, Postel, and Ackley, documented in
[curriculum/spec/PROVENANCE.md](curriculum/spec/PROVENANCE.md). This repo extracts and
re-presents; it does not replace the original, which is worth visiting in full costume.
