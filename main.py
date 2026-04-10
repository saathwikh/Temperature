import requests
import json
import pandas as pd
import psycopg2

def get_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&current_weather=true"
    response = requests.get(url)
    return response.json()

def save_raw(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

def process_data(data):
    temp = data["current_weather"]["temperature"]
    wind = data["current_weather"]["windspeed"]
    time = data["current_weather"]["time"]

    df = pd.DataFrame([{
        "temperature": temp,
        "windspeed": wind,
        "time": time
    }])

    return df

def save_to_db(df):
    conn = psycopg2.connect(   # conn = connection btw python & postgresql
        host="weatherdb.ca5koie4aeuq.us-east-1.rds.amazonaws.com",
        database="weatherdb",
        user="saathwikh",        
        password="Admin2026",    
        port="5432",
        sslmode="require"
    )

    cursor = conn.cursor() # cursor used to execute sql queries

    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO weather (temperature, windspeed, time) VALUES (%s, %s, %s)",
            (row["temperature"], row["windspeed"], row["time"])
        )

    conn.commit()
    conn.close()

def main():
    data = get_data()
    save_raw(data) # saving raw data to data.json
    df = process_data(data) # processing data
    save_to_db(df) # saving processed data to database
    print(df)

if __name__ == "__main__":
    main()