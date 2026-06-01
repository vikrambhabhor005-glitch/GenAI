from langchain_openai  import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain.tools import tool
# from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
import os
import requests
load_dotenv()
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)
@tool
def get_whether(city):
    """
    return currebt weather of a city """
    print(f"Fething the temprature of {city}....")
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    return response.json()["current_condition"][0]["FeelsLikeC"]


llm_with_tools = llm.bind_tools([get_whether])
a=input("Enter the city name : ")
response = llm_with_tools.invoke("What is the weather in {a}")

print(response.tool_calls)

if response.tool_calls:
    tool_call = response.tool_calls[0]
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    if tool_name == "get_whether":
        result = get_whether.invoke(tool_args)
        print(result)

else:
    print(response.content)


