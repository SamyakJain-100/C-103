import pandas as pd

import plotly.express as px

#reading data from csv files
df = pd.read_csv("datas.csv")
fig = px.bar(df, x='date', y='cases')
fig.show()
