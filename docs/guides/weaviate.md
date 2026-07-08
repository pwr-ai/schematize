# Weaviate Adapter

The `[weaviate]` extra provides `WeaviateRetriever`, a hybrid-search retriever backed by a Weaviate instance.

```bash
pip install "schematize[weaviate]"
```

---

## Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `WV_URL` | `localhost` | Weaviate host |
| `WV_PORT` | `8080` | Weaviate HTTP port |
| `WV_GRPC_PORT` | `50051` | Weaviate gRPC port |
| `WV_API_KEY` | _(empty)_ | Weaviate API key |

Set these in your `.env` file or shell. The retriever reads them at instantiation time; you can also pass them explicitly (see below).

---

## Basic usage

```python
from schematize.retrieval.weaviate import WeaviateRetriever

retriever = WeaviateRetriever(collection_name="LegalDocuments")
```

This connects using the environment variables above and runs hybrid search against the `LegalDocuments` collection.

---

## Named vector

If your collection uses named vectors, specify which one to search:

```python
retriever = WeaviateRetriever(
    collection_name="LegalDocuments",
    target_vector="text_embedding",
)
```

---

## Property filters

Narrow results by property equality before the vector search:

```python
retriever = WeaviateRetriever(
    collection_name="LegalDocuments",
    filters={"language": "pl", "document_type": "judgment"},
)
```

Multiple filters are combined with `AND`.

---

## Explicit connection parameters

Override environment variables at construction time:

```python
retriever = WeaviateRetriever(
    collection_name="LegalDocuments",
    host="weaviate.internal",
    port=8080,
    grpc_port=50051,
    api_key="my-key",
)
```

---

## Return format

Each document is returned as a dict of collection properties plus a `_score` key from Weaviate's hybrid search metadata:

```python
{
    "text": "...",
    "title": "...",
    "_score": 0.87,
}
```

---

## API reference

::: schematize.retrieval.weaviate.WeaviateRetriever
