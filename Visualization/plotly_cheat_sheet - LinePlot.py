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
list_of_pop_col = [ col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_pop_col]

data = [go.Scatter(x=df2.columns,
                   y=df2.loc[name],
                   mode = 'lines',
                   name=name) for name in df2.index]
pof.plot(data)

pof.plot(fig,"basic_line.html")
