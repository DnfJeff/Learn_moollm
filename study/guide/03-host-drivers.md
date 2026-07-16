# Guide 3 · Host Drivers

**One policy, N host adapters.** The least glamorous and most reusable mechanism in MOOLLM.

## The problem

Your agent policy says "read the file." But:

- In Claude Code, that's `Read`.
- In Cursor, that's `read_file`.
- In a bare API loop, it's your own tool schema.
- In a chat window with no tools, it's *"please paste the file."*

Write the policy against any one of these and it forks the moment you add a second host. Fork
the policy and the two copies drift, and now your agent behaves differently depending on where
it's running for reasons nobody can find.

## The solution

Write the policy against **abstract operations**. Put the mapping in a per-host adapter.

```yaml
# policy/drivers/claude-code.yml
driver:
  name: claude-code
  tier: 5

capabilities:
  file_read: true
  file_write: true
  file_search: true
  semantic_search: false
  terminal: true

tools:
  read_file:  { tool: Read }
  write_file: { tool: Write }
  edit_file:  { tool: Edit }
  list_dir:   { tool: Glob }
  search:     { tool: Grep }
  terminal:   { tool: Bash }

paths:
  session_root: .agent/
  output_sink:  .agent/output.md

fallbacks:
  semantic_search: "Use Grep with a regex approximation; widen and re-run if too few hits."
```

The policy says `read_file`. The driver says what that means here. New host = new adapter, not
a new fork.

## Capability tiers

Declare what a host *can* do so the agent can adapt instead of failing:

| Tier | Capabilities | Example hosts |
|---|---|---|
| 0 | Text only | Bare chat |
| 1 | + file read | Minimal IDE |
| 2 | + file write | Most IDEs |
| 3 | + search | Cursor, Claude Code |
| 4 | + execution | Cursor, Claude Code |
| 5 | + custom tools (MCP) | Claude Code |
| 6 | + full context control | A runtime you built |

Tier isn't decoration — it's a *guard*. The agent checks tier before assuming a capability.
MOOLLM's `generic.yml` (tier 1) is the instructive one: it assumes almost nothing and its
fallback for everything is "ask the user to do it and tell me what happened."

## Fallbacks are the point

The tools table is trivial. **The fallbacks are where the value is.**

Every capability you don't have needs a declared degradation:

| Capability | Full support | Fallback |
|---|---|---|
| Semantic search | `SemanticSearch` | Grep with regex approximation |
| Sandboxed exec | Isolated container | Ask before running; trust-based |
| Append-only enforcement | Host enforces | Convention; agent promises |
| `why` on tool calls | Tool schema field | State intent in prose before the call |
| Structured event log | JSONL | Markdown narrative with YAML blocks |

**A capability without a fallback is a crash waiting for the right host.** This is P9 (never
crash, degrade) made concrete: the fallback table *is* graceful degradation.

## Detection

The agent needs to know which driver applies:

```yaml
driver_detection:
  claude-code:
    indicators: ["Read/Edit/Bash tools available", "CLAUDE.md present"]
    load: drivers/claude-code.yml
  cursor:
    indicators: ["codebase_search available", ".cursorrules present"]
    load: drivers/cursor.yml
  generic:
    indicators: ["fallback"]
    load: drivers/generic.yml
```

In practice the model can usually tell from its own tool list. The value of writing it down is
that detection becomes *explicit and auditable* rather than a guess the model makes silently.

**Always ship a `generic.yml`.** It's the "I don't know where I am" case, and it should assume
tier 1 and degrade everything. An agent that can't run on an unknown host isn't portable — it's
just written for one host with extra ceremony.

## The honest read

On real hosts today, most fallbacks are `"convention only"`:

```yaml
append_only:
  supported: "via_mcp"
  instruction: "Otherwise, treat output.md as append-only by convention."
```

Which means: **nothing enforces it.** The agent promises. That's the whole mechanism.

This is fine *if you're honest about it*. It's not fine if you write "append-only" in a table
and let readers think something guarantees it. The distinction between a tendency and a
guarantee is the thing MOOLLM most consistently blurs — see
[analysis/05](../analysis/05-honest-assessment.md).

**If a guarantee actually matters, get a real hook.** In Claude Code, that's a `PreToolUse`
hook in `settings.json` that rejects writes to the file. That's enforcement. Everything else is
etiquette.

## Applying it

**Don't build this until you have a second host.** Seriously. One driver is a layer of
indirection with nothing on the other side — pure cost, zero benefit. YAGNI applies hard here.

**Build it when:** you actually run on two hosts, or you're publishing for others to run
somewhere you can't predict.

**Start minimal.** A driver needs four things:

```yaml
driver:  { name: <host>, tier: N }
capabilities: { <what it can do> }
tools:   { <abstract> : <concrete> }
fallbacks: { <missing capability> : "<what to do instead>" }
```

Paths and detection can come later.

## Checklist

- [ ] Policy is written against abstract operations, never concrete tool names
- [ ] One adapter per host, each declaring capabilities + tools + fallbacks
- [ ] Every capability you lack has a **declared fallback**
- [ ] A `generic.yml` exists for unknown hosts, assuming tier 1
- [ ] Tier is checked before a capability is assumed
- [ ] Anything described as "enforced" actually is — or is relabeled as convention
- [ ] You have ≥2 hosts (if not, skip this entirely)

Next: [04-externalized-state.md](04-externalized-state.md)
