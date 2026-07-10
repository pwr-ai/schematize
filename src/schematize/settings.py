from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent

CONFIG_PATH = ROOT_PATH / "configs"
PROMPTS_PATH = CONFIG_PATH / "prompt"

SUPPORTED_LANGUAGES = ("en", "pl")
SUPPORTED_SYSTEM_TYPES = ("tax", "law", "general")

LANGCHAIN_CACHE_FILE = Path.cwd() / ".langchain_cache.db"
