from langchain_openai  import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()
client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)


prompt = ChatPromptTemplate.from_messages(
    {("system","You are a helpful assistent"),
     ("user","create a quetion paper of topic{topic} ,of marks {marks} and {difficulty},dificultly level")
    }
)
topic= input("Enter tpic : ")
marks= input("Enter marks : ")
difficulty= input("Enter difficulty : ")
chain = prompt | client
response = chain.stream(
    {
        "topic": topic,
        "marks": marks,
        "difficulty": difficulty
    }
)
for chunk in response:
    print(chunk.content,end="")
