from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai  import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
import os


load_dotenv()

app = FastAPI()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

class Project(BaseModel):
    topic : str
    technology: str
    duration : str
    teamSize : int 

class Section(BaseModel):
    title:str 
    content : str
    
class ProjectDocument(BaseModel):
    topic : str
    technology: str
    duration : str
    section:list[Section]

parser = PydanticOutputParser(pydantic_object= ProjectDocument)                    

@app.post("/ProjectDocumentGenerator")
async def create_project(project : Project):
    print("001")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert exam paper generator. {format}."),
            ("user","Generate a Project Document of topic {topic}, by using {technology} and it is duration {duration} with the number of pepole in team {teamSize}")
        ]
    )
    print("002")
    chain = prompt | llm | parser
    print("003")

    response = chain.invoke(
        {
        "topic": project.topic,
        "technology": project.totalmarks,
        "duration": project.duration,
        "teamsize": project.teamsize,
        "format" : parser.get_format_instructions()
        }
    )
    print("003")

    print(response)
    print("002")

    return {
        "topic": project.topic,
        "technology": project.technology,
        "project_document": response
    }
 

