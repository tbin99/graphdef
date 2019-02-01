import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

# Define the app
app = dash.Dash()

#Import the data
df = pd.read_csv('https://raw.githubusercontent.com/TechieBIN/graphdef/master/Data/OldFaithful.csv')

app.layout = html.Div(
    [dcc.Graph(id='oldfaithful', figure = {
        'data':[
            go.Scatter(x=df['X'], y=df['Y'],
                       mode='markers',
                       marker={
                           'size':12,
                           'color': 'rgb(42,34,98)',
                           'symbol':'pentagon'
                       }
                       )

        ],
        'layout' : go.Layout(title='Old Faithful Eruption Intervals Vs Durations',xaxis={
            'title':'Interval to Next Eruption in Minutes'
        },
                             yaxis={
                                 'title':'Duration of Eruption in Minutes.'
                             }
                             )
    })]


)

if __name__ == '__main__':
    app.run_server()

