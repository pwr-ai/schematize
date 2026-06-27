# Evaluation

`SchemaEvaluator` scores a generated schema against a set of questions that the schema should be able to answer. For each question it checks whether the schema contains the fields needed to resolve it, and returns a confidence-weighted coverage summary.

---

## Setup

```python
import yaml
from langchain_openai import ChatOpenAI
from schematize import SchemaEvaluator
from schematize.settings import PROMPTS_PATH

llm = ChatOpenAI(model="gpt-4o")

# Load the bundled evaluation prompt (works after pip install, not just from the repo root).
with open(PROMPTS_PATH / "evaluator.yaml") as f:
    evaluation_prompt = yaml.safe_load(f)["schema_evaluator_prompt"]

evaluator = SchemaEvaluator(llm=llm, evaluation_prompt=evaluation_prompt)
```

You can also pass your own prompt string — it just needs `{questions}` and `{schema}` placeholders.

---

## Running evaluation

### Synchronous

```python
schema = {
    "fields": [
        {"name": "violation_type", "type_": "enum", "enum_values": ["privacy", "reputation"], "description": "..."},
        {"name": "severity", "type_": "integer", "description": "Severity score 0–5"},
    ]
}

questions = [
    "What type of personal right was violated?",
    "How severe was the violation?",
    "Was compensation awarded?",
]

result = evaluator.evaluate_schema(schema=schema, questions=questions)
print(result)
# SchemaEvaluation(total_questions=3, covered_questions=2,
#   high_confidence_coverage=1, medium_confidence_coverage=1, low_confidence_coverage=0)
```

### Asynchronous

```python
result = await evaluator.aevaluate_schema(schema=schema, questions=questions)
```

---

## Per-question detail

To see the verdict for each individual question:

```python
assessments = evaluator.evaluate_all(questions=questions, schema=schema)
for key, assessment in assessments.items():
    print(key, assessment.is_covered, assessment.confidence)
# question_1 True high
# question_2 True medium
# question_3 False high
```

Async variant: `await evaluator.aevaluate_all(questions, schema)`.

---

## Interpreting results

`SchemaEvaluation` has five fields:

| Field | Description |
|-------|-------------|
| `total_questions` | Total number of questions evaluated |
| `covered_questions` | Questions answered by the schema |
| `high_confidence_coverage` | Covered, clearly so |
| `medium_confidence_coverage` | Covered, but partially or with uncertainty |
| `low_confidence_coverage` | Covered, but the judge was unsure |

A question is counted as "covered" regardless of confidence level. The confidence breakdown shows how clearly the schema answers each question.

Coverage rate:

```python
coverage = result.covered_questions / result.total_questions
```

---

## API reference

::: schematize.eval.evaluator.SchemaEvaluator

::: schematize.eval.evaluator.SchemaEvaluation

::: schematize.eval.evaluator.CoverageAssessment
