import yaml

from schematize.settings import PROMPTS_PATH, SUPPORTED_LANGUAGES, SUPPORTED_SYSTEM_TYPES


def load_prompts(language: str, system_type: str) -> dict[str, str]:
    if language not in SUPPORTED_LANGUAGES:
        raise ValueError(f"language must be one of {SUPPORTED_LANGUAGES}, got {language!r}")
    if system_type not in SUPPORTED_SYSTEM_TYPES:
        raise ValueError(f"system_type must be one of {SUPPORTED_SYSTEM_TYPES}, got {system_type!r}")
    prompt_names = [
        "problem_definer_helper",
        "problem_definer",
        "schema_refiner",
        "schema_assessment",
        "schema_generator",
        "query_generator",
        "schema_data_assessment",
        "schema_data_assessment_merger",
        "schema_data_refiner",
        "init_chat",
    ]
    prompts = {}
    for name in prompt_names:
        with open(PROMPTS_PATH / language / system_type / f"{name}.yaml", encoding="utf-8") as f:
            prompts.update(yaml.safe_load(f))
    return prompts
