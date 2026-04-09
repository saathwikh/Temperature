import pandas as pd
import sqlite3

conn = sqlite3.connect("weather.db")

with open("fetch_data.sql", "r") as f:
    query = f.read()

df = pd.read_sql(query, conn)

print(df)

conn.close()