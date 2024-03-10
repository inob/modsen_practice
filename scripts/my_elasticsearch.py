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

es.indices.create(index='note', body=mapping, ignore=400)

conn = sqlite3.connect('./data/database.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM note")
rows = cursor.fetchall()

for row in rows:
    doc = {
        'iD': row[0],
        'text': row[1],
        'date': datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S'),
    }
    res = es.index(index='note', body=doc)

