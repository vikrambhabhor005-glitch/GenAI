from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

arr = [
    ("system", "You are a helpful assistant")
]

while True:
    x = input("Enter Your Query (type 'exit' to quit): ")
    s = input("Why are you exit")
    if x.lower() == "exit":
        print("meet on new questions !")
        print("Why are you exit ?",s)
        break
    print("okey i got it")
    arr.append(("user", s))
    arr.append(("user", x))

    prompt = ChatPromptTemplate.from_messages(arr)

    chain = prompt | client
    response = chain.invoke({})

    arr.append(("assistant", response.content))

    print("\nAI:", response.content)