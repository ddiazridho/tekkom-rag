from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

COLLECTION = "hello"

client.upsert(
    collection_name=COLLECTION,
    points= [
        models.PointStruct(
            id=4,
            vector=[1,2,5,100],
            payload={"kategori" : "mata kuliah"}
        ),
    ]
)
