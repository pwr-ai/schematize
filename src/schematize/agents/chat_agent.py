from typing import Any

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from schematize.agents.agent_state import AgentState
from schematize.agents.output_models import ChatOutput


class InitChatAgent:
    def __init__(self, llm, summarizer_prompt, system_message: str, first_message: str) -> None:
        self.parser = StrOutputParser()
        summarizer_prompt = PromptTemplate.from_template(summarizer_prompt)
        self.system_message = system_message
        self.first_message = first_message
        self.chain = summarizer_prompt | llm

    def __call__(self, state: AgentState) -> dict[str, Any]:
        user_input = state["user_input"]
        problem_help = state["problem_help"]
        user_feedback = state["user_feedback"]
        problem_definition = state["problem_definition"]
        current_schema = state["current_schema"]

        response = self.chain.invoke(
            {
                "user_input": user_input,
                "problem_help": problem_help,
                "user_feedback": user_feedback,
                "problem_definition": problem_definition,
                "current_schema": current_schema,
            }
        )
        generation_summary = self.parser.parse(response.content)
        message = self._format_message(generation_summary, state)
        return {
            "messages": [response],
            "generation_summary": generation_summary,
            "final_messages": [
                SystemMessage(content=self.system_message),
                AIMessage(content=message),
            ],
        }

    def _format_message(self, generation_summary: str, state: AgentState) -> str:
        return self.first_message.format(
            generation_summary=generation_summary,
            current_schema=state["current_schema"],
            user_input=state["user_input"],
            problem_help=state["problem_help"],
            user_feedback=state["user_feedback"],
            problem_definition=state["problem_definition"],
        )


class ChatAgent:
    def __init__(self, llm) -> None:
        self.llm = llm.with_structured_output(ChatOutput, include_raw=True)

    def __call__(self, state: AgentState) -> dict[str, Any]:
        final_messages = state["final_messages"]
        response = self.llm.invoke(final_messages)
        parsed = response["parsed"]
        update_dict = {"messages": [response["raw"]], "final_messages": [response["raw"]]}

        if parsed.is_refined:
            update_dict["current_schema"] = parsed.schema_
            update_dict["schema_history"] = [parsed.schema_]

        if parsed.end_conversation:
            update_dict["end_conversation"] = True

        return update_dict


class HumanMessageAgent:
    def __call__(self, state: AgentState) -> dict[str, Any]:
        message = input("Please provide message: ")
        return {
            "messages": [HumanMessage(content=message)],
            "final_messages": [HumanMessage(content=message)],
        }
