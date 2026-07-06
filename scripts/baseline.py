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

from schematize.agents.agent_state import msg_usage
from schematize.schema.model import SchemaFields
from schematize.utils.retry import StructuredOutputRunner

_SCRIPT_DIR = Path(__file__).parent
_DEFAULT_PROMPT = _SCRIPT_DIR / "prompts" / "schema_generator_baseline.yaml"
_DEFAULT_PROMPT_NO_PD = _SCRIPT_DIR / "prompts" / "schema_generator_baseline_no_pd.yaml"
_DEFAULT_CASES = Path("data/cases")
_DEFAULT_OUTPUT = Path("outputs/baseline")
_DEFAULT_OUTPUT_NO_PD = Path("outputs/baseline_no_pd")

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
    no_pd: Annotated[
        bool, typer.Option("--no-pd", help="Generate schema from user_input only, without problem_help/user_feedback")
    ] = False,
    output: Annotated[Optional[Path], typer.Option("--output", help="Output root directory")] = None,
    cases_path: Annotated[Path, typer.Option("--cases-path", help="Directory containing case YAML files")] = _DEFAULT_CASES,
    prompt_path: Annotated[Optional[Path], typer.Option("--prompt", help="Path to baseline prompt YAML")] = None,
    temperature: Annotated[float, typer.Option("--temperature")] = 1,
    max_tokens: Annotated[int, typer.Option("--max-tokens")] = 128000,
    api_key: Annotated[Optional[str], typer.Option("--api-key", envvar="API_KEY")] = None,
    api_url: Annotated[Optional[str], typer.Option("--api-url", envvar="API_URL")] = None,
) -> None:
    prompt_path = prompt_path or (_DEFAULT_PROMPT_NO_PD if no_pd else _DEFAULT_PROMPT)
    output = output or (_DEFAULT_OUTPUT_NO_PD if no_pd else _DEFAULT_OUTPUT)

    case_data = _load_case(cases_path, case)
    prompt_str = _load_prompt(prompt_path)

    llm = ChatOpenAI(
        model=model,
        base_url=api_url or None,
        api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens,
        use_responses_api=False,
        extra_body={"cache": {"no-cache": True}},
    )

    chain = StructuredOutputRunner(
        llm, SchemaFields, PromptTemplate.from_template(prompt_str), max_retries=15
    )

    inputs = {"user_input": case_data.get("user_input", "")}
    if not no_pd:
        inputs["problem_help"] = case_data.get("problem_help", "")
        inputs["user_feedback"] = case_data.get("user_feedback", "")

    logger.info("Running baseline for case={} model={}", case, model)
    response = chain.invoke(inputs)
    parsed: SchemaFields = response["parsed"]

    out_dir = output / model / case
    out_dir.mkdir(parents=True, exist_ok=True)

    schema_dict = parsed.model_dump()

    schema_path = out_dir / "schema.json"
    schema_path.write_text(parsed.model_dump_json(indent=2))
    logger.info("Schema saved to {}", schema_path)

    # Write state.json in the same format the full pipeline produces so that
    # schematize-evaluate can point at this directory directly via state_dir=...
    state_path = out_dir / "state.json"
    state_path.write_text(
        json.dumps(
            {
                "current_schema": schema_dict,
                "schema_history": [schema_dict],
                "token_usage": [msg_usage(response["raw"], "SchemaGeneratorBaseline")],
            },
            indent=2,
        )
    )
    logger.info("State saved to {}", state_path)


if __name__ == "__main__":
    app()
