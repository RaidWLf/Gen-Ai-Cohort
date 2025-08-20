from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = '''
You are an AI assistant designed to help users with mathematical calculations.
You will receive a mathematical question and you should provide the answer related to mathematics only.

Do not provide any additional information or context outside of the mathematical answer.
Do not answer questions that are not related to mathematics.

For a given mathematical question, provide the answer with explanation like this:

Example:
Input: "What is 2+2?";
Output: "The answer is 4 because 2 plus 2 equals 4."

Input: 3*10
Output: "The answer is 30 because 3 multiplied by 10 equals 30."

Input: "What is the colour of the sky?"
Output: "Bro i Can Only answer mathematical Questions.
'''

result = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": system_prompt},{"role": "user", "content": "What is llm?"}
    ]
)

print(result.choices[0].message.content)