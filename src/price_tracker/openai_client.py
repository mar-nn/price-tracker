import os
from openai import OpenAI

MODEL_NAME = os.getenv("OPENAI_MODEL","gpt-4o-mini")

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
    client = OpenAI()
        
    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {"role": "system", "content": "give me the price of the product from html"},
            {"role": "user", "content": html,},
        ],
        max_output_tokens=50,
    )

    return response.output_text