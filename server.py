import pandas as pd
import json
from flask import Flask
from main import predict

app = Flask(__name__)

def read_prediction(city, interval):
    return predict(city, int(interval) * 4 * 24)

def read_data(city):
    df = pd.read_csv("./data/amskv_" + city.strip().lower() + ".csv")
    df = df.drop(["Unnamed: 0"], axis=1)
    return df.tail().to_json()

@app.route('/aqi/<loc>', methods=['GET'])
def get_current_city(loc):
    return read_data(loc)

@app.route('/prediction/<loc>/<interval>', methods=['GET'])
def get_prediction_city(loc, interval):
    return read_prediction(loc, interval)

@app.route('/')
def index():
    return "Home Page"


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
