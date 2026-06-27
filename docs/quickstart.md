# Quickstart

This guide walks through a complete end-to-end example: loading an LLM, wiring up a retriever, running the pipeline, and inspecting the resulting schema.

## Prerequisites

```bash
pip install "schematize[huggingface]"
```

Set your LLM API key:

```bash
export API_KEY=sk-...
```

---

## Step 1 — Set up the LLM

`SchemaGenerator` accepts any LangChain `BaseChatModel`. Here we use OpenAI:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", api_key="sk-...")
```

Any LangChain `BaseChatModel` works, so you are not tied to one provider. The simplest way to reach
**any** model is a [LiteLLM](https://github.com/BerriAI/litellm) proxy — the setup we used for our
experiments — pointed at via `base_url`:

```python
from langchain_openai import ChatOpenAI

# The model name routes through the proxy to OpenAI, Anthropic, Gemini, a local model, etc.
llm = ChatOpenAI(
    model="claude-opus-4-8",
    base_url="http://localhost:4000",
    api_key="sk-litellm",
)
```

The same pattern covers any OpenAI-compatible endpoint (Ollama, vLLM, a self-hosted gateway):

```python
llm = ChatOpenAI(model="llama3.1", base_url="http://localhost:11434/v1", api_key="ollama")
```

---

## Step 2 — Set up a retriever

The data-grounded refinement stage needs a document retriever. Use the built-in HuggingFace adapter or [implement your own](guides/custom-retriever.md).

```python
from schematize.retrieval.huggingface import HuggingFaceRetriever

retriever = HuggingFaceRetriever(
    dataset_name="JuDDGES/pl-court-raw",
    text_column="text",
    max_documents=10_000,
    index_path=".cache/court-index",  # cached after first build
)
```

The index is built lazily on first call and saved to `index_path`. Subsequent runs load from disk.

---

## Step 3 — Load prompts

Bundled prompts are available for English and Polish, for tax and law domains:

```python
from schematize import load_prompts

prompts = load_prompts(language="en", system_type="law")
# language: "en" | "pl"
# system_type: "law" | "tax"
```

`load_prompts` returns a flat dict of named prompt strings. Wrap it in `SchemaGeneratorPrompts` before passing to `SchemaGenerator`.

---

## Step 4 — Build the generator

```python
from schematize import SchemaGenerator, SchemaGeneratorPrompts

generator = SchemaGenerator(
    llm=llm,
    retriever=retriever,
    prompts=SchemaGeneratorPrompts(**prompts),
    max_refinement_rounds=3,
    min_refinement_rounds=1,
    max_data_refinement_rounds=2,
    min_data_refinement_rounds=1,
    data_assessment_top_k=20,
    data_assessment_num_examples=3,
)
```

---

## Step 5 — Run the pipeline

```python
state = generator.stream_graph_updates(
    "Study personal-rights violations in civil cases and assess their severity."
)
```

The pipeline will:

1. Ask clarifying questions and wait for your answers (terminal input)
2. Generate a search query
3. Draft and refine the schema against quality criteria
4. Retrieve documents and refine against real data
5. Summarize the process and open a chat for final edits

---

## Step 6 — Inspect the result

```python
schema = state["current_schema"]
print(schema)
# {'fields': [{'name': 'violation_type', 'type_': 'enum', ...}, ...]}
```

Convert the schema to a Pydantic model for use in extraction:

```python
from schematize import SchemaFields, DynamicModelFactory

spec = SchemaFields(**schema)
model_cls = DynamicModelFactory()(spec)
print(model_cls.model_fields)
```

---

## Skipping pipeline stages

For faster iteration you can skip stages that don't apply to your use case:

```python
generator = SchemaGenerator(
    llm=llm,
    retriever=retriever,
    prompts=SchemaGeneratorPrompts(**prompts),
    skip_problem_definition=True,  # no clarification dialogue
    skip_refinement=False,
    skip_data_grounded=True,       # no document retrieval
)
```

When `skip_problem_definition=True`, the user input is used directly as the problem definition.
