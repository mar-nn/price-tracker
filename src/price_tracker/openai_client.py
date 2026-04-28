import os

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from openai import OpenAI

from price_tracker.prompts import SystemPrompt

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


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
    llm = ChatOpenAI(model_name=model_name)
    messages = [SystemPrompt(), HumanMessage(content=html)]
    response = llm.invoke(messages)
    return response.content
