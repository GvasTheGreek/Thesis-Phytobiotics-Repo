from tkinter import Variable
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import plotly.express as px
import pandas as pd
import os
from django.core.files.storage import default_storage


# Interactive heat plot accompanied by a histogram that is based on the options -- INTERACTIVE
app = DjangoDash('SimpleExample3')
app.layout = html.Div([
        html.H4('Interactive heat plot accompanied by a histogram that is based on the options'),
        dcc.Graph(id="scatter-plot"),
        html.P("Filter by selection:"),
        dcc.RangeSlider(
            id='range-slider',
            min=40, max=115, step=0.1,
            marks={0: '40', 115: '115'},
            value=[0, 115]
        ),
    ])


@app.callback(
    Output("scatter-plot", "figure"),
    Input("range-slider", "value"))
def update_bar_chart(slider_range):
    tips = pd.read_json(default_storage.open(os.path.join('files','Sensor_Data_RTH4.json')))
    low, high = slider_range
    mask = (tips['ambient_noise'] > low) & (tips['ambient_noise'] < high)
    fig = px.scatter(
        tips[mask], x="temperature", y="humidity",
        color="ambient_noise", size='ambient_noise',
        hover_data=['ambient_noise'],
        marginal_x="histogram", marginal_y="rug"
    )
    return fig
    


