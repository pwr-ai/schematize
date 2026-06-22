from typing import Any

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from loguru import logger

from schematize.agents.agent_state import AgentState
from schematize.agents.output_models import (
    SchemaAssessmentOutput,
    SchemaGenerationOutput,
    SchemaRefinementOutput,
)


class ProblemDefinerHelperAgent:
    def __init__(self, llm, prompt) -> None:
        self.parser = StrOutputParser()
        self.prompt = PromptTemplate.from_template(prompt)
        self.chain = self.prompt | llm

    def __call__(self, state: AgentState) -> dict[str, Any]:
        inputs = {"user_input": state["user_input"]}
        logger.debug("{} | prompt:\n{}", type(self).__name__, self.prompt.format(**inputs))
        response = self.chain.invoke(inputs)
        parsed_response = self.parser.parse(response.content)
        return {"messages": [response], "problem_help": parsed_response}


class ProblemDefinerAgent:
    def __init__(self, llm, prompt) -> None:
        self.parser = StrOutputParser()
        self.prompt = PromptTemplate.from_template(prompt)
        self.chain = self.prompt | llm

    def __call__(self, state: AgentState) -> dict[str, Any]:
        inputs = {
            "user_input": state["user_input"],
            "problem_help": state["problem_help"],
            "user_feedback": state["user_feedback"],
        }
        logger.debug("{} | prompt:\n{}", type(self).__name__, self.prompt.format(**inputs))
        response = self.chain.invoke(inputs)
        parsed_response = self.parser.parse(response.content)
        return {"messages": [response], "problem_definition": parsed_response}


class SchemaGeneratorAgent:
    def __init__(self, llm, prompt) -> None:
        structured_llm = llm.with_structured_output(SchemaGenerationOutput, include_raw=True)
        self.prompt = PromptTemplate.from_template(prompt)
        self.chain = self.prompt | structured_llm

    def __call__(self, state: AgentState) -> dict[str, Any]:
        inputs = {
            "user_input": state["user_input"],
            "problem_help": state["problem_help"],
            "user_feedback": state["user_feedback"],
            "problem_definition": state["problem_definition"],
        }
        logger.debug("{} | prompt:\n{}", type(self).__name__, self.prompt.format(**inputs))
        response = self.chain.invoke(inputs)
        parsed = response["parsed"]
        update_dict = {"messages": [response["raw"]]}
        if parsed.is_generated:
            update_dict["current_schema"] = parsed.schema_.model_dump()
            update_dict["schema_history"] = [parsed.schema_.model_dump()]
        return update_dict


class SchemaAssessmentAgent:
    def __init__(self, llm, prompt) -> None:
        structured_llm = llm.with_structured_output(SchemaAssessmentOutput, include_raw=True)
        self.prompt = PromptTemplate.from_template(prompt)
        self.chain = self.prompt | structured_llm

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
        return {"messages": [response["raw"]], "assessment_result": response["parsed"].model_dump()}


class SchemaRefinerAgent:
    def __init__(self, llm, prompt) -> None:
        structured_llm = llm.with_structured_output(SchemaRefinementOutput, include_raw=True)
        self.prompt = PromptTemplate.from_template(prompt)
        self.chain = self.prompt | structured_llm

    def __call__(self, state: AgentState) -> dict[str, Any]:
        inputs = {
            "user_input": state["user_input"],
            "problem_help": state["problem_help"],
            "user_feedback": state["user_feedback"],
            "problem_definition": state["problem_definition"],
            "current_schema": state["current_schema"],
            "assessment_result": state["assessment_result"],
        }
        logger.debug("{} | prompt:\n{}", type(self).__name__, self.prompt.format(**inputs))
        response = self.chain.invoke(inputs)
        parsed = response["parsed"]
        update_dict = {"messages": [response["raw"]], "refinement_rounds": 1}
        if parsed.is_refined:
            update_dict["current_schema"] = parsed.schema_.model_dump()
            update_dict["schema_history"] = [parsed.schema_.model_dump()]
        return update_dict
