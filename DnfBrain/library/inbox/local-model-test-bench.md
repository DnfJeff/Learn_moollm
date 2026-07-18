# inbox item — local-model test bench plan

**Breadcrumb:** captured 2026-07-18 from the DnfBrain initialization request (the owner's
stated plan, lightly structured). Unverified, unclassified — that's what the inbox is for.

The plan: use DnfBrain's procedures as a **test bench for local models** — the patterns are
proven on flagship models; the open question is what a small local model executes faithfully.

- Runner-up under test: **Gemma 4** (local), driven through an agentic CLI (**Hermes**).
- Serving: **LM Studio** today; evaluating **vLLM** (installed; Google-recommended for Gemma)
  as a replacement. Model folder is separate — try to **reuse LM Studio's downloaded models
  in place** with vLLM rather than re-downloading.
- First benchmark: the `project-intake` OPEN flow ("hey, I've got a new project"), run in a
  separate local session against a real first project. Judge by the files: instance in the
  right place, `references/` wired, by-project row present, `validate.py` passes.
- Real goal: rapid iteration with best-effort monitoring of what the model actually did —
  the library's file-native discipline is what makes that auditable.

**Triage note (for future filing):** likely atomizes into `tech/ai/local-models/` (vLLM vs
LM Studio findings; model-folder reuse), `tech/ai/agents/` (Hermes CLI behavior), and a
`projects/` instance for the first project itself. Results first; this stays here until there
are findings worth carding.
