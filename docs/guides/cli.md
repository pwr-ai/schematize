# Command-Line Runner

The installed package provides `schematize-run`, an interactive runner for the
pipeline. It prompts for the user input and each human-in-the-loop response.

```bash
schematize-run
```

It auto-loads a `.env` file in the working directory (see
[Configuration](../configuration.md)).

---

## Verbosity

`schematize-run` accepts a `--verbosity` flag controlling how much of the pipeline is logged:

| Value | Behaviour |
|-------|-----------|
| `minimal` (default) | Only the problem-definition helper dialogue and the final conversation are logged; every other step is shown as a progress bar |
| `all` | Every agent's output is logged at INFO level |
| `debug` | Same as `all`, plus DEBUG-level logging (prompts sent to the LLM, token usage) |

```bash
schematize-run --verbosity all
schematize-run --verbosity debug
```

---

## Paper reproduction runners

The mocked runner, evaluator, ablations, and baseline integrations are maintained
under [the research directory](https://github.com/pwr-ai/schematize/tree/master/research) for reproducing the paper. Install
their dependencies from a clone with `uv sync --extra research --extra
huggingface`, then validate them offline with `make research-check`.

## Example terminal session

`stream_graph_updates` logs each agent's output as the graph runs, so you can watch the schema take
shape:

```text
🤖 ProblemDefinerHelperAgent:
A few clarifying questions: which jurisdiction? civil only? ...
--------------------------------------------------
🤖 SchemaGeneratorAgent:
{"fields": [{"name": "violation_type", "type_": "enum", ...}]}
--------------------------------------------------
🤖 SchemaDataAssessmentAgent:
Field `compensation_amount` is often unfillable — many rulings dismiss the claim.
--------------------------------------------------
📊 SchemaDataRefinerAgent | tokens: {...}
--------------------------------------------------
```

See the [Pipeline](../pipeline.md) page for what each stage does.
