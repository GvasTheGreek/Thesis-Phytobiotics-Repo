from dash import dcc,  Input, Output
from dash import Dash,html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import plotly.express as px
import pandas as pd
import os
from django.core.files.storage import default_storage

from phytobiotics_v2.settings import MEDIA_ROOT


# Interactive heat plot accompanied by a histogram that is based on the options -- INTERACTIVE
app = DjangoDash('prwto_grafima_dash')

def serve_layout():

    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files"))

    return html.Div([
            html.H4('Interactive heat plot accompanied by a histogram that is based on the options'),      
            html.P("Filter by selection:"),
            html.Div([
            dcc.RangeSlider(
                id='range-slider',
                min=40, max=115, step=0.1,
                marks={0: '40', 115: '115'},
                value=[0, 115]
            ),
            dcc.Dropdown(
                get_file_list(),
                '',
                id='yaxis-column'
            )
            ]),
            dcc.Graph(id="scatter-plot")
        ])

app.layout = serve_layout

@app.callback(
    Output("scatter-plot", "figure"),
    Input("range-slider", "value"),
    Input("yaxis-column", "value"),)
def update_bar_chart(slider_range,yaxis_column_name):
    tips = pd.read_json(default_storage.open(os.path.join('files',yaxis_column_name)))
    low, high = slider_range
    mask = (tips['ambient_noise'] > low) & (tips['ambient_noise'] < high)
    fig = px.scatter(
        tips[mask], x="temperature", y="humidity",
        color="ambient_noise", size='ambient_noise',
        hover_data=['ambient_noise'],
        marginal_x="histogram", marginal_y="rug"
        )
    return fig

