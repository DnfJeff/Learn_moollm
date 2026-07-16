# Scaffold — zero to a working workspace

> **Tier:** Practitioner · deeper: [spec/MECHANISMS.md](../spec/MECHANISMS.md) · plainer: [onramp/THE-TEN-IDEAS.md](../onramp/THE-TEN-IDEAS.md)

This is the `create-app` moment. The template lives at
[`template/`](../../template/) and is deliberately small —
the architecture is four directories; everything else in the origin system is content.

## 1. Copy it in

```bash
cp -r template/ /path/to/your-project/agent/
cd /path/to/your-project/agent
cp AGENT.md ../CLAUDE.md        # Claude Code — or ../.cursorrules for Cursor
python validate.py              # should exit clean: 0 errors
```

Two minutes. Now the tour — every file, what it's for, what you edit.

## 2. What you just got

```
agent/
├── AGENT.md              ← the boot file (copied out as CLAUDE.md / .cursorrules)
├── validate.py           ← the floor. Wire into CI before anything else.
├── .agent/               ← the agent's memory & attention. Gitignore this.
│   ├── working-set.yml
│   ├── hot.yml
│   ├── session-log.md
│   └── output.md
├── policy/
│   ├── core.md           ← host-independent rules
│   └── drivers/          ← claude-code.yml, generic.yml
└── capabilities/
    ├── INDEX.yml         ← THE ENTRY POINT
    ├── example-capability/   ← annotated skeleton: copy to make new ones
    └── code-review/          ← a real worked example
```

**`CLAUDE.md` (from AGENT.md)** — the *free channel*: your host loads it automatically every
session, so its content is prepaid. It carries the standing constraints (six generic ones
with names like `CLAIM-LEDGER` and `VERBOSITY`, plus a project section you must replace), the
reading protocol, the state-file table, and pointers to everything else. Budget: ~2,000
tokens. Everything in it is a permanent tax on every call — that's why it holds pointers, not
copies.

**`.agent/`** — four files that make sessions survive:

| File | Mode | It is |
|---|---|---|
| `working-set.yml` | edit | The agent's attention. **Under 30 lines.** Wrong focus? Edit this file. |
| `hot.yml` | edit | Keep-loaded list; every entry carries a `why` or it becomes permanent by inertia |
| `session-log.md` | append | Decisions and reasons — not a transcript |
| `output.md` | append | Results for you |

**`policy/core.md`** — the eight portable rules (state in files, cheapest-tier reading,
prepaid names, liberal-in/strict-with-yourself, degrade-don't-crash, report honestly,
explicit intent, self-declaring capabilities). Read it once; it's the whole paradigm in two
pages.

**`policy/drivers/`** — per-host adapters. `generic.yml` is the "I don't know where I am"
floor: every capability the host lacks has a written fallback ("no search → ask the user,
don't claim you searched"). Delete this directory if you only ever run on one host; keep
`generic.yml` forever if you keep any.

**`capabilities/`** — the library. `INDEX.yml` is the entry point the agent reads first
(one line per capability, grouped, with an accurate `count:` that `validate.py` enforces).
`example-capability/` is the skeleton with the tier discipline written into its comments:

- `GLANCE.yml` (~400 tokens) — *a filter, not a summary*. Its `key_insight:` line is the
  payload: the one non-obvious thing to know before descending. **Never auto-generate it.**
- `CARD.yml` (~1,400) — interface: `invoke_when`, required tools, method signatures with
  effects, and `triggers:` (declarative routing — scored `when:` conditions; a trigger with
  `when: always` is a standing constraint).
- `SKILL.md` (~2,800, optional) — the protocol: steps, edge cases, named failure modes.
  Write it when CARD readers keep asking "but how?"

## 3. Make it yours (30 minutes)

1. **Rewrite the `## Project constraints` section of `CLAUDE.md`.** The placeholders
   (`NO-NEW-DEPS`, `SCOPE-CREEP`, `TEST-THE-BUG`) show the shape: NAME, one-line rule, a
   test. Yours are worth more than the generic ones — they encode your budget, your
   conventions, your scars. This step alone is most of the value.
2. **Reset `.agent/`.** The files ship with example content (an OAuth task). Blank the
   working set to your actual current task; empty `hot.yml` to `keep: []`.
3. **Decide about the library.** Fewer than ~10 capabilities? **Delete `capabilities/`.**
   Seriously — the ladder costs more than it saves on a small library, and the index is
   pure ceremony at n=2. Come back when you have a pile of prompts/procedures you keep
   re-explaining.
4. **Run `python validate.py --strict` and wire it into CI.** It checks YAML validity, tier
   presence, tier budgets, index count vs. reality, and the boot file's token budget — the
   exact four ways the origin system silently broke.

## 4. First capability (when you're ready)

```bash
cp -r capabilities/example-capability capabilities/my-thing
```

Then, in order — this order matters:

1. `CARD.yml` first: `invoke_when`, one method, one trigger. If you can't write the trigger's
   `when:` specifically enough for a model to judge, the capability isn't scoped yet.
2. `GLANCE.yml` second, **rewritten, not truncated**: what/why/when + the `key_insight` line.
   If you can't write the key insight, you don't understand the capability yet — that's the
   file telling you something.
3. `SKILL.md` only if the CARD can't carry the how.
4. Add one line to `INDEX.yml`, bump `count:`, run `validate.py`.

## 5. Verify the whole thing works

Open a fresh session and ask the agent something that should route through a capability.
Watch its reads: **INDEX first, then one GLANCE, then that CARD — and stop.** If it read
`SKILL.md` to answer a "what does this do" question, or skipped the index and globbed the
directory, the reading protocol isn't landing — see [FAQ](FAQ.md), smell #1.

Then end the session, start another, and ask "where were we?" It should answer from
`.agent/working-set.yml` + `session-log.md` without re-reading the project. That's the
pattern working: **resumption from five small files.**
