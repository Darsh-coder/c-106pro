import plotly.express as px
import csv
import numpy as np


def plot_figure(data_path) :
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x='Temperature' , y = "Ice-cream Sales" )
        fig.show()

def get_data_source(data_path):
    icecreamsales = []
    Temperature = []
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df :
            Temperature.append(float(row["Temperature"]))
            icecreamsales.append(float(row["Ice-cream Sales"]))
    return{"x":icecreamsales,"y":Temperature}

def findcorelation(data_source) :
    colrelation = np.corrcoef(data_source["x"],data_source["y"])
    print("corelation btw tempreture and ice cream sales",colrelation[0,1])

def setup():
    data_path = "ice.csv"
    data_source = get_data_source(data_path)

    findcorelation(data_source)
    plot_figure(data_path)


setup()



