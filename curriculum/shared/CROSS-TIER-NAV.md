# Cross-Tier Navigation Convention

Every series document carries a one-line tier bar directly under its H1, linking one tier up
and one tier down for the *same* content. Format:

```markdown
> **Tier:** Practitioner · deeper: [spec/MECHANISMS.md#m4](../spec/MECHANISMS.md#m4) · plainer: [onramp/THE-SIX-IDEAS.md#m4… ]
```

Rules:

1. **Up-link label is "deeper," down-link label is "plainer."** Never "advanced/beginner" —
   the tiers are resolutions, not ranks.
2. Link to the **specific section** covering the same mechanism (`#m1`…`#m10`, `#p1`…`#p3`),
   not to a document top, wherever a per-mechanism anchor exists.
3. Set A documents have no up-link (top rung: cite `study/` evidence instead).
   Set C documents have no down-link.
4. Anchors are stable: every tier's per-mechanism sections are headed with the canonical
   number and name from [CANON.md](CANON.md) (e.g. `## M4 · Externalized state`), so the
   anchor is predictable from the number alone.
5. The tier bar is the only place a document references other tiers. Body prose never says
   "as explained in the spec" — each tier must stand alone.
