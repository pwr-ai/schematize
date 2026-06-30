import json
import logging
import sys
from pathlib import Path
from typing import Annotated, Optional

import typer
import yaml
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from loguru import logger

from schematize.agents.output_models import SchemaGenerationOutput

_SCRIPT_DIR = Path(__file__).parent
_DEFAULT_PROMPT = _SCRIPT_DIR / "prompts" / "schema_generator_baseline.yaml"
_DEFAULT_CASES = Path("data/cases")
_DEFAULT_OUTPUT = Path("outputs/baseline")

load_dotenv()

logger.remove()
logger.add(sys.stderr, level="INFO")
logging.getLogger("httpx").setLevel(logging.WARNING)

app = typer.Typer(add_completion=False)


def _load_prompt(prompt_path: Path) -> str:
    with prompt_path.open() as f:
        data = yaml.safe_load(f)
    key = next(iter(data))
    return data[key]


def _load_case(cases_path: Path, case_name: str) -> dict:
    case_file = cases_path / f"{case_name}.yaml"
    if not case_file.exists():
        available = [p.stem for p in cases_path.glob("*.yaml")]
        raise typer.BadParameter(f"Case '{case_name}' not found. Available: {available}")
    with case_file.open() as f:
        return yaml.safe_load(f)


@app.command()
def main(
    case: Annotated[str, typer.Option("--case", help="Case name (stem of YAML file in cases-path)")],
    model: Annotated[str, typer.Option("--model", help="LLM model name")],
    output: Annotated[Path, typer.Option("--output", help="Output root directory")] = _DEFAULT_OUTPUT,
    cases_path: Annotated[Path, typer.Option("--cases-path", help="Directory containing case YAML files")] = _DEFAULT_CASES,
    prompt_path: Annotated[Path, typer.Option("--prompt", help="Path to baseline prompt YAML")] = _DEFAULT_PROMPT,
    temperature: Annotated[float, typer.Option("--temperature")] = 0.2,
    max_tokens: Annotated[int, typer.Option("--max-tokens")] = 32000,
    api_key: Annotated[Optional[str], typer.Option("--api-key", envvar="API_KEY")] = None,
    api_url: Annotated[Optional[str], typer.Option("--api-url", envvar="API_URL")] = None,
) -> None:
    case_data = _load_case(cases_path, case)
    prompt_str = _load_prompt(prompt_path)

    llm = ChatOpenAI(
        model=model,
        base_url=api_url or None,
        api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens,
        use_responses_api=False,
    )

    chain = PromptTemplate.from_template(prompt_str) | llm.with_structured_output(
        SchemaGenerationOutput, include_raw=True
    )

    inputs = {
        "user_input": case_data.get("user_input", ""),
        "problem_help": case_data.get("problem_help", ""),
        "user_feedback": case_data.get("user_feedback", ""),
    }

    logger.info("Running baseline for case={} model={}", case, model)
    response = chain.invoke(inputs)
    parsed: SchemaGenerationOutput = response["parsed"]

    if not parsed.is_generated:
        logger.error("Schema generation failed: {}", parsed.error)
        raise typer.Exit(code=1)

    out_dir = output / model / case
    out_dir.mkdir(parents=True, exist_ok=True)

    schema_dict = parsed.schema_.model_dump()

    schema_path = out_dir / "schema.json"
    schema_path.write_text(parsed.schema_.model_dump_json(indent=2))
    logger.info("Schema saved to {}", schema_path)

    # Write state.json in the same format the full pipeline produces so that
    # schematize-evaluate can point at this directory directly via state_dir=...
    state_path = out_dir / "state.json"
    state_path.write_text(
        json.dumps({"current_schema": schema_dict, "schema_history": [schema_dict]}, indent=2)
    )
    logger.info("State saved to {}", state_path)


if __name__ == "__main__":
    app()
