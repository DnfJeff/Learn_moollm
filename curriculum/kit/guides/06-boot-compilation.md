# Guide 6 · Boot compilation

> **Tier:** Practitioner · deeper: [spec/MECHANISMS.md#m6](../../spec/MECHANISMS.md#m6--boot-compilation) · plainer: [onramp/THE-TEN-IDEAS.md#m6](../../onramp/THE-TEN-IDEAS.md#m6--boot-compilation)

**The symptom.** Every session opens with the same ritual: the agent reads the same eight
files, re-derives the same orientation, asks the same "what are we working on?" You're
paying a fixed startup tax in tokens and minutes, every single day, for information that
barely changes.

**What you build.** Two things: a *free-channel discipline* (what goes in the auto-loaded
file) and a *recompile habit* (the loop that keeps it current).

## The free channel

Every host auto-loads something at session start — `CLAUDE.md`, `.cursorrules`, a system
prompt. Content there is **prepaid**: it arrives before the model does anything, at no
marginal read. The rule pair:

> **If you need it every session, it goes in the free channel — inlined.**
> **If you need it sometimes, it goes in the ladder — pointed at.**

Confusing these two is the most common context-budget mistake in both directions: hot
content left in the library costs N reads per session forever; cold content pasted into the
boot file taxes every call for nothing.

What earns inlining (the template's `AGENT.md` is this list, implemented): standing
constraints at full text · the reading rule · the state-file table · the host-detection
line. What gets pointers only: the capability index, policy details, drivers.

Measured effect in the origin: inlining the twelve always-on constraints replaced twelve
per-session file reads with zero and cut their resident cost ~3× (~5,000 → ~1,800 tokens).

## The loop

The boot file is a **compilation artifact with you as the compiler**:

```
work  →  introspect  →  compile  →  boot  →  (repeat, roughly monthly)
```

**Introspect:** skim recent `session-log.md` files and ask three questions — What did the
agent read every single session? (→ inline it or hot-list it.) What's in the boot file that
no session used? (→ evict it.) What correction did I issue twice? (→ new standing
constraint, [guide 5](05-standing-constraints.md).)

**Compile:** apply the answers to the boot file. Keep it under budget (~2,000 tokens — the
validator warns past it). **Compile *out* as aggressively as in** — the free channel isn't
free past the model's attention span; it's just prepaid.

The origin automates the introspect step with a host-specific tool; doing it by hand
quarterly captures most of the value and is host-proof.

## The boot sequence (one paragraph in your boot file)

Give session start a declared order instead of vibes:

> On start: (1) confirm which host you're on and load its driver; (2) check `.agent/` —
> create any missing file from its minimal stub ([guide 10](10-tolerant-interpretation.md));
> (3) read `working-set.yml` and `hot.yml`; (4) state the current task in one line and
> continue it.

Four steps, deterministic, cheap — and step 4 doubles as your smoke test.

## Verify it's working

1. Cold-start a session and say only "continue." Correct one-line statement of the current
   task, without a file-reading spree beyond `.agent/` — pass.
2. Count session-start reads before and after inlining. The delta is your saving; it should
   be roughly "number of always-needed files → zero."
3. `python validate.py` — it checks the boot file's token budget and (unlike the origin,
   whose boot file was silently invalid YAML for months) that it parses.

## The traps

- **Boot bloat** — the free channel becoming an attic. Rent applies to every call.
- **Stale compilation** — a boot file preloading last quarter's project. The recompile
  habit *is* the mechanism; without it this is just a config file that ages.
- **Compiling in what should be a pointer** — inline the always-needed *text*, point at
  everything else. The boot file is a lobby, not a warehouse.
