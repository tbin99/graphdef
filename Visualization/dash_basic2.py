import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go

app = dash.Dash()

np.random.seed(100)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div(
    [dcc.Graph(id='scatterplot', figure={
        'data': [
            go.Scatter(x=random_x, y=random_y,
                       mode='markers',
                       marker={
                           'size': 12,
                           'color': 'rgb(42,34,98',
                           'symbol': 'pentagon',
                           'line': {
                               'width': 2
                           }
                       }
                       )
        ], 'layout': go.Layout(title='My very good plot', xaxis={
            'title': 'Random X'
        }, yaxis={'title': 'Random Y'}
                               )

    })]

    ,

)

if __name__ == '__main__':
    app.run_server()
