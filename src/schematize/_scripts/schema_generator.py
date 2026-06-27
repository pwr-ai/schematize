import os
from pathlib import Path
from typing import Annotated, Optional

import typer
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from schematize.agents.agent_state import agent_state_to_json
from schematize.agents.schema_generator import SchemaGenerator, SchemaGeneratorPrompts
from schematize.utils.load import load_prompts

app = typer.Typer()


@app.command()
def main(
    model: Annotated[str, typer.Option()] = "gpt-4o-mini",
    language: Annotated[str, typer.Option(help="pl or en")] = "en",
    system_type: Annotated[str, typer.Option(help="tax or law")] = "tax",
    temperature: Annotated[float, typer.Option()] = 0.2,
    max_tokens: Annotated[int, typer.Option()] = 32_000,
    output: Annotated[Path, typer.Option()] = Path("state.json"),
    api_url: Annotated[Optional[str], typer.Option()] = None,
    api_key: Annotated[Optional[str], typer.Option()] = None,
    retriever_type: Annotated[str, typer.Option(help="weaviate | mmlw | huggingface")] = "weaviate",
    dataset: Annotated[Optional[str], typer.Option(help="HuggingFace dataset identifier")] = None,
    text_column: Annotated[str, typer.Option(help="Dataset column to embed and search")] = "text",
    max_documents: Annotated[Optional[int], typer.Option(help="Max rows to index (None = all)")] = None,
    index_path: Annotated[Optional[str], typer.Option(help="Directory to cache the FAISS index")] = None,
    collection_name: Annotated[Optional[str], typer.Option(help="Weaviate collection name")] = None,
    target_vector: Annotated[Optional[str], typer.Option(help="Weaviate named vector")] = None,
    wv_filter: Annotated[Optional[list[str]], typer.Option(help="Weaviate filters as key=value")] = None,
) -> None:
    load_dotenv(".env")

    if language not in ("pl", "en"):
        raise typer.BadParameter(f"language must be 'pl' or 'en', got '{language}'")
    if system_type not in ("tax", "law"):
        raise typer.BadParameter(f"system_type must be 'tax' or 'law', got '{system_type}'")

    prompts = load_prompts(language, system_type)

    if retriever_type == "weaviate":
        try:
            from schematize.retrieval.weaviate import WeaviateRetriever
        except ImportError:
            raise typer.Exit("Weaviate retriever requires: pip install schematize[weaviate]")
        if not collection_name:
            raise typer.BadParameter("--collection-name is required for weaviate retriever")
        filters = dict(f.split("=", 1) for f in (wv_filter or []))
        retriever = WeaviateRetriever(
            collection_name=collection_name,
            target_vector=target_vector,
            filters=filters,
        )
    else:
        try:
            from schematize.retrieval.huggingface import (
                HuggingFaceRetriever,
                MMLWRobertaV2Retriever,
            )
        except ImportError:
            raise typer.Exit("HuggingFace retriever requires: pip install schematize[huggingface]")
        if not dataset:
            raise typer.BadParameter("--dataset is required for huggingface/mmlw retriever")
        kwargs = dict(dataset_name=dataset, text_column=text_column, max_documents=max_documents, index_path=index_path)
        retriever = MMLWRobertaV2Retriever(**kwargs) if retriever_type == "mmlw" else HuggingFaceRetriever(**kwargs)

    model_kwargs = {"reasoning_effort": "low"} if model.startswith("o") else {}
    llm = ChatOpenAI(
        model=model,
        base_url=api_url or os.getenv("API_URL"),
        api_key=api_key or os.getenv("API_KEY"),
        temperature=temperature,
        max_tokens=max_tokens,
        use_responses_api=False,
        **model_kwargs,
    )

    schema_system = SchemaGenerator(
        llm,
        retriever,
        SchemaGeneratorPrompts(**prompts),
        recursion_limit=100,
    )

    typer.echo("Describe the schema to generate:")
    input_text = input()

    final_state = schema_system.stream_graph_updates(input_text)

    with output.open("w") as f:
        f.write(agent_state_to_json(final_state))

    typer.echo(f"State saved to {output}")


if __name__ == "__main__":
    app()
