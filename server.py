import pandas as pd
import json
from flask import Flask
app = Flask(__name__)


def read_data(city):
    df = pd.read_csv("./data/amskv_" + city.strip().lower() + ".csv")
    return df.tail().to_json()


@app.route('/aqi/<loc>')
def get_current_city(loc):
    return read_data(loc)


def main():
    pass


if __name__ == "__main__":
    main()
