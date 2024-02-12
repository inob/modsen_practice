import sqlite3
from elasticsearch import Elasticsearch
from passw import password
from datetime import datetime


es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}],
    http_auth=('elastic', password)
)


mapping = {
    "mappings": {
        "properties": {
            "iD": {"type": "text"},
            "text": {"type": "text"},
            "date": {
                "type": "date",
                "fields": {
                    "keyword": { 
                        "type": "keyword"
                    }
                }
            }
        }
    }
}

# Создайте индекс в Elasticsearch
es.indices.create(index='note', body=mapping, ignore=400)

# Создайте подключение к SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Выполните запрос SELECT для получения всех записей из таблицы note
cursor.execute("SELECT * FROM note")
rows = cursor.fetchall()

# Индексируйте каждую запись в Elasticsearch
for row in rows:
    doc = {
        'iD': row[0],
        'text': row[1],
        'date': datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S'),  # предполагается, что дата в формате 'YYYY-MM-DD HH:MM:SS'
    }
    res = es.index(index='note', body=doc)

