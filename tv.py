import plotly.express as px
import csv

with open("tv.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x='Size of TV' , y = "	Average time spent watching TV in a week (hours)" )

    fig.update_yaxes(rangemode = 'tozero')
    fig.update_layout(shapes=[dict(type = "line",y0 = fig , y1 =fig,x0 =0 ,x1 = fig)])


    fig.show()





