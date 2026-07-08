"""Optional Weaviate adapter for document retrieval.

Requires: pip install schematize[weaviate]

Environment variables:
    WV_URL       Weaviate host (default: localhost)
    WV_PORT      Weaviate HTTP port (default: 8080)
    WV_GRPC_PORT Weaviate gRPC port (default: 50051)
    WV_API_KEY   Weaviate API key
"""

from __future__ import annotations

import os
from typing import Any, Optional

from loguru import logger

try:
    import weaviate
    from weaviate.classes.init import Auth
    from weaviate.classes.query import Filter, MetadataQuery
except ImportError as _err:
    raise ImportError(
        "The Weaviate adapter requires additional dependencies. "
        "Install them with: pip install schematize[weaviate]"
    ) from _err


class _WeaviateDatabase:
    def __init__(
        self,
        host: str = os.environ.get("WV_URL", "localhost"),
        port: int = int(os.environ.get("WV_PORT", "8080")),
        grpc_port: int = int(os.environ.get("WV_GRPC_PORT", "50051")),
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
            http_port=self.port,
            http_secure=False,
            grpc_host=self.host,
            grpc_port=self.grpc_port,
            grpc_secure=False,
            auth_credentials=Auth.api_key(self._api_key),
        )
        await self.client.connect()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        if self.client and self.client.is_connected():
            await self.client.close()


class WeaviateRetriever:
    """DocumentRetriever backed by a Weaviate hybrid-search index.

    Works with any Weaviate collection. Connection parameters are read from
    environment variables by default but can be overridden.

    Args:
        collection_name: Weaviate collection to query.
        target_vector: Named vector to use for hybrid search. ``None`` uses
            the collection default.
        filters: Property-equality filters applied to every query, e.g.
            ``{"language": "pl", "document_type": "judgment"}``.
        host: Weaviate host (default: ``WV_URL`` env var or ``"localhost"``).
        port: Weaviate HTTP port (default: ``WV_PORT`` env var or ``8080``).
        grpc_port: Weaviate gRPC port (default: ``WV_GRPC_PORT`` env var or ``50051``).
        api_key: Weaviate API key (default: ``WV_API_KEY`` env var).
    """

    def __init__(
        self,
        collection_name: str,
        target_vector: Optional[str] = None,
        filters: Optional[dict[str, str]] = None,
        host: str = os.environ.get("WV_URL", "localhost"),
        port: int = int(os.environ.get("WV_PORT", "8080")),
        grpc_port: int = int(os.environ.get("WV_GRPC_PORT", "50051")),
        api_key: str = os.environ.get("WV_API_KEY", ""),
    ) -> None:
        self.collection_name = collection_name
        self.target_vector = target_vector
        self.filters = filters or {}
        self._db = _WeaviateDatabase(host=host, port=port, grpc_port=grpc_port, api_key=api_key)

    async def __call__(self, query: str, max_docs: int = 100) -> list[dict[str, Any]]:
        logger.info(f"Searching '{self.collection_name}' with query: {query}")
        async with self._db as db:
            collection = db.client.collections.get(self.collection_name)

            filter_parts = [Filter.by_property(k).equal(v) for k, v in self.filters.items()]
            filter_obj = (
                Filter.all_of(filter_parts) if len(filter_parts) > 1
                else filter_parts[0] if filter_parts
                else None
            )

            query_kwargs: dict[str, Any] = dict(
                query=query,
                limit=max_docs,
                return_metadata=MetadataQuery(score=True),
                filters=filter_obj,
            )
            if self.target_vector:
                query_kwargs["target_vector"] = self.target_vector

            response = await collection.query.hybrid(**query_kwargs)
            logger.info(f"Found {len(response.objects)} documents")

            return [
                {
                    **obj.properties,
                    "_score": obj.metadata.score if obj.metadata else None,
                }
                for obj in response.objects
            ]
