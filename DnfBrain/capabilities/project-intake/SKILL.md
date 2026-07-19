---
status: canonical
created: 2026-07-18
reviewed: 2026-07-18
provenance: "Authored during DnfBrain initialization; the 'new project' flow, written to be procedure-tested on a local model"
related: [../curator/SKILL.md, ../../library/_templates/project/README.md]
tags: [capability, library-ops]
---

# project-intake — the "I've got a new project" flow

Read this to change the intake procedure. To *run* it, `CARD.yml` is enough.

The premise: the moment a project is announced is the cheapest moment to wire it into the
library. Scope is stated out loud, the domains it touches are obvious, and nothing has
accumulated in the wrong place yet. Ten minutes of setup buys effortless promotion at the end.

## OPEN — from the sentence to the instance

1. **Interview, briefly** (three questions, not a form):
   - What does *done* look like? (one sentence — becomes the README goal)
   - What will it draw on / produce knowledge about? (names the domain shelves)
   - What's the first concrete deliverable? (seeds the roadmap or first job card)
2. **Instantiate.** Copy `library/_templates/project/` → `library/projects/<name>/`
   (lowercase-kebab). Fill the README's goal/status block.
3. **Wire it.** In `references/`, add a pointer file per domain shelf named in the interview —
   path + one line on what this project needs from or will feed into that shelf. Missing
   shelf? Finding-aid README stub via the section librarian, logged (repair-not-fatal).
4. **Register.** Row in `library/meta/by-project.md` (create that finding aid on first
   project — it comes online now, as the catalog says). First entry in `execution-logs/`:
   the interview answers, dated. That's the project's provenance.
5. **Validate.** `python validate.py`.

## STATUS — cheap check-in

README goal/status block + the latest `execution-logs/` entry. Report: goal, status, last
activity, next step. Do not load research/ and specs/ to answer "where are we?".

## CLOSE — finish without losing the yield

1. List candidate findings from `execution-logs/` and `specs/` — anything reusable beyond
   this project.
2. For each: curator **PROMOTE** (the finding graduates into its domain shelf as a unit).
3. Mark the README status `done`; move to `archives/` if you want it out of the active view.
4. Log the close (and the promoted units, by path) in `meta/structure-log.md`.

Archiving before promoting is the `ORPHAN-KNOWLEDGE` failure — the curator's gate applies.

## Failure modes (named, so they're checkable)

- **`PROJECT-AS-JUNK-DRAWER`** — durable knowledge accumulating in the project instead of
  being promoted as it lands. Projects hold *work*; domains hold *knowledge*.
- **`WIRELESS-PROJECT`** — an instance with an empty `references/`: nobody said what shelves
  it draws on, so its yield has no home waiting. The interview prevents this.
- **`FORM-NOT-FLOW`** — turning the three-question interview into a questionnaire. If the
  user's announcement already answered a question, don't re-ask it.
- **`SILENT-OPEN`** — creating the instance without the by-project row and the first log
  entry. An unregistered project is invisible to the finding aids (`LEDGER-SYNC`).
