from __future__ import annotations

import time
from typing import Any

from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import BasePromptTemplate
from langchain_core.runnables import Runnable
from loguru import logger
from openai import AuthenticationError, NotFoundError, OpenAIError, PermissionDeniedError
from pydantic import ValidationError

_RETRYABLE_ERRORS = (OpenAIError, ValidationError)
_NON_RETRYABLE_ERRORS = (AuthenticationError, PermissionDeniedError, NotFoundError)


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
        start = time.perf_counter()
        for attempt in range(self._max_retries + 1):
            try:
                result = self.chain.invoke(inputs)
            except _RETRYABLE_ERRORS as exc:
                if isinstance(exc, _NON_RETRYABLE_ERRORS) or attempt == self._max_retries:
                    raise
                logger.info(
                    "{} | {}: {}; retrying {}/{}",
                    self._name,
                    type(exc).__name__,
                    exc,
                    attempt + 1,
                    self._max_retries,
                )
                continue
            logger.debug("{} | elapsed: {:.2f}s", self._name, time.perf_counter() - start)
            return result

    async def ainvoke(self, inputs: Any) -> Any:
        start = time.perf_counter()
        for attempt in range(self._max_retries + 1):
            try:
                result = await self.chain.ainvoke(inputs)
            except _RETRYABLE_ERRORS as exc:
                if isinstance(exc, _NON_RETRYABLE_ERRORS) or attempt == self._max_retries:
                    raise
                logger.warning(
                    "{} | {}: {}; retrying {}/{}",
                    self._name,
                    type(exc).__name__,
                    exc,
                    attempt + 1,
                    self._max_retries,
                )
                continue
            logger.debug("{} | elapsed: {:.2f}s", self._name, time.perf_counter() - start)
            return result


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
