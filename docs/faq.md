# FAQ

## Do I need a vector database?

No. The core library has **no retrieval dependency**. Any object with an async
`__call__(query, max_docs)` satisfies the [`DocumentRetriever`](guides/custom-retriever.md) protocol:

```python
class MyRetriever:
    async def __call__(self, query: str, max_docs: int = 100) -> list:
        return [{"text": "..."}]
```

For real corpora, the bundled [HuggingFace](guides/huggingface.md) and [Weaviate](guides/weaviate.md)
adapters are ready to use.

---

## Can I skip stages or run non-interactively?

Skip any stage with the `skip_*` flags:

```python
from schematize import SchemaGenerator, SchemaGeneratorPrompts

generator = SchemaGenerator(
    llm=llm, retriever=retriever, prompts=SchemaGeneratorPrompts(**prompts),
    skip_problem_definition=True,  # use the raw user input as the problem definition
    skip_data_grounded=True,       # no document retrieval
)
```

The human-in-the-loop steps (clarification, final chat) read from the terminal via `input()`.
The `use_interrupt=True` mode for driving these via LangGraph interrupts is **not yet implemented**
and raises `NotImplementedError`. To run end-to-end without prompts, skip the interactive stages or
use the [mocked CLI runner](guides/cli.md).

---

## How do I control cost and latency?

The data-grounded stage dominates cost (it scales with documents × refinement rounds). Tune:

| Parameter | Default | Effect |
|-----------|---------|--------|
| `data_assessment_top_k` | 50 | Documents retrieved per query |
| `data_assessment_num_examples` | 3 | Documents assessed per round |
| `max_data_refinement_rounds` | 3 | Upper bound on data-grounded iterations |
| `max_refinement_rounds` | 3 | Upper bound on criteria-based iterations |

See the [Pipeline](pipeline.md) page for the full stopping rules.

---

## Which model or provider can I use?

Any of them. `SchemaGenerator` takes any LangChain
[`BaseChatModel`](https://python.langchain.com/docs/concepts/chat_models/), and because it honours an
OpenAI-compatible `base_url` you can point it at Ollama, vLLM, or a [LiteLLM](https://github.com/BerriAI/litellm)
proxy in front of another provider. See [Configuration](configuration.md#using-any-provider-via-litellm)
for the setup we use.

---

## How do I use the schema for extraction?

Convert the generated schema dict into a Pydantic model with `DynamicModelFactory`:

```python
from schematize import SchemaFields, DynamicModelFactory

model_cls = DynamicModelFactory()(SchemaFields(**state["current_schema"]))
```

Pass `model_cls` to your extractor (e.g. `llm.with_structured_output(model_cls)`).

---

## Can I use custom prompts or a new domain?

`load_prompts(language, system_type)` returns a flat dict you can edit before passing it on. Override
individual keys, or supply your own strings:

```python
from schematize import SchemaGenerator, SchemaGeneratorPrompts

prompts = load_prompts(language="en", system_type="law")
prompts["schema_generator_prompt"] = "Your custom schema-generation prompt..."

generator = SchemaGenerator(llm=llm, retriever=retriever, prompts=SchemaGeneratorPrompts(**prompts))
```

See [Configuration](configuration.md) for the prompt keys and bundled combinations.
