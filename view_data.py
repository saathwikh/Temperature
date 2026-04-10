import psycopg2

conn = psycopg2.connect(
    host="weatherdb.ca5koie4aeuq.us-east-1.rds.amazonaws.com",
    database="weatherdb",
    user="saathwikh",
    password="Admin2026",
    port="5432",
    sslmode="require"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM weather;")
rows = cursor.fetchall()

print("Data from AWS DB:\n")

for row in rows:
    print(row)

conn.close()