# Project Orchestration Template

A domain-neutral starting point distilled from [MOOLLM](https://github.com/SimHacker/moollm). No adventure games.

This implements the pattern from [framework/01-the-pattern.md](../study/framework/01-the-pattern.md).
It is deliberately small — most of MOOLLM's 4,489 files are content, not architecture.

## What's here

```
template/
├── AGENT.md              The free channel. Copy to CLAUDE.md / .cursorrules.
│                         Standing constraints inlined. Always loaded.
│
├── validate.py           Checks conformance and drift. MOOLLM has no equivalent;
│                         that's why its index is 8 skills out of sync and its
│                         boot file is invalid YAML.
│
├── .agent/               Runtime state. Gitignore this.
│   ├── working-set.yml     What I'm focused on
│   ├── hot.yml             Keep loaded
│   ├── session-log.md      What happened (append-only)
│   └── output.md           Results (append-only)
│
├── policy/
│   ├── core.md             Portable rules. Host-independent.
│   └── drivers/
│       ├── claude-code.yml
│       └── generic.yml
│
└── capabilities/
    ├── INDEX.yml           THE ENTRY POINT. Every capability, one line.
    ├── example-capability/ Annotated skeleton — copy this
    └── code-review/        A real, worked example
```

## Use it

```bash
cp -r template/ /path/to/your-project/agent/
cd /path/to/your-project/agent
cp AGENT.md ../CLAUDE.md      # or ../.cursorrules
python validate.py            # should pass
```

Then:

1. **Edit `CLAUDE.md`.** Replace the project-specific constraints with your own. This alone is
   most of the value — see [guide/05](../study/guide/05-standing-constraints.md).
2. **Delete `capabilities/` if you have fewer than ~10.** Seriously. The resolution ladder costs
   more than it saves on a small library. Come back when the index is hard to read.
3. **Delete `policy/drivers/` if you only run on one host.** One driver is indirection with
   nothing on the other side.
4. **Keep `.agent/` and `validate.py`.** Both are cheap and both pay immediately.

## Adoption order

Don't build all of it. In value-per-hour order:

| # | Do this | Cost | Prerequisite |
|---|---|---|---|
| 1 | `AGENT.md` standing constraints | 1 hour | none |
| 2 | `.agent/` state files | 1 hour | none |
| 3 | `validate.py` | already written | something to validate |
| 4 | `capabilities/` ladder | days | ~10+ capabilities |
| 5 | Declarative triggers | hours | index is hard to choose from |
| 6 | `policy/drivers/` | hours | an actual 2nd host |

**The trap is #4 before you need it.** MOOLLM has 141 capabilities and needs a ladder. You have
six and don't.

## What this is not

Stated plainly, because MOOLLM isn't:

- **Not a runtime.** Nothing executes. These are conventions the model reads and usually
  follows. That's the *designed floor*, not a missing feature: every control file here works
  in two modes — enforced by an orchestrator that understands it, or read and self-applied
  by the model. Same files either way; enforcement is an upgrade path.
- **Not enforcement.** `hot.yml` is a hint. "Append-only" is a promise. Want a guarantee? Use a
  `PreToolUse` hook in `.claude/settings.json`.
- **Not deterministic.** Trigger scores are read by a model, not evaluated by an engine.

It's a way to organize files so an agent can navigate more capability than it can hold, behave
consistently, and be corrected by a human. That's a modest, real, useful thing.

## The one thing MOOLLM doesn't have

`validate.py`. Run it in CI.

MOOLLM's `.cursorrules` has been invalid YAML for an unknown length of time — two standing
constraints silently fell out of the map — and its index is 8 skills out of sync. Both because
nothing checks, because the design says the LLM interprets and the LLM doesn't mind.

Be liberal in what you accept from users. Be strict about what you wrote yourself. See
[framework/02-principles.md](../study/framework/02-principles.md) §P8.
