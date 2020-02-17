import pandas as pd
import numpy as np


def read_data(city, without_nan=True) -> pd.DataFrame:
    df = pd.read_csv("./data/amskv_" + city.strip().lower() + ".csv")
    df = df.drop(["Unnamed: 0"], axis=1)
    if without_nan:
        df = df.bfill(axis=0)
    return df

def get_all_data() -> pd.DataFrame:
    df = pd.DataFrame()
    df_novisad = read_data("novisad")
    df_beograd = read_data("beograd")
    df_kragujevac = read_data("kragujevac")
    df_nis = read_data("nis")
    df_sabac = read_data("sabac")
    df_uzice = read_data("uzice")

    df_novisad["Mesto"] = "Novi Sad"
    df_beograd["Mesto"] = "Beograd"
    df_kragujevac["Mesto"] = "Kragujevac"
    df_nis["Mesto"] = "Nis"
    df_sabac["Mesto"] = "Sabac"
    df_uzice["Mesto"] = "Uzice"

    df = pd.concat([
        df_novisad, df_kragujevac, df_beograd,
        df_nis, df_sabac, df_uzice
    ], ignore_index=True)

    return df


def one_hot_encode(df: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([df, pd.get_dummies(df['Mesto'], prefix='Mesto')], axis=1)
    return df


