# Evidence and Methodology

> **Tier:** Specification · argument: [WHITEPAPER.md](WHITEPAPER.md) · rules: [MECHANISMS.md](MECHANISMS.md)

Every quantitative claim in this series traces to this page. Two kinds of evidence appear,
and they are labeled throughout:

- **Measured** — produced by [`study/evidence/measure.py`](../../study/evidence/measure.py),
  a read-only script over the origin corpus (`moollm/`). Re-run it; results land beside it
  in `RESULTS.txt`.
- **Reported** — worked demonstrations from the origin repository's session transcripts.
  Real artifacts, not controlled experiments; treated as existence proofs only.

## Method and its error bars

Token counts are estimated at 4 bytes/token — a reasonable average for English prose and
YAML. Real tokenizers vary roughly 3.5–4.5 bytes/token, so **every absolute figure below
carries ±15%**. The *ratios* — which are what the arguments rest on — are insensitive to
this, because the same estimator applies to both sides of every fraction.

## The corpus (measured, 2026)

141 capability-unit directories in the origin repo.

| Tier | n | Total KB | Mean B | ~Tokens |
|---|---:|---:|---:|---:|
| GLANCE.yml | 140 | 229 | 1,675 | 58,615 |
| CARD.yml | 140 | 743 | 5,432 | 190,133 |
| SKILL.md | 140 | 1,509 | 11,037 | 386,290 |
| README.md | 131 | 607 | 4,742 | 155,290 |
| **Whole corpus** | | **3,087** | | **~790,329** |

Catalog (`INDEX.yml`): 19.9 KB ≈ **5,096 tokens — 155× smaller than the corpus**.
Glance-only sweep: ~58.6K tokens (13.5× compression).

## Cost by strategy (measured)

| Strategy | ~Tokens | % of corpus |
|---|---:|---:|
| Load everything | 790,000 | 100% — impossible |
| Sweep every glance | 58,615 | 7.4% — possible, wasteful |
| **Read catalog, then descend** | **5,096 + selection** | **0.6% + selection** |
| Catalog + 5 units full depth | ~33,100 | **4.2% — a working session** |

Descent pricing: 1 unit ≈ 5.6K tokens · 3 ≈ 16.8K · 5 ≈ 28.0K · 10 ≈ 56.1K. Because
sessions descend into a handful of units regardless of library size, **per-session cost is
nearly flat in corpus size** — the scaling claim behind M1.

## The free channel (measured)

The origin's boot file (`.cursorrules`, 12.7 KB ≈ 3,160 tokens) is auto-loaded by the host
every session. Inlining the twelve always-on constraints there, condensed, versus loading
their glance files individually:

```
12 × ~420 tokens + 12 file reads  →  ~1,800 tokens + 0 file reads   (~3×, and earlier)
```

## Tier discipline, verified by inspection

`skills/card/GLANCE.yml` (2.4 KB) against `skills/card/SKILL.md` (25.1 KB): the glance is
not the skill's opening — it is a different document whose payload is a one-line editorial
judgment (*"Cards are ACTIVATION TRIGGERS, not handlers"*) that no truncation of the longer
file would surface. This is the direct evidence for P3 (rewrite, not truncate).

## Negative findings (measured) — kept deliberately

The same script that produces the efficiency numbers detects the origin's failures. These
are part of the evidence *for the limits*, not embarrassments to hide:

| Finding | Value |
|---|---|
| Pyramid conformance | 131/141 units have all four tiers |
| Catalog drift | index claims 133 units; 141 exist (+8); the index *header comment* says 132, contradicting its own body |
| Published counts | four different skill-counts in origin docs; none correct |
| Boot artifact validity | `.cursorrules` **does not parse as YAML** (bad indentation, line 208) — and worked anyway for an unknown period, because only a model ever read it |

The last row is the single most instructive artifact in the corpus: simultaneous proof that
model-as-parser tolerance works (M10) and that it produces zero signal on corruption (M10
rule 5, whitepaper limit 2).

## Reported demonstrations (origin transcripts — existence proofs only)

| Demonstration | Scale | Calls used | Call-per-agent price |
|---|---|---:|---:|
| Multi-persona game session (rule-changing card game, 8+ personas) | 33 turns | 1 | ≥33 |
| Parallel character simulation (10 independent actors) | 21 turns · 210 character-turns | 1 | ≥210 |
| Character-creation deliberation with multi-persona tribunal | 1 ceremony | 1 | ~5–10 |

What these show: multi-turn, multi-perspective coherence within a single call is
achievable at nontrivial scale (M7). What they do not show: output *quality* versus a
call-per-agent baseline, persona independence (see M7 rule 4), or reproducibility across
models. Nobody has run those comparisons.

## What is not evidenced anywhere (open questions)

Stated once, bluntly, so no downstream document overclaims:

1. **Selection accuracy.** No eval measures whether a model picks the *right* unit from a
   catalog entry. This is the load-bearing question for M1/M2 adoption at scale.
2. **Ladder vs. embeddings.** No comparison against vector retrieval on cost or accuracy.
   The ladder's defensible advantage today is legibility/editability, not proven retrieval
   superiority.
3. **Ensemble quality.** No benchmark of in-context ensemble output against independent
   calls on the same task.
4. **Cross-model generalization.** All measurements and demonstrations come from one
   ecosystem of hosts and models.

## Reproducing

```
cd study
python evidence/measure.py     # read-only over ../moollm; writes nothing outside evidence/
```

The script checks pyramid conformance, computes the token economics, detects catalog drift,
and validates the boot artifact — i.e., it is both the measurement harness and the
reference implementation of the validator that limit 2 says every adoption needs.
