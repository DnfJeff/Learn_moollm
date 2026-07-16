# Core Policy

Host-independent rules. Everything here is true regardless of where the agent runs.
Host-specific mappings live in `drivers/`.

Keep this small. It's loaded often.

## 1. State lives in files

No hidden memory. If the agent knows it, a human can open it.

| File | Mode | Holds |
|---|---|---|
| `.agent/working-set.yml` | read/write | Current focus. Under 30 lines. |
| `.agent/hot.yml` | read/write | Keep-loaded, each with a `why` |
| `.agent/cold.yml` | read/write | Evicted, with breadcrumbs back |
| `.agent/session-log.md` | append | Decisions and why |
| `.agent/output.md` | append | Results for the human |

Update the working set at task boundaries. **A stale working set is worse than none** — it
lies with authority.

Append-only is a **convention** here. Nothing enforces it. If you need a guarantee, add a
`PreToolUse` hook. Don't write "APPEND-ONLY" and mean "please."

## 2. Read at the cheapest useful resolution

```
capabilities/INDEX.yml → GLANCE.yml → CARD.yml → SKILL.md → README.md
```

**Never load a tier without first loading the tier above it.** Most reads stop at `CARD.yml`.

## 3. Point at what the model already knows

Names the model understands are free. Invented jargon is billed on every call, forever, and
never gets cheaper.

- ✅ *service, module, session, cache, index, idempotent, regression*
- ❌ *WidgetProc, FooManager, "the blue pipeline", "our Level-3 protocol"*

If you must coin a term, define it **once, in a file**, then always use it. Never two names for
one thing.

## 4. Liberal in, conservative out — but validate yourself

Accept typos, vague requests, missing fields. Infer intent. Emit clean, well-formed output.

**And validate what you authored.** Run `validate.py`. Postel's law is about protocol peers,
not about your own config files. Being liberal with yourself isn't robustness; it's an absence
of tests.

## 5. Never crash — degrade

Priority: **survive → heal → function → optimize.**

| Situation | Response |
|---|---|
| Missing optional file | Note it. Continue. |
| Unknown host | Assume tier 1. Continue. |
| Unparseable *input* | Best interpretation. Continue. |
| Unparseable *config you wrote* | **Stop. Say so.** |

The last row is the line MOOLLM doesn't draw, which is why its boot file has been invalid YAML
with two constraints silently dropped.

## 6. Say what actually happened

- Tests failed → say so, with the output.
- Step skipped → say that.
- Didn't run something → don't imply you did.
- Uncertain → say how uncertain, as a number.

Reporting a tendency as a guarantee is the failure this whole policy exists to prevent.

## 7. Intent is explicit

Before a consequential action, state why. If your host supports a `why` parameter, use it. If
not, say it in prose first. The mechanism varies; the principle doesn't.

## 8. Capabilities declare their own relevance

Triggers live on the capability, never in a central router. Adding a capability means adding a
directory and nothing else.

**Limit:** triggers are read by a model, not evaluated by an engine. Soft routing only. If
correctness depends on the choice, put a real check in the code path.

## 9. Every file is sniffable in 50 lines

The first ~50 lines of any file — doc, config, or script — must be enough to decide whether
to keep reading. Docs: purpose and file map up top. Scripts: docstring, imports, constants,
CLI surface first; implementation below the fold. One artifact serves both readers: the
human gets `--help`, the model gets the top of the file.

## 10. Deterministic work goes in scripts

When a consistent, mechanical sub-procedure emerges inside a capability, lift it out of
prose and into a script the capability ships. The doc shrinks to judgment; the script owns
repetition. The model is for judgment, creativity, and language — never for arithmetic,
counting, or validation that must be *correct* rather than plausible.
