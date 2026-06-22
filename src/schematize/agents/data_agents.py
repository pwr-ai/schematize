import asyncio
import random
from typing import Any

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from loguru import logger
from pydantic import BaseModel

from schematize.agents.output_models import (
    DataAssessmentMergerOutput,
    SchemaRefinementOutput,
)
from schematize.retrieval.base import DocumentRetriever


class QueryGeneratorAgent:
    class Query(BaseModel):
        query: str

    def __init__(self, llm, prompt) -> None:
        structured_llm = llm.with_structured_output(self.Query, include_raw=True)
        self.prompt = PromptTemplate.from_template(prompt)
        self.chain = self.prompt | structured_llm

    def __call__(self, state: dict[str, Any]) -> dict[str, Any]:
        inputs = {
            "user_input": state["user_input"],
            "problem_help": state["problem_help"],
            "user_feedback": state["user_feedback"],
            "problem_definition": state["problem_definition"],
        }
        logger.debug("{} | prompt:\n{}", type(self).__name__, self.prompt.format(**inputs))
        response = self.chain.invoke(inputs)
        logger.info("{} | query: {}", type(self).__name__, response["parsed"].query)
        return {"messages": [response["raw"]], "query": response["parsed"].query}


class SchemaDataAssessmentAgent:
    def __init__(
        self,
        llm,
        prompt,
        retriever: DocumentRetriever,
        top_k: int = 50,
        num_examples: int = 3,
        random_seed: int = 17,
    ) -> None:
        self.parser = StrOutputParser()
        self.prompt = PromptTemplate.from_template(prompt)
        self.chain = self.prompt | llm
        self.random = random.Random(random_seed)
        self.top_k = top_k
        self.num_examples = num_examples
        self.retriever = retriever

    def __call__(self, state: dict[str, Any]) -> dict[str, Any]:
        responses, data_assessment_results = asyncio.run(
            self._process_documents(
                state["query"],
                state["user_input"],
                state["problem_help"],
                state["user_feedback"],
                state["problem_definition"],
                state["current_schema"],
            )
        )
        return {"messages": responses, "data_assessment_results": data_assessment_results}

    async def _process_documents(
        self,
        query: str,
        user_input: str,
        problem_help: str,
        user_feedback: str,
        problem_definition: str,
        current_schema: str,
    ) -> tuple[list[Any], list[str]]:
        example_documents = await self._get_example_documents(query)
        tasks = []
        for doc in example_documents:
            inputs = {
                "user_input": user_input,
                "problem_help": problem_help,
                "user_feedback": user_feedback,
                "problem_definition": problem_definition,
                "current_schema": current_schema,
                "example_document": doc,
            }
            logger.debug("{} | prompt:\n{}", type(self).__name__, self.prompt.format(**inputs))
            tasks.append(self.chain.ainvoke(inputs))
        responses = await asyncio.gather(*tasks)
        data_assessment_results = [self.parser.parse(r.content) for r in responses]
        return responses, data_assessment_results

    async def _get_example_documents(self, query: str) -> list[Any]:
        documents = await self.retriever(query, max_docs=self.top_k)
        sampled = self.random.sample(documents, min(self.num_examples, len(documents)))
        logger.info(
            "{} | retrieved {} docs, sampled {}: {}",
            type(self).__name__,
            len(documents),
            len(sampled),
            [str(d)[:120] for d in sampled],
        )
        return sampled


class SchemaDataAssessmentMergerAgent:
    def __init__(self, llm, prompt) -> None:
        structured_llm = llm.with_structured_output(DataAssessmentMergerOutput, include_raw=True)
        self.prompt = PromptTemplate.from_template(prompt)
        self.chain = self.prompt | structured_llm

    def __call__(self, state: dict[str, Any]) -> dict[str, Any]:
        data_assessment_results = state["data_assessment_results"]
        data_assessment_results_str = "".join(
            f"### Assessment {i + 1}\n\n{r}\n\n"
            for i, r in enumerate(data_assessment_results)
        )
        inputs = {
            "user_input": state["user_input"],
            "problem_help": state["problem_help"],
            "user_feedback": state["user_feedback"],
            "problem_definition": state["problem_definition"],
            "current_schema": state["current_schema"],
            "data_assessment_results": data_assessment_results_str,
        }
        logger.debug("{} | prompt:\n{}", type(self).__name__, self.prompt.format(**inputs))
        response = self.chain.invoke(inputs)
        return {"messages": [response["raw"]], "merged_data_assessment": response["parsed"].model_dump()}


class SchemaDataRefinerAgent:
    def __init__(self, llm, prompt) -> None:
        structured_llm = llm.with_structured_output(SchemaRefinementOutput, include_raw=True)
        self.prompt = PromptTemplate.from_template(prompt)
        self.chain = self.prompt | structured_llm

    def __call__(self, state: dict[str, Any]) -> dict[str, Any]:
        inputs = {
            "user_input": state["user_input"],
            "problem_help": state["problem_help"],
            "user_feedback": state["user_feedback"],
            "problem_definition": state["problem_definition"],
            "current_schema": state["current_schema"],
            "merged_data_assessment": state["merged_data_assessment"],
        }
        logger.debug("{} | prompt:\n{}", type(self).__name__, self.prompt.format(**inputs))
        response = self.chain.invoke(inputs)
        parsed = response["parsed"]
        update_dict = {"messages": [response["raw"]], "data_refinement_rounds": 1}
        if parsed.is_refined:
            update_dict["current_schema"] = parsed.schema_
            update_dict["schema_history"] = [parsed.schema_]
        return update_dict
