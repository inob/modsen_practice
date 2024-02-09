from elasticsearch import Elasticsearch
from passw import password
es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}],
    http_auth=('elastic', password)
)

response = es.search(
    index="practice",
    body={
        "query": {
            "match_all": {}
        }
    }
)

for hit in response['hits']['hits']:
    print(hit['_source'])