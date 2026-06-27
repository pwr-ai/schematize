# schematize

**schematize** turns a natural language research question into a typed, validated extraction schema — ready to drive structured information extraction from document collections.

Instead of hand-crafting a JSON schema, you describe what you want to extract. The pipeline asks clarifying questions, drafts a schema, refines it against quality criteria, tests it against real documents from your corpus, and opens a chat so you can make final adjustments.

---

## Why schematize?

- **Designing extraction schemas by hand is slow and brittle.** You guess the fields, miss edge cases, and only find out when extraction quality is poor.
- **Asking an LLM for a schema once gives you an untested first draft** — no critique loop, no contact with your real data, no typing guarantees.
- **schematize closes the loop:** clarify → draft → criteria-based refinement → data-grounded refinement against retrieved documents → interactive chat. The result is a Pydantic model you can plug straight into extraction.
- **Use any LLM:** works with any LangChain chat model and any OpenAI-compatible endpoint — run it through a [LiteLLM](https://github.com/BerriAI/litellm) proxy (the setup we used) to reach OpenAI, Anthropic, Gemini, or local models through one interface, with no provider lock-in.
- **Bring your own data:** implementing a retriever is a single async method; HuggingFace and Weaviate adapters ship in the box, plus a built-in evaluator that scores how well a schema answers your expert questions.

---

## Key features

- **Five-stage agentic pipeline** — clarification → schema generation → criteria-based refinement → data-grounded refinement → interactive chat
- **Model-agnostic** — any `BaseChatModel`; reach 100+ providers through a LiteLLM proxy, no lock-in
- **Pluggable retrieval** — implement one async method, or use the bundled HuggingFace and Weaviate adapters
- **Typed output** — schemas are Pydantic models with named fields, types, descriptions, and enum support
- **Configurable depth** — control refinement rounds, document sample size, and which pipeline stages to run

---

## Quick look

Any object with an async `__call__(query, max_docs)` is a valid retriever, so you can get a first
schema without standing up a vector store:

```python
from langchain_openai import ChatOpenAI
from schematize import SchemaGenerator, load_prompts


class MyRetriever:
    async def __call__(self, query: str, max_docs: int = 100) -> list:
        return [{"text": "The court awarded 15,000 PLN for breach of personal rights..."}]


llm = ChatOpenAI(model="gpt-4o")
generator = SchemaGenerator(
    llm=llm,
    retriever=MyRetriever(),
    **load_prompts(language="en", system_type="law"),
)

state = generator.stream_graph_updates(
    "Study personal-rights violations and assess their severity."
)
print(state["current_schema"])
```

For real corpora, swap in the bundled [HuggingFace](guides/huggingface.md) or [Weaviate](guides/weaviate.md) adapter.

---

## What you get

A generated schema is a typed spec — field names, types, descriptions, and enums:

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
    ]
}
```

Convert it to a Pydantic model and use it for extraction:

```python
from schematize import SchemaFields, DynamicModelFactory

model_cls = DynamicModelFactory()(SchemaFields(**state["current_schema"]))
```

---

## Next steps

- [Install the library](installation.md)
- [Follow the quickstart](quickstart.md)
- [Understand the pipeline](pipeline.md)
- [Write a custom retriever](guides/custom-retriever.md)
- [Evaluate a schema](guides/evaluation.md)
- [Use the command-line runners](guides/cli.md)
- [Browse the API reference](api/schema_generator.md)
