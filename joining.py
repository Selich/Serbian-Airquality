import pandas as pd 


df = pd.read_csv("./data/amskv_data.csv")
df.head()

labels = [
    "Unnamed: 0",
    "SO2 [ug.m-3]",
    "O3 [ug.m-3]",
    "NO2 [ug.m-3]",
    "NOX [ug.m-3]",
    "CO [mg.m-3]",
    "NO [ug.m-3]"
]

vreme = [
    "Unnamed: 0",
    "V [m/s]",
    "dd [°]",
    "P [mb]",
    "t [°C]"
]


df_vreme = df.drop(labels=labels, axis=1)
df_vreme.to_csv("./data/amskv_vreme.csv")

df_kvalitet = df.drop(labels=vreme, axis=1)
df_kvalitet.to_csv("./data/amskv_kvalitet.csv")


print(df.head())
