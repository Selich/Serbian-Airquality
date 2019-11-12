# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%%
from IPython import get_ipython

#%% [markdown]
# # Predvidjanje kvaliteta vazduha u periodu od nedelju dana
#%% [markdown]
# ### Potrebne biblioteke:
# - numpy
#     - Koristimo za rad nad matricama
# - pandas
#     - Omogucava dobru organizaciju podataka i rad sa kljucevima i ostalim obelezijama
# - requests
#     - Sluzi za slanje http zahteva koji koristimo za pozivaje API-a
# - selenium
#     - Koristi se za automatsko koriscenje internet pretrazivaca
# - BeautifulSoup
#     - Omogucava citanje html stranica i izvacenje informacija iz iste

#%%
get_ipython().system('pip install --user beautifulsoup4 selenium numpy pandas ')
import numpy as np
import pandas as pd
import requests as req
from bs4 import BeautifulSoup
import urllib.request
import time
import re

#%% [markdown]
# ### Poziv na API radi pribavljanja podataka
# 
# 
# 

#%%

api_key = "c8055f9d-1fd0-4ad3-ab23-678ee0727b7b"
base_url = "https://api.airvisual.com/v2"
url_key = "?key=" + api_key
url = base_url + "/countries" + url_key

url_nearest_city = base_url + "/nearest_city" + url_key


#%%
data = req.get(url)
nearest_city = req.get(url_nearest_city)


#%%
nearest_city.json()

#%% [markdown]
# ### Stavljanje podataka u Pandas dataframe
# - Dobavljanje podataka za lokaciju Liman, Novi Sad sa sajta http://www.sepa.gov.rs/ za period od 30 dana.
# 

#%%


#%% [markdown]
# - Scraping podatke sa Sepa

#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
amskv_url = "http://www.amskv.sepa.gov.rs/pregledpodatakazbirni.php"
driver = webdriver.Chrome()
driver.get(amskv_url)
#%%

check_box = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[1]/div/label[10]/input")
check_box.click()
#%%

komponente = [
    "/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/div[1]/label[1]/input",
    "/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/div[1]/label[3]/input",
    "/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/div[1]/label[4]/input",
    "/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/div[1]/label[5]/input",
    "/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/div[1]/label[6]/input",
    "/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/div[1]/label[12]/input",
    "/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/div[1]/label[35]/input",
    "/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/div[1]/label[36]/input",
    "/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/div[1]/label[37]/input",
    "/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/div[1]/label[38]/input",
    "/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/div[1]/label[39]/input"
]

for k in komponente:
    driver.find_element_by_xpath(k).click()

prikazi = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/a").click()

#%%
trideset_dana = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div[2]/div/div/div/div[1]/div/div[1]/label[3]").click()
prikazi = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div[2]/div/div/ul/li[2]/a").click()

#%%
NUMBER_OF_ROWS = 720

def get_row_data(row,item):
    row_url = "/html/body/div[2]/div[2]/div/div[2]/form/div/div[2]/div/div/div/div[2]/div/table/tbody/tr[" + row + "]/td[" + item + "]"
    item = driver.find_element_by_xpath(row_url)
    return item

def populate_with_labels(driver):

    labels = []
    for i in range(1,12):
        label = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div[2]/div/div/div/div[2]/div/table/thead/tr/th["+str(i)+"]")
        data = label.text
        data = data.replace("\nNovi Sad Liman", "")
        labels.append(data)

    return labels

def get_table_data(driver,df):
    mat = []
    for i in range(1,NUMBER_OF_ROWS):
        arr = []
        for j in range(1,12):
            data = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div[2]/div/div/div/div[2]/div/table/tbody/tr["+str(i)+"]/td["+str(j)+"]")
            arr.append(data.text)
            print(data.text)
        mat.append(arr)

    return mat




#%%
labels = populate_with_labels(driver)

df = pd.DataFrame(columns=labels)
data = get_table_data(driver,df)
labels
#%%
for i in range(0,NUMBER_OF_ROWS - 1):
    df.loc[i+1] = data[i]

df.head()
#%%
df.to_csv("./data/amskv_data.csv")
#%% [markdown]
# 
# ## Linearna regresija
# Linearna regresija (Linear Regression) je jedna od najpoznatijih metoda nadgledanog učenja
# Za početak bavićemo se prostom linearnom regresijom (simple LR, univariate LR)
# Imamo jednu ulaznu promenljivu (feature) i jednu izlaznu promenljivu
# - Notacija:
#     - $x$: Ulazni podaci (features), $x^{(i)}$: Ulazni podatak iz i-tog trening primera
#     - $y$: Izlazni podaci (labels), $y^{(i)}$: Izlazni podatak iz i-tog trening primera
#     - $m$: Veličina trening skupa - broj semplova
# - Hipoteza (model): $ h_\theta(x) = \theta_0 + \theta_1 x $
#     - Linearna funkcija
#     - "Učimo" parametre $\theta_0$ i $\theta_1$, tj. modifikujemo ih tako da budu "što bolji"
# - Funkcija troška (kriterijumska funkcija, funkcija koštanja, cost function, loss function)
#     - U ovom slučaju za funkciju troška uzimamo MSE (srednje kvadratno odstupanje, mean squared error)
#     - $J(\theta_0, \theta_1) = \frac{1}{m} \sum\limits_{i=1}^{m} (h_\theta(x^{(i)} - y^{(i)})^2$ (nekada $\frac{1}{2m}$ zbog lepšeg izvoda)
#     - Dakle, menjamo $\theta_0$ i $\theta_1$ tako da minimizujemo funkciju troška, kako?
# - Optimizacija: gradijentni spust (gradient descent): iterativni optimizacioni metod za minimizaciju funkcije
# - Određuje u kom smeru treba da se krećemo da što efikasnije poboljšamo vrednosti parametara, varijante:
#     - Stochastic: Računamo funkciju troška za svaki trening primer i ažuriramo parametre jednom po primeru
#     - Batch: Agregiramo funkciju troška za sve primere u trening skupu i ažuriramo parametre jednom za ceo skup
#     - Minibatch: Delimo trening skup na manje skupove (batches) fiksne veličine, i nad njima agregiramo funkciju troška, jedno ažuriranje parametara po batch-u

#%%



