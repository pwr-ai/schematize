import json
import logging
from pathlib import Path
from typing import Any

import hydra
import yaml
from langchain_openai import ChatOpenAI
from omegaconf import DictConfig
from tqdm import tqdm

from schematize.eval.evaluator import SchemaEvaluator
from schematize.settings import PROMPTS_PATH
from schematize.utils.langchain import setup_langchain_llm_cache


@hydra.main(version_base=None, config_path="../../../config", config_name="evaluate")
def main(cfg: DictConfig) -> None:
    logging.getLogger("httpx").setLevel(logging.WARNING)

    if cfg.llm_cache:
        setup_langchain_llm_cache()

    llm = ChatOpenAI(
        model=cfg.model_name,
        base_url=cfg.api_url,
        api_key=cfg.api_key,
        temperature=cfg.llm.temperature,
        max_tokens=cfg.llm.max_tokens,
        extra_body={
            "chat_template_kwargs": {"enable_thinking": cfg.llm.enable_thinking},
        },
    )

    with open(PROMPTS_PATH / "evaluator.yaml", "r") as f:
        prompts = yaml.safe_load(f)

    evaluator = SchemaEvaluator(llm, prompts["schema_evaluator_prompt"])

    state_paths = _get_state_paths(Path(cfg.state_dir))
    case_dir = Path(cfg.case_dir)

    if not case_dir.exists():
        raise ValueError(f"Case directory not found at {case_dir}")

    expert_files = sorted(case_dir.glob("expert_*.yaml"))
    assert len(expert_files) > 0, f"No expert files found in {case_dir}"

    for state_path in tqdm(state_paths):
        state = _load_state(state_path)
        schema_history = state.get("schema_history", [])
        if state.get("current_schema"):
            schema_history.append(state["current_schema"])

        results = _evaluate(evaluator, state_path, case_dir, schema_history, expert_files)

        output_path = (
            Path(cfg.output) / state_path.relative_to(cfg.state_dir).parent / "evaluation.json"
        )
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(results, f, indent=2)


def _load_state(state_path: Path) -> dict:
    with open(state_path, "r") as f:
        return json.load(f)


def _load_expert_questions(expert_path: Path) -> list[str]:
    with open(expert_path, "r") as f:
        return yaml.safe_load(f).get("questions", [])


def _get_state_paths(state_dir: Path) -> list[Path]:
    result = [
        p for p in state_dir.glob("*/state.json")
        if not (p.parent / "evaluation.json").exists()
    ]
    if not result:
        raise ValueError(f"No unevaluated state files found in {state_dir}")
    return result


def _evaluate(
    evaluator: SchemaEvaluator,
    state_path: Path,
    case_dir: Path,
    schema_history: list[dict],
    expert_files: list[Path],
) -> dict[str, Any]:
    results: dict[str, Any] = {
        "state_path": str(state_path),
        "case_dir": str(case_dir),
        "num_schemas": len(schema_history),
        "num_experts": len(expert_files),
        "evaluations": [],
    }

    for schema_idx, schema in tqdm(
        enumerate(schema_history), desc="Evaluating schemas", total=len(schema_history)
    ):
        schema_results: dict[str, Any] = {
            "schema_index": schema_idx,
            "num_fields": len(schema),
            "experts": [],
        }
        for expert_file in expert_files:
            questions = _load_expert_questions(expert_file)
            evaluation = evaluator.evaluate_schema(schema, questions)
            schema_results["experts"].append(
                {
                    "expert": expert_file.stem,
                    "total_questions": evaluation.total_questions,
                    "covered_questions": evaluation.covered_questions,
                    "high_confidence": evaluation.high_confidence_coverage,
                    "medium_confidence": evaluation.medium_confidence_coverage,
                    "low_confidence": evaluation.low_confidence_coverage,
                }
            )
        results["evaluations"].append(schema_results)

    return results


if __name__ == "__main__":
    main()
