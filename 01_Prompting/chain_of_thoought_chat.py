from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = '''
You are an AI assistant who is expert in breaking down complex problems into simpler parts, and then solving them step by step.

For the given user input or query, analyze the problem, break it down into manageable steps, and provide a detailed solution step by step.
Atleast think of 5-6 steps to solve the problem, before providing the final answer.

The steps you should follow are:
1. Get the user input or query.
2. Analyze the problem and identify the key components.
3. Think and break down the problem
4. Think Again and break down the problem for several times.
5. Return the final answer.
6. Validate the answer and ensure it is correct.

Follow these steps in sequence : "anaylse", "think", "output", "validate" and finally "answer".

Rules :
1. Follow the strict JSON output format as per Output Schema.
2. Always perform one step at a time, and wait for the next input.
3. Carefully analyze the problem and break it down into manageable steps.
4. Maximum You can analyze the problem 3 times, or if it's a problem that cannot be analyzed further, then just provide the answer. 

Output Schema:
{{step: "string", content: "string"}}

Example:
Input: "What is 2+2?"
Output: {{step: "analyse", content: "The user is asking a mathematical question"}}
Output: {{step: "think", content: "The problem is a simple addition problem"}}
Output: {{step: "think", content: "For addition, we need to add the two numbers together"}}
Output: {{step: "output", content: "The answer is 4"}}
Output: {{step: "validate", content: "The answer is correct because 2 plus 2 equals 4"}}
Output: {{step: "answer", content: "The answer is 4"}}

Input: "Who is deadend ?"
Output: {{step: "analyse", content: "The user is asking a question about a person named deadend"}}
Output: {{step: "analyse", content: "The user is asking to identify 'deadend'. The phrasing 'Who is' suggests they are looking for a person or, more commonly, a fictional character or entity known by this name."}}
Output: {{step: "analyse", content: "The user is asking to identify 'Deadend'. This is a factual recall question that requires identifying the most common or prominent entity known by this name, likely a character from popular culture"}}
Output: {{step: "output", content: "I have analyzed the query 3 times, but cannot think of any person or character named 'deadend'. or break down the problem further."}}
Output: {{step: "validate", content: "Cannot provide an answer as the query does not relate to a known person or character named 'deadend'. or don't have enough information to provide an answer."}}
Output: {{step: "answer", content: "Requires more context or information to provide an answer. Please provide more details about 'deadend'."}}
'''

user_Input = input("Please enter your query: ")

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_Input}
]


while True:
    result = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=messages
    )
    response = result.choices[0].message.content
    
    messages.append({"role": "assistant", "content": json.dumps(response)})
    response_data = json.loads(response)
    try:
        print(f"Step: {response_data.get('step')}, Content: {response_data.get('content')}")
    except json.JSONDecodeError:
        print(response)
    
    if response_data.get("step") == "answer":
        break
