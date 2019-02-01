import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('https://raw.githubusercontent.com/TechieBIN/graphdef/master/Data/gapminderDataFiveYear.csv')

print(df.head())

years = []
for year in df['year'].unique():
    years.append({'label':str(year),'value':year})

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='select-year',options=years,value=df['year'].min())

])

@app.callback(Output('graph','figure'),

              [Input('select-year','value')])
def update_graph(selected_year):
    df_filter_year = df[df['year'] == selected_year]
    traces = []

    for cont in df_filter_year['continent'].unique():
        df_filter_con = df_filter_year[df_filter_year['continent'] == cont]
        traces.append(go.Scatter(
            x = df_filter_con['gdpPercap'],
            y= df_filter_con['lifeExp'],
            mode = 'markers',
            opacity = '0.7',
            marker = { 'size':15},
            name = cont

        ))

        title = "GDP vs Life Expectency for the Year {}".format(selected_year)

    return {'data':traces,
            'layout': go.Layout(title=title,
                                xaxis= { 'title':'GDP Per Cap','type':'log'},
                                yaxis = { 'title': 'Life Expectancy '}
                                                                )
            }


if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=80)