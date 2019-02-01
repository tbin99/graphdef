import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='intake',value='Enter Something Here', type='text'),
    html.Div(id='displayout')

])


@app.callback(Output(component_id='displayout',component_property='children'),[Input(component_id='intake',component_property='value')])

def update_output_div(input_value):
    return "You entered: {}".format(input_value)



if __name__ == '__main__':
    app.run_server()