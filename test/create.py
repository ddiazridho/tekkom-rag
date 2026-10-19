from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

COLLECTION = "hello"
client.create_collection(
    collection_name= COLLECTION, 
    vectors_config=models.VectorParams(
        size = 4,
        distance = models.Distance.COSINE,
    ))