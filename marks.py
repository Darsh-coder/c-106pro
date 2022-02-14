import plotly.express as px
import csv
import numpy as np


def plot_figure(data_path) :
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x='Days Present' , y = "Marks In Percentage" )
        fig.show()

def get_data_source(data_path):
    MarksInPercentage = []
    DaysPresent = []
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df :
            MarksInPercentage.append(float(row["Marks In Percentage"]))
            DaysPresent.append(float(row["Days Present"]))
    return{"x":MarksInPercentage,"y":DaysPresent}

def findcorelation(data_source) :
    colrelation = np.corrcoef(data_source["x"],data_source["y"])
    print("corelation btw marks and student attendence",colrelation[0,1])

def setup():
    data_path = "student.csv"
    data_source = get_data_source(data_path)

    findcorelation(data_source)
    plot_figure(data_path)


setup()
