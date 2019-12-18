import pandas as pd
import json
from flask import Flask
app = Flask(__name__)


def read_data(city):
    df = pd.read_csv("./data/amskv_" + city.strip().lower() + ".csv")
    return df.tail().to_json()


@app.route('/aqi/<loc>', methods=['GET'])
def get_current_city(loc):
    return read_data(loc)


@app.route('/')
def index():
    return "This home"


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
