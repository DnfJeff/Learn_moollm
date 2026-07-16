# Guide 8 · Directory-as-object

> **Tier:** Practitioner · deeper: [spec/MECHANISMS.md#m8](../../spec/MECHANISMS.md#m8--directory-as-object) · plainer: [onramp/THE-TEN-IDEAS.md#m8](../../onramp/THE-TEN-IDEAS.md#m8--directory-as-object)

**The symptom.** Your agent's capabilities live in a registry that needs regenerating, a
config that needs syncing, or a database nobody can diff. Finding out "what can this system
do" requires tooling. Adding a capability touches four files in three places.

**What you build.** A convention, mostly — this guide is more habits than artifacts:

1. **One capability = one directory. The path *is* the identity.**
   `capabilities/code-review/` needs no ID, no registration, no manifest entry beyond its
   one index line. References are paths; fragment references reach into bundles
   (`capabilities/checks/INDEX.yml#no-secrets`).
2. **Marker files are interfaces.** A directory *is* whatever its marker files say it is:
   `CARD.yml` present → routable capability. Add `TEMPLATE.yml.tmpl` → it's also a factory.
   "Does X support Y?" is a file-existence check — no schema registry, and a directory can
   be several things at once.
3. **Discovery is `ls`.** The capability list is the directory listing. Git provides
   versioning, diffing, review, and history for free because everything is text. There is
   no build step to break.

## The factory pattern (the 20% you'll actually feel)

Capabilities that produce recurring *instances* — report formats, checklists, session
templates — ship templates and a starter catalog:

```
capabilities/retro/
├── CARD.yml
├── RETRO.md.tmpl            # the factory: instantiation copies this out
└── retros/                  # instance library: worked examples users copy or reference
    ├── 2026-06-sprint.md
    └── incident-postmortem.md
```

Behavior lives in the prototype (the capability); state lives in the instances (the copies,
elsewhere, accumulating their own content). This is the scaffold experience in miniature —
what [SCAFFOLD.md](../SCAFFOLD.md) did for the whole workspace, any capability can do for
its own outputs.

**And instantiation has a cost dial.** Cheapest first: *mention* the capability by name (no
files — often enough) → use it *in-conversation* → *embed* its output in an existing doc →
*instantiate* a full stateful copy. Start at the cheap end; most uses never need the
expensive end.

## What to defer

The origin goes further: prototype inheritance chains (`parents:` arrays resolved
Self-style), multi-marker dispatch, per-directory metadata sidecars. All coherent; none of
it is the load-bearing part. **Identity = path, interface = marker file, discovery = `ls`**
is the 80%. Add an inheritance resolver the day you have a demonstrated need and not
before — ceremony is the documented failure mode of this mechanism.

## Verify it's working

1. `ls capabilities/` answers "what can this agent do?" with no tooling.
2. Delete a capability directory (in a branch). Nothing else breaks except its index line —
   which `validate.py` catches as drift.
3. Ask the agent to create an instance from a factory capability. It copies the template
   out, into the right place, and the instance carries its own state from then on.

## The traps

- **Ceremony creep** — four tier files and a prototype chain for a two-line helper. A
  capability earns structure by being used, not by existing.
- **Registry regression** — a generated `manifest.json` that something starts depending on.
  The moment discovery needs a build step, you've reinstalled the disease.
- **Instances drifting into the prototype** — worked examples accumulating inside the
  capability until nobody can tell the template from the copies. Instances live in the
  library subdirectory or outside; the prototype stays clean.
