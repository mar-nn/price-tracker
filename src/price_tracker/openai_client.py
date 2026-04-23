import os
from pathlib import Path

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from openai import OpenAI

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

PROMPT_PATH = Path(__file__).parent / "prompts" / "price_extraction.txt"


def load_system_prompt() -> str:
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read()


def openai_caller():
    client = OpenAI()

    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {"role": "user", "content": "knock knock."},
            {"role": "assistant", "content": "Who's there?"},
            {"role": "user", "content": "Orange."},
        ],
    )

    return response.output_text


def price_extractor(html: str, model_name: str):
    llm = ChatOpenAI()

    system_prompt = load_system_prompt()

    messages = [SystemMessage(content=system_prompt), HumanMessage(content=html)]

    response = llm.invoke(messages)

    return response.content
