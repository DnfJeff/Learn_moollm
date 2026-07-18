# DnfBrain — a Legible Library instance

**A long-term "everything" brain space: every finding, spec, decision, and reference —
classified like a library, browsable on GitHub and in Obsidian, and navigable by an AI agent
that will never fit it in one context window.**

This is a fully scaffolded instance of the
[Legible Library](https://github.com/DnfJeff/Learn_moollm) pattern — the
[MOOLLM](https://github.com/SimHacker/moollm) mechanisms by **Don Hopkins**, applied at
collection scale. Staged 2026-07-18; built to be transplanted into its own repository and
used forever going forward.

## The idea

You wouldn't walk into an empty library and start stacking books in the walkways. This space
is organized **before** it is full: the shelves exist ahead of the books, so everything —
including things that don't exist or aren't known yet — already has a route down the tree to
a unique address. And the address carries the backstory:

```
library/domains/arts/film/tv/1950s/sitcom/the-danny-thomas-show/characters/danny-thomas.md
library/domains/tech/pc/gaming/simulation/the-sims/the-sims-1/technical/dev/docs/
```

It's clear who Danny was — and where a Sims file-format doc would be shelved — from the path
alone, before a single file opens.

## Navigation — everything from here

| Door | Go to | For |
|---|---|---|
| 🏛️ **Front desk** | [HOME.md](HOME.md) | the landing note; open as an Obsidian vault here |
| 📇 **The directory** | [library/INDEX.md](library/INDEX.md) | the chief librarian: which section holds what |
| 🎭 **Characters** | [library/characters/](library/characters/README.md) | by-name lookup; cards route to full write-ups |
| 📥 **Inbox** | [library/inbox/](library/inbox/README.md) | drop anything, classify later |
| 🗂️ **The sections** | [library/domains/](library/domains/README.md) | arts · tech · science · humanities · life · practices |
| 🚧 **Projects** | [library/projects/](library/projects/README.md) | time-bound work; feeds the sections |
| 🧰 **Capabilities** | [capabilities/INDEX.yml](capabilities/INDEX.yml) | curator · registrar · project-intake |
| 📜 **How it evolved** | [library/meta/structure-log.md](library/meta/structure-log.md) | every structural change, with reasons |

## The three moves that make it work

1. **The card stack.** Every shelf and note is written at four sizes — `GLANCE.yml` (is this
   relevant?) → `CARD.yml` (routing) → `SKILL.md` (the knowledge/ledger) → `README.md`
   (history, for humans). A reader loads the cheapest tier that answers the question. YAML
   for agents, Markdown for humans, side by side — one directory, two audiences.
2. **The librarian chain.** Nobody holds the whole map. The directory names the section; the
   section's librarian knows its shelves; each shelf's finding aid maps the next level. New
   material walks the chain (`capabilities/curator/`); new projects get wired at birth
   (`capabilities/project-intake/`).
3. **Registries.** Some things are reached by *name*, not by class — characters first, maybe
   languages and tools later. A registry is a surfaced layer of small YAML quick cards (plus
   a browsable roster) routing to the full write-ups deep in the tree — one card, N
   appearances, never a second copy. Standardized in
   [library/_templates/registry/](library/_templates/registry/README.md), maintained by
   `capabilities/registrar/`.

## Using it

```bash
# as an agent workspace: AGENT.md is the boot file (already mirrored to CLAUDE.md)
python validate.py          # card stacks, ledgers, and counts stay honest — run it in CI

# as a human: open this folder as an Obsidian vault, start at HOME.md
```

Capture is free; filing is deliberate. Anything goes in the inbox the moment you have it —
the librarians place it later.

## Credit

The mechanisms originate in [MOOLLM](https://github.com/SimHacker/moollm) by Don Hopkins
(SimHacker), presented domain-neutrally in
[Learn_moollm](https://github.com/DnfJeff/Learn_moollm), from whose `library-template/` this
instance was staged. The registry layer and the six-section spread are this instance's own
configuration of that pattern — logged, like everything structural, in the
[structure log](library/meta/structure-log.md).
