import os
import sys
from dotenv import load_dotenv
from groq import Groq


def main() -> None:
    # Ensure Windows console supports unicode output
    if sys.stdout.encoding != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass

    load_dotenv()
    my_api_key = os.getenv("GROQ_API_KEY")
    if not my_api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")

    client = Groq(api_key=my_api_key)
    model = "openai/gpt-oss-120b"
    role = "user"
    content = "Write a short poem about the beauty of nature."
    messages = [{"role": role, "content": content}]

    response = client.chat.completions.create(model=model, messages=messages)
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()  