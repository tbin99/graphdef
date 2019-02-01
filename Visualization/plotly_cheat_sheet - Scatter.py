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
df = pd.read_csv('https://raw.githubusercontent.com/TechieBIN/graphdef/master/Data/nst-est2017-alldata.csv')
# Create a sub dataframe with values from Division 1
df2 = df[ df['DIVISION'] == '1']
# Set the index of Column index as name
df2.set_index('NAME',inplace=True)







x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)
trace = go.Scatter(x=x_values,y=y_values,
                   mode='line',name='markers')
data = [trace]

layout = go.Layout(title='Basic Scatter', xaxis = dict(title='Lin Spaced X'),
                   yaxis = dict(title ='Random N Y'),
                   )
fig = go.Figure(data=data,layout=layout)
pof.plot(fig,"basic_line.html")
