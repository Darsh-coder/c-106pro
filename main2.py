import plotly.express as px
import csv
import numpy as np


def plot_figure(data_path) :
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x='Size of TV' , y = "Average time spent watching TV in a week (hours)" )
        fig.show()

def get_data_source(data_path):
    Sizeoftv = []
    AveragetimespentwatchingTVinaweekhours = []
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df :
            Sizeoftv.append(float(row["Size of TV"]))
            AveragetimespentwatchingTVinaweekhours.append(float(row["Average time spent watching TV in a week (hours)"]))
    return{"x":Sizeoftv,"y":AveragetimespentwatchingTVinaweekhours}

def findcorelation(data_source) :
    colrelation = np.corrcoef(data_source["x"],data_source["y"])
    print("corelation btw tv time and tv size",colrelation[0,1])

def setup():
    data_path = "tv.csv"
    data_source = get_data_source(data_path)

    findcorelation(data_source)
    plot_figure(data_path)


setup()
