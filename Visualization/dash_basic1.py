import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1('Hello Dash!', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Div('A second level heading'),
    dcc.Graph(id='FirstGraph', figure={'data': [{'x': [1, 2, 3, 4], 'y': [2, 7, 6, 9], 'type': 'bar', 'name': 'SOF'},
                                                {'x': [1, 2, 3, 4], 'y': [3, 5, 7, 10], 'type': 'bar', 'name': 'NYC'}],
                                       'layout': {
                                           'title': 'Bar Plots in Dash', 'plot_bgcolor': colors['background'],
                                           'paper_bgcolor': colors['background'], 'font': {'color': colors['text']}

                                       }},
              )

])

if __name__ == '__main__':
    app.run_server()
