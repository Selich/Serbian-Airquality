import pandas as pd
import json
from flask import Flask

app = Flask(__name__)

def read_prediction_aqi(city):
    df = pd.read_csv("./data/prediction_" + city.strip().lower() + ".csv")
    return df.tail().to_json()

def read_data(city):
    df = pd.read_csv("./data/amskv_" + city.strip().lower() + ".csv")
    df = df.drop(["Unnamed: 0"], axis=1)
    return df.tail().to_json()

@app.route('/aqi/<loc>', methods=['GET'])
def get_current_city(loc):
    return read_data(loc)

@app.route('/prediction/<loc>', methods=['GET'])
def get_prediction_city(loc):
    return read_prediction(loc)

@app.route('/')
def index():
    return "Picko"


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
