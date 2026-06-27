# HuggingFace Adapter

The `[huggingface]` extra provides two FAISS-indexed retrievers backed by HuggingFace datasets.

```bash
pip install "schematize[huggingface]"
```

Both retrievers:

- Load a HuggingFace dataset and embed it with a sentence-transformers model
- Build a FAISS index lazily on first call
- Cache the index to disk — subsequent instantiations load from cache instead of re-embedding

---

## HuggingFaceRetriever

General-purpose retriever. You choose the dataset, the text column, and the embedding model.

```python
from schematize.retrieval.huggingface import HuggingFaceRetriever

retriever = HuggingFaceRetriever(
    dataset_name="JuDDGES/pl-court-raw",
    text_column="text",
    embedding_model="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    max_documents=50_000,          # None = entire dataset
    split="train",
    batch_size=256,
    device=None,                   # None = auto-detect (GPU if available)
    index_path=".cache/my-index",  # omit to disable disk caching
)
```

### Index caching

The first call builds and embeds the dataset (can take a while for large datasets). With `index_path` set, the FAISS index and dataset arrow files are saved to disk. Subsequent instantiations detect the cache, validate metadata (dataset name, column, model, split, max_documents), and load from disk if all match.

To force a rebuild:

```python
import asyncio
asyncio.run(retriever.build_index())
```

### Rebuilding with different settings

Change any constructor parameter and the metadata check will detect the mismatch — the cache is ignored and the index is rebuilt.

---

## MMLWRobertaV2Retriever

A Polish-optimised retriever that doubles as a **worked example of a custom retriever** — it
specialises the HuggingFace base for a specific model and language, which makes it a useful template
for building your own (see the [custom retriever guide](custom-retriever.md#a-worked-example-mmlwrobertav2retriever)).

It uses `sdadas/mmlw-retrieval-roberta-large-v2`, a model fine-tuned for retrieval on Polish benchmarks (NDCG@10 of 60.71 on PIRB). Queries are automatically prefixed with `[query]: ` as required by the model.

```python
from schematize.retrieval.huggingface import MMLWRobertaV2Retriever

retriever = MMLWRobertaV2Retriever(
    dataset_name="JuDDGES/pl-court-raw",
    text_column="text",
    max_documents=50_000,
    index_path=".cache/mmlw-index",
)
```

The model is loaded in `bfloat16` by default (as recommended by the model authors). Override with `model_kwargs`:

```python
retriever = MMLWRobertaV2Retriever(
    dataset_name="JuDDGES/pl-court-raw",
    text_column="text",
    model_kwargs={"model_kwargs": {"torch_dtype": "float32"}},
)
```

---

## Choosing the right retriever

| | `HuggingFaceRetriever` | `MMLWRobertaV2Retriever` |
|---|---|---|
| Language | Any | Polish (optimised) |
| Model | Your choice | `sdadas/mmlw-retrieval-roberta-large-v2` |
| Memory | Depends on model | ~1.3 GB (bfloat16) |
| Query prefix | None | `[query]: ` (automatic) |

---

## API reference

::: schematize.retrieval.huggingface.HuggingFaceRetriever

::: schematize.retrieval.huggingface.MMLWRobertaV2Retriever
