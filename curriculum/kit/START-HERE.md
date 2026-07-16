# Start Here — the Legible Workspace in ten minutes

> **Tier:** Practitioner · deeper: [spec/WHITEPAPER.md](../spec/WHITEPAPER.md) · plainer: [onramp/WHY-YOUR-AI-FORGETS.md](../onramp/WHY-YOUR-AI-FORGETS.md)

You use Claude Code or Cursor daily. Your agent re-learns your project every session, reads
whole directories to find one thing, drifts off your conventions, and when it goes wrong you
can't see why. This kit fixes those four problems with **files** — no runtime, no service,
no framework dependency.

The pattern is called the **Legible Workspace**. Its mechanisms come from
[MOOLLM](https://github.com/SimHacker/moollm) by Don Hopkins; this kit is the domain-neutral, hands-on version.

## The idea in one paragraph

Everything the agent knows, wants, may do, and is currently focused on becomes plain text in
your repo. Its capabilities are directories written at several sizes so it reads summaries
before details. Each capability announces when it's relevant, so there's no dispatcher to
maintain. Its memory and even its *attention* are small YAML files you can open and edit —
if the agent is focused on the wrong thing, you fix a 20-line file. House rules live in the
one file your host auto-loads every session, so they're always active and never re-argued.
Because it's all text, the whole system is inspectable, diffable, and correctable by you.

## What you get

| Problem you have | What fixes it | Guide |
|---|---|---|
| Agent re-learns the project every session | `.agent/` state files | [04](guides/04-externalized-state.md) |
| Agent reads everything to find anything | The resolution ladder | [01](guides/01-resolution-ladder.md) |
| "Which helper applies here?" logic sprawls | Self-declaring capabilities | [02](guides/02-declarative-routing.md) |
| Agent keeps violating your conventions | Standing constraints in the boot file | [05](guides/05-standing-constraints.md) |
| Session start wastes tokens re-orienting | Boot compilation | [06](guides/06-boot-compilation.md) |
| Same setup breaks on a second host | Host drivers | [03](guides/03-host-drivers.md) |
| Multi-perspective work costs N API calls | In-context ensembles | [07](guides/07-in-context-ensemble.md) |

Plus three that are more habits than builds: [directory-as-object](guides/08-directory-as-object.md),
[names-as-addresses](guides/09-names-as-addresses.md), [tolerant interpretation](guides/10-tolerant-interpretation.md).

## What it costs

- **An editorial habit.** Summaries are written by you, not generated. That's the mechanism,
  not a chore attached to it.
- **Write-back discipline.** State files must be updated at task boundaries or they lie.
- **A validator in CI.** One script, already written. Non-negotiable — the origin system
  skipped it and shipped a broken boot file for months without noticing.

## When NOT to use this

Honest scoping, because the pattern's own origin over-applied it:

- **Under ~10 capabilities?** Skip the ladder and the index entirely. Standing constraints +
  state files (an afternoon of work) are still worth it; the library machinery is not.
- **One-shot scripts, throwaway analyses?** Skip all of it.
- **Rules that must NEVER be violated** (security checks, spend limits)? These files create
  strong tendencies, not guarantees. Put hard rules in hooks or code, and use this pattern
  for everything softer.

## Your path

1. **New project or clean slate** → [SCAFFOLD.md](SCAFFOLD.md). Working workspace in under
   an hour.
2. **Existing project with existing habits** → [RETROFIT.md](RETROFIT.md). Adopt in value
   order, stop at any level.
3. **Something's not working** → [FAQ.md](FAQ.md). The failure smells are known and named.
4. **A term you don't recognize** → [GLOSSARY.md](GLOSSARY.md).

Each mechanism guide is a recipe: *the symptom → what you build → the files → how you verify
it's working.* None assumes you read the spec; all link to it.
