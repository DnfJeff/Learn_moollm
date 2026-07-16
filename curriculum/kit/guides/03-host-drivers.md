# Guide 3 · Host drivers

> **Tier:** Practitioner · deeper: [spec/MECHANISMS.md#m3](../../spec/MECHANISMS.md#m3--host-drivers) · plainer: [onramp/THE-TEN-IDEAS.md#m3](../../onramp/THE-TEN-IDEAS.md#m3--host-drivers)

**The symptom.** Your setup works in Claude Code and breaks in Cursor — or you maintain two
diverging copies of your rules. Your policy docs say "use the Grep tool," which means
nothing on a host that doesn't have one. Or you paste your agent setup into a bare API
playground and it confidently pretends it can search files.

**What you build.** One host-independent policy (`policy/core.md`) plus one small YAML
adapter per host (`policy/drivers/<host>.yml`). Policy names *abstract operations*; drivers
map them to whatever this host actually has — and declare a fallback for everything it
doesn't.

**Skip this guide entirely if you run on one host.** One driver is indirection with nothing
on the other side. Come back when a second host actually exists.

## The files

`policy/drivers/claude-code.yml` (shape, from the template):

```yaml
driver:
  name: claude-code
  tier: 5                    # 1 minimal … 6 full-control
  detect: ["CLAUDE.md was loaded", "Claude Code tool names present"]

capabilities:
  file_read: true
  file_search: true
  terminal: true
  semantic_search: false     # not built in

tools:
  read_file:  { tool: "Read" }
  file_search:{ tool: "Grep" }
  terminal:   { tool: "Bash" }

fallbacks:
  semantic_search: "Use Grep with 2-3 keyword variants; say which terms you tried."
```

And **always ship `generic.yml`** — the tier-1 "I don't know where I am" floor. Its
fallbacks are the paradigm in miniature:

```yaml
fallbacks:
  file_search: |
    No search. Ask the user where something is, or infer from what you've been shown.
    Do not claim you searched.
  terminal: |
    No execution. Describe the command you would run; ask the user to run it and paste
    the output.
```

Three rules:

1. **Policy never names concrete tools.** If `core.md` says "Grep," you've forked your
   policy by accident.
2. **Every missing capability gets a written fallback** — even when the fallback is "ask
   the user." A declared floor beats a confident lie. (This is P1: advisory mode is the
   designed floor, not a failure.)
3. **Behavior keys off `tier`, not host name**, wherever possible — so an unknown host that
   detects as tier 3 gets tier-3 behavior instead of crashing your assumptions.

## Verify it's working

1. In your main host: ask the agent to find something. It uses the mapped search tool.
2. Simulate the bare case (paste your policy + `generic.yml` into a plain chat with no
   tools): same request. It should **ask you** where the thing is — and explicitly not
   claim to have searched. If it fakes capability, your generic fallbacks aren't loaded or
   aren't blunt enough.
3. Grep `policy/core.md` for your host's tool names. Zero hits.

## The traps

- **Policy leaking hostisms** — the slow fork. The grep test above, in CI if you like.
- **Driver growing policy** — drivers carry *mappings*, not rules. If a sentence would be
  true on every host, it belongs in `core.md`.
- **Fallback theater** — writing `fallback: degrade gracefully` is writing nothing. A
  fallback is an instruction someone could follow.
