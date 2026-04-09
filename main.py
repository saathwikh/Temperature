import requests
import json
import pandas as pd
import sqlite3

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
    conn = sqlite3.connect("weather.db")
    df.to_sql("weather", conn, if_exists="append", index=False)
    conn.close()

def main():
    data = get_data()
    save_raw(data)
    df = process_data(data)
    save_to_db(df)
    print(df)

if __name__ == "__main__":
    main()