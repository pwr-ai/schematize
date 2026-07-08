import asyncio
from enum import Enum

import typer

from schematize.retrieval.huggingface import HuggingFaceRetriever, MMLWRobertaV2Retriever

app = typer.Typer()


class RetrieverType(str, Enum):
    huggingface = "huggingface"
    mmlw = "mmlw"


@app.command()
def main(
    dataset: str = typer.Argument(..., help="HuggingFace dataset identifier, e.g. JuDDGES/pl-court-raw"),
    query: str = typer.Argument(..., help="Search query"),
    text_column: str = typer.Option("text", help="Dataset column to embed and return"),
    split: str = typer.Option("train"),
    max_documents: int = typer.Option(None, help="Rows to stream and index (None = no limit)"),
    max_docs: int = typer.Option(5, help="Number of results to return"),
    retriever: RetrieverType = typer.Option(RetrieverType.mmlw, help="Retriever backend to use"),
    device: str = typer.Option(None, help="Device for embedding model (None = auto-detect)"),
    index_path: str = typer.Option(None, help="Directory to save/load the FAISS index"),
) -> None:
    async def run() -> None:
        if retriever == RetrieverType.mmlw:
            r = MMLWRobertaV2Retriever(
                dataset_name=dataset,
                text_column=text_column,
                max_documents=max_documents,
                split=split,
                device=device,
                index_path=index_path,
            )
        else:
            r = HuggingFaceRetriever(
                dataset_name=dataset,
                text_column=text_column,
                max_documents=max_documents,
                split=split,
                device=device,
                index_path=index_path,
            )
        docs = await r(query, max_docs=max_docs)
        for i, doc in enumerate(docs, 1):
            typer.echo(f"\n--- result {i} ---")
            typer.echo(str(doc[text_column]))

    asyncio.run(run())


if __name__ == "__main__":
    app()
