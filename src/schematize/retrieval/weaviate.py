"""Optional Weaviate adapter for document retrieval.

Requires: pip install schematize[weaviate]

Environment variables:
    WV_URL      Weaviate host (default: localhost)
    WV_PORT     Weaviate HTTP port (default: 8080)
    WV_GRPC_PORT Weaviate gRPC port (default: 50051)
    WV_API_KEY  Weaviate API key
"""

from __future__ import annotations

import json
import os
from typing import Any, Optional

try:
    import weaviate
    from loguru import logger
    from weaviate.classes.init import Auth
    from weaviate.classes.query import Filter, MetadataQuery
except ImportError as _err:
    raise ImportError(
        "The Weaviate adapter requires additional dependencies. "
        "Install them with: pip install schematize[weaviate]"
    ) from _err


class _VectorName:
    BASE = "base"
    DEV = "dev"
    FAST = "fast"


class _WeaviateDatabase:
    def __init__(
        self,
        host: str = os.environ.get("WV_URL", "localhost"),
        port: str = os.environ.get("WV_PORT", "8080"),
        grpc_port: str = os.environ.get("WV_GRPC_PORT", "50051"),
        api_key: str = os.environ.get("WV_API_KEY", ""),
    ):
        self.host = host
        self.port = port
        self.grpc_port = grpc_port
        self._api_key = api_key
        self.client: weaviate.WeaviateAsyncClient

    async def __aenter__(self) -> "_WeaviateDatabase":
        self.client = weaviate.use_async_with_custom(
            http_host=self.host,
            http_port=int(self.port),
            http_secure=False,
            grpc_host=self.host,
            grpc_port=int(self.grpc_port),
            grpc_secure=False,
            auth_credentials=Auth.api_key(self._api_key),
        )
        await self.client.connect()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        if self.client and self.client.is_connected():
            await self.client.close()


class _WeaviateLegalDatabase(_WeaviateDatabase):
    LEGAL_DOCUMENTS_COLLECTION = "LegalDocuments"
    DOCUMENT_CHUNKS_COLLECTION = "DocumentChunks"

    @property
    def legal_documents_collection(self):
        return self.client.collections.get(self.LEGAL_DOCUMENTS_COLLECTION)


def _get_list(prop):
    if isinstance(prop, list):
        return prop
    if isinstance(prop, str):
        try:
            val = json.loads(prop)
            if isinstance(val, list):
                return val
        except Exception:
            pass
    return []


def _get_str(prop):
    if prop is None:
        return ""
    if isinstance(prop, str):
        return prop
    return json.dumps(prop, ensure_ascii=False)


def _parse_metadata(obj):
    metadata: dict[str, Any] = {}
    if hasattr(obj, "metadata") and hasattr(obj.metadata, "score"):
        metadata["score"] = obj.metadata.score
    metadata_prop = obj.properties.get("metadata")
    if isinstance(metadata_prop, str):
        try:
            parsed = json.loads(metadata_prop)
            if isinstance(parsed, dict):
                metadata.update(parsed)
        except (json.JSONDecodeError, TypeError):
            pass
    elif isinstance(metadata_prop, dict):
        metadata.update(metadata_prop)
    return metadata


async def _search_documents(
    query: str,
    max_docs: int = 100,
    document_type: Optional[str] = None,
    language: Optional[str] = None,
) -> list[dict[str, Any]]:
    logger.info(f"Searching documents with query: {query}")
    async with _WeaviateLegalDatabase() as db:
        filters = []
        if document_type:
            filters.append(Filter.by_property("document_type").equal(document_type))
        if language:
            filters.append(Filter.by_property("language").equal(language.lower()))
        filter_obj = Filter.all_of(filters) if filters else None

        response = await db.legal_documents_collection.query.hybrid(
            query=query,
            target_vector=_VectorName.BASE,
            limit=max_docs,
            return_metadata=MetadataQuery(score=True),
            filters=filter_obj,
        )
        logger.info(f"Found {len(response.objects)} matching documents")

        return [
            {
                "document_id": obj.properties.get("document_id", ""),
                "document_type": obj.properties.get("document_type", ""),
                "title": obj.properties.get("title", ""),
                "language": obj.properties.get("language", ""),
                "full_text": obj.properties.get("full_text", ""),
                "summary": obj.properties.get("summary", ""),
                "keywords": _get_list(obj.properties.get("keywords", [])),
                "metadata": _parse_metadata(obj),
            }
            for obj in response.objects
        ]


class WeaviateRetriever:
    """DocumentRetriever backed by a Weaviate hybrid-search index.

    Requires ``pip install schematize[weaviate]`` and the following environment
    variables to be set:

    - ``WV_URL`` — Weaviate host
    - ``WV_PORT`` — Weaviate HTTP port
    - ``WV_GRPC_PORT`` — Weaviate gRPC port
    - ``WV_API_KEY`` — Weaviate API key

    Args:
        document_type: Optional document type filter string
                       (e.g. ``"tax_interpretation"``, ``"judgment"``).
        language: Optional ISO 639-1 language filter (e.g. ``"pl"``, ``"en"``).
    """

    def __init__(
        self,
        document_type: Optional[str] = None,
        language: Optional[str] = None,
    ) -> None:
        self.document_type = document_type
        self.language = language

    async def __call__(self, query: str, max_docs: int = 100) -> list[dict[str, Any]]:
        return await _search_documents(
            query=query,
            max_docs=max_docs,
            document_type=self.document_type,
            language=self.language,
        )


class DocumentType:
    """String constants for legal document types used with WeaviateRetriever."""

    JUDGMENT = "judgment"
    TAX_INTERPRETATION = "tax_interpretation"
    LEGAL_ACT = "legal_act"
