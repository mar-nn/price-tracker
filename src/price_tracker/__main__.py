import argparse
import requests
import os
from openai import OpenAI
from openai_client import openai_caller, price_extractor

MODEL_NAME = os.getenv("OPENAI_MODEL","gpt-4o-mini")

def main():
    #result = openai_caller()
    result = price_extractor()
    print(result)


if __name__ == "__main__":
    main()