# Guide 4 · Externalized state

> **Tier:** Practitioner · deeper: [spec/MECHANISMS.md#m4](../../spec/MECHANISMS.md#m4--externalized-state) · plainer: [onramp/THE-TEN-IDEAS.md#m4](../../onramp/THE-TEN-IDEAS.md#m4--externalized-state)

**The symptom.** Every session starts with re-explaining the project. Yesterday's decisions
are gone. You can't tell what the agent thinks it's doing, and when it's doing the wrong
thing your only lever is arguing with it in chat.

**What you build.** A `.agent/` directory: the agent's memory *and its attention*, as files.
This is the cheapest mechanism in the whole pattern — an hour — and the one to build first.

## The files

| File | Mode | It holds | Discipline |
|---|---|---|---|
| `working-set.yml` | edit | Current focus: task, active files, blockers | **Under 30 lines.** Update at task boundaries. |
| `hot.yml` | edit | Keep-loaded list | Every entry has a `why`, or it's permanent by inertia |
| `cold.yml` | edit | Evicted items | Each with a breadcrumb back |
| `session-log.md` | **append** | Decisions and *why* — not a transcript | Corrections are new entries, never rewrites |
| `output.md` | **append** | Results for the human | |

`working-set.yml`, whole file:

```yaml
focus:
  task: "Migrate auth to OAuth2"
  branch: feature/oauth2
active_files:
  - src/auth/session.ts
  - docs/auth-design.md
notes:
  - "Legacy session cookies must keep working through Q3"
  - "Blocked on library choice — see session-log"
```

**The underrated move: attention is now a document you can edit.** Agent fixated on the
wrong file? Don't argue in chat — edit `working-set.yml` and tell it to re-read. You just
went from persuading a model to correcting a record.

Two supporting rules:

- **The promotion pattern.** Data born in the log (a finding, a config decision) is fine to
  *reference* in place — but the moment you need to *edit* it, promote it to its own YAML
  file. Append-only files hold history; editable files hold state. Never both in one file.
- **Files beat recollection.** If the conversation and the files disagree, the files win.
  Say so in your boot file.

## Verify it's working

1. Do half a task. Close the session.
2. New session: "where were we?" — answered from `.agent/` alone, no project re-read, no
   history replay. That's resumption, the headline benefit.
3. Mid-task, open `working-set.yml` yourself. Does it describe what the agent is actually
   doing *right now*? If it describes last Tuesday, you have write-back drift — see below.

## The traps

- **Stale working set** — worse than none, because it lies with authority. The fix is a
  boot-file rule: *update at task boundaries*, plus your own habit of glancing at it.
- **Hot-list hoarding** — a keep-loaded list that only grows is a second copy of the repo.
  The `why` field exists so entries can be evicted when the why stops being true.
- **Append-only as theater** — nothing enforces it; it's a convention (P1). If you need a
  guarantee — and for audit logs you might — add a `PreToolUse` hook. Don't write
  "APPEND-ONLY" and mean "please."
- **The log as a transcript** — logging everything buries the decisions. Log *what was
  decided and why*; the chat scrollback already has the rest.
