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

def price_extractor():
    client = OpenAI()
    html = ""
        
    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {"role": "system", "content": "give me the price of the product from html"},
            {"role": "user", "content": html,},
        ],
    )

    return response.output_text