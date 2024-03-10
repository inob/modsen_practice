from fastapi import FastAPI
from elasticsearch import Elasticsearch, NotFoundError
from passw import password
import asyncio
import aiohttp

app = FastAPI()

async def get_es():
    async with aiohttp.ClientSession() as session:
        es = Elasticsearch(
            [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}],
            http_auth=('elastic', password),
            loop=asyncio.get_event_loop(),
            http_async_client=session
        )
        return es

@app.get("/search/{text}")
async def search(text: str):
    es = await get_es()
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

    results = await es.search(index="note", body=search_query)
    return results['hits']['hits']

@app.delete("/delete/{iD}")
async def delete(iD: int):
    es = await get_es()
    iD = str(iD)
    search_query = {
        "query": {
            "match": {
                "iD": iD
            }
        }
    }
    results = await es.search(index="note", body=search_query)
    
    if results['hits']['hits']:
        doc_id = results['hits']['hits'][0]['_id']
        await es.delete(index="note", id=doc_id)
        return {"detail": "Document deleted"}
    else:
        return {"detail": "Document does not exist"}
