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
             "date.keyword": {"order": "desc"}  
         }
    ]
}

    results = es.search(index="note", body=search_query)
    return results['hits']['hits']

@app.delete("/delete/{iD}")
async def delete(iD: int):
    iD = str(iD)
    search_query = {
        "query": {
            "match": {
                "iD": iD
            }
        }
    }
    results = es.search(index="note", body=search_query)
    
    if results['hits']['hits']:
        doc_id = results['hits']['hits'][0]['_id']
        es.delete(index="note", id=doc_id)
        return {"detail": "Document deleted"}
    else:
        return {"detail": "Document does not exist"}