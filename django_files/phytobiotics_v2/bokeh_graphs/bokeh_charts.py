import pandas as pd
from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter, ColorBar, ColumnDataSource, LinearColorMapper, PrintfTickFormatter, BasicTicker
from bokeh.models import Div, RangeSlider, Spinner, DateRangeSlider, Slider, CustomJS, Dropdown,HoverTool ,FileInput,Select
from bokeh.plotting import figure, show, output_file,curdoc
from bokeh.embed import components
from bokeh.layouts import layout,row , column
from django.shortcuts import render
import os
from django.core.files.storage import default_storage
from phytobiotics_v2.settings import MEDIA_ROOT
from bokeh.transform import linear_cmap, transform,dodge



def f5():
    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))
        
    def get_columns():
        files_list = []
        #columns_list = []
        for col in get_file_list():
            files_list.append(col)
        return files_list[0]
    
    
    tips = pd.read_json(default_storage.open(os.path.join('files_bokeh', get_columns())))
    x = tips["Timestamp"]
    y = tips["humidity"]

    colors = [(255, int(round(value * 255 / 100)), 0) for value in y]

    tips.drop('ambient_noise', axis=1, inplace=True)
    tips.drop('temperature', axis=1, inplace=True)
    tips.drop('Entity-Name', axis=1, inplace=True)
    tips.drop('CO2', axis=1, inplace=True)
    tips.drop('ambient_light', axis=1, inplace=True)
    tips.drop('NH3', axis=1, inplace=True)

    source = ColumnDataSource(data = dict(
        x = tips["Timestamp"],
        y = tips["humidity"],
        colors = colors
                ))

      

    # create a new plot with a specific size
    
    p = figure(
        title="heatmap υγρασίας στο χρόνο. Το χρώμα αλλάζει ανάλογα με την τιμή.",
        sizing_mode="stretch_width",
        max_width=1500,
        height=750,
        x_axis_label="Timestamp", y_axis_label="humidity",
        output_backend="webgl"
    )

    # add circle renderer
    p.circle('x' , 'y' , 
        fill_color ='colors',
        fill_alpha=2,
        line_color="lightgrey",
        size=10,
        legend_label="humidity",
        source = source)
    p.xaxis[0].formatter = DatetimeTickFormatter(days="%Y %m/%d %H:%M",
                                                 months="%Y %m/%d %H:%M",
                                                 hours="%Y %m/%d %H:%M",
                                                 minutes="%Y %m/%d %H:%M")

    p.add_tools(HoverTool(tooltips = [('x','@x{%Y-%m-%d %H:%M:%S}'),('y','$y'),("Sample", "$index")],
            formatters={'@x':'datetime'},))

    # show the results
    script, div = components(p)
    return script,div

def f4b():
    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))
        
    def get_columns():
        files_list = []
        #columns_list = []
        for col in get_file_list():
            files_list.append(col)
        return files_list[0]

    tips = pd.read_json(default_storage.open(os.path.join('files_bokeh', get_columns())))
    x = tips["temperature"]
    y1 = tips["humidity"]
    y2 = tips["ambient_noise"]

    tips.drop('Timestamp', axis=1, inplace=True)
    tips.drop('Entity-Name', axis=1, inplace=True)
    tips.drop('CO2', axis=1, inplace=True)
    tips.drop('ambient_light', axis=1, inplace=True)
    tips.drop('NH3', axis=1, inplace=True)

    source = ColumnDataSource(data = dict(
        x = tips["temperature"],
        y1 = tips["humidity"],
                ))

    p = figure(x_range=(5, 35), y_range=(0, 125), height=750, title="H υγρασία στις τιμές της θερμοκρασίας me κύκλους στις τιμές",
               sizing_mode="stretch_width",output_backend="webgl")

    p.vbar(x=dodge("x", -0.0, range=p.x_range), top="y1", width=0.01, source=source,
           color="red", legend_label="Humidity")

    p.circle('x', 'y1', fill_color="blue", legend_label="Humidity_value", size=5,source=source)

    p.xgrid.grid_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"

    p.add_tools(HoverTool(tooltips = [('x','@x{0.00}'),('y1','@y1{0.00}')],
            formatters={'@x':'numeral','@y1':'numeral'},))

    script, div = components(p)
    return script,div

def f7():
    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))
        
    def get_columns():
        files_list = []
        #columns_list = []
        for col in get_file_list():
            files_list.append(col)
        return files_list[0]

    tips = pd.read_json(default_storage.open(os.path.join('files_bokeh', get_columns())))
    x = tips["humidity"]
    y = tips["temperature"]
    z = tips["ambient_noise"]

    x = x * 1
    y = y * 1
    z = z * 1

    # generate radii and colors based on data
    radii = y / 100 * 2
    colors = ["#%02x%02x%02x" % (255, int(round(value * 255)), 255) for value in z]


    source = ColumnDataSource(data = dict(
        x = tips["humidity"],
        y = tips["temperature"],
        z = tips["ambient_noise"],
        colors = colors,
        radii = radii
        ))

    # create a new plot with a specific size
    p = figure(
        title="HeatMap υγρασίας & θερμοκρασίας με παράγοντα τον θόρυβο στο χρώμα",
        sizing_mode="stretch_width",
        max_width=1500,
        height=1500,
        x_axis_label="humidity", y_axis_label="temperature",
        output_backend="webgl"
    )

    # add circle renderer
    p.circle(
        'x',
        'y',
        radius='radii',
        fill_color='colors',
        fill_alpha=0.6,
        line_color="lightgrey",
        source = source
    )

    p.add_tools(HoverTool(tooltips = [('x','@x{0.00}'),('y','@y{0.00}'),('z','@z{0.00}')],
            formatters={'@x':'numeral','@y':'numeral','@z':'numeral'},))

    # show the results
    script, div = components(p)
    return script,div


def f7d():
    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))
        
    def get_columns():
        files_list = []
        #columns_list = []
        for col in get_file_list():
            files_list.append(col)

        """
        if len(get_file_list()) == 0:
            return 'Insert File'
        else:
            var = pd.read_json(default_storage.open(os.path.join('files',files_list[0])))
            var.drop('Entity-Name', axis=1, inplace=True)
            for i in var.columns:
                columns_list.append(i)
    
            return columns_list
        """
        return files_list[0]
    
    #TOOLS = "box_select,lasso_select,help"
    
    tips = pd.read_json(default_storage.open(os.path.join('files_bokeh', get_columns()),'r'))
    x = tips["Timestamp"]
    y1 = tips["temperature"]
    y2 = tips["humidity"]
    y3 = tips["ambient_noise"]

    source = ColumnDataSource(data = dict(
        x = tips["Timestamp"],
        y1 = tips["temperature"],
        y2 = tips["humidity"],
        y3 = tips["ambient_noise"],
        ))

    
    

    # create three plots
    # S1
    s1 = figure(width=1750, height=350, background_fill_color="#fafafa",output_backend="webgl", tools = "box_select,lasso_select,help")
    s1.line('x', 'y1', legend_label="Temperature", color="blue", line_width=2,source = source)
    s1.circle('x', 'y1',legend_label="Temperature", size=3, color="#53777a", alpha=0.8,source=source)
    s1.xaxis[0].formatter = DatetimeTickFormatter(days="%Y %m/%d %H:%M",months="%Y %m/%d %H:%M",hours="%Y %m/%d %H:%M",minutes="%Y %m/%d %H:%M")

    s1.add_tools(HoverTool(tooltips = [('x','@x{%Y-%m-%d %H:%M:%S}'),('y1','@y1{0.00}')],
            formatters={'@x':'datetime','@y1':'numeral'},))

    # S2
    s2 = figure(width=1750, height=350, background_fill_color="#fafafa",output_backend="webgl",x_range = s1.x_range,tools = "box_select,lasso_select,help")
    s2.line('x', 'y2', legend_label="Humidity", color="red", line_width=2,source = source)
    s2.circle('x', 'y2',legend_label="Humidity", size=3, color="#c02942", alpha=0.8,source=source)
    s2.xaxis[0].formatter = DatetimeTickFormatter(days="%Y %m/%d %H:%M",months="%Y %m/%d %H:%M",hours="%Y %m/%d %H:%M",minutes="%Y %m/%d %H:%M")

    s2.add_tools(HoverTool(tooltips = [('x','@x{%Y-%m-%d %H:%M:%S}'),('y2','@y2{0.00}')],
            formatters={'@x':'datetime','@y2':'numeral'},))

    # S3
    s3 = figure(width=1750, height=350, background_fill_color="#fafafa",output_backend="webgl", x_range= s1.x_range, tools = "box_select,lasso_select,help")
    s3.line('x', 'y3', legend_label="Ambient_noise", color="green", line_width=2,source = source)
    s3.circle('x', 'y3', legend_label="Ambient_noise",size=3, color="#d95b43", alpha=0.8,source=source)
    s3.xaxis[0].formatter = DatetimeTickFormatter(days="%Y %m/%d %H:%M",months="%Y %m/%d %H:%M",hours="%Y %m/%d %H:%M",minutes="%Y %m/%d %H:%M")

    s3.add_tools(HoverTool(tooltips = [('x','@x{%Y-%m-%d %H:%M:%S}'),('y3','@y3{0.00}')],
            formatters={'@x':'datetime','@y3':'numeral'},))

    range_slider = DateRangeSlider(
        title="Adjust x-axis range",  # a title to display above the slider
        start=x[0],  # set the minimum value for the slider
        end=x[len(x)-1],  # set the maximum value for the slider
        step=1,  # increments for the slider
        value=(x[0], x[len(x)-1]),  # initial values for slider
    )

    range_slider.js_link("value", s1.x_range, "start", attr_selector=0)
    range_slider.js_link("value", s1.x_range, "end", attr_selector=1)

    
    tlayout = layout([
        [range_slider],
        [column(s1,s2,s3)],
        ])
    
    script, div = components(tlayout)
    return script,div



# Multiple Interactive Line Plots With intercative circles that represent the sample's values taken.
def f6b():
    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))
        
    def get_columns():
        files_list = []
        #columns_list = []
        for col in get_file_list():
            files_list.append(col)

        return files_list[0]

    tips = pd.read_json(default_storage.open(os.path.join('files', get_columns()),'r'))
    x = tips["Timestamp"]

    source = ColumnDataSource(data = dict(
        x = tips["Timestamp"],
        y1 = tips["temperature"],
        y2 = tips["humidity"],
        y3 = tips["ambient_noise"],
        ))

    # create a new plot with a title and axis labels
    p = figure(title="Multiple Interactive Line Plots With intercative circles that represent the sample's values taken.", x_axis_label="Timestamp", 
                y_axis_label="Temperature & Humidity & Ambient_noise",
               width=1250, height=750, output_backend="webgl")

    # add multiple renderers
    p.line('x', 'y1', legend_label="Temperature", color="blue", line_width=2,source = source)
    p.line('x', 'y2', legend_label="Humidity", color="red", line_width=2,source = source)
    p.line('x', 'y3', legend_label="Ambient_noise", color="green", line_width=2,source = source)

    points1 = p.circle('x', 'y1', fill_color="yellow", fill_alpha=2, size=2, legend_label="Temperature Circle 1",source = source)
    points2 = p.circle('x', 'y2', fill_color="yellow", fill_alpha=2, size=2, legend_label="Humidity Circle 2",source = source)
    points3 = p.circle('x', 'y3', fill_color="orange", fill_alpha=2, size=2, legend_label="Ambient_noise Circle 3",source = source)

    p.xaxis[0].formatter = DatetimeTickFormatter(days="%Y %m/%d %H:%M",
                                                 months="%Y %m/%d %H:%M",
                                                 hours="%Y %m/%d %H:%M",
                                                 minutes="%Y %m/%d %H:%M")

    p.add_tools(HoverTool(tooltips = [('x','@x{%Y-%m-%d %H:%M:%S}'),('y1','@y1{0.00}'),('y2','@y2{0.00}'),('y3','@y3{0.00}')],
            formatters={'@x':'datetime','@y1':'numeral','@y2':'numeral','@y3':'numeral'},))

    div = Div(
        text="""
        <p>Select the circle's size using this control element:</p>
        """,
        width=250,
        height=10,
    )

    spinner1 = Spinner(
        title="Circle1 size",  # a string to display above the widget
        low=0,  # the lowest possible number to pick
        high=60,  # the highest possible number to pick
        step=1,  # the increments by which the number can be adjusted
        value=points1.glyph.size,  # the initial value to display in the widget
        width=200,  # the width of the widget in pixels
    )
    spinner1.js_link("value", points1.glyph, "size")
    spinner2 = Spinner(
        title="Circle2 size",  # a string to display above the widget
        low=0,  # the lowest possible number to pick
        high=60,  # the highest possible number to pick
        step=1,  # the increments by which the number can be adjusted
        value=points2.glyph.size,  # the initial value to display in the widget
        width=200,  # the width of the widget in pixels
    )
    spinner2.js_link("value", points2.glyph, "size")
    spinner3 = Spinner(
        title="Circle3 size",  # a string to display above the widget
        low=0,  # the lowest possible number to pick
        high=60,  # the highest possible number to pick
        step=1,  # the increments by which the number can be adjusted
        value=points3.glyph.size,  # the initial value to display in the widget
        width=200,  # the width of the widget in pixels
    )
    spinner3.js_link("value", points3.glyph, "size")

    range_slider1 = DateRangeSlider(
        title="Adjust x-axis range",  # a title to display above the slider
        start=x[0],  # set the minimum value for the slider
        end=x[len(x)-1],  # set the maximum value for the slider
        step=1,  # increments for the slider
        value=(x[0], x[len(x)-1]),  # initial values for slider
    )

    range_slider1.js_link("value", p.x_range, "start", attr_selector=0)
    range_slider1.js_link("value", p.x_range, "end", attr_selector=1)

    range_slider2 = RangeSlider(
        title="Adjust y-axis range",  # a title to display above the slider
        start=0,  # set the minimum value for the slider
        end=120,  # set the maximum value for the slider
        step=0.1,  # increments for the slider
        value=(0, 120),  # initial values for slider
    )

    range_slider2.js_link("value", p.y_range, "start", attr_selector=0)
    range_slider2.js_link("value", p.y_range, "end", attr_selector=1)

    tlayout = layout([
        [p],
        [div, spinner1, spinner2, spinner3],
        [range_slider1, range_slider2],
    ])

    p.legend.title = "Observations"
    p.legend.label_text_font = "times"
    p.legend.label_text_font_style = "italic"
    p.legend.label_text_color = "navy"
    p.legend.click_policy="hide"

    script, div = components(tlayout)
    return script,div