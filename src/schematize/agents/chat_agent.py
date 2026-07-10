from typing import Any

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from loguru import logger

from schematize.agents.agent_state import AgentState, msg_usage
from schematize.agents.output_models import ChatOutput
from schematize.utils.retry import StructuredOutputRunner


class InitChatAgent:
    def __init__(self, llm, summarizer_prompt, system_message: str, first_message: str) -> None:
        self.parser = StrOutputParser()
        self.prompt = PromptTemplate.from_template(summarizer_prompt)
        self.system_message = system_message
        self.first_message = first_message
        self.chain = self.prompt | llm

    def __call__(self, state: AgentState) -> dict[str, Any]:
        inputs = {
            "user_input": state["user_input"],
            "problem_help": state["problem_help"],
            "user_feedback": state["user_feedback"],
            "problem_definition": state["problem_definition"],
            "current_schema": state["current_schema"],
        }
        logger.debug("{} | prompt:\n{}", type(self).__name__, self.prompt.format(**inputs))
        response = self.chain.invoke(inputs)
        generation_summary = self.parser.parse(response.content)
        message = self._format_message(generation_summary, state)
        return {
            "messages": [response],
            "generation_summary": generation_summary,
            "final_messages": [
                SystemMessage(content=self.system_message),
                AIMessage(content=message),
            ],
            "token_usage": [msg_usage(response, type(self).__name__)],
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
    def __init__(self, llm, max_retries: int = 3) -> None:
        self.chain = StructuredOutputRunner(llm, ChatOutput, max_retries=max_retries)

    def __call__(self, state: AgentState) -> dict[str, Any]:
        final_messages = state["final_messages"]
        logger.debug(
            "{} | messages:\n{}",
            type(self).__name__,
            "\n---\n".join(f"[{m.type}] {m.content}" for m in final_messages),
        )
        response = self.chain.invoke(final_messages)
        parsed = response["parsed"]
        update_dict = {"messages": [response["raw"]], "final_messages": [response["raw"]], "token_usage": [msg_usage(response["raw"], type(self).__name__)]}

        if parsed.is_refined:
            update_dict["current_schema"] = parsed.schema_
            update_dict["schema_history"] = [parsed.schema_]

        if parsed.end_conversation:
            update_dict["end_conversation"] = True

        return update_dict


class HumanMessageAgent:
    def __call__(self, state: AgentState) -> dict[str, Any]:
        message = input("🤖 Human (message): ")
        return {
            "messages": [HumanMessage(content=message)],
            "final_messages": [HumanMessage(content=message)],
        }
