import argparse
import os

from price_tracker.openai_client import price_extractor
from price_tracker.webscraper import get_rendered_html

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def main(url: str, model: str):
    html = get_rendered_html(url)

    result = price_extractor(html, model)

    print(result)


def cli():
    parser = argparse.ArgumentParser(description="extract price from URL")

    parser.add_argument("--url", required=True, help="URL of the product page")

    parser.add_argument("--model", default=MODEL_NAME, help="OpenAI model to use")

    args = parser.parse_args()

    main(url=args.url, model=args.model)


if __name__ == "__main__":
    cli()
