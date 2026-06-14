import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()
client = QdrantClient(url=os.getenv("QDRANT_URL"))

# Let's see if the collection actually exists and how many points are in it
try:
    info = client.get_collection(collection_name="Rag_Project_HF_Fixed")
    print(f"✅ Collection found! Total vectors stored: {info.points_count}")
except Exception as e:
    print(f"❌ Could not find collection. Error: {e}")