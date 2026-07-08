# Baselines

External systems run on the same cases, documents, and evaluation protocol as
schematize, so their numbers are directly comparable with schematize runs.

Currently included: **ScheMatiQ** ([shaharl6000/ScheMatiQ](https://github.com/shaharl6000/ScheMatiQ),
arXiv:2604.09237) — query-driven schema discovery over a document collection.

## Quick start

```bash
# 1. Pull + install ScheMatiQ (pinned commit) into the uv environment
bash baselines/setup_schematiq.sh

# 2. Inference, then evaluation
bash baselines/baseline_schematiq.sh
bash baselines/eval_schematiq.sh
```

`API_KEY`/`API_URL` are read the same way as in `scripts/experiments/` — from
the environment or `.env` (unset `API_URL` = native OpenAI API, set = an
OpenAI-compatible proxy such as LiteLLM). Both steps pick them up automatically.

## Scripts

### `setup_schematiq.sh [ref]`

Clones ScheMatiQ into `baselines/ScheMatiQ` (gitignored — third-party repo),
checks out the pinned commit used for the published baseline results
(`dc8f93d…`, override with a ref argument), installs the project environment
(`uv sync --extra huggingface --extra scripts`) plus `schematiq-lib` in
editable mode, and smoke-tests the import.

### `run_schematiq_baseline.py --case <case> --model <model>` (inference, one case)

Runs ScheMatiQ schema discovery for a single case in `data/cases/*.yaml` and
writes a schematize-compatible output, mirroring `scripts/baseline.py`.

Pipeline:

1. **Document retrieval** — top `--top-k-docs` (50) rulings from
   `JuDDGES/pl-court-raw` using `sdadas/mmlw-retrieval-roberta-large-v2`
   (schematize's default retriever, `config/retriever/mmlw.yaml`) over the
   **full corpus** by default (`--max-documents null`; pass an integer to cap it).
   The FAISS index is cached at `.cache/schematize/JuDDGES_pl-court-raw`
   (schematize's default retriever cache location) and reused across runs.
   The retrieval query is the same as the discovery query (full case dialogue),
   and documents are fed to ScheMatiQ in descending relevance order.
2. **Schema discovery** — ScheMatiQ `discover_schema` with the **full case
   dialogue** as query (`user_input` + clarification questions + user answers;
   `--no-full-dialogue` for the query-only variant), its passage-level
   `EmbeddingRetriever` localized to **`sdadas/mmlw-retrieval-roberta-large-v2`**
   for Polish (`--passage-k` 8 passages/doc; the ScheMatiQ default is a weak
   multilingual MiniLM — only the embedding backbone is swapped, the algorithm is
   unchanged), batches of `--documents-batch-size` (4) docs, up to `--max-iters`
   (6) iterations or Jaccard convergence. Column count is **unlimited** by
   default (`--max-keys-schema null`, ScheMatiQ's native `MAX_KEYS_DEFAULT`);
   pass an integer to cap and prune to the most query-relevant columns.
   Note: ScheMatiQ reads at most `documents_batch_size × max_iters`
   (≈24) documents — the top-`top_k_docs` shortlist only needs to exceed that.
3. **Output** — under
   `outputs/schematiq/schematiq_<model>_<variant>/<case>/`:
   - `schematiq_artifact.json` — native ScheMatiQ artifact (columns,
     observation unit, document contributions, schema evolution).
   - `state.json` — schematize-compatible state: `current_schema` in
     `SchemaFields` format (see below) plus baseline metadata. Existing
     `state.json` ⇒ the case is skipped (idempotent).

Environment: `API_KEY` (required, envvar or `.env`), `API_URL` (optional
proxy) — read the same way as `scripts/baseline.py`, and mapped internally to
`OPENAI_API_KEY`/`OPENAI_BASE_URL` for ScheMatiQ's OpenAI backend.

ScheMatiQ adaptations (in `PatchedOpenAILLM`, no upstream changes):

- `max_output_tokens` → `max_tokens` (ScheMatiQ passes the former to a client
  that only accepts the latter).
- Native-OpenAI reasoning models: on BadRequest, retries with
  `max_completion_tokens` and/or default temperature (a LiteLLM proxy
  translates these automatically; the native API does not).

Schema mapping ScheMatiQ → schematize `SchemaFields`: column `name` → field
`name`; `definition` + `rationale` concatenated → `description`;
`allowed_values` present → `type_: enum` with `enum_values`, else
`type_: string`.

### `baseline_schematiq.sh` (inference, all models × all cases)

Loops `run_schematiq_baseline.py` over the same `MODELS` × `CASES` matrix as
`scripts/experiments/baseline.sh` (edit the `MODELS` array to enable more
generation models).

### `eval_schematiq.sh [eval_model]` (evaluation, all models × all cases)

Runs `scripts/evaluate_schema.py` per generation model / case (`final_only=true`,
judge = `eval_model`, default `gpt-5.4-mini`) against the outputs of
`baseline_schematiq.sh`, mirroring `scripts/experiments/eval_baseline.sh`.

## Evaluation protocol — parity with schematize

Both the baseline and schematize library runs are scored by the **same**
pipeline; verified equivalences:

| Aspect | schematize | ScheMatiQ baseline |
|---|---|---|
| Cases | `data/cases/*.yaml` | same files |
| User information | `user_input`, then mocked replay of `problem_help`/`user_feedback` (`schema_generator_mocked.py`) | same dialogue concatenated into the discovery query (`full_dialogue` variant) |
| Corpus & retriever | `JuDDGES/pl-court-raw`, mmlw-roberta-large-v2 | identical (shared FAISS index cache) |
| Schema in `state.json` | `SchemaFields.model_dump()` → `{"fields": [...]}` (`basic_agents.py`) | identical structure |
| Judge | `scripts/evaluate_schema.py`: `evaluator.yaml` prompt, structured per-question `is_covered` + confidence | same script, same prompt, same judge model/params |
| Expert questions | `data/eval/<case>/expert_*.yaml` (`rejected_expert_*` excluded by the glob) | same |
| Final-schema scoring | `final_only=true` (`scripts/experiments/eval_multirun.sh`) | same flag |
| Metrics | covered / high / medium / low confidence per expert | same |

Known caveats:

1. **Corpus** — the baseline now indexes the **full corpus** by default
   (`--max-documents null`), matching schematize's `config/retriever/mmlw.yaml`
   (`max_documents: null`), so both systems retrieve from the same pool. Pass an
   integer to `--max-documents` to cap it for a faster smoke test.
2. **Evaluator prompt format note** — `evaluator.yaml` describes a
   name-keyed schema format, while both systems actually submit the
   `{"fields": [...]}` dump. Both deviate identically, so the comparison is
   unbiased, but the prompt could be tightened.
3. **Baseline descriptions** — ScheMatiQ column `definition`+`rationale` are
   concatenated into `description`, which gives the judge slightly more prose
   per field than typical schematize descriptions. Content-equivalent, not
   protocol-divergent.
