from dash import dcc, html, Input, Output, Dash
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import plotly.express as px
import pandas as pd
import os
from django.core.files.storage import default_storage
from phytobiotics_v2.settings import MEDIA_ROOT


app = DjangoDash('pempto_grafima_dash')

# Temperature change during Time based on ambient_light  -- STATIC
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
            for i in var.columns:
                columns_list.append(i)
    
            return columns_list



    return html.Div([
        html.Div([
            html.H4('temperature in Time'),
            html.H4('Temperature change during Time based on ambient_light'),
            html.Div([
            dcc.Dropdown(
                get_file_list(),
                '',
                id='choose_file'
            )
            ]),
            html.Div([
                html.P("Filter by z-axis:"),
                dcc.Dropdown(
                    get_columns(),
                    'ambient_noise',
                    id='zaxis_column'
                )
            ],  style={'width': '32%', 'float': 'right' ,'display': 'inline-block'}),

            html.Div([
                html.P("Filter by y-axis:"),
                dcc.Dropdown(
                    get_columns(),
                    'temperature',
                    id='yaxis_column'
                )
            ],  style={'width': '32%',  'display': 'inline-block'}),

            html.Div([
                dcc.Graph(id="graph"),
            ])
    ])
])


app.layout = serve_layout

@app.callback(
    Output("graph", "figure"),
    [Input("yaxis_column","value"),
    Input("zaxis_column","value"),
    Input("choose_file",'value'),
    #Input("checklist", "value"),
    ]
    )

def update_line_chart(yaxis_column_name,zaxis_column_name,choose_file):

    df = pd.read_json(default_storage.open(os.path.join('files',choose_file)))



    fig = px.line(x=df["Timestamp"], y=df[yaxis_column_name], color=df[zaxis_column_name], markers=True)

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title = "Timestamp")
    fig.update_yaxes(title=yaxis_column_name)


    return fig

    