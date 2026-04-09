import psycopg2

conn = psycopg2.connect(
    host="weatherdb.ca5koie4aeuq.us-east-1.rds.amazonaws.com",
    database="postgres",
    user="saathwikh",
    password="Admin2026",
    port="5432",
    sslmode="require"
)

print("Connected successfully!")

conn.close()