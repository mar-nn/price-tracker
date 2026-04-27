import os
from pathlib import Path

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from openai import OpenAI

from price_tracker.product import Product

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

PROMPT_PATH = Path(__file__).parents[2] / "assets" / "prompts" / "price_extraction.txt"


def load_system_prompt() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8")


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

    structured_llm = llm.with_structured_output(Product)

    system_prompt = load_system_prompt()

    messages = [SystemMessage(content=system_prompt), HumanMessage(content=html)]

    result = structured_llm.invoke(messages)

    return result
