import os
from pathlib import Path

from langchain_core.messages import SystemMessage
from pydantic import Field, field_validator

PROMPT_PATH = Path(
    os.getenv("SYSTEM_PROMPT_PATH", "assets/prompts/price_extraction.txt")
)


class SystemPrompt(SystemMessage):
    content: str = Field(
        default_factory=lambda: PROMPT_PATH.read_text(encoding="utf-8"),
        frozen=True,
    )

    @field_validator("content", mode="before")
    @classmethod
    def set_default_content(cls, v):
        if v is None:
            return PROMPT_PATH.read_text(encoding="utf-8")
        return v
