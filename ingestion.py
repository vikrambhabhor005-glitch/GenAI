from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings


from pymongo import MongoClient
import os


load_dotenv()
loader = PyPDFLoader("vk.pdf")
documents = loader.load()
# print(documents)
 
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

Docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)

client = MongoClient("mongodb+srv://admin:admin@cluster0.q0erqhu.mongodb.net/?appName=Cluster0")
db = client["LDRP_RAG"]
collection = db["documents"]

for doc in Docs:
    embedding = embeddings.embed_query(doc.page_content)
    document_data = {
        "text" : doc.page_content,
        "embedding" : embedding
    }
    collection.insert_one(document_data)

print("***********************************************")