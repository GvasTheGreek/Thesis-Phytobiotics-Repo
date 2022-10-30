from dash import dcc, html, Input, Output, Dash
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import plotly.express as px
import pandas as pd
import os
from django.core.files.storage import default_storage
from phytobiotics_v2.settings import MEDIA_ROOT


app = DjangoDash('tetarto_grafima_dash')

def serve_layout():

    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files"))
        
    def get_columns():
        files_list = []
        columns_list = []
        for col in get_file_list():
            files_list.append(col)


        if len(get_file_list()) == 0:
            return 'Insert File'
        else:
            var = pd.read_json(default_storage.open(os.path.join('files',files_list[0])))
            var.drop('Entity-Name', axis=1, inplace=True)
            for i in var.columns:
                columns_list.append(i)
    
            return columns_list

    return html.Div([
        html.Div([
            html.H4('Interactive heat plot accompanied by a histogram. User determines the input. Slider option is available'),
            html.Div([
            dcc.Dropdown(
                get_file_list(),
                '',
                id='choose_file'
            )
            ]),
            html.Div([
                html.P("Filter by x-axis:"),
                dcc.Dropdown(
                    get_columns(),
                    'ambient_noise',
                    id='xaxis-column'
                )
            ], style={'width': '32%', 'float': 'left' ,'display': 'inline-block'}),

            html.Div([
                html.P("Filter by y-axis:"),
                dcc.Dropdown(
                    get_columns(),
                    'temperature',
                    id='yaxis-column'
                )
            ], style={'width': '32%', 'float': 'right', 'display': 'inline-block'}),

            html.Div([
                html.P("Filter by z-axis:"),
                dcc.Dropdown(
                    get_columns(),
                    'temperature',
                    id='zaxis-column'
                )
            ], style={'width': '32%', 'float': 'center', 'display': 'inline-block'}),

            html.Div(
                dcc.Graph(id='indicator-graphic')
            )

        ])
])

app.layout = serve_layout

@ app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('zaxis-column', 'value'),
    Input('choose_file','value'),]

    )
def update_graph(xaxis_column_name, yaxis_column_name, zaxis_column_name,choose_file):

    df = pd.read_json(default_storage.open(os.path.join('files',choose_file)))

    fig = px.density_heatmap(x=df[xaxis_column_name], y=df[yaxis_column_name], z=df[zaxis_column_name], nbinsx=75, nbinsy=75, marginal_x="histogram", marginal_y="histogram", text_auto=False)

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')


    fig.update_xaxes(title=xaxis_column_name)

    fig.update_yaxes(title=yaxis_column_name)

    return fig


