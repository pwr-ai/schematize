# Prompts

Bundled prompts live under `src/schematize/configs/prompt/{language}/{system_type}/` as YAML files and are
loaded with `load_prompts(language, system_type)` (see [Configuration](configuration.md#prompts) for the
bundled combinations and how to override individual prompt strings). This page covers the directory
convention in more detail and how to add a new language or `system_type`/domain.

!!! note
    The paper's experiments use the `pl`/`law` domain (Polish legal judgments); `tax` and `general`
    are additional prompt sets for use beyond the paper.

## Directory convention

```
configs/prompt/
├── en/
│   ├── tax/
│   ├── law/
│   └── general/
└── pl/
    ├── tax/
    └── law/
```

Each `{language}/{system_type}` directory must contain exactly these 10 files, one YAML top-level key per
file:

| File | Key | Consumed by |
|------|-----|--------------|
| `problem_definer_helper.yaml` | `problem_definer_helper_prompt` | `ProblemDefinerHelperAgent` |
| `problem_definer.yaml` | `problem_definer_prompt` | `ProblemDefinerAgent` |
| `schema_generator.yaml` | `schema_generator_prompt` | `SchemaGeneratorAgent` |
| `schema_assessment.yaml` | `schema_assessment_prompt` | `SchemaAssessmentAgent` |
| `schema_refiner.yaml` | `schema_refiner_prompt` | `SchemaRefinerAgent` |
| `query_generator.yaml` | `query_generator_prompt` | `QueryGeneratorAgent` |
| `schema_data_assessment.yaml` | `schema_data_assessment_prompt` | `SchemaDataAssessmentAgent` |
| `schema_data_assessment_merger.yaml` | `schema_data_assessment_merger_prompt` | `SchemaDataAssessmentMergerAgent` |
| `schema_data_refiner.yaml` | `schema_data_refiner_prompt` | `SchemaDataRefinerAgent` |
| `init_chat.yaml` | `init_chat_generation_summarizer_prompt`, `init_chat_system_message_prompt`, `init_chat_first_message_prompt` | `InitChatAgent` |

`load_prompts` reads all 10 files and merges their keys into a single flat dict, which is then unpacked into
`SchemaGeneratorPrompts(**prompts)`.

Every prompt string is a Python `.format()` template. The placeholders each file expects must be preserved
exactly if you add or edit a prompt — the agents fill them in at runtime:

- `{user_input}`, `{problem_help}`, `{user_feedback}` — present in nearly every prompt
- `{problem_definition}` — everything after the problem-definition stage
- `{current_schema}` — schema-assessment, schema-refiner, data-assessment, data-refiner, and init-chat prompts
- `{assessment_result}` — `schema_refiner_prompt` only
- `{example_document}` — `schema_data_assessment_prompt` only
- `{data_assessment_results}` — `schema_data_assessment_merger_prompt` only
- `{merged_data_assessment}` — `schema_data_refiner_prompt` only
- `{generation_summary}` — `init_chat_first_message_prompt` only

## Overriding a prompt value

See [Configuration → Prompts](configuration.md#prompts) — load the bundled dict and replace individual keys
before wrapping in `SchemaGeneratorPrompts`.

## Adding a new language or domain (`system_type`)

To bundle a brand-new domain (e.g. a new subject area) or language:

1. Create `src/schematize/configs/prompt/{language}/{system_type}/` with all 10 files above, matching the
   exact key names and placeholders. The `en/general` domain is a good template if you want a domain-neutral
   starting point rather than the tax/law-specific wording.
2. Add the new `language`/`system_type` value to `SUPPORTED_LANGUAGES` / `SUPPORTED_SYSTEM_TYPES` in
   `src/schematize/settings.py` — this is the single place that gates which values `load_prompts` and the
   CLI/Hydra scripts accept.
3. If you use the Hydra-based runners (`schematize-run-mocked`, ablation script), add a matching
   `config/case/*.yaml` with the new `language`/`system_type`.
4. Add a test in `tests/test_public_api.py` asserting `load_prompts(language, system_type)` returns all
   expected keys, then run `uv run pytest`.
