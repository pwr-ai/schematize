# Agent State

`AgentState` is the shared state dictionary threaded through the LangGraph pipeline. Each node reads from and writes to this dict.

## AgentState fields

| Field | Type | Description |
|-------|------|-------------|
| `messages` | `list` | Full message history (LangGraph `add_messages` reducer) |
| `user_input` | `str` | Original user request |
| `problem_help` | `str \| None` | Clarifying questions from the helper agent |
| `user_feedback` | `str \| None` | User's answers to the clarifying questions |
| `problem_definition` | `str \| None` | Formalised problem definition |
| `query` | `str \| None` | Search query for document retrieval |
| `current_schema` | `dict \| None` | Latest version of the schema |
| `schema_history` | `list` | All previous schema versions (append-only) |
| `refinement_rounds` | `int` | Criteria-based refinement iteration count |
| `assessment_result` | `dict \| None` | Latest criteria-based assessment |
| `data_assessment_results` | `list[str] \| None` | Per-document assessment outputs |
| `merged_data_assessment` | `dict \| None` | Merged data assessment |
| `data_refinement_rounds` | `int` | Data-grounded refinement iteration count |
| `final_messages` | `list` | Messages visible in the chat stage |
| `end_conversation` | `bool \| None` | `True` when the chat agent signals end of session |
| `token_usage` | `list` | Token usage records from each agent node |

## Serialisation

::: schematize.agents.agent_state.agent_state_to_json
