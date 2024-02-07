import sqlite3
import requests
import json
from passw import password
from requests.auth import HTTPBasicAuth

conn = sqlite3.connect('posts.db')
c = conn.cursor()

c.execute("SELECT * FROM posts")

records = c.fetchall()

url = "http://localhost:9200/practice/_doc"
headers = {'Content-Type': 'application/json'}
for record in records:
    doc = {
        "iD": record[0],
        "text": record[1]
    }
    response = requests.post(url, auth=HTTPBasicAuth('elastic', password), headers=headers, data=json.dumps(doc))

    if response.status_code != 201:
        print(f"Error indexing record {record[0]}: {response.text}")
