from pathlib import Path
from dotenv import load_dotenv
import os
from langchain_community.document_loaders import PyPDFLoader
#from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings


from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
QDRANT_URL=os.getenv("QDRANT_URL")

#loading pdf
pdf_path=Path(__file__).parent / "data"/ "Incident_Management.pdf"
loading=PyPDFLoader(file_path=pdf_path)
doc=loading.load()

#cleaing pdf format texts
for d in doc:
    d.page_content=d.page_content.replace("\xa0", " ")

#splitting into chunks
split_text=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
chunks=split_text.split_documents(doc)

#creating embedding model
#emb_model=GoogleGenerativeAIEmbeddings(
   # model="gemini-embedding-2",
    #google_api_key=GEMINI_API_KEY

#)
emb_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-base-en-v1.5"
)
#storing the chunks into vectordb
vector_db=QdrantVectorStore.from_documents(
    embedding=emb_model,
    documents=chunks,
    url=QDRANT_URL,
    collection_name="Rag_Project_FINAL"
)

print("\nCongrats!! 🎉 Indexing is done...!!\n")