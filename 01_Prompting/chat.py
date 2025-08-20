from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

result = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "user", "content": "what is 2+2"}]
)

print(result.choices[0].message.content)