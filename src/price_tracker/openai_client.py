import os
from openai import OpenAI

MODEL_NAME = os.getenv("OPENAI_MODEL","gpt-4o-mini")

client = OpenAI()

def openaicaller():

    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {"role": "user", "content": "knock knock."},
            {"role": "assistant", "content": "Who's there?"},
            {"role": "user", "content": "Orange."},
        ],
    )

    return response.output_text