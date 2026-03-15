from openai import OpenAI

def openaicaller():
    client = OpenAI()

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "user", "content": "knock knock."},
            {"role": "assistant", "content": "Who's there?"},
            {"role": "user", "content": "Orange."},
        ],
    )

    return response.output_text

if __name__ == "__main__":
    print(openaicaller())