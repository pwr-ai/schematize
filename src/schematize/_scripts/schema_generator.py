import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from schematize.agents.agent_state import agent_state_to_json
from schematize.agents.schema_generator import SchemaGenerator
from schematize.utils.load import load_prompts

MODEL_NAME = "gpt-4o-mini"
LANGUAGE = "pl"
SYSTEM_TYPE = "tax"
TEMPERATURE = 0.2
MAX_TOKENS = 32_000
MODELS_KWARGS: dict = {"reasoning_effort": "low"} if MODEL_NAME.startswith("o") else {}

OUTPUT_PATH = "state.json"


def main() -> None:
    load_dotenv(".env")

    assert LANGUAGE in ["pl", "en"], "Invalid language"
    assert SYSTEM_TYPE in ["law", "tax"], "Invalid system type"

    try:
        from schematize.retrieval.weaviate import DocumentType, WeaviateRetriever
    except ImportError:
        raise SystemExit(
            "This script requires the weaviate extra: pip install schematize[weaviate]"
        )

    document_type = (
        DocumentType.JUDGMENT if SYSTEM_TYPE == "law" else DocumentType.TAX_INTERPRETATION
    )

    prompts = load_prompts(LANGUAGE, SYSTEM_TYPE)
    retriever = WeaviateRetriever(document_type=document_type, language=LANGUAGE)

    llm = ChatOpenAI(
        model=MODEL_NAME,
        base_url=os.getenv("API_URL"),
        api_key=os.getenv("API_KEY"),
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        use_responses_api=False,
        **MODELS_KWARGS,
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

    print("Input text with description of the schema to generate:")
    input_text = input()

    final_state = schema_system.stream_graph_updates(input_text)

    output_path = Path(OUTPUT_PATH)
    with output_path.open("w") as f:
        f.write(agent_state_to_json(final_state))

    print(f"State saved to {output_path}")


if __name__ == "__main__":
    main()
