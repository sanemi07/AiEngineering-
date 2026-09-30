import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")   


client=Groq(api_key=my_api_key) 

prompt1="hii"
prompt2="hello how are you"
prompt3="give me  an essay on the topic of climate change"

prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
        "role": "user",
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,)
    usage=response.usage
    print(f"Prompt: {prompt} input tokens: {usage.prompt_tokens}, output tokens: {usage.completion_tokens}, total tokens: {usage.total_tokens}")


