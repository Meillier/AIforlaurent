import os

from dotenv import load_dotenv
load_dotenv()

# Test version - comment out OpenAI for now
from openai import OpenAI
client = OpenAI(api_key=os.environ["API_KEY"])

system_prompt = "This is AI for Laurent!"

user_prompt = input("What's your question? ")

print(f"System prompt: {system_prompt}")
print(f"User question: {user_prompt}")


chat_completion = client.chat.completions.create(
     messages=[
         {"role": "system", "content": system_prompt},
         {"role": "user", "content": user_prompt},
     ],
     model="gpt-4o",
 )

response_text = chat_completion.choices[0].message.content

print(response_text)
