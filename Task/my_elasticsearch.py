import sqlite3
from elasticsearch import Elasticsearch
from passw import password

es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}],
    http_auth=('elastic', password)
)


conn = sqlite3.connect('posts.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM posts")
rows = cursor.fetchall()

count = 0
for row in rows:
    count += 1
    doc = {
        'id': str(count),  
        'date': row[3],
        'text': row[2]
    }
    es.index(index='practice', id=doc['id'], body=doc)  

conn.close()


# search_query = {
#     "query": {
#         "match": {
#             "id": "1500"
#         }
#     }
# }

# # Отправляем запрос и получаем результат
# results = es.search(index="practice", body=search_query)

# # Обрабатываем результат
# for hit in results['hits']['hits']:
#     print(hit['_source'])