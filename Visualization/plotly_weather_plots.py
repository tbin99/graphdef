# Import required libraries
import numpy as np
import plotly.offline as pof
import plotly.graph_objs as go
import pandas as pd
#----------------------------------------------------------------------
#                                                                     !
#                      Line Plot                                   !
#                                                                     !
#                                                                     !
# ---------------------------------------------------------------------

# Read the csv from github
df = pd.read_csv('https://raw.githubusercontent.com/TechieBIN/graphdef/master/Data/2010YumaAZ.csv')
# Create a sub dataframe with values from Division 1
week_days = ['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY']

data = []

for day in week_days:
    df2 = df[df['DAY'] == day]
    trace = go.Scatter(x=df['LST_TIME'],
                       y=df[df['DAY'] == day]['T_HR_AVG'],
                       name=day,
                       mode='line')
    data.append(trace)

# Define the layout
layout = go.Layout(
    title='Daily temperatures from June 1-7, 2010 in Yuma, Arizona',
    hovermode='closest'
)

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pof.plot(fig, filename='solution2a.html')






#pof.plot(fig,"basic_line.html")
