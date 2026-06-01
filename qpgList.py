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

class Paper(BaseModel):
    topic : str
    totalmarks: int
    questiontype : str
    marksperquestion : int 

class question(BaseModel):
    Ques:str 
    Option : list[str]
    answer: str
    
class questionPaper(BaseModel):
    topic : str
    passing_marks: int
    questions : list[question]

parser = PydanticOutputParser(pydantic_object=questionPaper)                    

@app.post("/questionpaperGenerator")
async def create_paper_(paper: Paper):
    print("001")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert exam paper generator. {format}."),
            ("user","Generate a question paper of topic {topic},of total marks {totalmarks} and the type of questions {questiontype} with marks of that question should be {marksperquestion}")
        ]
    )
    print("002")
    chain = prompt | llm | parser
    print("003")

    response = chain.invoke(
        {
        "topic": paper.topic,
        "totalmarks": paper.totalmarks,
        "questiontype": paper.questiontype,
        "marksperquestion": paper.marksperquestion,
        "format" : parser.get_format_instructions()
        }
    )
    print("003")

    print(response)
    print("002")

    return {
        "msg": "Question paper generated successfully",
        "paper": response
    }
 

