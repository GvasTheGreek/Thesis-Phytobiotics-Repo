#from django.shortcuts import render
from django.core.files.storage import default_storage
from phytobiotics_v2.settings import MEDIA_ROOT
#import requests
import pandas as pd
import os


import io
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
import urllib , base64
import numpy as np
import base64

tips = pd.read_json(default_storage.open(os.path.join('files_static', 'sample_RTH3.json')))
tips1 = pd.read_json(default_storage.open(os.path.join('files_static', 'sample_RTH4.json')))
tips2 = pd.read_json(default_storage.open(os.path.join('files_static', "sample_covid.json")))

import matplotlib.style as mplstyle
import matplotlib as mpl

import random
import json



def fi():
    
    px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    figure, axs = plt.subplots(ncols=2,figsize=(580*px, 400*px) )

    mpl.rcParams['path.simplify'] = True

    sns.set_theme(style="darkgrid")
    sns.countplot(y='temperature', data=tips, ax=axs[0],rasterized=True)
    axs[0].set_xlabel('Count Of Records')
    axs[0].set_ylabel('temperature')
    axs[0].set_title("θερμοκρασία ανά Δείγματα")

    sns.countplot(y='humidity', data=tips, ax=axs[1])
    axs[1].set_xlabel('Count Of Records')
    axs[0].set_ylabel('humidity')
    axs[1].set_title("Υγρασία ανά Δείγματα")
    plt.subplots_adjust(bottom=0.15)

    imgdata = io.StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    mplstyle.use('fast')
    return data


# Triple Lineplot -- Showing the progress of the temperature , humitidy and ambient_noise in time.
def fc():
    #tips = pd.read_json(default_storage.open(os.path.join('files', 'Sensor_Data_RTH3.json')))

    px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    figure = plt.figure(figsize=(625*px, 450*px))

    mpl.rcParams['path.simplify'] = True

    sns.lineplot(data=tips, x="Timestamp", y="temperature", marker="o",rasterized=True)
    sns.lineplot(data=tips, x="Timestamp", y="humidity", marker='*',rasterized=True)
    sns.lineplot(data=tips, x="Timestamp", y="ambient_noise",rasterized=True)
    plt.legend(['temperature', 'humidity', 'ambient_noise'])
    plt.xlabel('Timestamp')
    plt.ylabel('temp - humidity - ambient noise')
    plt.title("H αλλαγή θερμοκρασίας υγρασίας θορύβου στο χρόνο")
    
    imgdata = io.StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    mplstyle.use('fast')
    return data

def fks():
    

    px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    figure = plt.figure(figsize=(625*px, 450*px))

    mpl.rcParams['path.simplify'] = True

    sns.scatterplot(x=tips1.temperature, y=tips1.CO2, hue=tips1.ambient_noise, s=70,rasterized=True)
    plt.xlabel('temperature')
    plt.ylabel('CO2')
    plt.title("Heatmap θερμοκρασίας ανά CO2 χωρισμένο ανά ποσοστό θορύβου")

    imgdata = io.StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    mplstyle.use('fast')
    return data
    
def fg():
    #tips = pd.read_json(default_storage.open(os.path.join('files', 'Sensor_Data_RTH3.json')))

    px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    figure = plt.figure(figsize=(625*px, 450*px))

    sns.set_theme(style="darkgrid")
    sns.countplot(y='ambient_noise', data=tips,rasterized=True)
    plt.xlabel('Count Of Records')
    plt.ylabel('θόρυβος Περιβάλλοντος')
    plt.title("Αριθμός Δειγμάτων Ανά Θόρυβο Περιβάλλοντος")

    imgdata = io.StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    mplstyle.use('fast')
    return data


def countplot_CO2():
    
    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))
        
    def get_columns():
        files_list = []
        #columns_list = []
        for col in get_file_list():
            files_list.append(col)
        return files_list[0]
    

    with default_storage.open(os.path.join('files_bokeh', get_columns())) as f:
        data = json.load(f)

        if len(data) < 75:
            dat = random.sample(data, k=len(data))
        else:
            dat = random.sample(data, k=75)
        
        dat = pd.DataFrame(dat)

        
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        figure = plt.figure(figsize=(625*px, 450*px))

        sns.countplot(y='CO2', data=dat,rasterized=True)
        plt.xlabel('Count Of Records')
        plt.ylabel('Διοξείδιο του Άνθρακα')
        plt.title("Αριθμός Δειγμάτων Ανά CO2")

        imgdata = io.StringIO()
        figure.savefig(imgdata, format='svg')
        imgdata.seek(0)

        result = imgdata.getvalue()
        return result
        
def countplot_NH3():
    
    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))
        
    def get_columns():
        files_list = []
        #columns_list = []
        for col in get_file_list():
            files_list.append(col)
        return files_list[0]
    

    with default_storage.open(os.path.join('files_bokeh', get_columns())) as f:
        data = json.load(f)

        if len(data) < 75:
            dat = random.sample(data, k=len(data))
        else:
            dat = random.sample(data, k=75)
        
        dat = pd.DataFrame(dat)

        
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        figure = plt.figure(figsize=(625*px, 450*px))

        sns.countplot(y='NH3', data=dat,rasterized=True)
        plt.xlabel('Count Of Records')
        plt.ylabel('Άζωτο')
        plt.title("Αριθμός Δειγμάτων Ανά NH3")

        imgdata = io.StringIO()
        figure.savefig(imgdata, format='svg')
        imgdata.seek(0)

        result = imgdata.getvalue()
        return result


def fr():
    #tips = pd.read_json(default_storage.open(os.path.join('files', 'Sensor_Data_RTH4.json')))

    px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    figure = plt.figure(figsize=(625*px, 450*px))

    mpl.rcParams['path.simplify'] = True

    sns.scatterplot(x=tips1.CO2, y=tips1.humidity, hue=tips1.temperature, size=tips1.temperature, s=60,rasterized=True)
    plt.xlabel('Διοξείδιο του Άνθρακα')
    plt.ylabel('Υγρασία')
    plt.title("Heatmap Διοξείδιου ανά υγρασία με βάση τη θερμοκρασία")
    
    imgdata = io.StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    mplstyle.use('fast')
    return data


def pie_chart_max():

    
    px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    mpl.rcParams['path.simplify'] = True
    

    new = pd.DataFrame(tips2, columns=['Country', 'New_cases'])
    tp = new.groupby('Country').sum()
    tp = tp.to_dict()

    countries = []
    cases_per_countries = []

    for i in tp.keys():
        for j in tp[i].keys():
            countries.append(j)
        for k in tp[i].values():
            cases_per_countries.append(k)

    cases_per_countries, countries = zip(*sorted(zip(cases_per_countries, countries), reverse=True))

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    sizes = [cases_per_countries[0], cases_per_countries[1], cases_per_countries[2], cases_per_countries[3], cases_per_countries[4]]
    labels = [countries[0], countries[1], countries[2], countries[3], countries[4]]
    explode = (0, 0.1, 0, 0, 0)

    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)
        return my_autopct

    figure = plt.figure(figsize=(625*px, 450*px))
    plt.pie(sizes, labels=labels, autopct=make_autopct(sizes),
            shadow=True, startangle=90, explode=explode)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Οι 5 χώρες με τα περισσότερα κρούσματα Covid")

    imgdata = io.StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    mplstyle.use('fast')
    return data

def pie_chart_min():
    
    #tips = pd.read_json(default_storage.open(os.path.join('files', "WHO-COVID-19-global-data.json")))

    px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    #mpl.rcParams['path.simplify'] = True
    
    new = pd.DataFrame(tips2, columns=['Country', 'New_cases'])
    tp = new.groupby('Country').sum()
    tp = tp.to_dict()

    countries = []
    cases_per_countries = []

    for i in tp.keys():
        for j in tp[i].keys():
            countries.append(j)
        for k in tp[i].values():
            cases_per_countries.append(k)

    cases_per_countries, countries = zip(*sorted(zip(cases_per_countries, countries), reverse=True))

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    sizes_min = [cases_per_countries[-6], cases_per_countries[-7], cases_per_countries[-8], cases_per_countries[-9], cases_per_countries[-10]]
    labels_min = [countries[-6], countries[-7], countries[-8], countries[-9], countries[-10]]
    explode = (0, 0.1, 0, 0, 0)

    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)
        return my_autopct

    figure = plt.figure(figsize=(625*px, 450*px))
    plt.pie(sizes_min, labels=labels_min, autopct=make_autopct(sizes_min),
            shadow=True, startangle=90, explode=explode)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Οι 5 χώρες με τα λιγότερα κρούσματα Covid")

    imgdata = io.StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    #mplstyle.use('fast')
    return data



def pairplot():
    
    #px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    #mpl.rcParams['path.simplify'] = True
    

    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))
        
    def get_columns():
        files_list = []
        #columns_list = []
        for col in get_file_list():
            files_list.append(col)
        return files_list[0]


    tips = pd.read_json(default_storage.open(os.path.join('files_bokeh', get_columns())))
    tips = pd.DataFrame(tips)

    #figure = plt.figure(figsize=(1000*px, 1000*px))
    figure = sns.pairplot(data=tips, hue="Entity-Name")
    plt.suptitle("Pairplot")
    

    imgdata = BytesIO()
    figure.savefig(imgdata, format='jpeg')
    imgdata.seek(0)

    data = base64.b64encode(imgdata.getvalue()).decode()
    #result['chart'] = data
    #data = imgdata.read()
    return data


    



# Scatterplot -- Presenting how much Temperature is affected by Ambient_noise and CO2 accompanied by distplot
def jointplot_hum_temp():
    
    #px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    #mpl.rcParams['path.simplify'] = True
    

    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))
        
    def get_columns():
        files_list = []
        #columns_list = []
        for col in get_file_list():
            files_list.append(col)
        return files_list[0]


    tips = pd.read_json(default_storage.open(os.path.join('files_bokeh', get_columns())))
        
    #figure = plt.figure(figsize=(625*px, 450*px))
    figure = sns.jointplot(data=tips, x="humidity", y="temperature", hue="ambient_noise", rasterized=True)
    plt.suptitle("HeatMap Υγρασίας & Θερμοκρασίας με παράγοντα τον θόρυβο")

    imgdata = io.StringIO()
    figure.savefig(imgdata, format='svg',block=True)
    imgdata.seek(0)

    data = imgdata.getvalue()
    #mplstyle.use('fast')
    return data


def jointplot_CO2_temp():
    #px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    #mpl.rcParams['path.simplify'] = True
    
    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))
        
    def get_columns():
        files_list = []
        #columns_list = []
        for col in get_file_list():
            files_list.append(col)
        return files_list[0]


    tips = pd.read_json(default_storage.open(os.path.join('files_bokeh', get_columns())))    

    #sns.scatterplot(x="CO2", y="humidity", hue="temperature", size="temperature", style="Entity-Name", data=tips)
    #figure = plt.figure(figsize=(625*px, 450*px))
    figure=sns.jointplot(data=tips, x="CO2", y="temperature", hue="ambient_light", kind="hist",rasterized=True)
    plt.suptitle("Your title here")

    imgdata = io.StringIO()
    figure.savefig(imgdata, format='svg',block=True)
    imgdata.seek(0)

    data = imgdata.getvalue()
    #mplstyle.use('fast')
    return data


def dist_plot_CO2_NH3():
    #px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    #mpl.rcParams['path.simplify'] = True
    
    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))
        
    def get_columns():
        files_list = []
        #columns_list = []
        for col in get_file_list():
            files_list.append(col)
        return files_list[0]

    tips = pd.read_json(default_storage.open(os.path.join('files_bokeh', get_columns())))

    #figure = plt.figure(figsize=(1000*px, 1000*px))
    figure = sns.displot(data=tips, x="CO2", hue="NH3", multiple="stack", kind="kde",rasterized=True)
    plt.suptitle("Distribution plot based on CO2 and NH3.")
    
    imgdata = io.StringIO()
    figure.savefig(imgdata, format='svg',block=True)
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

def jointplot_CO2_ambient_noise():
    #px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    #mpl.rcParams['path.simplify'] = True
    
    def get_file_list():
        return os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))
        
    def get_columns():
        files_list = []
        #columns_list = []
        for col in get_file_list():
            files_list.append(col)
        return files_list[0]


    tips = pd.read_json(default_storage.open(os.path.join('files_bokeh', get_columns())))    

    #sns.scatterplot(x="CO2", y="humidity", hue="temperature", size="temperature", style="Entity-Name", data=tips)
    #figure = plt.figure(figsize=(625*px, 450*px))
    figure=sns.jointplot(data=tips, x="CO2", y="ambient_noise", hue="NH3", kind="hist",rasterized=True)
    plt.suptitle("Γράφημα CO2 & θορύβου με βάση το ΄Αζωτο.")

    imgdata = io.StringIO()
    figure.savefig(imgdata, format='svg',block=True)
    imgdata.seek(0)

    data = imgdata.getvalue()
    #mplstyle.use('fast')
    return data