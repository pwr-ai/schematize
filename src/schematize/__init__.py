"""schematize — agentic extraction-schema generation."""

__version__ = "0.1.0"

from schematize.agents.agent_state import AgentState, agent_state_to_json
from schematize.agents.schema_generator import SchemaGenerator
from schematize.eval.evaluator import SchemaEvaluator
from schematize.retrieval.base import DocumentRetriever
from schematize.schema.model import (
    DynamicModelFactory,
    FieldDef,
    FieldType,
    NamedFieldDef,
    SchemaFields,
)
from schematize.utils.load import load_prompts

__all__ = [
    "__version__",
    "SchemaGenerator",
    "SchemaEvaluator",
    "DocumentRetriever",
    "SchemaFields",
    "FieldDef",
    "NamedFieldDef",
    "FieldType",
    "DynamicModelFactory",
    "AgentState",
    "agent_state_to_json",
    "load_prompts",
]
