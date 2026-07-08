import asyncio
import json
import logging
from pathlib import Path
from typing import Any

import hydra
import yaml
from langchain_openai import ChatOpenAI
from omegaconf import DictConfig
from tqdm.asyncio import tqdm as atqdm

from schematize.eval.evaluator import SchemaEvaluator
from schematize.settings import PROMPTS_PATH
from schematize.utils.langchain import setup_langchain_llm_cache

_CONFIG_PATH = str(Path(__file__).parent / "../../../config")


@hydra.main(version_base=None, config_path=_CONFIG_PATH, config_name="evaluate")
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
        use_responses_api=False,
        **cfg.llm.model_kwargs,
    )

    with open(PROMPTS_PATH / "eval" / "schema_evaluator.yaml", encoding="utf-8") as f:
        prompts = yaml.safe_load(f)

    evaluator = SchemaEvaluator(llm, prompts["schema_evaluator_prompt"])

    state_paths = _get_state_paths(Path(cfg.state_dir))
    case_dir = Path(cfg.case_dir)

    if not case_dir.exists():
        raise ValueError(f"Case directory not found at {case_dir}")

    expert_files = sorted(case_dir.glob("expert_*.yaml"))
    assert len(expert_files) > 0, f"No expert files found in {case_dir}"

    asyncio.run(_run_all(evaluator, state_paths, case_dir, expert_files, cfg))


async def _run_all(
    evaluator: SchemaEvaluator,
    state_paths: list[Path],
    case_dir: Path,
    expert_files: list[Path],
    cfg: DictConfig,
) -> None:
    semaphore = asyncio.Semaphore(cfg.get("max_concurrent", 10))
    await atqdm.gather(
        *[
            _evaluate_and_save(evaluator, p, case_dir, expert_files, cfg, semaphore)
            for p in state_paths
        ],
        desc="States",
    )


async def _evaluate_and_save(
    evaluator: SchemaEvaluator,
    state_path: Path,
    case_dir: Path,
    expert_files: list[Path],
    cfg: DictConfig,
    semaphore: asyncio.Semaphore,
) -> None:
    state = _load_state(state_path)
    if cfg.final_only:
        schema_history = [state["current_schema"]] if state.get("current_schema") else []
    else:
        schema_history = state.get("schema_history", [])
        if state.get("current_schema"):
            schema_history.append(state["current_schema"])

    results = await _evaluate(evaluator, state_path, case_dir, schema_history, expert_files, semaphore)

    output_path = (
        Path(cfg.output) / state_path.relative_to(cfg.state_dir).parent / "evaluation.json"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Evaluation results saved to {output_path}")


async def _evaluate(
    evaluator: SchemaEvaluator,
    state_path: Path,
    case_dir: Path,
    schema_history: list[dict],
    expert_files: list[Path],
    semaphore: asyncio.Semaphore,
) -> dict[str, Any]:
    schema_results: dict[int, dict] = {
        i: {"schema_index": i, "num_fields": len(schema), "experts": []}
        for i, schema in enumerate(schema_history)
    }

    async def eval_one(schema_idx: int, schema: dict, expert_file: Path) -> tuple:
        questions = _load_expert_questions(expert_file)
        async with semaphore:
            evaluation = await evaluator.aevaluate_schema(schema, questions)
        return schema_idx, expert_file.stem, evaluation

    tasks = [
        eval_one(schema_idx, schema, expert_file)
        for schema_idx, schema in enumerate(schema_history)
        for expert_file in expert_files
    ]

    for coro in asyncio.as_completed(tasks):
        schema_idx, expert_stem, evaluation = await coro
        schema_results[schema_idx]["experts"].append(
            {
                "expert": expert_stem,
                "total_questions": evaluation.total_questions,
                "covered_questions": evaluation.covered_questions,
                "high_confidence": evaluation.high_confidence_coverage,
                "medium_confidence": evaluation.medium_confidence_coverage,
                "low_confidence": evaluation.low_confidence_coverage,
            }
        )

    return {
        "state_path": str(state_path),
        "case_dir": str(case_dir),
        "num_schemas": len(schema_history),
        "num_experts": len(expert_files),
        "evaluations": [schema_results[i] for i in range(len(schema_history))],
    }


def _load_state(state_path: Path) -> dict:
    with open(state_path, encoding="utf-8") as f:
        return json.load(f)


def _load_expert_questions(expert_path: Path) -> list[str]:
    with open(expert_path, encoding="utf-8") as f:
        return yaml.safe_load(f).get("questions", [])


def _get_state_paths(state_dir: Path) -> list[Path]:
    direct = state_dir / "state.json"
    if direct.exists():
        return [direct]
    result = [
        p for p in state_dir.glob("*/state.json")
        if not (p.parent / "evaluation.json").exists()
    ]
    if not result:
        raise ValueError(f"No unevaluated state files found in {state_dir}")
    return result


if __name__ == "__main__":
    main()
