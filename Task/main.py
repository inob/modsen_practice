from fastapi import FastAPI
from elasticsearch import Elasticsearch, NotFoundError
from passw import password
import sqlite3

app = FastAPI()

es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}],
    http_auth=('elastic', password)
)

@app.get("/search/{text}")
async def search(text: str):
    search_query = {
        "query": {
            "match": {
                "text": text
            }
        },
        "size": 20,
        "sort": [
             {
                 "id": {"order": "asc"}  
             }
        ]
    }

    results = es.search(index="practice", body=search_query)
    return results['hits']['hits']

@app.delete("/delete/{id}")
async def delete(id: int):
    id = str(id)  # Преобразуем id в строку
    if es.exists(index="practice", id=id):
        es.delete(index="practice", id=id)
        return {"detail": "Document deleted"}
    else:
        return {"detail": "Document does not exist"}