import pandas as pd
import sqlite3


# Created db with data from csv
 
df = pd.read_csv('./data/posts.csv')
conn = sqlite3.connect('./data/database.db')
df.to_sql('note', conn, if_exists='replace', index=True)
conn.close()



#Show info from db

# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM note")
# rows = cursor.fetchall()
# for row in rows:
#     # row[0] - id
#     # row[1] - text
#     # row[2] - date
#     # row[3] - rubrics
#     print(row[2])
# conn.close()
