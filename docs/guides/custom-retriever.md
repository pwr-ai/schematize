# Custom Retriever

The core library has no retrieval dependency. `SchemaGenerator` accepts any object that satisfies the `DocumentRetriever` protocol — an async callable with the signature:

```python
async def __call__(self, query: str, max_docs: int = 100) -> list[Any]: ...
```

This means you can connect any document store — Elasticsearch, PostgreSQL full-text search, a local vector DB, a REST API — without modifying the pipeline.

---

## Minimal example

```python
class MyRetriever:
    async def __call__(self, query: str, max_docs: int = 100) -> list[dict]:
        results = await my_search_engine.search(query, limit=max_docs)
        return [{"text": r.text, "id": r.id} for r in results]
```

The return type is `list[Any]`. Each element is passed as-is to the data-assessment agent, which receives it as a string representation. Returning dicts with a `"text"` key is a good convention, but any serialisable structure works.

---

## Using the protocol type

For type-checking, import and annotate with `DocumentRetriever`:

```python
from schematize.retrieval.base import DocumentRetriever

def build_generator(retriever: DocumentRetriever) -> SchemaGenerator:
    ...
```

The protocol is `runtime_checkable`, so `isinstance(obj, DocumentRetriever)` works at runtime.

---

## Wrapping a synchronous retriever

If your search function is synchronous, wrap it with `asyncio.to_thread`:

```python
import asyncio

class SyncRetrieverWrapper:
    def __init__(self, sync_fn):
        self._fn = sync_fn

    async def __call__(self, query: str, max_docs: int = 100) -> list:
        return await asyncio.to_thread(self._fn, query, max_docs)
```

---

## Caching

For development or repeated runs on the same queries, a simple in-memory cache:

```python
from functools import lru_cache

class CachedRetriever:
    def __init__(self, inner):
        self._inner = inner
        self._cache: dict[tuple, list] = {}

    async def __call__(self, query: str, max_docs: int = 100) -> list:
        key = (query, max_docs)
        if key not in self._cache:
            self._cache[key] = await self._inner(query, max_docs)
        return self._cache[key]
```

---

## A worked example: `MMLWRobertaV2Retriever`

`MMLWRobertaV2Retriever` is a good template to read when building your own retriever. It is a custom
retriever specialised for Polish: it builds on the HuggingFace base, swaps in the
`sdadas/mmlw-retrieval-roberta-large-v2` embedding model, loads it in `bfloat16`, and prefixes
queries with `[query]: ` as the model requires — all behind the same `DocumentRetriever` interface.

Use it as a model for specialising retrieval to your own embedding model, language, or corpus. See
its source and usage in the [HuggingFace guide](huggingface.md#mmlwrobertav2retriever).

## Built-in adapters

If you are working with HuggingFace datasets or a Weaviate instance, ready-made adapters are available:

- [HuggingFace adapter](huggingface.md) — `HuggingFaceRetriever` (and `MMLWRobertaV2Retriever`)
- [Weaviate adapter](weaviate.md) — `WeaviateRetriever`
