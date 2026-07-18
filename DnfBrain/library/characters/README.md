---
status: canonical
tags: [registry, character, finding-aid]
---

# 🎭 Characters — the by-name registry

**This is the browsable layer of the characters registry: the human navigation that sits
beside the YAML cards, the way a README sits beside a SKILL everywhere else in the moollm
pattern.** Agents scan [`MANIFEST.yaml`](MANIFEST.yaml) and the cards; you browse this page.
Same roster, two audiences.

A character's **full write-up lives with its work**, deep in the tree — that's where the
path carries the backstory
(`arts/film/tv/1950s/sitcom/the-danny-thomas-show/characters/danny-thomas.md` tells you who
Danny was before you open it). This registry exists because people are *looked up by name*:
one small card per figure, routing to every write-up that figure has earned, across shows if
need be.

## The roster

| Figure | Known for | Full write-up(s) |
|---|---|---|
| **Danny Thomas** (Danny Williams) | star of *The Danny Thomas Show*, 1950s sitcom; St. Jude founder | [on The Danny Thomas Show](../domains/arts/film/tv/1950s/sitcom/the-danny-thomas-show/characters/danny-thomas.md) |

## How this works

- **[`MANIFEST.yaml`](MANIFEST.yaml)** — the scan tier: every card, one row, machine-fast.
- **`<name>.yaml`** — the quick card: who, why known, aliases, and `appearances:` routes to
  the write-up(s). Small on purpose; content lives in the write-ups.
- **[`SKILL.md`](SKILL.md)** — the registry rules (what keeps cards from becoming a second
  home) and the annotated roster.
- **Adding someone:** write-up first (with its work), then card + manifest + this table — the
  [`registrar`](../../capabilities/registrar/README.md) capability walks it.

Registries are a standardized pattern, not a characters-only trick — see
[`../_templates/registry/`](../_templates/registry/README.md) for when a category (languages,
tools, people) earns a surfaced by-name layer like this one.
