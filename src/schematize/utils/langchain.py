from pathlib import Path

from langchain_community.cache import SQLiteCache
from langchain_core.globals import set_llm_cache

from schematize.settings import LANGCHAIN_CACHE_FILE


def setup_langchain_llm_cache(cache_path: Path = LANGCHAIN_CACHE_FILE) -> None:
    set_llm_cache(SQLiteCache(database_path=str(cache_path)))
