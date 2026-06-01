from langchain_openai  import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import  pydantic
from 
import os


load_dotenv()
llm = ChatOpenAI(
    model="gpt-3.5-turbo"
)
class Question(BaseModel)

prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert exam paper generator."),
            ("user","Generate a question paper of topic {topic},of total marks {totalmarks} and the type of questions {questiontype} with marks of that question should be {marksperquestion}")
        ]
    )
# parser = JsonOutputParser
chain = prompt | llm |  

response = chain.invoke(
    {
        "topic" :
        "quetion_type" :
        difficulty_level" : 
        num_quetions" :
        "format" :  
    }
)