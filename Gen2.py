from openai  import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)
message = [
    {
        "role":"system",
        "content": "You are a helpful assisment"
    }
]
for i in range(3):
    user_input = input("User:")
    message.append({
        "role": "user",
        "content": user_input
    })
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message
    )
    assistent_response = response.choices[0].message.content
    print("assistent:", assistent_response)
    message.append({
        "role":"assistent",
        "content":assistent_response
    })