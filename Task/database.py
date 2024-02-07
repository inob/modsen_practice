import sqlite3
import pandas as pd

conn = sqlite3.connect('posts.db')
data = pd.read_csv('posts.csv')
data.to_sql('posts', conn, if_exists='append', index = False)