# Configuration

## Environment variables

Scripts and adapters read configuration from environment variables. The recommended way to set them is a `.env` file in your working directory — it is loaded automatically via `python-dotenv`.

### LLM access

schematize talks to your LLM through the **OpenAI-compatible chat completions API** (via
`ChatOpenAI`), so any provider or server implementing that API works — the official OpenAI API,
[LiteLLM](https://github.com/BerriAI/litellm), [vLLM](https://github.com/vllm-project/vllm), Ollama,
and many others. Point `API_URL` at whichever one you're using.

| Variable | Required | Description |
|----------|----------|-------------|
| `API_KEY` | Yes | API key for the LLM provider |
| `API_URL` | No | Base URL for the LLM endpoint. Omit for the provider default (the official OpenAI API). Set for LiteLLM, vLLM, Ollama, or any other OpenAI-compatible endpoint. |

Example `.env`:

```env
API_KEY=sk-...
API_URL=https://api.openai.com/v1
```

For a local Ollama model:

```env
API_KEY=ollama
API_URL=http://localhost:11434/v1
```

For a self-hosted [vLLM](https://github.com/vllm-project/vllm) server:

```env
API_KEY=vllm
API_URL=http://localhost:8000/v1
```

### Using any provider via LiteLLM

Because `API_URL` accepts any OpenAI-compatible endpoint, the recommended way to reach **any** LLM is
to run a [LiteLLM](https://github.com/BerriAI/litellm) proxy and point schematize at it — this is the
setup we used for our experiments. Start the proxy, then:

```env
API_KEY=sk-litellm
API_URL=http://localhost:4000
```

The model name (`model_name` for the CLI, or `model=` for `ChatOpenAI`) is routed by the proxy to the
underlying provider — OpenAI, Anthropic, Gemini, local models, etc. — so you switch providers without
touching schematize.

---

### Weaviate

Required only when using the `[weaviate]` extra.

| Variable | Default | Description |
|----------|---------|-------------|
| `WV_URL` | `localhost` | Weaviate host |
| `WV_PORT` | `8080` | Weaviate HTTP port |
| `WV_GRPC_PORT` | `50051` | Weaviate gRPC port |
| `WV_API_KEY` | _(empty)_ | Weaviate API key |

Example:

```env
WV_URL=weaviate.example.com
WV_PORT=8080
WV_GRPC_PORT=50051
WV_API_KEY=my-weaviate-key
```

---

## Prompts

Bundled prompts are YAML files under `src/schematize/configs/prompt/` and are included as package data. Load them with:

```python
from schematize import load_prompts

prompts = load_prompts(language="en", system_type="law")
```

| `language` | `system_type` | Domain |
|-----------|--------------|--------|
| `"en"` | `"law"` | English legal judgments |
| `"en"` | `"tax"` | English tax interpretations |
| `"en"` | `"general"` | Domain-neutral, for any document corpus |
| `"pl"` | `"law"` | Polish legal judgments |
| `"pl"` | `"tax"` | Polish tax interpretations |

The paper's experiments use the `pl`/`law` combination; the others are additional prompt sets for use
beyond the paper.

`load_prompts` returns a flat dict of named prompt strings. Wrap it in `SchemaGeneratorPrompts` before passing to `SchemaGenerator`:

```python
from schematize import SchemaGenerator, SchemaGeneratorPrompts

generator = SchemaGenerator(llm=llm, retriever=retriever, prompts=SchemaGeneratorPrompts(**prompts))
```

To use custom prompts, replace individual keys in the dict before wrapping:

```python
prompts = load_prompts(language="en", system_type="law")
prompts["schema_generator_prompt"] = "Your custom schema generator prompt..."

generator = SchemaGenerator(llm=llm, retriever=retriever, prompts=SchemaGeneratorPrompts(**prompts))
```

See [Prompts](prompts.md) for the directory convention, required placeholders per prompt, and how to bundle
a new language or `system_type`/domain.

---

## LangChain LLM cache

For development, enable caching to avoid redundant LLM calls:

```python
from schematize.utils.langchain import setup_langchain_llm_cache

setup_langchain_llm_cache()  # uses SQLite by default
```

This calls `langchain.globals.set_llm_cache` with a SQLite-backed cache. It is not enabled by default in the library itself.
