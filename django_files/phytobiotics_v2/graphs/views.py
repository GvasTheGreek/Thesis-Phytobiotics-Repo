from importlib.metadata import files
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
import requests
import pandas as pd
import os
#from django.shortcuts import redirect


import io
import matplotlib.pyplot as plt
import seaborn as sns
import urllib , base64
import numpy as np

from phytobiotics_v2.settings import MEDIA_ROOT
# Create your views here.




@login_required
def graphs_interactive(request):

    files_list = []
    for col in os.listdir(os.path.join(MEDIA_ROOT, "files")):
        files_list.append(col)

    if len(os.listdir(os.path.join(MEDIA_ROOT, "files"))) == 0:
        t = "NULL"
    else:
        t = len(os.listdir(os.path.join(MEDIA_ROOT, "files")))
    



    #path = {'t': os.listdir(os.path.join(MEDIA_ROOT, "files"))}
    path = {'t':files_list,  'ttt': t}

    return render(request, 'graphs/graphs_interactive.html',path)   


