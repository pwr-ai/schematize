import os
from pathlib import Path
from typing import Annotated, Optional

import typer
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from schematize.agents.agent_state import agent_state_to_json
from schematize.agents.schema_generator import SchemaGenerator
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
) -> None:
    load_dotenv(".env")

    if language not in ("pl", "en"):
        raise typer.BadParameter(f"language must be 'pl' or 'en', got '{language}'")
    if system_type not in ("tax", "law"):
        raise typer.BadParameter(f"system_type must be 'tax' or 'law', got '{system_type}'")

    try:
        from schematize.retrieval.weaviate import DocumentType, WeaviateRetriever
    except ImportError:
        raise typer.Exit("This script requires the weaviate extra: pip install schematize[weaviate]")

    document_type = DocumentType.JUDGMENT if system_type == "law" else DocumentType.TAX_INTERPRETATION
    prompts = load_prompts(language, system_type)
    retriever = WeaviateRetriever(document_type=document_type, language=language)

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
        prompts["problem_definer_helper_prompt"],
        prompts["problem_definer_prompt"],
        prompts["schema_generator_prompt"],
        prompts["schema_assessment_prompt"],
        prompts["schema_refiner_prompt"],
        prompts["query_generator_prompt"],
        prompts["schema_data_assessment_prompt"],
        prompts["schema_data_assessment_merger_prompt"],
        prompts["schema_data_refiner_prompt"],
        prompts["init_chat_generation_summarizer_prompt"],
        prompts["init_chat_system_message_prompt"],
        prompts["init_chat_first_message_prompt"],
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
