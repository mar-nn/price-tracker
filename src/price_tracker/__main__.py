import os
from openai import OpenAI
from openai_client import openaicaller

MODEL_NAME = os.getenv("OPENAI_MODEL","gpt-4o-mini")

def main():
    result = openaicaller()
    print(result)


if __name__ == "__main__":
    main()