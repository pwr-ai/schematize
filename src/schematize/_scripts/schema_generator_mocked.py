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


@hydra.main(version_base=None, config_path=_CONFIG_PATH, config_name="run_mocked")
def main(cfg: DictConfig) -> None:
    
    assert cfg.case.language in ["pl", "en"], "Invalid language"
    assert cfg.case.system_type in ["law", "tax"], "Invalid system type"

    if cfg.llm_cache:
        setup_langchain_llm_cache()

    prompts = load_prompts(cfg.case.language, cfg.case.system_type)
    cases = load_cases(Path(cfg.cases_path))

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
        reasoning_effort=cfg.llm.reasoning_effort,
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
        data_assessment_document_max_chars=sg_cfg.data_assessment_document_max_chars,
        recursion_limit=100,
    )

    if "problem_help" in case_data:
        schema_system.problem_definer_helper = create_mock_problem_helper(case_data["problem_help"])
    if "user_feedback" in case_data:
        schema_system.human_feedback = create_mock_user_feedback(case_data["user_feedback"])
    if "human_message" in case_data:
        schema_system.human_message = create_mock_human_message(case_data["human_message"])

    schema_system.graph = schema_system.build_graph()

    user_input = case_data.get("user_input", "Generate a schema for legal documents")
    final_state = schema_system.stream_graph_updates(user_input)

    output_path = Path(cfg.output) / "state.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w") as f:
        f.write(agent_state_to_json(final_state))
    logger.info("State saved to {}", output_path)

    schema_path = Path(cfg.output) / "schema.json"
    schema_path.write_text(final_state.get("current_schema").model_dump_json(indent=2))
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


def load_cases(cases_path: Path) -> dict[str, dict[str, str]]:
    assert cases_path.exists(), f"Cases directory does not exist: {cases_path}"
    cases = {}
    for case_file in cases_path.glob("*.yaml"):
        with open(case_file, "r") as f:
            cases[case_file.stem] = yaml.safe_load(f)
    return cases


def create_mock_problem_helper(problem_help_text: str):
    def mock_problem_helper(state: AgentState) -> dict[str, Any]:
        response = AIMessage(content=problem_help_text)
        return {"messages": [response], "problem_help": problem_help_text}
    return mock_problem_helper


def create_mock_user_feedback(user_feedback_text: str):
    def mock_user_feedback(state: AgentState) -> dict[str, Any]:
        return {
            "user_feedback": user_feedback_text,
            "messages": [HumanMessage(content=user_feedback_text)],
        }
    return mock_user_feedback


def create_mock_human_message(human_message_text: str):
    def mock_human_message(state: AgentState) -> dict[str, Any]:
        return {
            "messages": [HumanMessage(content=human_message_text)],
            "final_messages": [HumanMessage(content=human_message_text)],
        }
    return mock_human_message

if __name__ == "__main__":
    main()
