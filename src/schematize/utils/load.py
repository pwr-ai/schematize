import yaml

from schematize.settings import PROMPTS_PATH


def load_prompts(language: str, system_type: str) -> dict[str, str]:
    assert language in ["pl", "en"], "Invalid language"
    assert system_type in ["law", "tax"], "Invalid system type"
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
        with open(PROMPTS_PATH / language / system_type / f"{name}.yaml", "r") as f:
            prompts.update(yaml.safe_load(f))
    return prompts
