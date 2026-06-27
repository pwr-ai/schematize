import logging
import sys
from pathlib import Path
from typing import Any

import hydra
import yaml
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from loguru import logger
from omegaconf import DictConfig

from schematize.agents.agent_state import AgentState, agent_state_to_json
from schematize.agents.schema_generator import SchemaGenerator, SchemaGeneratorPrompts
from schematize.utils.langchain import setup_langchain_llm_cache
from schematize.utils.load import load_prompts

_CONFIG_PATH = str(Path(__file__).parent / "../../../config")

load_dotenv()

logger.remove()
logger.add(sys.stderr, level="INFO")
logging.getLogger("httpx").setLevel(logging.WARNING)


@hydra.main(version_base=None, config_path=_CONFIG_PATH, config_name="ablation")
def main(cfg: DictConfig) -> None:
    assert cfg.case.language in ["pl", "en"], "Invalid language"
    assert cfg.case.system_type in ["law", "tax"], "Invalid system type"

    if cfg.llm_cache:
        setup_langchain_llm_cache()

    prompts = load_prompts(cfg.case.language, cfg.case.system_type)
    cases = _load_cases(Path(cfg.cases_path))

    case_name = cfg.case.name
    assert case_name in cases, f"Case '{case_name}' not found. Available: {list(cases.keys())}"
    case_data = cases[case_name]

    retriever = _build_retriever(cfg.retriever)

    llm = ChatOpenAI(
        model=cfg.model_name,
        base_url=cfg.api_url,
        api_key=cfg.api_key,
        temperature=cfg.llm.temperature,
        max_tokens=cfg.llm.max_tokens,
        use_responses_api=False,
        **cfg.llm.model_kwargs,
    )

    sg_cfg = cfg.schema_generator
    schema_system = SchemaGenerator(
        llm,
        retriever,
        SchemaGeneratorPrompts(**prompts),
        max_refinement_rounds=sg_cfg.max_refinement_rounds,
        min_refinement_rounds=sg_cfg.min_refinement_rounds,
        max_data_refinement_rounds=sg_cfg.max_data_refinement_rounds,
        min_data_refinement_rounds=sg_cfg.min_data_refinement_rounds,
        data_assessment_top_k=sg_cfg.data_assessment_top_k,
        data_assessment_num_examples=sg_cfg.data_assessment_num_examples,
        data_assessment_random_seed=sg_cfg.data_assessment_random_seed,
        skip_problem_definition=sg_cfg.skip_problem_definition,
        skip_refinement=sg_cfg.skip_refinement,
        skip_data_grounded=sg_cfg.skip_data_grounded,
        recursion_limit=100,
    )

    if not sg_cfg.skip_problem_definition:
        if "problem_help" in case_data:
            schema_system.problem_definer_helper = _mock_problem_helper(case_data["problem_help"])
        if "user_feedback" in case_data:
            schema_system.human_feedback = _mock_user_feedback(case_data["user_feedback"])
    if "human_message" in case_data:
        schema_system.human_message = _mock_human_message(case_data["human_message"])

    schema_system.graph = schema_system.build_graph()

    user_input = case_data.get("user_input", "Generate a schema for legal documents")
    final_state = schema_system.stream_graph_updates(user_input)

    output_path = Path(cfg.output) / "state.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w") as f:
        f.write(agent_state_to_json(final_state))
    logger.info("State saved to {}", output_path)

    schema_path = Path(cfg.output) / "schema.yaml"
    with schema_path.open("w") as f:
        yaml.dump(final_state.get("current_schema"), f, allow_unicode=True, sort_keys=False)
    logger.info("Schema saved to {}", schema_path)


def _build_retriever(r_cfg):
    if r_cfg.type == "weaviate":
        try:
            from schematize.retrieval.weaviate import WeaviateRetriever
        except ImportError:
            raise SystemExit("Weaviate retriever requires: pip install schematize[weaviate]")
        filters = dict(r_cfg.wv_filters) if r_cfg.wv_filters else {}
        return WeaviateRetriever(
            collection_name=r_cfg.collection_name,
            target_vector=r_cfg.target_vector or None,
            filters=filters,
        )
    try:
        from schematize.retrieval.huggingface import HuggingFaceRetriever, MMLWRobertaV2Retriever
    except ImportError:
        raise SystemExit("HuggingFace retriever requires: pip install schematize[huggingface]")
    kwargs = dict(
        dataset_name=r_cfg.dataset_name,
        text_column=r_cfg.text_column,
        split=r_cfg.split,
        max_documents=r_cfg.max_documents,
        index_path=r_cfg.index_path,
    )
    return MMLWRobertaV2Retriever(**kwargs) if r_cfg.type == "mmlw" else HuggingFaceRetriever(**kwargs)


def _load_cases(cases_path: Path) -> dict[str, dict[str, str]]:
    assert cases_path.exists(), f"Cases directory does not exist: {cases_path}"
    return {p.stem: yaml.safe_load(p.read_text()) for p in cases_path.glob("*.yaml")}


def _mock_problem_helper(text: str):
    def _fn(state: AgentState) -> dict[str, Any]:
        return {"messages": [AIMessage(content=text)], "problem_help": text}
    return _fn


def _mock_user_feedback(text: str):
    def _fn(state: AgentState) -> dict[str, Any]:
        return {"user_feedback": text, "messages": [HumanMessage(content=text)]}
    return _fn


def _mock_human_message(text: str):
    def _fn(state: AgentState) -> dict[str, Any]:
        return {
            "messages": [HumanMessage(content=text)],
            "final_messages": [HumanMessage(content=text)],
        }
    return _fn


if __name__ == "__main__":
    main()
