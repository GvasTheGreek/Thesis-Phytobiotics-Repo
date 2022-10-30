from django.shortcuts import render
from importlib.metadata import files
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
import requests
import pandas as pd
import os
from django.shortcuts import redirect


import io
import matplotlib.pyplot as plt
import seaborn as sns
import urllib , base64
import numpy as np
from myapp.temp import *


from . bokeh_charts import *

from phytobiotics_v2.settings import MEDIA_ROOT

# Create your views here.

@login_required
def visualization(request):
    
    if len(os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))) == 0:
        return redirect('upload_file')
    else:
    
        script, div = f5()
        script1,div1 =f4b()
        script2,div2 = f7()
        script3,div3 = f7d()
        script4,div4= f6b()
        h = {
                'graph1' : fi(),'graph2' : fc(),'graph3' : fks(),'graph4' : fg(),'graph5' : fr(),
                'graph6' : pie_chart_max(),'graph7' : pie_chart_min(), 'graph8':pairplot(),
                'graph9': jointplot_hum_temp(), 'graph10':jointplot_CO2_temp(), 'graph11': dist_plot_CO2_NH3(), 
                'graph12': countplot_CO2(),'graph13': countplot_NH3(), 'graph14': jointplot_CO2_ambient_noise(),
                'script': script,'div': div,
                'script1': script1,'div1': div1,
                'script2' : script2, 'div2':div2,
                'script3' : script3, 'div3':div3,
                'script4' : script4, 'div4':div4,
            }
    return render(request, 'bokeh_graphs/visualize.html',h)


