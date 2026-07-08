from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class DocumentRetriever(Protocol):
    """Protocol for document retrievers used in schema data assessment.

    Implementors fetch a list of documents (any type) for a given query.
    The schema data assessment agent calls this to sample example documents
    that are used to evaluate whether the generated schema fits real-world data.
    """

    async def __call__(self, query: str, max_docs: int = 100) -> list[Any]: ...
