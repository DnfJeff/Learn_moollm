# Guide 9 · Names as addresses

> **Tier:** Practitioner · deeper: [spec/MECHANISMS.md#m9](../../spec/MECHANISMS.md#m9--names-as-addresses) · plainer: [onramp/THE-TEN-IDEAS.md#m9](../../onramp/THE-TEN-IDEAS.md#m9--names-as-addresses)

**The symptom.** Your docs spend paragraphs re-explaining things the model already knows
("our retry system, which attempts the operation again after failure with increasing
delays…"). Meanwhile your *actual* project concepts have three names each, or names that
mean nothing ("the blue pipeline", `FooManager2`), and every session pays to re-establish
them.

**What you build.** A naming discipline plus one small file. The economics, from the origin,
worth memorizing:

> **Latent knowledge is prepaid; respelled knowledge is billed per call, forever. Novel
> jargon is a cache miss that never fills.**

"Exponential backoff" costs three tokens and activates everything the model knows about
retries, jitter, and thundering herds. Your paragraph costs 60 tokens, every call, and
activates less.

## The discipline

1. **The test, before naming anything:** *is the pointee already in the model's latent
   space?* If yes — **point.** Say `idempotent`, `write-ahead log`, `circuit breaker`,
   `Postel's law`. Don't explain them; explaining prepaid names to the model is paying
   twice (the origin names this anti-pattern: humansplaining).
2. **If no — coin once, in a file.** Project-specific concepts deserve names, defined
   exactly once, then used everywhere without re-explanation. Never two names for one
   thing.
3. **Names are for humans too.** A doc that says "this is basically SimAntics" and stops
   has served the model and abandoned your teammate. One sentence of gloss for the human,
   the bare name for the model — both readers, one line.

## The files

`GLOSSARY.yml` at the workspace root — the project's controlled vocabulary:

```yaml
# Project vocabulary. Coin here once; point everywhere else.
INGEST-PIPELINE:
  means: "S3 drop → schema check → dedupe → warehouse load"
  defined_in: docs/ingest.md
  not_to_be_confused_with: "the export pipeline (reports/)"
SOFT-DELETE:
  means: "status=archived + 90-day purge job; rows never DELETEd in app code"
  invoke_when: "any schema or deletion discussion"
```

And a **file-naming rule** that makes listings do addressing work: most-significant
component first, so related files sort together (`auth-design.md`, `auth-migration.md`,
`auth-review-2026-06.md` — a directory listing *is* an index, and the agent reads listings
constantly). Sidecar files inherit their subject's prefix and cluster with it.

## Verify it's working

1. Grep your docs for re-explanations of standard concepts. Each is a paragraph that should
   be a name.
2. Ask the agent (fresh session) what `SOFT-DELETE` means here. Correct answer from the
   glossary, without you pasting anything — the name now routes.
3. The teammate test: can a new person read one doc without asking you to translate? Every
   term they'd ask about is either standard (fine) or in the glossary (fine) or neither
   (fix it).

## The traps

- **Private jargon accretion** — coining what didn't need coining. Every invented term is a
  tax on models *and* humans; the origin's game-world codebook is the cautionary tale — free
  for the model, a wall for every human without the codebook.
- **Two names, one thing** — "the ingest pipeline," "the loader," "Dave's script." Pick one,
  glossary it, kill the rest.
- **Glossary sprawl** — if it needs sections, most entries aren't earning their place. It's
  a controlled vocabulary, not a wiki.
