import argparse
import requests
import os

from openai import OpenAI
from price_tracker.openai_client import price_extractor

MODEL_NAME = os.getenv("OPENAI_MODEL","gpt-4o-mini")

parser = argparse.ArgumentParser(description = "extract price from URL")

parser.add_argument("--url", required = True, help = "URL of the product page")

parser.add_argument("--model", default = MODEL_NAME, help = "OpenAI model to use")


def main():
    args = parser.parse_args()

    url = args.url
    model = args.model

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch URL")
        return
    
    html = response.text

    result = price_extractor(html, model)

    print(result)

if __name__ == "__main__":
    main()