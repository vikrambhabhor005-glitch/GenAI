from langchain_openai  import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

arr=[
        ("system","You are a helpful assistant"),
    ]   

for i in range(5):
    x= input("Enter Your query : ")
    arr.append(("user",x))
    prompt = ChatPromptTemplate.from_messages(arr)

    chain = prompt | client
    response = chain.invoke({})
    arr.append(("ai",response.content))    
    print(response.content)