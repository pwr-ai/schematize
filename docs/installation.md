# Installation

Python 3.12 or newer is required.

## Core library

```bash
pip install schematize
```

The core package includes the pipeline, schema models, and evaluator. It has **no retrieval dependency** — you bring your own document store or install one of the optional adapters below.

## Optional extras

### Weaviate adapter

```bash
pip install "schematize[weaviate]"
```

Adds [`WeaviateRetriever`](guides/weaviate.md) for hybrid-search retrieval against a Weaviate instance.

### HuggingFace adapter

```bash
pip install "schematize[huggingface]"
```

Adds [`HuggingFaceRetriever`](guides/huggingface.md) and [`MMLWRobertaV2Retriever`](guides/huggingface.md) for FAISS-indexed retrieval over HuggingFace datasets.

### Research reproduction

The paper's Hydra runners and analysis notebooks live outside the distributable
package. From a source checkout, install them with:

```bash
uv sync --extra dev --extra research --extra huggingface
```

See the [research README](https://github.com/pwr-ai/schematize/tree/master/research).

### Development

```bash
pip install "schematize[dev]"
```

Adds pytest, coverage, ruff, mypy, and pre-commit.

### Multiple extras at once

```bash
pip install "schematize[weaviate,dev]"
```

---

## Installing with uv

```bash
uv add schematize
uv add "schematize[huggingface]"
```

---

## Environment variables

Set these before running the pipeline. See [Configuration](configuration.md) for details.

```bash
# LLM access (required)
API_KEY=sk-...
API_URL=https://api.openai.com/v1   # optional, for self-hosted endpoints

# Weaviate (only needed with [weaviate] extra)
WV_URL=localhost
WV_PORT=8080
WV_GRPC_PORT=50051
WV_API_KEY=...
```

Scripts auto-load a `.env` file in the working directory via `python-dotenv`.

---

## CLI runner

The package installs one supported console command:

| Command | Description |
|---------|-------------|
| `schematize-run` | Interactive pipeline (prompts for user input at each step) |

```bash
schematize-run
```
