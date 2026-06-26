import json
import operator
from typing import Annotated, Any

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph.message import add_messages
from pydantic import BaseModel
from typing_extensions import TypedDict


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    user_input: str
    problem_help: str | None
    user_feedback: str | None
    problem_definition: str | None
    query: str | None
    current_schema: dict[str, Any] | None
    schema_history: Annotated[list, operator.add]
    refinement_rounds: Annotated[int, operator.add]
    assessment_result: dict[str, Any] | None
    data_assessment_results: list[str] | None
    merged_data_assessment: dict[str, Any] | None
    data_refinement_rounds: Annotated[int, operator.add]
    final_messages: Annotated[list, add_messages]
    end_conversation: bool | None
    token_usage: Annotated[list, operator.add]


def msg_usage(msg, node: str) -> dict:
    usage = getattr(msg, "usage_metadata", None) or {}
    return {"node": node, **usage}


class AgentStateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (AIMessage, HumanMessage, SystemMessage)):
            return {
                "_type": obj.__class__.__name__,
                "content": obj.content,
                "additional_kwargs": obj.additional_kwargs,
                "response_metadata": obj.response_metadata,
                "id": obj.id,
                "usage_metadata": getattr(obj, "usage_metadata", None),
            }
        if isinstance(obj, BaseModel):
            return obj.model_dump()
        return super().default(obj)


def agent_state_to_json(state: AgentState | dict) -> str:
    return json.dumps(state, indent=2, cls=AgentStateEncoder)
