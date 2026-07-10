import logging
import os
import sys
from pathlib import Path
from typing import Annotated, Optional

import typer
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from loguru import logger

from schematize.agents.agent_state import agent_state_to_json
from schematize.agents.schema_generator import (
    VERBOSITY_LEVELS,
    SchemaGenerator,
    SchemaGeneratorPrompts,
)
from schematize.settings import SUPPORTED_LANGUAGES, SUPPORTED_SYSTEM_TYPES
from schematize.utils.load import load_prompts

_SINK_LEVEL = {"minimal": "INFO", "all": "INFO", "debug": "DEBUG"}

logging.getLogger("httpx").setLevel(logging.WARNING)

app = typer.Typer()


@app.command()
def main(
    model: Annotated[str, typer.Option()],
    language: Annotated[str, typer.Option(help="pl or en")] = "en",
    system_type: Annotated[str, typer.Option(help="tax, law, or general")] = "general",
    temperature: Annotated[Optional[float], typer.Option()] = None,
    max_tokens: Annotated[int, typer.Option()] = 32_000,
    reasoning_effort: Annotated[Optional[str], typer.Option(help="Reasoning effort of the LLM")] = None,
    output: Annotated[Path, typer.Option()] = Path("state.json"),
    api_url: Annotated[Optional[str], typer.Option()] = None,
    api_key: Annotated[Optional[str], typer.Option()] = None,
    retriever_type: Annotated[str, typer.Option(help="weaviate | mmlw | huggingface")] = "huggingface",
    dataset: Annotated[Optional[str], typer.Option(help="HuggingFace dataset identifier")] = None,
    text_column: Annotated[str, typer.Option(help="Dataset column to embed and search")] = "text",
    max_documents: Annotated[Optional[int], typer.Option(help="Max rows to index (None = all)")] = None,
    index_path: Annotated[Optional[str], typer.Option(help="Directory to cache the FAISS index")] = None,
    collection_name: Annotated[Optional[str], typer.Option(help="Weaviate collection name")] = None,
    target_vector: Annotated[Optional[str], typer.Option(help="Weaviate named vector")] = None,
    wv_filter: Annotated[Optional[list[str]], typer.Option(help="Weaviate filters as key=value")] = None,
    max_refinement_rounds: Annotated[int, typer.Option()] = 3,
    min_refinement_rounds: Annotated[int, typer.Option()] = 2,
    max_data_refinement_rounds: Annotated[int, typer.Option()] = 4,
    min_data_refinement_rounds: Annotated[int, typer.Option()] = 2,
    data_assessment_top_k: Annotated[int, typer.Option()] = 50,
    data_assessment_num_examples: Annotated[int, typer.Option()] = 1,
    data_assessment_random_seed: Annotated[int, typer.Option()] = 17,
    data_assessment_document_max_chars: Annotated[int, typer.Option()] = 32_000,
    verbosity: Annotated[str, typer.Option(help="minimal | all | debug")] = "minimal",
) -> None:
    load_dotenv(".env")

    if verbosity not in VERBOSITY_LEVELS:
        raise typer.BadParameter(f"verbosity must be one of {VERBOSITY_LEVELS}, got '{verbosity}'")
    logger.remove()
    logger.add(sys.stderr, level=_SINK_LEVEL[verbosity])

    if language not in SUPPORTED_LANGUAGES:
        raise typer.BadParameter(f"language must be one of {SUPPORTED_LANGUAGES}, got '{language}'")
    if system_type not in SUPPORTED_SYSTEM_TYPES:
        raise typer.BadParameter(f"system_type must be one of {SUPPORTED_SYSTEM_TYPES}, got '{system_type}'")

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

    llm = ChatOpenAI(
        model=model,
        base_url=api_url or os.getenv("API_URL"),
        api_key=api_key or os.getenv("API_KEY"),
        temperature=temperature,
        max_tokens=max_tokens,
        use_responses_api=False,
        reasoning_effort=reasoning_effort,
    )

    schema_system = SchemaGenerator(
        llm,
        retriever,
        SchemaGeneratorPrompts(**prompts),
        max_refinement_rounds=max_refinement_rounds,
        min_refinement_rounds=min_refinement_rounds,
        max_data_refinement_rounds=max_data_refinement_rounds,
        min_data_refinement_rounds=min_data_refinement_rounds,
        data_assessment_top_k=data_assessment_top_k,
        data_assessment_num_examples=data_assessment_num_examples,
        data_assessment_random_seed=data_assessment_random_seed,
        data_assessment_document_max_chars=data_assessment_document_max_chars,
        recursion_limit=100,
    )

    typer.echo("👤 Describe the schema to generate:")
    input_text = input()

    final_state = schema_system.stream_graph_updates(input_text, verbosity=verbosity)

    with output.open("w", encoding="utf-8") as f:
        f.write(agent_state_to_json(final_state))

    typer.echo(f"State saved to {output}")


if __name__ == "__main__":
    app()
