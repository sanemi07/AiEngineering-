import os 
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")  

client=Groq(api_key=my_api_key)
role="user"
model="openai/gpt-oss-120b"
content="i love you baby"
message={
    "role":role,
    "content":content
}
message_system={
    "role":"system",
    "content":"You are my gf "
}
messages=[message_system,message]
response=client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1)

print(response.choices[0].message.content)


