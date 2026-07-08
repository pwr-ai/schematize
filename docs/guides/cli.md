# Command-Line Runners

The `[scripts]` extra installs three [Hydra](https://hydra.cc/)-based console scripts for running the
pipeline and evaluator without writing Python.

```bash
pip install "schematize[scripts]"
```

| Command | Description |
|---------|-------------|
| `schematize-run` | Interactive pipeline — prompts for your input at each human-in-the-loop step |
| `schematize-run-mocked` | Replays a stored case file instead of prompting (great for demos and CI) |
| `schematize-evaluate` | Scores generated schemas against expert questions |

```bash
schematize-run
schematize-run-mocked +case=en_age cases_path=data/cases model_name=gpt-4o
schematize-evaluate +case_name=age
```

Or run the scripts directly from a cloned repo:

```bash
python scripts/schema_generator.py
python scripts/schema_generator_mocked.py +case=en_age cases_path=data/cases model_name=gpt-4o
python scripts/evaluate_schema.py +case_name=age
```

All scripts auto-load a `.env` file in the working directory (see [Configuration](../configuration.md)).

---

## Mocked runner cases

The mocked runner replays pre-written answers instead of prompting for live user input — useful for
reproducible demos, regression checks, and CI. A case is a YAML file that can define any combination
of the human-supplied inputs:

```yaml
# my_case.yaml
user_input: "Extract information about personal injury lawsuits"
problem_help: "The schema should capture plaintiff, defendant, compensation, and verdict."
user_feedback: "Add a field for the court name."
human_message: "Can you also add a field for the date of the ruling?"
```

| Key | Description |
|-----|-------------|
| `user_input` | Initial prompt passed to the pipeline |
| `problem_help` | Mocked response during the problem-definition step |
| `user_feedback` | Mocked human feedback during schema refinement |
| `human_message` | Mocked final human message in the interactive chat |

All keys are optional — omit any you want to answer interactively. The filename (without `.yaml`)
becomes the case name used with `+case=<name>`.

Example cases live in [`data/cases/`](https://github.com/pwr-ai/schematize/tree/master/data/cases)
in the repository. Point the runner at that directory — or your own — with `cases_path`:

```bash
# From a cloned repo
schematize-run-mocked +case=en_age cases_path=data/cases model_name=gpt-4o

# After pip install, point at your own cases
schematize-run-mocked +case=my_case cases_path=/path/to/my/cases model_name=gpt-4o
```

---

## Example terminal session

`stream_graph_updates` logs each agent's output as the graph runs, so you can watch the schema take
shape:

```text
👤 Human:
Study personal-rights violations and assess their severity.
--------------------------------------------------
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
