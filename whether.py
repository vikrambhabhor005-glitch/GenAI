from langchain_openai  import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
# from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
import os
load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

import requests
def get_whether(city):
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    return response.json()["current_condition"][0]["FeelsLikeC"]

whether= get_whether(input("Enter city name : "))

prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an assistent."),
            ("user","The whether in {whether} ")
        ]
    )



chain = prompt | llm 
response=chain.invoke(
    {
       "whether": whether
    }
)
print(response.content)
print(whether)

