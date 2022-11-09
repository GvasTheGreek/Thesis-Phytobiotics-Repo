# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from datetime import date

###############################################################     PRE MADE EXAMPLES       #########################################################################


def f1():
    app = Dash(__name__)

    # assume you have a "long-form" data frame
    # see https://plotly.com/python/px-arguments/ for more options
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

    if __name__ == '__main__':
        app.run_server(debug=True)


def f2():
    # Run this app with `python app.py` and
    # visit http://127.0.0.1:8050/ in your web browser.

    app = Dash(__name__)

    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }

    # assume you have a "long-form" data frame
    # see https://plotly.com/python/px-arguments/ for more options
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='Hello Dash',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div(children='Dash: A web application framework for your data.', style={
            'textAlign': 'center',
            'color': colors['text']
        }),

        dcc.Graph(
            id='example-graph-2',
            figure=fig
        )
    ])

    if __name__ == '__main__':
        app.run_server(debug=True)


def f3():

    df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

    def generate_table(dataframe, max_rows=10):
        return html.Table([
            html.Thead(
                html.Tr([html.Th(col) for col in dataframe.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ]) for i in range(min(len(dataframe), max_rows))
            ])
        ])

    app = Dash(__name__)

    app.layout = html.Div([
        html.H4(children='US Agriculture Exports (2011)'),
        generate_table(df)
    ])

    if __name__ == '__main__':
        app.run_server(debug=True)


def f4():
    # Run this app with `python app.py` and
    # visit http://127.0.0.1:8050/ in your web browser.

    app = Dash(__name__)

    df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

    fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                     size="population", color="continent", hover_name="country",
                     log_x=True, size_max=60)

    app.layout = html.Div([
        dcc.Graph(
            id='life-exp-vs-gdp',
            figure=fig
        )
    ])

    if __name__ == '__main__':
        app.run_server(debug=True)


def f5():

    app = Dash(__name__)

    app.layout = html.Div([
        html.H6("Change the value in the text box to see callbacks in action!"),
        html.Div([
            "Input: ",
            dcc.Input(id='my-input', value='initial value', type='text')
        ]),
        html.Br(),
        html.Div(id='my-output'),

    ])

    @app.callback(
        Output(component_id='my-output', component_property='children'),
        Input(component_id='my-input', component_property='value')
    )
    def update_output_div(input_value):
        return f'Output: {input_value}'

    if __name__ == '__main__':
        app.run_server(debug=True)


def f6():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

    app = Dash(__name__)

    app.layout = html.Div([
        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            df['year'].min(),
            df['year'].max(),
            step=None,
            value=df['year'].min(),
            marks={str(year): str(year) for year in df['year'].unique()},
            id='year-slider'
        )
    ])

    @app.callback(
        Output('graph-with-slider', 'figure'),
        Input('year-slider', 'value'))
    def update_figure(selected_year):
        filtered_df = df[df.year == selected_year]

        fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                         size="pop", color="continent", hover_name="country",
                         log_x=True, size_max=55)

        fig.update_layout(transition_duration=500)

        return fig

    if __name__ == '__main__':
        app.run_server(debug=True)


def f7():
    app = Dash(__name__)

    df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

    app.layout = html.Div([
        html.Div([

            html.Div([
                dcc.Dropdown(
                    df['Indicator Name'].unique(),
                    'Fertility rate, total (births per woman)',
                    id='xaxis-column'
                ),
                dcc.RadioItems(
                    ['Linear', 'Log'],
                    'Linear',
                    id='xaxis-type',
                    inline=True
                )
            ], style={'width': '48%', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    df['Indicator Name'].unique(),
                    'Life expectancy at birth, total (years)',
                    id='yaxis-column'
                ),
                dcc.RadioItems(
                    ['Linear', 'Log'],
                    'Linear',
                    id='yaxis-type',
                    inline=True
                )
            ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
        ]),

        dcc.Graph(id='indicator-graphic'),

        dcc.Slider(
            df['Year'].min(),
            df['Year'].max(),
            step=None,
            id='year--slider',
            value=df['Year'].max(),
            marks={str(year): str(year) for year in df['Year'].unique()},

        )
    ])

    @app.callback(
        Output('indicator-graphic', 'figure'),
        Input('xaxis-column', 'value'),
        Input('yaxis-column', 'value'),
        Input('xaxis-type', 'value'),
        Input('yaxis-type', 'value'),
        Input('year--slider', 'value'))
    def update_graph(xaxis_column_name, yaxis_column_name,
                     xaxis_type, yaxis_type,
                     year_value):
        dff = df[df['Year'] == year_value]

        fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                         y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                         hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

        fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

        fig.update_xaxes(title=xaxis_column_name,
                         type='linear' if xaxis_type == 'Linear' else 'log')

        fig.update_yaxes(title=yaxis_column_name,
                         type='linear' if yaxis_type == 'Linear' else 'log')

        return fig

    if __name__ == '__main__':
        app.run_server(debug=True)


def f8():

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout = html.Div([
        dcc.Input(
            id='num-multi',
            type='number',
            value=5
        ),
        html.Table([
            html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
            html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
            html.Tr([html.Td([2, html.Sup('x')]), html.Td(id='twos')]),
            html.Tr([html.Td([3, html.Sup('x')]), html.Td(id='threes')]),
            html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')]),
        ]),
    ])

    @app.callback(
        Output('square', 'children'),
        Output('cube', 'children'),
        Output('twos', 'children'),
        Output('threes', 'children'),
        Output('x^x', 'children'),
        Input('num-multi', 'value'))
    def callback_a(x):
        return x**2, x**3, 2**x, 3**x, x**x

    if __name__ == '__main__':
        app.run_server(debug=True)


def f9():
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = Dash(__name__, external_stylesheets=external_stylesheets)

    all_options = {
        'America': ['New York City', 'San Francisco', 'Cincinnati'],
        'Canada': [u'Montréal', 'Toronto', 'Ottawa']
    }
    app.layout = html.Div([
        dcc.RadioItems(
            list(all_options.keys()),
            'America',
            id='countries-radio',
        ),

        html.Hr(),

        dcc.RadioItems(id='cities-radio'),

        html.Hr(),

        html.Div(id='display-selected-values')
    ])

    @app.callback(
        Output('cities-radio', 'options'),
        Input('countries-radio', 'value'))
    def set_cities_options(selected_country):
        return [{'label': i, 'value': i} for i in all_options[selected_country]]

    @app.callback(
        Output('cities-radio', 'value'),
        Input('cities-radio', 'options'))
    def set_cities_value(available_options):
        return available_options[0]['value']

    @app.callback(
        Output('display-selected-values', 'children'),
        Input('countries-radio', 'value'),
        Input('cities-radio', 'value'))
    def set_display_children(selected_country, selected_city):
        return u'{} is a city in {}'.format(
            selected_city, selected_country,
        )

    if __name__ == '__main__':
        app.run_server(debug=True)


###############################################################          EXAMPLES       ###############################################################################


# Temperature change during Time based on ambient_light  -- STATIC
def f10():
    app = Dash(__name__)
    tips = pd.read_json("Sensor_Data_RTH4.json")

    fig = px.line(tips, x="Timestamp", y="temperature", title='Temperature change during Time based on ambient_light', color="ambient_light", markers=True)
    fig.show()


# Temperature change during Time based on ambient_light  -- STATIC
def f11():
    app = Dash(__name__)

    tips = pd.read_json("Sensor_Data_RTH4.json")

    app.layout = html.Div([
        html.H4('temperature in Time'),
        dcc.Graph(id="graph"),
        dcc.Checklist(
            id="checklist",
            # options=tips["humidity"].unique(),
            value=[],
            inline=True
        ),
    ])

    @app.callback(
        Output("graph", "figure"),
        Input("checklist", "value"))
    def update_line_chart(continents):
        fig = px.line(tips,
                      x="Timestamp", y="temperature", color="NH3", markers=True, title='Temperature change during Time based on ambient_light')
        return fig

    app.run_server(debug=True)


# Θερμοκρασία & Υγρασία & θόρυβος στο χρόνο με διαφορετική εμφάνιση -- STATIC
def f12():

    tips = pd.read_json("Sensor_Data_RTH4.json")

    # Create traces
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=tips["Timestamp"], y=tips["temperature"],
                             mode='lines', line_shape='spline',
                             name='Temp'))
    fig.add_trace(go.Scatter(x=tips["Timestamp"], y=tips["humidity"],
                             mode='lines+markers', line_shape='spline',
                             name='humidity'))
    fig.add_trace(go.Scatter(x=tips["Timestamp"], y=tips["ambient_noise"],
                             mode='markers', name='ambient_noise'))

    fig.update_layout(title='Θερμοκρασία & Υγρασία & θόρυβος στο χρόνο με διαφορετική εμφάνιση')
    fig.show()


# Scatterplot katanomi deigmatwn ws pros humidity & ambient noise based on temperature color -- STATIC
def f13():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    fig = px.scatter(tips, x="humidity", y="ambient_noise", color='temperature', title='Θερμοκρασία σε σχέση με την υγρασία & τον θόρυβο')
    fig.show()


# Heat Map - Scatter based on 2 variables and filtered by the third -- INTERACTIVE
def f14():

    app = Dash(__name__)
    app.layout = html.Div([
        html.H4('Interactive scatter plot with Iris dataset'),
        dcc.Graph(id="scatter-plot"),
        html.P("Filter by petal width:"),
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
        tips = pd.read_json("Sensor_Data_RTH4.json")  # replace with your own data source
        low, high = slider_range
        mask = (tips['ambient_noise'] > low) & (tips['ambient_noise'] < high)
        fig = px.scatter(
            tips[mask], x="temperature", y="humidity",
            color="ambient_noise", size='ambient_noise',
            hover_data=['ambient_noise'])
        return fig

    app.run_server(debug=True)


# Interactive heat plot accompanied by a histogram that is based on the options -- INTERACTIVE
def f15():
    app = Dash(__name__)
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
        tips = pd.read_json("Sensor_Data_RTH4.json")
        low, high = slider_range
        mask = (tips['ambient_noise'] > low) & (tips['ambient_noise'] < high)
        fig = px.scatter(
            tips[mask], x="temperature", y="humidity",
            color="ambient_noise", size='ambient_noise',
            hover_data=['ambient_noise'],
            marginal_x="histogram", marginal_y="rug"
        )
        return fig

    app.run_server(debug=True)


# Bar PLots -- Not so much appealing -- STATIC
def f16():
    tips = pd.read_json("Sensor_Data_RTH4.json")

    df = pd.DataFrame({
        "ambient_noise": tips["ambient_noise"],
        "temperature": tips["temperature"],
        "humidity": tips["humidity"],
        "Timestamp": tips["Timestamp"],
        "ambient_light": tips["ambient_light"],
        "Entity-Name": tips["Entity-Name"]
    })

    #fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    fig = px.bar(df, x='ambient_noise', y='Entity-Name', color="temperature", barmode="group")
    fig.show()


# Interactive heat plot accompanied by a histogram. User determines the input. Slider option is available -- INTERACTIVE
def f17():
    app = Dash(__name__)

    df = pd.read_json("Sensor_Data_RTH4.json")
    df.drop('Timestamp', axis=1, inplace=True)

    my_list = []
    for col in df.columns:
        my_list.append(col)

    app.layout = html.Div([
        html.Div([
            html.H4('Interactive heat plot accompanied by a histogram. User determines the input. Slider option is available'),
            html.Div([
                dcc.Dropdown(
                    my_list,
                    'ambient_noise',
                    id='xaxis-column'
                ),
                dcc.RadioItems(
                    ['Linear', 'Log'],
                    'Linear',
                    id='xaxis-type',
                    inline=True
                )
            ], style={'width': '32%', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    my_list,
                    'temperature',
                    id='yaxis-column'
                ),
                dcc.RadioItems(
                    ['Linear', 'Log'],
                    'Linear',
                    id='yaxis-type',
                    inline=True
                )
            ], style={'width': '32%', 'float': 'right', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    my_list,
                    'temperature',
                    id='zaxis-column'
                ),
                dcc.RadioItems(
                    ['Linear'],
                    'Linear',
                    id='zaxis-type',
                    inline=True
                )
            ], style={'width': '32%', 'float': 'center', 'display': 'inline-block'}),

            html.Div(
                dcc.Graph(id='indicator-graphic')
            )

        ])
    ])

    @app.callback(
        Output('indicator-graphic', 'figure'),
        [Input('xaxis-column', 'value'),
         Input('yaxis-column', 'value'),
         Input('zaxis-column', 'value'),
         Input('xaxis-type', 'value'),
         Input('yaxis-type', 'value')]

    )
    def update_graph(xaxis_column_name, yaxis_column_name, zaxis_column_name,
                     xaxis_type, yaxis_type):

        fig = px.scatter(x=df[xaxis_column_name],
                         y=df[yaxis_column_name],
                         hover_name=df[yaxis_column_name], color=df[zaxis_column_name], marginal_x="histogram")

        fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest', xaxis=dict(rangeslider=dict(visible=True)))

        fig.update_xaxes(title=xaxis_column_name,
                         type='linear' if xaxis_type == 'Linear' else 'log')

        fig.update_yaxes(title=yaxis_column_name,
                         type='linear' if yaxis_type == 'Linear' else 'log')

        return fig

    if __name__ == '__main__':
        app.run_server(debug=True)


#  Scatter Plot With User Option For Input -- Interactive
def f18():
    app = Dash(__name__)

    tips = pd.read_json("Sensor_Data_RTH4.json")
    df = pd.read_json("Sensor_Data_RTH4.json")
    #df.drop('Timestamp', axis=1, inplace=True)
    df.drop('Entity-Name', axis=1, inplace=True)

    my_list = []
    for col in df.columns:
        my_list.append(col)

    print(df[my_list[0]].min())

    app.layout = html.Div([
        html.Div([

            html.Div([
                dcc.Dropdown(
                    my_list,
                    'CO2',
                    id='xaxis-column'
                ),
                dcc.RadioItems(
                    ['Linear', 'Log'],
                    'Linear',
                    id='xaxis-type',
                    inline=True
                )
            ], style={'width': '48%', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    my_list,
                    'temperature',
                    id='yaxis-column'
                ),
                dcc.RadioItems(
                    ['Linear', 'Log'],
                    'Linear',
                    id='yaxis-type',
                    inline=True
                )
            ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
        ]),

        dcc.Graph(id='indicator-graphic'),

    ])

    @ app.callback(
        Output('indicator-graphic', 'figure'),
        Input('xaxis-column', 'value'),
        Input('yaxis-column', 'value'),
        Input('xaxis-type', 'value'),
        Input('yaxis-type', 'value'),
        #Input('year--slider', 'start_date'),
        #Input('year--slider', 'end_date')
    )
    def update_graph(xaxis_column_name, yaxis_column_name,
                     xaxis_type, yaxis_type,  # start_date,
                     # end_date
                     ):

        fig = px.scatter(x=df[xaxis_column_name],
                         y=df[yaxis_column_name],
                         hover_name=tips["Timestamp"], color=df[yaxis_column_name])

        fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

        fig.update_xaxes(title=xaxis_column_name,
                         #type='linear' if xaxis_type == 'Linear' else 'log'
                         )

        fig.update_yaxes(title=yaxis_column_name,
                         type='linear' if yaxis_type == 'Linear' else 'log')

        return fig

    if __name__ == '__main__':
        app.run_server(debug=True)


def f19():
    app = Dash(__name__)

    tips = pd.read_json("Sensor_Data_RTH4.json")
    df = pd.read_json("Sensor_Data_RTH4.json")
    df.drop('Entity-Name', axis=1, inplace=True)

    my_list = []
    for col in df.columns:
        my_list.append(col)

    app.layout = html.Div([


        html.Div([
            dcc.Dropdown(
                my_list,
                'temperature',
                id='yaxis-column'
            ),
            dcc.RadioItems(
                ['Linear', 'Log'],
                'Linear',
                id='yaxis-type',
                inline=True
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

        dcc.Graph(id='indicator-graphic'),

    ])

    @ app.callback(
        Output('indicator-graphic', 'figure'),
        Input('yaxis-column', 'value'),
        Input('yaxis-type', 'value'),
    )
    def update_graph(yaxis_column_name, yaxis_type):

        fig = px.scatter(x=df["Timestamp"],
                         y=df[yaxis_column_name],
                         hover_name=tips["Timestamp"], color=df[yaxis_column_name])

        fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

        fig.update_xaxes(title="Timestamp")

        fig.update_yaxes(title=yaxis_column_name,
                         type='linear' if yaxis_type == 'Linear' else 'log')

        return fig

    if __name__ == '__main__':
        app.run_server(debug=True)


def f20():
    app = Dash(__name__)

    df = pd.read_json("Sensor_Data_RTH4.json")

    tips = pd.read_json("Sensor_Data_RTH4.json")
    df = pd.read_json("Sensor_Data_RTH4.json")
    #df.drop('Timestamp', axis=1, inplace=True)
    df.drop('Entity-Name', axis=1, inplace=True)

    my_list = []
    for col in df.columns:
        my_list.append(col)

    print(df[my_list[0]].min())

    app.layout = html.Div([
        html.Div([

            html.Div([
                dcc.Dropdown(
                    my_list,
                    'CO2',
                    id='xaxis-column'
                ),
                dcc.RadioItems(
                    ['Linear', 'Log'],
                    'Linear',
                    id='xaxis-type',
                    inline=True
                )
            ], style={'width': '48%', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    my_list,
                    'temperature',
                    id='yaxis-column'
                ),
                dcc.RadioItems(
                    ['Linear', 'Log'],
                    'Linear',
                    id='yaxis-type',
                    inline=True
                )
            ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
        ]),

        dcc.Graph(id='indicator-graphic'),

    ])

    @ app.callback(
        Output('indicator-graphic', 'figure'),
        Input('xaxis-column', 'value'),
        Input('yaxis-column', 'value'),
        Input('xaxis-type', 'value'),
        Input('yaxis-type', 'value'),
        #Input('year--slider', 'start_date'),
        #Input('year--slider', 'end_date')
    )
    def update_graph(xaxis_column_name, yaxis_column_name,
                     xaxis_type, yaxis_type,  # start_date,
                     # end_date
                     ):

        fig = px.density_heatmap(x=df[xaxis_column_name], y=df[yaxis_column_name], z=df[yaxis_column_name], nbinsx=75, nbinsy=75, marginal_x="histogram", marginal_y="histogram", text_auto=True)

        fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

        fig.update_xaxes(title=xaxis_column_name,
                         #type='linear' if xaxis_type == 'Linear' else 'log'
                         )

        fig.update_yaxes(title=yaxis_column_name,
                         type='linear' if yaxis_type == 'Linear' else 'log')

        fig.update_

        return fig

    if __name__ == '__main__':
        app.run_server(debug=True)
