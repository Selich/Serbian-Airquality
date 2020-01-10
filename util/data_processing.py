import pandas as pd
import numpy as np


def fill_nan(df: pd.DataFrame, mode="bfill") -> pd.DataFrame:
    if mode == "ffill":
        df = df.ffill(axis=0)
    else:
        df = df.bfill(axis=0)
    return df


def split_dataset(x, y):
    train_size = int(round(len(x) * 0.8))

    x_train = x[:train_size]
    x_test = x[train_size:]
    y_train = x[:train_size]
    y_test = x[train_size:]
    return x_train, x_test, y_train, y_test


def read_data(city, without_nan=True) -> pd.DataFrame:
    df = pd.read_csv("./data/amskv_" + city.strip().lower() + ".csv")
    df = df.drop(["Unnamed: 0"], axis=1)
    if without_nan:
        df = fill_nan(df, "bfill")

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



