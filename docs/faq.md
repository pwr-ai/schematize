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
and raises `NotImplementedError`. To run end-to-end without prompts, skip the interactive stages
with the `skip_*` flags, or use the mocked runners in
[`research/`](https://github.com/pwr-ai/schematize/tree/master/research).

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

If your documents aren't tax or law, the bundled `system_type="general"` (English only) gives you a
domain-neutral prompt set as a starting point instead of overriding every key by hand.

See [Prompts](prompts.md) for the prompt keys, required placeholders, and how to bundle an entirely new
language or `system_type`/domain, or [Configuration](configuration.md) for the bundled combinations.

---

## How do I cite schematize?

If you use schematize in your research, please cite our [EMNLP 2026 System Demonstrations paper](https://aclanthology.org/2026.emnlp-demos.66/):

```bibtex
@inproceedings{sawczyn-etal-2026-schematize,
    title = "Schematize: An Agentic System for Generating and Refining Information-Extraction Schemas for Legal Research",
    author = "Sawczyn, Albert  and
      Binkowski, Jakub  and
      Tagowski, Kamil  and
      Augustyniak, Lukasz  and
      Kaczmarek-Templin, Berenika  and
      Kajdanowicz, Tomasz Jan",
    editor = "Agrawal, Sweta  and
      Abad, Alberto",
    booktitle = "Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = oct,
    year = "2026",
    address = "Budapest, Hungary",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.emnlp-demos.66/",
    doi = "10.18653/2026.emnlp-demos.66",
    pages = "696--705",
    ISBN = "979-8-89176-461-3",
    abstract = "Empirical legal research often relies on turning research questions into structured data extracted from large collections of rulings and judgments. Designing the extraction schema and then extracting the data remain a manual, expertise-heavy bottleneck. We present schematize, an open-source multi-agent system that interactively turns a researcher{'}s problem statement into a validated extraction schema that can later be used for autonomous extraction. Schematize couples (i) a clarification dialogue that elicits implicit expert intent, (ii) iterative schema generation, (iii) data-grounded refinement that tests the schema against documents, and (iv) chat-based post-editing. We evaluated the system with human legal professional, introducing our novel methodology, and schematize achieves top performance in most of tested configurations. While the system is designed to be domain-agnostic and applicable to any document collection, we tailor and evaluate it on legal research problems. We release schematize as a pip-installable Python package with full documentation."
}
```
