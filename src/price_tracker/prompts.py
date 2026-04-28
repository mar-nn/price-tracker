from pathlib import Path

from langchain_core.messages import SystemMessage

PROMPT_PATH = Path(__file__).parents[2] / "assets" / "prompts" / "price_extraction.txt"


class SystemPrompt(SystemMessage):
    def __init__(self, **kwargs):
        if "content" not in kwargs:
            kwargs["content"] = PROMPT_PATH.read_text(encoding="utf-8")
        super().__init__(**kwargs)
