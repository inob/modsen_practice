import sqlite3
import pandas as pd

# conn = sqlite3.connect('posts.db')
# data = pd.read_csv('posts.csv')
# data.to_sql('posts', conn, if_exists='append', index = False)



conn = sqlite3.connect('posts.db')

cursor = conn.cursor()
cursor.execute("SELECT * FROM posts")
rows = cursor.fetchall()


for row in rows:
    
    #row[1] - VK_ID
    #row[2] - Text
    #row[3] - date    
    
    print(row[3])

conn.close()