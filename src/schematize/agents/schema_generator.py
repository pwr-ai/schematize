from dataclasses import dataclass
from typing import Any

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage
from langgraph.graph import END, START, StateGraph
from langgraph.types import interrupt
from loguru import logger

from schematize.agents.agent_state import AgentState
from schematize.agents.basic_agents import (
    ProblemDefinerAgent,
    ProblemDefinerHelperAgent,
    SchemaAssessmentAgent,
    SchemaGeneratorAgent,
    SchemaRefinerAgent,
)
from schematize.agents.chat_agent import ChatAgent, HumanMessageAgent, InitChatAgent
from schematize.agents.data_agents import (
    QueryGeneratorAgent,
    SchemaDataAssessmentAgent,
    SchemaDataAssessmentMergerAgent,
    SchemaDataRefinerAgent,
)
from schematize.retrieval.base import DocumentRetriever

@dataclass
class SchemaGeneratorPrompts:
    problem_definer_helper_prompt: str
    problem_definer_prompt: str
    schema_generator_prompt: str
    schema_assessment_prompt: str
    schema_refiner_prompt: str
    query_generator_prompt: str
    schema_data_assessment_prompt: str
    schema_data_assessment_merger_prompt: str
    schema_data_refiner_prompt: str
    init_chat_generation_summarizer_prompt: str
    init_chat_system_message_prompt: str
    init_chat_first_message_prompt: str


_NODE_TO_AGENT = {
    "llm_problem_definer_helper": "ProblemDefinerHelperAgent",
    "llm_problem_definer": "ProblemDefinerAgent",
    "llm_schema_generator": "SchemaGeneratorAgent",
    "llm_first_schema_assessment": "SchemaAssessmentAgent",
    "llm_schema_assessment": "SchemaAssessmentAgent",
    "llm_schema_refiner": "SchemaRefinerAgent",
    "llm_query_generator": "QueryGeneratorAgent",
    "llm_schema_data_assessment": "SchemaDataAssessmentAgent",
    "llm_schema_data_assessment_merger": "SchemaDataAssessmentMergerAgent",
    "llm_schema_data_refiner": "SchemaDataRefinerAgent",
    "summarizer": "InitChatAgent",
    "chat": "ChatAgent",
    "human_message": "Human",
    "user_feedback_node": "Human",
}


class HumanFeedback:
    def __call__(self, state: AgentState) -> dict[str, Any]:
        feedback = input("Please provide feedback: ")
        return {"user_feedback": feedback, "messages": [HumanMessage(content=feedback)]}


class HumanFeedbackWithInterrupt:
    def __call__(self, state: AgentState) -> dict[str, Any]:
        value = interrupt({"user_feedback": state["user_feedback"]})
        return {"user_feedback": value, "messages": [HumanMessage(content=value)]}


class SchemaGenerator:
    """Multi-agent pipeline that turns a natural language problem statement into a typed extraction schema.

    The pipeline runs five stages: problem definition (clarification dialogue + formalisation),
    query generation, criteria-based schema generation and refinement, data-grounded assessment
    and refinement against retrieved documents, and a summarisation + interactive chat phase.
    Any stage can be skipped via the `skip_*` flags.

    Args:
        llm: Language model used by all agents.
        retriever: Document retriever for the data-grounded refinement stage. Any async
            callable matching `(query, max_docs) -> list` works; see
            [`DocumentRetriever`][schematize.retrieval.base.DocumentRetriever].
        prompts: All agent prompt strings; see [`SchemaGeneratorPrompts`][schematize.agents.schema_generator.SchemaGeneratorPrompts].
        max_refinement_rounds: Upper bound on criteria-based refinement iterations. Default: 3.
        min_refinement_rounds: Minimum criteria-based refinement iterations. Default: 2.
        max_data_refinement_rounds: Upper bound on data-grounded refinement iterations. Default: 3.
        min_data_refinement_rounds: Minimum data-grounded refinement iterations. Default: 2.
        data_assessment_top_k: Documents retrieved per query for the assessment pool. Default: 50.
        data_assessment_num_examples: Documents sampled per assessment round. Default: 3.
        data_assessment_random_seed: Seed for reproducible document sampling. Default: 17.
        use_interrupt: Use LangGraph interrupts instead of terminal input for human steps.
            Not yet fully implemented; raises `NotImplementedError` if set. Default: False.
        graph_compilation_kwargs: Extra kwargs forwarded to `StateGraph.compile`.
        recursion_limit: Maximum LangGraph execution depth. Default: 100.
        skip_problem_definition: Skip clarification dialogue; use raw user input as problem
            definition. Default: False.
        skip_refinement: Skip the criteria-based assessment/refinement loop. Default: False.
        skip_data_grounded: Skip data-grounded assessment and refinement. Default: False.
    """

    def __init__(
        self,
        llm: BaseChatModel,
        retriever: DocumentRetriever,
        prompts: SchemaGeneratorPrompts,
        use_interrupt: bool = False,
        graph_compilation_kwargs: dict[str, Any] | None = None,
        recursion_limit: int = 100,
        max_refinement_rounds: int = 3,
        min_refinement_rounds: int = 2,
        max_data_refinement_rounds: int = 3,
        min_data_refinement_rounds: int = 2,
        data_assessment_top_k: int = 50,
        data_assessment_num_examples: int = 3,
        data_assessment_random_seed: int = 17,
        skip_problem_definition: bool = False,
        skip_refinement: bool = False,
        skip_data_grounded: bool = False,
    ) -> None:
        self.recursion_limit = recursion_limit
        self.max_refinement_rounds = max_refinement_rounds
        self.min_refinement_rounds = min_refinement_rounds
        self.max_data_refinement_rounds = max_data_refinement_rounds
        self.min_data_refinement_rounds = min_data_refinement_rounds
        self.skip_problem_definition = skip_problem_definition
        self.skip_refinement = skip_refinement
        self.skip_data_grounded = skip_data_grounded

        self.problem_definer_helper = ProblemDefinerHelperAgent(llm, prompts.problem_definer_helper_prompt)
        self.use_interrupt = use_interrupt
        self.human_feedback = (
            HumanFeedbackWithInterrupt() if use_interrupt else HumanFeedback()
        )
        self.problem_definer = ProblemDefinerAgent(llm, prompts.problem_definer_prompt)

        self.schema_generator = SchemaGeneratorAgent(llm, prompts.schema_generator_prompt)
        self.schema_assessment = SchemaAssessmentAgent(llm, prompts.schema_assessment_prompt)
        self.schema_refiner = SchemaRefinerAgent(llm, prompts.schema_refiner_prompt)

        self.query_generator = QueryGeneratorAgent(llm, prompts.query_generator_prompt)
        self.schema_data_assessment = SchemaDataAssessmentAgent(
            llm,
            prompts.schema_data_assessment_prompt,
            retriever,
            top_k=data_assessment_top_k,
            num_examples=data_assessment_num_examples,
            random_seed=data_assessment_random_seed,
        )
        self.schema_data_assessment_merger = SchemaDataAssessmentMergerAgent(
            llm, prompts.schema_data_assessment_merger_prompt
        )
        self.schema_data_refiner = SchemaDataRefinerAgent(llm, prompts.schema_data_refiner_prompt)
        self.summarizer = InitChatAgent(
            llm,
            prompts.init_chat_generation_summarizer_prompt,
            prompts.init_chat_system_message_prompt,
            prompts.init_chat_first_message_prompt,
        )

        if use_interrupt:
            raise NotImplementedError("Human message with interrupt is not implemented yet!")
        self.human_message = HumanMessageAgent()

        self.chat_agent = ChatAgent(llm)

        self.graph = self.build_graph(compilation_kwargs=graph_compilation_kwargs)

    def build_graph(self, compilation_kwargs: dict[str, Any] | None = None):
        graph_builder = StateGraph(AgentState)

        if self.skip_problem_definition:
            graph_builder.add_edge(START, "llm_query_generator")
        else:
            graph_builder.add_node("llm_problem_definer_helper", self.problem_definer_helper)
            graph_builder.add_node("user_feedback_node", self.human_feedback)
            graph_builder.add_node("llm_problem_definer", self.problem_definer)
            graph_builder.add_edge(START, "llm_problem_definer_helper")
            graph_builder.add_edge("llm_problem_definer_helper", "user_feedback_node")
            graph_builder.add_edge("user_feedback_node", "llm_problem_definer")
            graph_builder.add_edge("llm_problem_definer", "llm_query_generator")

        graph_builder.add_node("llm_query_generator", self.query_generator)
        graph_builder.add_node("llm_schema_generator", self.schema_generator)
        graph_builder.add_node("summarizer", self.summarizer)
        graph_builder.add_node("human_message", self.human_message)
        graph_builder.add_node("chat", self.chat_agent)

        graph_builder.add_edge("llm_query_generator", "llm_schema_generator")

        if self.skip_refinement:
            next_after_schema = "summarizer" if self.skip_data_grounded else "llm_schema_data_assessment"
            graph_builder.add_edge("llm_schema_generator", next_after_schema)
        else:
            graph_builder.add_node("llm_schema_assessment", self.schema_assessment)
            graph_builder.add_node("llm_schema_refiner", self.schema_refiner)
            graph_builder.add_edge("llm_schema_generator", "llm_schema_assessment")
            graph_builder.add_conditional_edges("llm_schema_assessment", self.route_after_assessment)
            graph_builder.add_edge("llm_schema_refiner", "llm_schema_assessment")

        if not self.skip_data_grounded:
            graph_builder.add_node("llm_schema_data_assessment", self.schema_data_assessment)
            graph_builder.add_node(
                "llm_schema_data_assessment_merger", self.schema_data_assessment_merger
            )
            graph_builder.add_node("llm_schema_data_refiner", self.schema_data_refiner)
            graph_builder.add_edge("llm_schema_data_assessment", "llm_schema_data_assessment_merger")
            graph_builder.add_conditional_edges(
                "llm_schema_data_assessment_merger", self.route_after_data_assessment_merger
            )
            graph_builder.add_edge("llm_schema_data_refiner", "llm_schema_data_assessment")

        graph_builder.add_edge("summarizer", "human_message")
        graph_builder.add_edge("human_message", "chat")
        graph_builder.add_conditional_edges("chat", self.route_after_chat)

        return graph_builder.compile(**(compilation_kwargs or {}))

    def stream_graph_updates(self, user_input: str, current_schema: dict = None) -> None:
        if self.use_interrupt:
            raise NotImplementedError(
                "Can't use stream_graph_updates with use_interrupt set!"
            )
        logger.info("👤 Human:\n{}\n{}", user_input, "-" * 50)
        initial_state = AgentState(
            messages=[],
            user_input=user_input,
            problem_help=None,
            user_feedback=None,
            problem_definition=user_input if self.skip_problem_definition else None,
            query=None,
            current_schema=current_schema,
            schema_history=[],
            refinement_rounds=0,
            assessment_result=None,
            data_assessment_results=None,
            merged_data_assessment=None,
            data_refinement_rounds=0,
            token_usage=[],
        )

        final_state = None
        for event_type, data in self.graph.stream(
            initial_state,
            stream_mode=["updates", "values"],
            config={"recursion_limit": self.recursion_limit},
        ):
            if event_type == "updates":
                for node_name, update in data.items():
                    agent = _NODE_TO_AGENT.get(node_name, node_name)
                    for msg in update.get("messages", []):
                        logger.info("🤖 {}:\n{}\n{}", agent, msg.content, "-" * 50)
                    for usage in update.get("token_usage", []):
                        logger.info("📊 {} | tokens: {}", agent, usage)
            else:
                final_state = data

        return final_state

    def get_complete_results(self, user_input: str, current_schema: dict = None) -> dict:
        if self.use_interrupt:
            raise NotImplementedError(
                "Can't use get_complete_results with use_interrupt set!"
            )
        initial_state = AgentState(
            messages=[],
            user_input=user_input,
            problem_help=None,
            user_feedback=None,
            problem_definition=user_input if self.skip_problem_definition else None,
            query=None,
            current_schema=current_schema,
            schema_history=[],
            refinement_rounds=0,
            assessment_result=None,
            merged_data_assessment=None,
            data_refinement_rounds=0,
            final_messages=[],
            token_usage=[],
            cumulative_token_usage=None,
        )
        config = {"recursion_limit": self.recursion_limit} if self.recursion_limit is not None else {}
        result = self.graph.invoke(initial_state, config=config)
        return result

    def route_after_assessment(self, state: AgentState) -> str:
        assessment = state.get("assessment_result", {})
        refinement_rounds = state.get("refinement_rounds", 0)
        needs_refinement = assessment.get("needs_refinement", False)
        max_rounds_reached = refinement_rounds >= self.max_refinement_rounds

        if refinement_rounds < self.min_refinement_rounds:
            return "llm_schema_refiner"
        if needs_refinement and not max_rounds_reached:
            return "llm_schema_refiner"
        return "summarizer" if self.skip_data_grounded else "llm_schema_data_assessment"

    def route_after_data_assessment_merger(self, state: AgentState) -> str:
        assessment = state.get("merged_data_assessment", {})
        needs_refinement = assessment.get("needs_refinement", False)
        data_refinement_rounds = state.get("data_refinement_rounds", 0)
        max_rounds_reached = data_refinement_rounds >= self.max_data_refinement_rounds

        if data_refinement_rounds < self.min_data_refinement_rounds:
            return "llm_schema_data_refiner"
        if needs_refinement and not max_rounds_reached:
            return "llm_schema_data_refiner"
        return "summarizer"

    def route_after_chat(self, state: AgentState) -> str:
        if state.get("end_conversation", False):
            return END
        return "human_message"
