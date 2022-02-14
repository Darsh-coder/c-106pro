from time import sleep
import plotly.express as px
import csv
import numpy as np


def plot_figure(data_path) :
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x='Coffee in ml' , y = "sleep in hours" )
        fig.show()

def get_data_source(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df :
            sleep.append(float(row["sleep in hours"]))
            coffee.append(float(row["Coffee in ml"]))
    return{"x":coffee,"y":sleep}

def findcorelation(data_source) :
    colrelation = np.corrcoef(data_source["x"],data_source["y"])
    print("corelation btw sleep and amount of coffee",colrelation[0,1])

def setup():
    data_path = "ad.csv"
    data_source = get_data_source(data_path)

    findcorelation(data_source)
    plot_figure(data_path)


setup()
