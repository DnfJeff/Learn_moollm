---
status: canonical
tags: [templates]
---

# _templates — copy-me card stacks

**This is the templates README: the prototypes you copy to add to the library. Underscore-prefixed
so it sorts to the top and never gets mistaken for real content.**

Instantiation is copy-a-directory. Each template is a card stack you fill in.

| To add… | Copy | To |
|---|---|---|
| A new classification **section** | [`section/`](section/) | `library/domains/<name>/` |
| A new knowledge **unit** (full card stack) | [`unit/`](unit/) | `library/domains/<section>/<name>/` |
| A quick **note** (cheap rung, one file) | [`note.md`](note.md) | anywhere a unit goes; graduate later |
| A new **project** (instance) | [`project/`](project/) | `library/projects/<name>/` |

## The cost dial — start cheap

Not everything needs a full stack. Cheapest first: *mention* it in another unit → *model* it in a
project log → *embed* it in a larger doc → *instantiate* a full carded directory. Use `note.md`
for something you're not sure will grow; graduate it to a `unit/` directory when it becomes
reference-grade or routable. Never four files for a two-line helper.

## After you copy
1. Fill the tiers — each rewritten for its depth, never truncated from the one below.
2. Put real `provenance`/`status` in the `SKILL.md` frontmatter.
3. Register it: the section ledger (`SKILL.md`), the catalog line, `meta/by-*` finding aids.
4. `python validate.py`.
