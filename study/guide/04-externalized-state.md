# Guide 4 · Externalized State

**No hidden memory. If the agent knows it, a human can open it.**

MOOLLM calls this Files-as-State. It's the cheapest mechanism to adopt and one of the highest
value.

## The problem

An LLM is stateless. Between calls it remembers nothing. So "memory" is whatever the harness
puts back in the prompt — which means memory is a *design decision* someone is making, whether
deliberately or by default.

The default is: replay the whole conversation. This fails in three ways.

1. **It doesn't survive.** New session, cleared context, different machine — gone.
2. **It's opaque.** You can't see what the agent thinks is important. You can only infer it
   from behavior, after the fact, when it's already gone wrong.
3. **It's not correctable.** The agent is focused on the wrong five files and you have no lever
   except more prose.

## The solution

Put it in files.

```
.agent/                    # gitignored — this is runtime state
├── working-set.yml        # What I'm focused on now
├── hot.yml                # Keep these loaded, with priority
├── cold.yml               # Evicted, with breadcrumbs back
├── session-log.md         # What happened (append-only)
└── output.md              # Results for the human (append-only)
```

Here is MOOLLM's live `working-set.yml` — 607 bytes, the entire session's attention:

```yaml
focus:
  adventure: .moollm/mayberry/
  player: .moollm/mayberry/characters/real-people/jeff-adkins/

active_files:
  - .moollm/mayberry/ADVENTURE.yml
  - .moollm/mayberry/town-square/ROOM.yml
  - .moollm/mayberry/characters/real-people/jeff-adkins/CHARACTER.yml

notes:
  - "Day 1 antic: barney-bullet-inspection"
  - "Say NEW DAY for next antic from pool"
```

You can read that in five seconds and know exactly what the agent is thinking about.

## The three wins

People conflate these. They're distinct, and the third is the one that matters.

**1. Resumption.** A new session reads five small files instead of replaying an hour of
conversation. Cheaper and more accurate — the files are curated; the transcript is noise.

**2. Auditability.** You can *see* the agent's attention. Not infer it. Open the file.

**3. Correctability.** You can **edit** it. Agent focused on the wrong module? Change
`working-set.yml`. Attention stops being a property of the conversation and becomes a document
under your control.

The third is the underrated one, and it's the reason to do this. Most agent frameworks treat
context as something that happens *to* the agent and to you. Here it's a text file you can fix
with an editor.

## The files

### `working-set.yml` — current focus

```yaml
focus:
  task: "Migrate auth to OAuth2"
  branch: feature/oauth2

active_files:
  - src/auth/session.ts
  - src/auth/oauth.ts
  - docs/auth-design.md

notes:
  - "Legacy session cookies must keep working through Q3"
  - "Blocked on: which library — see decision log"
```

**Keep it small.** If it's over ~30 lines it's not a working set, it's a filing cabinet. The
whole point is that a human reads it at a glance.

### `hot.yml` — keep loaded

```yaml
keep:
  - path: docs/auth-design.md
    why: "Core spec, referenced constantly"
    touches: 12
  - path: src/auth/session.ts
    why: "Currently editing"
    touches: 8
```

`why` is not decoration. It's what lets a human — or the agent, later — decide whether the
entry still earns its place. An entry without a `why` becomes permanent by inertia.

### `cold.yml` — evicted, with breadcrumbs

```yaml
evict:
  - path: logs/build-001.txt
    why: "Superseded by build-005"
    action: delete_from_working_set
  - path: research/oauth-comparison.md
    why: "Decision made — summarized"
    action: summarize_then_evict
    summary: .agent/summaries/oauth-decision.md
```

**Forgetting should be visible.** Cold isn't a graveyard — it's a record that says *I used to
care about this, here's why I stopped, here's how to get it back.* This is what makes
compression trustworthy: you can always audit what was dropped.

### `session-log.md` — append-only

```markdown
## 2026-07-15

- **Action:** Migrated session.ts to OAuth2 flow
- **Decision:** Kept legacy cookie path behind a feature flag
- **Why:** Q3 clients haven't migrated
- **Next:** Update docs/auth-design.md
```

Decisions and why. Not a transcript — a changelog for the agent's reasoning.

### `output.md` — append-only

Results for the human. The deliverable surface.

## Append-only, honestly

MOOLLM marks logs append-only, then adds this to `.cursorrules`:

> `possible_exception: "OK to Ninja Edit for consistency, coherence, error correction..."`
> `default_exception: "Ninja Edit if you can get away with it, but be careful!"`

That's not append-only. That's "append-only unless you feel like it," and it's a good example
of documenting a guarantee while shipping a tendency.

**Be honest.** Either:
- It's a **convention** — say so. The agent usually appends. Fine for a log nobody audits.
- It's **enforced** — get a hook. In Claude Code, a `PreToolUse` hook in `settings.json` that
  rejects `Edit` on `output.md`. That's a guarantee.

Don't write "APPEND-ONLY" in caps and mean "please."

## The advise/decide split

MOOLLM's intended design:

> *The model advises. The orchestrator decides.*

The model writes `hot.yml` proposing what to keep. The orchestrator reads it, weighs it against
budget and policy, and assembles context. The model doesn't get to be the only judge of what
it's allowed to forget.

**Nothing implements this.** On every real host, the model advises and then also decides,
because there's no one else in the room.

**For you:** that's fine — just know it. The files are still worth it for resumption,
auditing, and correctability, all three of which work with zero enforcement. But don't tell
yourself there's a memory manager. There's a diary the agent writes and re-reads.

If you want a real decider, the cheapest version is a human: read `hot.yml` at the start of a
session and edit it. That's a decider. It's you.

## Applying it

**This is the first mechanism to adopt.** One hour, works immediately, no prerequisites.

**Minimum viable:**

```
.agent/
├── working-set.yml     # what I'm doing
└── session-log.md      # what I did
```

Two files. Add `hot.yml` when you notice re-reading the same things. Add `cold.yml` when you
start compressing. Add `output.md` when you have deliverables.

**Gitignore `.agent/`.** It's runtime state, not source. MOOLLM gets this right.

**The failure mode:** files that drift from reality. A `working-set.yml` nobody updates is
*worse* than none, because it lies with authority. Update it at natural boundaries — task
switch, session end, major decision — or delete it.

## Checklist

- [ ] `.agent/` exists and is gitignored
- [ ] `working-set.yml` is under ~30 lines
- [ ] `hot.yml` entries all have a `why`
- [ ] `cold.yml` records *why* something was dropped and how to recover it
- [ ] `session-log.md` records decisions, not transcripts
- [ ] Anything labeled "append-only" is either enforced by a hook or honestly labeled convention
- [ ] Files get updated at task boundaries, or deleted
- [ ] You know whether you have a decider (you probably don't — that's OK)

Next: [05-standing-constraints.md](05-standing-constraints.md)
