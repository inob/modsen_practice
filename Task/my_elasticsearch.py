from elasticsearch import Elasticsearch
from passw import password
import sqlite3
es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}],
    http_auth=('elastic', password)
)

# Тут мы индексируем данные в эластик, из sqlite
# conn = sqlite3.connect('posts.db')
# cursor = conn.cursor()

# # Получаем данные из таблицы posts
# cursor.execute("SELECT * FROM posts")
# rows = cursor.fetchall()

# count = 0
# for row in rows:
#     count+=1
#     doc = {
#         'id': count,
#         'date': row[3],
#         'text': row[2]
#     }
#     es.index(index='practice', body=doc)
# conn.close()

search_query = {
    "query": {
        "match": {
            "id": "1500"
        }
    }
}

# Отправляем запрос и получаем результат
results = es.search(index="practice", body=search_query)

# Обрабатываем результат
for hit in results['hits']['hits']:
    print(hit['_source'])