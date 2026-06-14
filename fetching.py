from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
QDRANT_URL=os.getenv("QDRANT_URL")

#embedding model same in indexing
#emb_model=GoogleGenerativeAIEmbeddings(
  #  model="gemini-embedding-2",
  #  google_api_key=GEMINI_API_KEY
#)
emb_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-base-en-v1.5"
)

#vector db creation same in ndexing but using .from existing
vector_search=QdrantVectorStore.from_existing_collection(
        embedding=emb_model,
        url=QDRANT_URL,
        collection_name="Rag_Project_FINAL"
)

def fetch(qry:str, k: int=4):
    #results=vector_search.similarity_search(qry,k=k)
    #for better results and diversity, use MMR
    results=vector_search.max_marginal_relevance_search(qry,k=5,fetch_k=20)
    return results