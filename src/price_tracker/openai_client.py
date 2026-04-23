import os

from langchain_openai import ChatOpenAI
from openai import OpenAI

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
    llm = ChatOpenAI()

    system_prompt = (
        "You're a helpful assistant that extracts the price of a product "
        "from its given HTML. You should only return the price."
    )

    messages = [("system", system_prompt), ("human", html)]

    response = llm.invoke(messages)

    return response.content
