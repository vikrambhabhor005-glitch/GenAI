from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
import os

load_dotenv()

client = MongoClient("mongodb+srv://admin:admin@cluster0.q0erqhu.mongodb.net/?appName=Cluster0")

db = client["LDRP_RAG"]
collection = db["documents"]

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)

vector_store = MongoDBAtlasVectorSearch(
    collection=collection,
    embedding=embeddings,
    index_name="RAG_index"
)

query="What is the defination of AI Agent"

ans = vector_store.similarity_search(query, k=3)

context = " ".join(
    doc.page_content for doc in ans
)

prompt= f"""

Amswer only based on the following context.
 
if answer is not found in the context, say you don't know.PermissionError

Context:{context}
Question: {query}
"""

llm = ChatOpenAI(
    model="gpt-3.5-turbo"
)

response = llm.invoke(prompt)
print("Answer : ",response.content)