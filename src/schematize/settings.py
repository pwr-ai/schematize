from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent

CONFIG_PATH = ROOT_PATH / "configs"
PROMPTS_PATH = CONFIG_PATH / "prompt"

LANGCHAIN_CACHE_FILE = Path.cwd() / ".langchain_cache.db"
