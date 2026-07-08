from __future__ import annotations

from typing import Any

from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import BasePromptTemplate
from langchain_core.runnables import Runnable
from loguru import logger
from openai import OpenAIError
from pydantic import ValidationError

_RETRYABLE_ERRORS = (OpenAIError, ValidationError)


class RetryingChain:
    """Wraps an arbitrary `Runnable`, retrying `invoke`/`ainvoke` unchanged on any
    `openai.OpenAIError` (e.g. rate limits, transient API errors, or a reasoning
    model exhausting its `max_tokens` budget before producing any output) or
    `pydantic.ValidationError` (e.g. the model emitting malformed JSON that fails
    structured-output parsing).
    """

    def __init__(self, chain: Runnable, max_retries: int = 3, name: str = "") -> None:
        self.chain = chain
        self._max_retries = max_retries
        self._name = name

    def invoke(self, inputs: Any) -> Any:
        for attempt in range(self._max_retries + 1):
            try:
                return self.chain.invoke(inputs)
            except _RETRYABLE_ERRORS as exc:
                if attempt == self._max_retries:
                    raise
                logger.info(
                    "{} | {}: {}; retrying {}/{}",
                    self._name,
                    type(exc).__name__,
                    exc,
                    attempt + 1,
                    self._max_retries,
                )

    async def ainvoke(self, inputs: Any) -> Any:
        for attempt in range(self._max_retries + 1):
            try:
                return await self.chain.ainvoke(inputs)
            except _RETRYABLE_ERRORS as exc:
                if attempt == self._max_retries:
                    raise
                logger.warning(
                    "{} | {}: {}; retrying {}/{}",
                    self._name,
                    type(exc).__name__,
                    exc,
                    attempt + 1,
                    self._max_retries,
                )


class StructuredOutputRunner(RetryingChain):
    """`RetryingChain` specialised for structured-output chains."""

    def __init__(
        self,
        llm: BaseChatModel,
        output_model: type,
        prompt: BasePromptTemplate | None = None,
        max_retries: int = 3,
        include_raw: bool = True,
    ) -> None:
        self._output_model = output_model
        structured_llm = llm.with_structured_output(output_model, include_raw=include_raw)
        chain: Runnable = prompt | structured_llm if prompt is not None else structured_llm
        super().__init__(chain, max_retries, name=output_model.__name__)
