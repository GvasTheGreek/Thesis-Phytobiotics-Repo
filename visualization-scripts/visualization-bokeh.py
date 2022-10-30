import pandas as pd
import numpy as np
import xyzservices.providers as xyz
from bokeh.plotting import figure, show, output_file
from bokeh.io import curdoc
from datetime import datetime, timedelta
from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter, ColorBar, ColumnDataSource, LinearColorMapper, PrintfTickFormatter, BasicTicker
from bokeh.models import Div, RangeSlider, Spinner, DateRangeSlider, Slider, CustomJS, Dropdown,HoverTool
from bokeh.layouts import layout,row , column
from bokeh.transform import linear_cmap, transform,dodge
from bokeh.util.hex import hexbin
from bokeh.transform import jitter
from bokeh.tile_providers import get_provider


#################################################################      STATIC GRAPHS       ##############################################################################
#################################################################       LINE PLOTS         ##############################################################################


# Basic line -- Temperature during Time
def f1():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    x = tips["Timestamp"]
    y = tips["temperature"]

    p = figure(title="Η θερμοκρασία στο χρόνο", x_axis_label="Timestamp", y_axis_label="temperature", output_backend="webgl")
    p.line(x, y, legend_label="Temp.", line_width=2)
    p.xaxis[0].formatter = DatetimeTickFormatter(days="%Y %m/%d %H:%M",
                                                 months="%Y %m/%d %H:%M",
                                                 hours="%Y %m/%d %H:%M",
                                                 minutes="%Y %m/%d %H:%M")
    show(p)
#f1()


# Multiple Lines on the same figure --- Not for the thesis
def f2():
    x = [1, 2, 3, 4, 5]
    y1 = [6, 7, 2, 4, 5]
    y2 = [2, 3, 4, 5, 6]
    y3 = [4, 5, 5, 7, 2]

    # create a new plot with a title and axis labels
    p = figure(title="Multiple line example", x_axis_label="x", y_axis_label="y", width=1000, height=450, output_backend="webgl")

    # add multiple renderers
    p.line(x, y1, legend_label="Temp.", color="blue", line_width=2)
    p.line(x, y2, legend_label="Rate", color="red", line_width=2)
    p.line(x, y3, legend_label="Objects", color="green", line_width=2)

    # show the results
    show(p)
# f2()


# Multiple Lines on the same figure --- Temp , humidity, ambient noise
def f2a():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    tips2 = pd.read_json("Sensor_Data_RTH4.json")
    x = tips["Timestamp"]
    y1 = tips["temperature"]
    y2 = tips["humidity"]
    y3 = tips["ambient_noise"]

    tips.drop('Entity-Name', axis=1, inplace=True)
    tips.drop('CO2', axis=1, inplace=True)
    tips.drop('ambient_light', axis=1, inplace=True)
    tips.drop('NH3', axis=1, inplace=True)

    source = ColumnDataSource(data = dict(x = tips["Timestamp"] ,y1 = tips["temperature"],y2=tips["humidity"],y3=tips["ambient_noise"]))
 

    # create a new plot with a title and axis labels
    p = figure(title="θερμοκρασία-Υγρασία-Θόρυβος Περιβάλλοντος στο χρόνο",
               x_axis_label="Timestamp", y_axis_label="Temperature & Humidity & Ambient_noise", width=1000, height=450, output_backend="webgl" )

    # add multiple renderers
    p.line('x', 'y1', legend_label="Temperature", color="blue", line_width=2, source=source)
    p.line('x', 'y2', legend_label="Humidity", color="red", line_width=2, source=source)
    p.line('x', 'y3', legend_label="Ambient_noise", color="green", line_width=2, source=source)
    p.xaxis[0].formatter = DatetimeTickFormatter(days="%Y %m/%d %H:%M",
                                                 months="%Y %m/%d %H:%M",
                                                 hours="%Y %m/%d %H:%M",
                                                 minutes="%Y %m/%d %H:%M")
    p.legend.title = "Obervations"
    p.legend.label_text_font = "times"
    p.legend.label_text_font_style = "italic"
    p.legend.label_text_color = "navy"

    p.add_tools(HoverTool(tooltips = [('x','@x{%Y-%m-%d %H:%M:%S}'),('y1','@y1{0.00}'),("y2", "@y2{0.00}"),("y3", "@y3{0.00}")],
            formatters={'@x':'datetime',"y1": "numeral","y2": "numeral","y3": "numeral"},))

    show(p)
#f2a()

def f5():
    tips = pd.read_json("Sensor_Data_RTH4.json")
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
    show(p)
#f5()



# Basic Line Plot -- Η θερμοσκρασία στο χρόνο με κυκλους στα σημεία των δειγμάτων.
# Ο κύκλος είναι στατικός σε αυτό το παράδειγμα.
def f3():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    x = tips["Timestamp"]
    y = tips["temperature"]

    colors = ["#%02x%02x%02x" % (255, int(round(value * 255 / 100)), 255) for value in y]

    source = ColumnDataSource(data = dict(
        x = tips["Timestamp"],
        y = tips["temperature"],
        colors = colors
                ))

    p = figure(
        title="Η θερμοσκρασία στο χρόνο με κυκλους στα σημεία των δειγμάτων",
        sizing_mode="stretch_width",
        max_width=1500,
        height=1250,
        x_axis_label="Timestamp", y_axis_label="temperature", output_backend="webgl")

    line = p.line('x', 'y', line_color="blue", line_width=1,source = source)
    circle = p.circle('x', 'y', fill_color='colors', line_color="blue", size=15,source= source)
    p.xaxis[0].formatter = DatetimeTickFormatter(days="%Y %m/%d %H:%M",
                                                 months="%Y %m/%d %H:%M",
                                                 hours="%Y %m/%d %H:%M",
                                                 minutes="%Y %m/%d %H:%M")
    curdoc().theme = 'light_minimal'
    p.add_tools(HoverTool(tooltips = [('x','@x{%Y-%m-%d %H:%M:%S}'),('y','$y'),("Sample", "$index")],
            formatters={'@x':'datetime'},))

    show(p)
#f3()


#################################################################      BAR PLOTS          ##############################################################################


# Vertical Bars --- H υγρασία στην θερμοκρασία!
def f4():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    x = tips["temperature"]
    y = tips["humidity"]
    curdoc().theme = "dark_minimal"

    tips.drop('ambient_noise', axis=1, inplace=True)
    tips.drop('Timestamp', axis=1, inplace=True)
    tips.drop('Entity-Name', axis=1, inplace=True)
    tips.drop('CO2', axis=1, inplace=True)
    tips.drop('ambient_light', axis=1, inplace=True)
    tips.drop('NH3', axis=1, inplace=True)    

    source = ColumnDataSource(data = dict(
        x = tips["temperature"],
        y = tips["humidity"]
                ))

    p = figure(title="H υγρασία στην θερμοκρασία", x_axis_label="temperature", y_axis_label="humidity", sizing_mode="stretch_width", output_backend="webgl")
    p.toolbar.autohide = True
    p.vbar('x', top='y', legend_label="Temp by humidity", width=0.01, bottom=0, color="red",source=source)

    p.add_tools(HoverTool(tooltips = [('x','@x{0.00}'),('y','@y{0.00}'),("Sample", "$index")],
            formatters={'@x':'numeral','@y':'numeral'},))

    show(p)
#f4()


# Vertical Bar -- H υγρασία και ο θόρυβος στις τιμές της θερμοκρασίας
def f4a():
    tips = pd.read_json("Sensor_Data_RTH4.json")
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
        y2 = tips["ambient_noise"]
                ))

    p = figure(x_range=(5, 35), y_range=(0, 125), height=750, title="H υγρασία και ο θόρυβος στις τιμές της θερμοκρασίας",
                sizing_mode="stretch_width", output_backend="webgl")

    p.vbar(x=dodge("x", -0.25, range=p.x_range), top="y1", width=0.01, source=source,
           color="red", legend_label="Humidity")

    p.vbar(x=dodge("x", 0.0, range=p.x_range), top="y2", width=0.01, source=source,
           color="blue", legend_label="Ambient_noise")

    p.xgrid.grid_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"
    curdoc().theme = "light_minimal"

    p.add_tools(HoverTool(tooltips = [('x','@x{0.00}'),('y1','@y1{0.00}'),("y2", "@y2{0.00}")],
            formatters={'@x':'numeral','@y1':'numeral','@y2':'numeral'},))

    show(p)
#f4a()


# Vertical Bar & Circle -- H υγρασία στις τιμές της θερμοκρασίας me κύκλους στα values
def f4b():
    tips = pd.read_json("Sensor_Data_RTH4.json")
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

    show(p)
#f4b()


# Side bar With Circles -- -Mas deixnei tis times tou NH3 με βάση την θερμοκρασία!
def f4c():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    y = tips["temperature"]
    x = tips["NH3"]

    p = figure(title="Οι τιμές του NH3 και της θερμοκρασίας των δειγμάτων", toolbar_location="right",
               y_range=(0, 35), width=1000, output_backend="webgl")

    p.segment(0, y, x, y, line_width=2, line_color="green", )
    p.circle(x, y, size=10, fill_color="orange", line_color="green", line_width=3, )

    show(p)
#f4c()


################################################################      SCATTER - HEAT PLOTS          #####################################################################


# ScatterPlot - HeatMap of humidty scatter in time. Moreover the color of the dot is based on the density
def f5():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    x = tips["Timestamp"]
    y = tips["humidity"]

    colors = [(255, int(round(value * 255 / 100)), 0) for value in y]

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
        height=1250,
        x_axis_label="Timestamp", y_axis_label="humidity",
        output_backend="webgl"
    )

    # add circle renderer
    p.circle(
        'x',
        'y',
        fill_color='colors',
        fill_alpha=2,
        line_color="lightgrey",
        size=10,
        legend_label="humidity",
        source = source
    )
    p.xaxis[0].formatter = DatetimeTickFormatter(days="%Y %m/%d %H:%M",
                                                 months="%Y %m/%d %H:%M",
                                                 hours="%Y %m/%d %H:%M",
                                                 minutes="%Y %m/%d %H:%M")

    p.add_tools(HoverTool(tooltips = [('x','@x{%Y-%m-%d %H:%M:%S}'),('y','@y{0.00}')],
            formatters={'@x':'datetime','@y':'numeral'},))

    # show the results
    show(p)
#f5()


# Scatterplot - HeatMap -- Η διαφορά εδώ είναι ότι μπαίνει τριτη μεταβλητή
# και με βάση τη συσχέτιση μικραίνει ή μεγαλώνει.
def f7():
    tips = pd.read_json("Sensor_Data_RTH4.json")
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
    show(p)
#f7()


# Eksagwna μια διαφορετική προσέγγιση του heatmap
def f8():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    x = tips["humidity"]
    y = tips["temperature"]
    z = tips["ambient_noise"]


    bins = hexbin(x, y, 1)

    p = figure(tools="wheel_zoom,reset", match_aspect=True, background_fill_color='#440154', x_axis_label="humidity", y_axis_label="temperature",
               output_backend="webgl", title="heatMap Εξαγώνων")
    p.grid.visible = False

    p.hex_tile(q="q", r="r", size=0.1, line_color=None, source=bins,
               fill_color=linear_cmap('counts', 'Viridis256', 0, max(bins.counts)))

    show(p)
#f8()


# I pio sintheti version tou HeatMap - Scatterplot
# H leitourgia apaitei να χαλάσω τα δεδομένα τύπου string γιατί δεν μπορεί να τα κάνει dataframe
def f9():

    tips = pd.read_json("Sensor_Data_RTH4.json")
    x = tips["humidity"]
    y = tips["temperature"]
    z = tips["ambient_noise"]

    tips.drop('Timestamp', axis=1, inplace=True)
    tips.drop('Entity-Name', axis=1, inplace=True)
    tips.drop('CO2', axis=1, inplace=True)
    tips.drop('ambient_light', axis=1, inplace=True)
    tips.drop('NH3', axis=1, inplace=True)

    result = []
    result = find_min_max("Sensor_Data_RTH4.json", x, y)

    # this is the colormap from the original NYTimes plot
    colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
    mapper = LinearColorMapper(palette=colors, low=tips.ambient_noise.min(), high=tips.ambient_noise.max())

    source = ColumnDataSource(data = dict(
        x = tips["humidity"],
        y = tips["temperature"],
        z = tips["ambient_noise"],
        ))

    p = figure(width=1500, height=1000, title="Περιβαντολλογικός Θόρυβος σε σύγκριση με την θερμοκρασία & υγρασία",
               x_range=(result[0] - 1, result[1] + 1), y_range=(result[2] - 1, result[3] + 1),
               toolbar_location=None, tools="", x_axis_label="humidity", y_axis_label="temperature", output_backend="webgl")

    p.rect(x="x", y="y", width=0.5, height=0.5, source=source,
           line_color=None, fill_color=transform('z', mapper))

    # p.circle(x="humidity", y="temperature", source=source,
    # line_color=None, fill_color=transform('ambient_noise', mapper))

    color_bar = ColorBar(color_mapper=mapper,
                         ticker=BasicTicker(desired_num_ticks=len(colors)),
                         formatter=PrintfTickFormatter(format="%d%%"))

    p.add_layout(color_bar, 'right')

    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font_size = "7px"
    p.axis.major_label_standoff = 0
    p.xaxis.major_label_orientation = 1.0

    p.add_tools(HoverTool(tooltips = [('x','@x{0.00}'),('y','@y{0.00}')],
            formatters={'@x':'numeral','@y':'numeral'},))

    show(p)


def find_min_max(var1, var2, var3):

    tips = pd.read_json(var1)
    min_val = var2[0]
    max_val = var2[0]

    min_v = var3[0]
    max_v = var3[0]

    for i in range(len(tips)):
        if min_val > var2[i]:
            min_val = var2[i]
        elif max_val < var2[i]:
            max_val = var2[i]
        else:
            pass

    for i in range(len(tips)):
        if min_v > var3[i]:
            min_v = var3[i]
        elif max_v < var3[i]:
            max_v = var3[i]
        else:
            pass

    return min_val, max_val, min_v, max_v


#f9()


#################################################################      INTERACTIVE GRAPHS       #########################################################################
#################################################################          LINE PLOTS           #########################################################################


# Line Plot ---- Interactive with Time and circle variations
def f6():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    x = tips["Timestamp"]
    y = tips["temperature"]
    curdoc().theme = "dark_minimal"
    colors = ["#%02x%02x%02x" % (255, int(round(value * 255 / 100)), 255) for value in y]

    source = ColumnDataSource(data = dict(
        x = tips["Timestamp"],
        y = tips["temperature"],
        colors = colors,
        ))

    p = figure(title="Η θερμοκρασία στο χρόνο", sizing_mode="stretch_width", max_width=1750, height=1050,
               x_axis_label="Timestamp", y_axis_label="temperature", x_range=(0, 11325), output_backend="webgl")
    line = p.line('x', 'y', line_color="blue", line_width=1, source=source)
    points = p.circle('x', 'y', fill_color='colors', fill_alpha=2, line_color="red", size=10, source=source)
    p.xaxis[0].formatter = DatetimeTickFormatter(days="%Y %m/%d %H:%M", months="%Y %m/%d %H:%M", hours="%Y %m/%d %H:%M", minutes="%Y %m/%d %H:%M")


    p.add_tools(HoverTool(tooltips = [('x','@x{%Y-%m-%d %H:%M:%S}'),('y','@y{0.00}')],
            formatters={'@x':'datetime','@y':'numeral'},))

    div = Div(
        text="""
        <p>Select the circle's size using this control element:</p>
        """,
        width=750,
        height=10,
    )

    spinner = Spinner(
        title="Circle size",  # a string to display above the widget
        low=0,  # the lowest possible number to pick
        high=60,  # the highest possible number to pick
        step=1,  # the increments by which the number can be adjusted
        value=points.glyph.size,  # the initial value to display in the widget
        width=200,  # the width of the widget in pixels
    )
    spinner.js_link("value", points.glyph, "size")

    range_slider = DateRangeSlider(
        title="Adjust x-axis range",  # a title to display above the slider
        start=x[0],  # set the minimum value for the slider
        end=x[11324],  # set the maximum value for the slider
        step=1,  # increments for the slider
        value=(x[0], x[11324]),  # initial values for slider
    )

    range_slider.js_link("value", p.x_range, "start", attr_selector=0)
    range_slider.js_link("value", p.x_range, "end", attr_selector=1)

    tlayout = layout([
        [div, spinner],
        [range_slider],
        [p],
    ])

    show(tlayout)
#f6()


# Interactive Bar Plot Of humidity and noise in temperature with slider zoom
def f6a():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    x = tips["temperature"]
    y1 = tips["humidity"]
    y2 = tips["ambient_noise"]

    tips.drop('Timestamp', axis=1, inplace=True)
    tips.drop('Entity-Name', axis=1, inplace=True)
    tips.drop('CO2', axis=1, inplace=True)
    tips.drop('ambient_light', axis=1, inplace=True)
    tips.drop('NH3', axis=1, inplace=True)

    df = pd.DataFrame(tips)
    source = ColumnDataSource(df)

    p = figure(x_range=(5, 35), y_range=(0, 125), height=750, title="Υγρασία & θόρυβος στην θερμοκρασία",
               toolbar_location=None, sizing_mode="stretch_width", output_backend="webgl")

    p.vbar(x=dodge("temperature", -0.25, range=p.x_range), top="humidity", width=0.001, source=source,
           color="red", legend_label="Humidity")

    p.vbar(x=dodge("temperature", 0.0, range=p.x_range), top="ambient_noise", width=0.001, source=source,
           color="blue", legend_label="Ambient_noise")

    # p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"

    range_slider = RangeSlider(
        title="Adjust x-axis range",  # a title to display above the slider
        start=4,  # set the minimum value for the slider
        end=35,  # set the maximum value for the slider
        step=0.01,  # increments for the slider
        value=(4, 35),  # initial values for slider
    )

    range_slider.js_link("value", p.x_range, "start", attr_selector=0)
    range_slider.js_link("value", p.x_range, "end", attr_selector=1)
    # range_slider.js_on_change("value", CustomJS(code="  console.log('slider: value=' + this.value, this.toString())")
    # callback = CustomJS(code="console.log('tap event occurred')")
    # range_slider.js_on_event('tap', callback)
    tlayout = layout([
        [range_slider],
        [p],
    ])

    show(tlayout)
#f6a()


# Multiple Interactive Line Plots With intercative circles that represent the sample's values taken.
def f6b():
    tips = pd.read_json("Sensor_Data_RTH4.json")
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

    # create a new plot with a title and axis labels
    p = figure(title="Multiple line example", x_axis_label="Timestamp", y_axis_label="Temperature & Humidity & Ambient_noise",
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
        end=x[11323],  # set the maximum value for the slider
        step=1,  # increments for the slider
        value=(x[0], x[11323]),  # initial values for slider
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
        [div, spinner1, spinner2, spinner3],
        [range_slider1, range_slider2],
        [p],
    ])

    p.legend.title = "Observations"
    p.legend.label_text_font = "times"
    p.legend.label_text_font_style = "italic"
    p.legend.label_text_color = "navy"
    p.legend.click_policy="hide"

    show(tlayout)


#f6b()




# Scatterplot - HeatMap -- Η διαφορά εδώ είναι ότι μπαίνει τριτη μεταβλητή
# και με βάση τη συσχέτιση μικραίνει ή μεγαλώνει.
def f7c():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    x = tips["humidity"]
    y = tips["temperature"]
    z = tips["ambient_noise"]

    x = x * 1
    y = y * 1
    z = z * 1

    # generate radii and colors based on data
    radii = y / 100 * 2
    colors = ["#%02x%02x%02x" % (255, int(round(value * 255)), 255) for value in z]
    mapper = LinearColorMapper(palette=colors, low=tips.ambient_noise.min(), high=tips.ambient_noise.max())


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
        max_width=2500,
        height=1500,
        x_axis_label="humidity", y_axis_label="temperature",
        output_backend="webgl"
    )

    # add circle renderer
    points1 = p.circle(
        'x',
        'y',
        radius='radii',
        fill_color=transform('z', mapper),
        fill_alpha=0.6,
        line_color="lightgrey",
        source = source
    )

    p.add_tools(HoverTool(tooltips = [('x','@x{0.00}'),('y','@y{0.00}'),('z','@z{0.00}')],
            formatters={'@x':'numeral','@y':'numeral','@z':'numeral'},))

    div = Div(
        text="""
        <p>Select the circle's size using this control element:</p>
        """,
        width=250,
        height=10,
    )

    range_slider = RangeSlider(
        title="Adjust x-axis range",  # a title to display above the slider
        start=28,  # set the minimum value for the slider
        end=95,  # set the maximum value for the slider
        step=0.1,  # increments for the slider
        value=(28, 95),  # initial values for slider
    )

    range_slider.js_link("value", p.x_range, "start", attr_selector=0)
    range_slider.js_link("value", p.x_range, "end", attr_selector=1)

    color_bar = ColorBar(color_mapper=mapper,
                         ticker=BasicTicker(desired_num_ticks=len(colors)),
                         formatter=PrintfTickFormatter(format="%d%%"))
    p.add_layout(color_bar, 'right')

    tlayout = layout([
        [range_slider],
        [p],
    ])

    # show the results
    show(tlayout)
#f7c()


def f7d():



    tips = pd.read_json("Sensor_Data_RTH4.json")
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

    TOOLS = "box_select,lasso_select,help"

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
        end=x[11323],  # set the maximum value for the slider
        step=1,  # increments for the slider
        value=(x[0], x[11323]),  # initial values for slider
    )

    range_slider.js_link("value", s1.x_range, "start", attr_selector=0)
    range_slider.js_link("value", s1.x_range, "end", attr_selector=1)


    tlayout = layout([
        [range_slider],
        [column(s1,s2,s3)],
        ])

    # put the results in a row and show
    show(tlayout)




def temp():
    from bokeh.io import show
    from bokeh.models import CustomJS, Select

    select = Select(title="Option:",  options=["foo", "bar", "baz", "quux"])

    select.js_on_change("value", CustomJS(code="""
        return this.value;
    """))

    print(select)

    show(select)




def temp2():
    import numpy as np
    import pandas as pd

    from bokeh.palettes import brewer
    from bokeh.plotting import figure, show

    N = 8
    df = pd.read_json("Sensor_Data_RTH4.json")
    df = pd.DataFrame(data=dict(x=df["Timestamp"],
            y1=df["temperature"],
            y2=df["humidity"]
            ))

    p = figure(width=1250, height=350,background_fill_color = "#fafafa")
    p.grid.minor_grid_line_color = '#eeeeee'

    p.varea_stack(['y1','y2'],x='x',color=("red","blue") ,source=df)
    p.xaxis.formatter = DatetimeTickFormatter(days="%Y %m/%d %H:%M",months="%Y %m/%d %H:%M",hours="%Y %m/%d %H:%M",minutes="%Y %m/%d %H:%M")

    show(p)


