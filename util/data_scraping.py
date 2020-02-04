get_ipython().system('pip install --user beautifulsoup4 selenium numpy pandas ')
from IPython import get_ipython
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd
import requests as req
from bs4 import BeautifulSoup
import urllib.request
import time
import re

amskv_url = "http://www.amskv.sepa.gov.rs/pregledpodatakazbirni.php"
driver = webdriver.Chrome()
driver.get(amskv_url)

check_box = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[1]/div/label[10]/input")
check_box.click()

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

trideset_dana = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div[2]/div/div/div/div[1]/div/div[1]/label[3]").click()
prikazi = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div[1]/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div[2]/div/div/ul/li[2]/a").click()

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


labels = populate_with_labels(driver)

df = pd.DataFrame(columns=labels)
data = get_table_data(driver,df)
labels

for i in range(0,NUMBER_OF_ROWS - 1):
    df.loc[i+1] = data[i]

df.to_csv("./data/amskv_data.csv")



