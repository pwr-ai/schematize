# schematize

Agentic system for automated extraction-schema generation. Given a natural language description of what information you want to extract, schematize runs a multi-agent LangGraph pipeline that produces a structured schema suitable for information extraction from documents.

## Features

- Multi-agent pipeline: problem definition → query generation → schema generation → refinement → data-grounded assessment
- Interactive chat at the end to refine the schema further
- Built-in evaluator that scores schemas against expert questions
- Language support: English (`en`) and Polish (`pl`)
- Domain support: tax interpretations (`tax`) and legal judgments (`law`)
- Pluggable document retriever via a clean protocol — bring your own corpus or use the optional Weaviate adapter

## Install

```bash
pip install schematize
```

With the optional Weaviate adapter (for the built-in legal document retriever):

```bash
pip install schematize[weaviate]
```

With the Hydra-based runner scripts:

```bash
pip install schematize[scripts]
```

## Quickstart

```python
from langchain_openai import ChatOpenAI
from schematize import SchemaGenerator, load_prompts

# 1. Implement the DocumentRetriever protocol to fetch example documents
#    for data-grounded schema refinement.

class MyRetriever:
    async def __call__(self, query: str, max_docs: int = 100) -> list:
        # Return a list of documents relevant to `query`.
        # Each document can be any object — it is passed as `example_document`
        # to the data assessment prompt.
        return []  # replace with your retrieval logic

# 2. Load prompts for your language/domain.
prompts = load_prompts(language="en", system_type="tax")

llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

schema_system = SchemaGenerator(
    llm=llm,
    retriever=MyRetriever(),
    **{k: v for k, v in prompts.items()},  # unpacks all required prompt args
)

# 3. Run the interactive pipeline.
schema_system.stream_graph_updates("Extract information about tax rulings on cryptocurrency")
```

### Using the built-in Weaviate adapter

If you have a Weaviate index with legal documents, use the built-in retriever:

```python
from schematize.retrieval.weaviate import DocumentType, WeaviateRetriever

retriever = WeaviateRetriever(
    document_type=DocumentType.TAX_INTERPRETATION,
    language="pl",
)
```

Required environment variables:

| Variable     | Description                 |
|--------------|-----------------------------|
| `WV_URL`     | Weaviate host               |
| `WV_PORT`    | Weaviate HTTP port          |
| `WV_GRPC_PORT` | Weaviate gRPC port        |
| `WV_API_KEY` | Weaviate API key            |

## Prompts

Prompts are bundled with the package under `configs/prompt/{language}/{system_type}/`:

| Language | System type | Description              |
|----------|-------------|--------------------------|
| `en`     | `tax`       | English, tax rulings     |
| `en`     | `law`       | English, court judgments |
| `pl`     | `tax`       | Polish, tax rulings      |
| `pl`     | `law`       | Polish, court judgments  |

## Runner scripts (requires `[scripts]` extra)

```bash
# Interactive — prompts for user input
schematize-run

# Mocked — replays a stored case via Hydra
schematize-run-mocked +case=en_age

# Evaluate schemas against expert questions
schematize-evaluate +case_name=age
```

Or run directly from the repo:

```bash
python scripts/schema_generator.py
python scripts/schema_generator_mocked.py +case=en_age
python scripts/evaluate_schema.py +case_name=age
```

## Schema model

```python
from schematize.schema.model import DynamicModelFactory, NamedFieldDef, SchemaFields

spec = SchemaFields(fields=[
    NamedFieldDef(name="amount", type_="float", description="Fine amount in PLN"),
    NamedFieldDef(name="age_category", type_="enum", enum_name="AgeGroup",
                  enum_values=["minor", "young_adult", "adult", "senior"],
                  description="Defendant's age category"),
])

Model = DynamicModelFactory()(spec)
```

## Evaluator

```python
from schematize.eval.evaluator import SchemaEvaluator

evaluator = SchemaEvaluator(llm, evaluation_prompt)
result = evaluator.evaluate_schema(schema_dict, questions=["What is the fine amount?", ...])
print(result.covered_questions, "/", result.total_questions)
```

## Development

```bash
# Install with dev dependencies
uv sync --extra dev

# Lint
make check

# Test
make test

# Fix lint
make fix
```

## Environment

Set API credentials in a `.env` file (auto-loaded by scripts):

```
API_KEY=...
API_URL=...   # optional, for self-hosted endpoints
```
