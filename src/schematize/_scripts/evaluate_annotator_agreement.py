import asyncio
import json
import logging
from itertools import permutations
from pathlib import Path
from typing import Any

import hydra
import yaml
from langchain_openai import ChatOpenAI
from omegaconf import DictConfig
from tqdm.asyncio import tqdm as atqdm

from schematize.eval.evaluator import AnnotatorAgreementEvaluator
from schematize.settings import PROMPTS_PATH
from schematize.utils.langchain import setup_langchain_llm_cache

_CONFIG_PATH = str(Path(__file__).parent / "../../../config")


@hydra.main(version_base=None, config_path=_CONFIG_PATH, config_name="evaluate_agreement")
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

    with open(PROMPTS_PATH / "eval" / "annotator_agreement.yaml", encoding="utf-8") as f:
        prompts = yaml.safe_load(f)

    evaluator = AnnotatorAgreementEvaluator(llm, prompts["annotator_agreement_prompt"])

    case_dir = Path(cfg.case_dir)
    if not case_dir.exists():
        raise ValueError(f"Case directory not found at {case_dir}")

    expert_files = sorted(case_dir.glob("expert_*.yaml"))
    assert len(expert_files) >= 2, f"Need at least 2 expert files in {case_dir}"

    results = asyncio.run(_evaluate_all_pairs(evaluator, case_dir, expert_files, cfg))

    output_path = Path(cfg.output) / "agreement.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Annotator agreement results saved to {output_path}")


async def _evaluate_all_pairs(
    evaluator: AnnotatorAgreementEvaluator,
    case_dir: Path,
    expert_files: list[Path],
    cfg: DictConfig,
) -> dict[str, Any]:
    semaphore = asyncio.Semaphore(cfg.get("max_concurrent", 10))

    async def eval_pair(target_file: Path, reference_file: Path) -> dict:
        target_questions = _load_expert_questions(target_file)
        reference_questions = _load_expert_questions(reference_file)
        async with semaphore:
            evaluation = await evaluator.aevaluate_agreement(target_questions, reference_questions)
        return {
            "target": target_file.stem,
            "reference": reference_file.stem,
            "total_questions": evaluation.total_questions,
            "covered_questions": evaluation.covered_questions,
            "high_confidence": evaluation.high_confidence_coverage,
            "medium_confidence": evaluation.medium_confidence_coverage,
            "low_confidence": evaluation.low_confidence_coverage,
        }

    pairs = await atqdm.gather(
        *[eval_pair(target, reference) for target, reference in permutations(expert_files, 2)],
        desc="Expert pairs",
    )

    return {
        "case_dir": str(case_dir),
        "num_experts": len(expert_files),
        "pairs": pairs,
    }


def _load_expert_questions(expert_path: Path) -> list[str]:
    with open(expert_path, encoding="utf-8") as f:
        return yaml.safe_load(f).get("questions", [])


if __name__ == "__main__":
    main()
