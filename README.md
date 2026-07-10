<div align="center">

<img src="https://raw.githubusercontent.com/pwr-ai/schematize/master/docs/assets/logo.png" alt="schematize logo" width="200" height="200">

# schematize

**Turn a plain research problem into a typed, data-tested extraction schema.**


[![PyPI version](https://img.shields.io/pypi/v/schematize.svg)](https://pypi.org/project/schematize/)
[![Docs](https://img.shields.io/badge/docs-pwr--ai.github.io-blue.svg)](https://pwr-ai.github.io/schematize)
[![Python](https://img.shields.io/pypi/pyversions/schematize.svg)](https://pypi.org/project/schematize/)
[![CI](https://github.com/pwr-ai/schematize/actions/workflows/ci.yml/badge.svg)](https://github.com/pwr-ai/schematize/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


[Documentation](https://pwr-ai.github.io/schematize) ·
[**Examples**](https://pwr-ai.github.io/schematize/examples/) ·
[Quickstart](https://pwr-ai.github.io/schematize/quickstart/) ·
[Pipeline](https://pwr-ai.github.io/schematize/pipeline/) ·
[API reference](https://pwr-ai.github.io/schematize/api/schema_generator/)

</div>

---

`schematize` is a Python library that turns a natural-language description of *what you want to
extract* into a **typed, validated extraction schema** — field names, types, descriptions, and
enums — ready to drive structured information extraction from a document collection.

Instead of hand-writing JSON schemas and discovering their gaps in production, you describe the
problem. A multi-agent [LangGraph](https://langchain-ai.github.io/langgraph/) pipeline asks
clarifying questions, drafts a schema, critiques and refines it, **tests it against real documents
from your corpus**, and opens a chat for final tweaks.

**See it in action first:** [worked examples](https://pwr-ai.github.io/schematize/examples/) show
three real, unedited pipeline runs — the clarifying-question chat and the resulting schema — each
run through five different LLMs.

## Why schematize?

- **Designing extraction schemas by hand is slow and brittle.** You guess the fields, miss edge
  cases, and only find out when extraction quality is poor.
- **Raw "ask an LLM for a schema" gives you an untested first draft.** No critique loop, no contact
  with your actual data, no typing guarantees.
- **schematize closes the loop:** clarify → draft → criteria-based refinement → **data-grounded
  refinement against retrieved documents** → interactive chat. The output is a Pydantic model you
  can plug straight into an extraction pipeline.
- **Use any LLM.** schematize accepts any LangChain chat model and talks to it through the
  OpenAI-compatible API, so the official OpenAI API, [LiteLLM](https://github.com/BerriAI/litellm),
  [vLLM](https://github.com/vllm-project/vllm), Ollama, and many other providers/servers work out of
  the box. We ran our experiments through a LiteLLM proxy. No provider lock-in.
- **Bring your own data.** Implementing a retriever is one async method; HuggingFace and Weaviate
  adapters are built in. A schema-coverage evaluator is included too.

| | Hand-written schema | Ask-an-LLM once | **schematize** |
|---|:---:|:---:|:---:|
| Clarifies an ambiguous request | ❌ | ❌ | ✅ |
| Iterative critique & refinement | ❌ | ❌ | ✅ |
| Validated against **real documents** | ❌ | ❌ | ✅ |
| Typed Pydantic output | manual | ❌ | ✅ |
| Built-in coverage evaluation | ❌ | ❌ | ✅ |

## Install

```bash
pip install schematize
```

Optional adapters and tooling:

```bash
pip install "schematize[huggingface]"   # FAISS retriever over HuggingFace datasets
pip install "schematize[weaviate]"      # hybrid-search retriever for a Weaviate instance
pip install "schematize[scripts]"       # Hydra-based CLI runners
```

Requires Python 3.12+. Full options in the [installation guide](https://pwr-ai.github.io/schematize/installation/).

## Quickstart

```python
from langchain_openai import ChatOpenAI
from schematize import SchemaGenerator, load_prompts


# 1. Any object with this async __call__ is a valid retriever (DocumentRetriever protocol).
#    Return documents relevant to `query`; each is shown to the data-assessment agent.
class MyRetriever:
    async def __call__(self, query: str, max_docs: int = 100) -> list:
        return [
            {"text": "The court awarded 15,000 PLN in damages for breach of personal rights..."},
            {"text": "Claim dismissed; the plaintiff failed to prove the violation..."},
        ]


# 2. Load bundled prompts for your language/domain (en|pl × law|tax).
prompts = load_prompts(language="en", system_type="law")

llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

generator = SchemaGenerator(llm=llm, retriever=MyRetriever(), **prompts)

# 3. Run the pipeline (interactive: it asks clarifying questions in the terminal).
state = generator.stream_graph_updates(
    "Study personal-rights violations in civil cases and assess their severity."
)
print(state["current_schema"])
```

A generated schema looks like this — a typed spec you can act on immediately:

```python
{
    "fields": [
        {"name": "violation_type", "type_": "enum", "enum_name": "ViolationType",
         "enum_values": ["privacy", "reputation", "image", "bodily_integrity"],
         "description": "Category of personal right that was violated."},
        {"name": "severity", "type_": "integer",
         "description": "Severity of the violation on a 0–5 scale."},
        {"name": "compensation_awarded", "type_": "boolean",
         "description": "Whether monetary compensation was granted."},
        {"name": "compensation_amount", "type_": "float",
         "description": "Awarded amount in PLN, if any."},
    ]
}
```

Turn it into a Pydantic model and use it for extraction:

```python
from schematize import SchemaFields, DynamicModelFactory

model_cls = DynamicModelFactory()(SchemaFields(**state["current_schema"]))
```

## Use any LLM (via LiteLLM)

`SchemaGenerator` takes any LangChain [`BaseChatModel`](https://python.langchain.com/docs/concepts/chat_models/).
Because it also honours an OpenAI-compatible `base_url`, the simplest way to reach **any** provider is
to put a [LiteLLM](https://github.com/BerriAI/litellm) proxy in front and point schematize at it —
the setup we used for our experiments:

```python
from langchain_openai import ChatOpenAI

# Point at a LiteLLM proxy; the model name routes to OpenAI, Anthropic, Gemini, local, etc.
llm = ChatOpenAI(model="claude-opus-4-8", base_url="http://localhost:4000", api_key="sk-litellm")
```

One interface, 100+ providers, no lock-in. See [Configuration](https://pwr-ai.github.io/schematize/configuration/).

## Retrieval is pluggable

The core library has **no retrieval dependency**. Implementing your own retriever is a single async
method — the `DocumentRetriever` protocol shown in the quickstart — so you can wrap Elasticsearch,
Postgres FTS, a REST API, or any vector store.

Two adapters ship in the box:

**HuggingFace** (`[huggingface]`) — FAISS index over any HuggingFace dataset, cached to disk:

```python
from schematize.retrieval.huggingface import HuggingFaceRetriever

retriever = HuggingFaceRetriever(
    dataset_name="JuDDGES/pl-court-raw", text_column="text", index_path=".cache/court-index"
)
```

**Weaviate** (`[weaviate]`) — hybrid search against a Weaviate instance:

```python
from schematize.retrieval.weaviate import WeaviateRetriever

retriever = WeaviateRetriever(collection_name="LegalDocuments")
```

Needs `WV_URL`, `WV_PORT`, `WV_GRPC_PORT`, `WV_API_KEY`. See the
[Weaviate guide](https://pwr-ai.github.io/schematize/guides/weaviate/).

`MMLWRobertaV2Retriever` (Polish-optimised, built on the HuggingFace base) is a worked **example of a
custom retriever** — read it as a template for specialising retrieval to your own model or language.
See the [custom retriever guide](https://pwr-ai.github.io/schematize/guides/custom-retriever/).

## Evaluate a schema

Score how well a schema can answer a set of expert questions:

```python
import yaml
from langchain_openai import ChatOpenAI
from schematize import SchemaEvaluator
from schematize.settings import PROMPTS_PATH

with open(PROMPTS_PATH / "eval" / "schema_evaluator.yaml") as f:
    evaluation_prompt = yaml.safe_load(f)["schema_evaluator_prompt"]

evaluator = SchemaEvaluator(ChatOpenAI(model="gpt-4o"), evaluation_prompt)
result = evaluator.evaluate_schema(schema, questions=["How severe was the violation?", ...])
print(result.covered_questions, "/", result.total_questions)
```

More in the [evaluation guide](https://pwr-ai.github.io/schematize/guides/evaluation/).

## Command-line runners

With the `[scripts]` extra you get three console scripts:

```bash
schematize-run                              # interactive pipeline
schematize-run-mocked +case=en_age          # replay a stored case (no live prompts)
schematize-evaluate +case_name=age          # evaluate against expert questions
```

See the [CLI guide](https://pwr-ai.github.io/schematize/guides/cli/) for mocked-case files and options.

## Reproducing our study

The experiments from our paper are driven by the mocked runner (schema generation) and the evaluator
(schema scoring against expert questions). Cases live in [`data/cases/`](data/cases/) and expert
question sets in [`data/eval/`](data/eval/) (`pl_age`, `pl_personal_rights`, `pl_medical_errors`).

The paper's experiments use the `pl`/`law` domain (Polish legal judgments); `tax` and `general` are
additional prompt sets for use beyond the paper.

```bash
git clone https://github.com/pwr-ai/schematize && cd schematize
uv sync --extra scripts --extra huggingface

# Configure the LLM in a .env file (we used a LiteLLM proxy — see "Use any LLM" above)
printf 'API_KEY=...\nAPI_URL=...\n' > .env

# 1. Generate schemas for every case (multiple runs per case)
bash scripts/experiments/search_params.sh

# 2. Ablation over pipeline components (no problem-definition / no refinement / no data-grounding)
bash scripts/experiments/ablation.sh <model>

# 3. Evaluate generated schemas against expert questions
bash scripts/experiments/eval_multirun.sh <eval_model> <generation_model>
```

The shell scripts in [`scripts/experiments/`](scripts/experiments/) are thin Hydra wrappers; edit the
`MODEL`/`CASES` variables at the top to change the grid. Results are written to the Hydra output
directory.

> **Note:** exact model names, seeds, and hyperparameters used in the paper are documented in the
> [reproduction guide](https://pwr-ai.github.io/schematize/) — fill in once the study is published.

## Citation

If you use schematize in your research, please cite:

```bibtex
TBA
```

## Development

```bash
uv sync --extra dev
make check    # ruff lint
make test     # pytest + coverage
make fix      # ruff --fix
```

## License

Released under the [MIT License](LICENSE).
