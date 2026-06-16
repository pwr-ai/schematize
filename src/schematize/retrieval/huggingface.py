"""Optional HuggingFace + FAISS adapter for document retrieval.

Requires: pip install schematize[huggingface]
"""

from __future__ import annotations

import asyncio
import itertools
import json
from pathlib import Path
from typing import Any

try:
    import numpy as np
    from datasets import Dataset, load_dataset
    from sentence_transformers import SentenceTransformer
except ImportError as _err:
    raise ImportError(
        "The HuggingFace adapter requires additional dependencies. "
        "Install them with: pip install schematize[huggingface]"
    ) from _err


class _BaseHuggingFaceRetriever:
    def __init__(
        self,
        dataset_name: str,
        text_column: str,
        embedding_model: str,
        max_documents: int | None,
        split: str,
        batch_size: int,
        device: str | None,
        index_path: str | Path | None,
    ) -> None:
        self.dataset_name = dataset_name
        self.text_column = text_column
        self.embedding_model = embedding_model
        self.max_documents = max_documents
        self.split = split
        self.batch_size = batch_size
        self.device = device
        self.index_path = Path(index_path) if index_path else None

        self._dataset: Dataset | None = None
        self._model: SentenceTransformer | None = None
        self._lock = asyncio.Lock()

    async def __call__(self, query: str, max_docs: int = 100) -> list[dict[str, Any]]:
        await self._ensure_index()
        return await asyncio.to_thread(self._search, query, max_docs)

    async def build_index(self) -> None:
        """Force (re)build the index and save it if index_path is set."""
        async with self._lock:
            self._dataset = None
            self._model = None
            await asyncio.to_thread(self._build)

    async def _ensure_index(self) -> None:
        async with self._lock:
            if self._dataset is not None:
                return
            if self.index_path and self._index_saved():
                await asyncio.to_thread(self._load)
            else:
                await asyncio.to_thread(self._build)

    def _index_metadata(self) -> dict:
        return {
            "dataset_name": self.dataset_name,
            "text_column": self.text_column,
            "embedding_model": self.embedding_model,
            "split": self.split,
            "max_documents": self.max_documents,
        }

    def _index_saved(self) -> bool:
        p = self.index_path
        if not (p and (p / "dataset").exists() and (p / "embeddings.faiss").exists()):
            return False
        meta = p / "metadata.json"
        return meta.exists() and json.loads(meta.read_text()) == self._index_metadata()

    def _load(self) -> None:
        p = self.index_path
        dataset = Dataset.load_from_disk(str(p / "dataset"))
        dataset.load_faiss_index("embeddings", str(p / "embeddings.faiss"))
        self._model = SentenceTransformer(self.embedding_model, device=self.device)
        self._dataset = dataset

    def _build(self) -> None:
        model = SentenceTransformer(self.embedding_model, device=self.device)
        streamed = load_dataset(self.dataset_name, split=self.split, streaming=True)
        rows = list(itertools.islice(streamed, self.max_documents))
        dataset = Dataset.from_list(rows)

        def _embed(batch: dict[str, list]) -> dict[str, list]:
            texts = [t or "" for t in batch[self.text_column]]
            vecs = model.encode(texts, batch_size=self.batch_size, show_progress_bar=False)
            return {"embeddings": vecs.tolist()}

        dataset = dataset.map(_embed, batched=True, batch_size=self.batch_size)
        dataset.add_faiss_index(column="embeddings")

        if self.index_path:
            self.index_path.mkdir(parents=True, exist_ok=True)
            dataset.save_faiss_index("embeddings", str(self.index_path / "embeddings.faiss"))
            dataset.drop_index("embeddings")
            dataset.save_to_disk(str(self.index_path / "dataset"))
            (self.index_path / "metadata.json").write_text(json.dumps(self._index_metadata()))
            dataset.load_faiss_index("embeddings", str(self.index_path / "embeddings.faiss"))

        self._model = model
        self._dataset = dataset

    def _prepare_query(self, query: str) -> str:
        return query

    def _search(self, query: str, max_docs: int) -> list[dict[str, Any]]:
        assert self._dataset is not None and self._model is not None
        query_vec = self._model.encode(self._prepare_query(query), show_progress_bar=False)
        query_vec = np.array(query_vec, dtype=np.float32)
        _, results = self._dataset.get_nearest_examples("embeddings", query_vec, k=max_docs)
        n = len(next(iter(results.values())))
        return [{k: v[i] for k, v in results.items() if k != "embeddings"} for i in range(n)]


class HuggingFaceRetriever(_BaseHuggingFaceRetriever):
    """DocumentRetriever backed by a HuggingFace dataset + FAISS index.

    Embeddings are computed with a sentence-transformers model. The index is built
    lazily on first use. Pass ``index_path`` to persist the index to disk — subsequent
    instantiations will load it instead of re-embedding.

    Args:
        dataset_name: HuggingFace dataset identifier (e.g. ``"JuDDGES/pl-court-raw"``).
        text_column: Dataset column to embed and return as search target.
        embedding_model: Sentence-transformers model name or path.
        max_documents: Number of rows to stream and index (``None`` = no limit).
        split: Dataset split to load.
        batch_size: Batch size for embedding computation.
        device: Device for sentence-transformers (``None`` = auto-detect).
        index_path: Directory to save/load the FAISS index and dataset arrow files.
    """

    def __init__(
        self,
        dataset_name: str,
        text_column: str,
        embedding_model: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        max_documents: int | None = None,
        split: str = "train",
        batch_size: int = 32,
        device: str | None = None,
        index_path: str | Path | None = None,
    ) -> None:
        super().__init__(
            dataset_name, text_column, embedding_model,
            max_documents, split, batch_size, device, index_path,
        )


class MMLWRobertaRetriever(_BaseHuggingFaceRetriever):
    """DocumentRetriever using sdadas/mmlw-roberta-large for Polish retrieval.

    Backed by a HuggingFace dataset with a FAISS index. Pass ``index_path`` to
    persist the index to disk — subsequent instantiations will load it instead of
    re-embedding.

    Args:
        dataset_name: HuggingFace dataset identifier.
        text_column: Dataset column to embed and return as search target.
        max_documents: Number of rows to stream and index (``None`` = no limit).
        split: Dataset split to load.
        batch_size: Batch size for embedding computation.
        device: Device for sentence-transformers (``None`` = auto-detect).
        index_path: Directory to save/load the FAISS index and dataset arrow files.
    """

    _MODEL_ID = "sdadas/mmlw-roberta-large"
    _QUERY_PREFIX = "zapytanie: "

    def __init__(
        self,
        dataset_name: str,
        text_column: str,
        max_documents: int | None = None,
        split: str = "train",
        batch_size: int = 32,
        device: str | None = None,
        index_path: str | Path | None = None,
    ) -> None:
        super().__init__(
            dataset_name, text_column, self._MODEL_ID,
            max_documents, split, batch_size, device, index_path,
        )

    def _prepare_query(self, query: str) -> str:
        return self._QUERY_PREFIX + query
