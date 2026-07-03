from __future__ import annotations

from typing import Any

from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import BasePromptTemplate
from langchain_core.runnables import Runnable
from loguru import logger
from openai import OpenAIError


class StructuredOutputRunner:
    """Invokes an (optionally prompted) structured-output chain, retrying the call
    unchanged on any `openai.OpenAIError` (e.g. rate limits, transient API errors,
    or a reasoning model exhausting its `max_tokens` budget before producing any
    output).
    """

    def __init__(
        self,
        llm: BaseChatModel,
        output_model: type,
        prompt: BasePromptTemplate | None = None,
        max_retries: int = 3,
        include_raw: bool = True,
    ) -> None:
        self._output_model = output_model
        self._max_retries = max_retries
        structured_llm = llm.with_structured_output(output_model, include_raw=include_raw)
        self.chain: Runnable = prompt | structured_llm if prompt is not None else structured_llm

    def invoke(self, inputs: Any) -> Any:
        for attempt in range(self._max_retries + 1):
            try:
                return self.chain.invoke(inputs)
            except OpenAIError as exc:
                if attempt == self._max_retries:
                    raise
                logger.info(
                    "{} | {}: {}; retrying {}/{}",
                    self._output_model.__name__,
                    type(exc).__name__,
                    exc,
                    attempt + 1,
                    self._max_retries,
                )

    async def ainvoke(self, inputs: Any) -> Any:
        for attempt in range(self._max_retries + 1):
            try:
                return await self.chain.ainvoke(inputs)
            except OpenAIError as exc:
                if attempt == self._max_retries:
                    raise
                logger.warning(
                    "{} | {}: {}; retrying {}/{}",
                    self._output_model.__name__,
                    type(exc).__name__,
                    exc,
                    attempt + 1,
                    self._max_retries,
                )
