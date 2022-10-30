from turtle import onclick
from django.shortcuts import render, redirect
from pyparsing import replace_html_entity
from .search import search
from .json import json_data_types
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
from . models import FilesModel
from . forms import UploadFilesForm
from elasticsearch import Elasticsearch
import json
import urllib3
import time
from django.core.files.storage import default_storage
import os
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
from bs4 import BeautifulSoup
import string
import itertools 
import html
import io
#from graphs.dash_example3 import *
from requests.auth import HTTPBasicAuth
from requests.structures import CaseInsensitiveDict
import shutil
from phytobiotics_v2.settings import MEDIA_ROOT

# Create your views here.

@login_required
def search_index(request):
    results = []
    city_term = ""
    state_term = ""
    if request.GET.get('temperature') and request.GET.get('ambient_noise'):
        city_term = request.GET['temperature']
        state_term = request.GET['ambient_noise']
    elif request.GET.get('temperature'):
        city_term = request.GET['temperature']
    elif request.GET.get('ambient_noise'):
        state_term = request.GET['ambient_noise']
    search_term = city_term or state_term
    results = search(city_term, state_term)
    print(results)
    context = {'results': results, 'count': len(results), 'search_term':  search_term}
    return render(request,  'elk/search.html',  context)




# Function to handle an uploaded file.
@login_required
def BookUploadView(request):
    if request.method == 'POST':
        form = UploadFilesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # Here is upload to elk function
            index= form.cleaned_data['Index_Name']
            files = form.cleaned_data['files'].name
            time.sleep(4)
            bokeh_upload_file(files)
            body = json_data_types(files)
            time.sleep(4)
            #to_elastic(index,files,body)           ##### FOR THE ORIGINAL VERSION  #####
            temp =to_elastic(index,files,body)      ##### FOR THE SECOND VERSION  #####
            time.sleep(3)
            delete_file(temp)                       ##### FOR THE SECOND VERSION  #####
            time.sleep(3)
            create_data_view(index)

            context = {
                'form':form,
                'success': 'yes'
            }
    else:
        form = UploadFilesForm(request.POST,request.FILES)
        context = {
            'form':form,
            'success': 'no'
        }
    
    return render(request, 'elk/upload_to_elastic.html', context)

### THE ORIGINAL VERSION OF UPLOADING. USING ES LIBRARY. CHECK json.py ###
""" 
def to_elastic(variable1,variable2, variable3):
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    es = Elasticsearch(['https://localhost:9200'], http_auth=('elastic', 'elastic'), verify_certs=False)
    
    def function():
        p = 0
        es.indices.create(index=variable1, body=variable3, params=None, headers=None, ignore=400)
        # es.index(index='custom-mapping-index', document='Sensor_Data_RTH1.json', doc_type=None, id=None, params=None, headers=None)
        
        with default_storage.open(os.path.join('files', variable2)) as f:
            data = json.loads(f.read())
            for row in range(len(data)):
                # put document into elastic search
                es.index(index=variable1, body=data[row], id=p)
                # print(obj)
                p = p + 1
        
    function()
"""    

### START SECOND VERSION ###
def to_elastic(variable1,variable2, variable3):
    i =0
    variable22 = "to_be_deleted_" + variable2 
    default_storage.open(os.path.join('files', variable22),'w')
    shutil.copy(default_storage.path(os.path.join('files', variable2)),default_storage.path(os.path.join('files', variable22)))
    with default_storage.open(os.path.join('files', variable22)) as f:
        # Reading from file
        data = json.loads(f.read())
        print(len(data))
        # Closing file
        #f.close()

    with default_storage.open(os.path.join('files', variable22),'w') as f:
        for i in range(len(data)):
            json.dump({"index": {"_id": i}}, f)
            f.write('\n')
            json.dump((data[i]), f)
            f.write('\n')

    response = requests.get('https://host.docker.internal:9200', verify=False, auth=HTTPBasicAuth('elastic', 'elastic'))

    # print request object
    print(response)

    payload = default_storage.open(os.path.join('files', variable22),'rb')
    headers = {
        'content-type': 'application/json'
    }
    r = requests.put('https://localhost:9200/'+ variable1+ '?pretty', verify=False, auth=('elastic', 'elastic'))
    print(r)
    r = requests.put('https://localhost:9200/' + variable1 + '/_mapping', headers=headers, verify=False, auth=('elastic', 'elastic'), json=variable3)
    print(r)
    r = requests.post('https://localhost:9200/dummy_index/_bulk?pretty', headers=headers, data=payload, verify=False, auth=('elastic', 'elastic'))  # 18/8
    print(r)

    new_index = {
        "source": {
            "index": "dummy_index",
            "query": {
                "match_all": {}
            }
        },

        "dest": {
            "index": variable1
        }
    }

    time.sleep(5)
    r = requests.post('https://localhost:9200/_reindex', headers=headers, json=new_index, verify=False, auth=HTTPBasicAuth('elastic', 'elastic'))
    print(r)
    
    return variable22

def delete_file(var):
    default_storage.delete(os.path.join('files', var))

### END SECOND VERSION ###          




def test(request):
    func3()
    my_list = find_id()
    to_html(my_list)
    form = {
        'form': my_list,
    }
    return render(request, 'elk/dashboards.html', form)


def func3():
    headers = {
        'kbn-xsrf': 'true',
        # Already added when you pass json= but not when you pass data=
        'Content-Type': 'application/json',
    }

    json_data = {
        'type': 'dashboard',
    }

    response = requests.post('https://localhost:5601/api/saved_objects/_export', headers=headers, json=json_data, verify=False, auth=('elastic', 'elastic'))
    print(response)

    with default_storage.open(os.path.join('files_static', 'test.json'),'wb') as f:
        f.write(response.content)

    with default_storage.open(os.path.join('files_static',"test.json"), "r+") as file:

        # Move the pointer (similar to a cursor in a text editor) to the end of the file
        file.seek(0, os.SEEK_END)

        # This code means the following code skips the very last character in the file -
        # i.e. in the case the last line is null we delete the last line
        # and the penultimate one
        pos = file.tell() - 1

        # Read each character in the file one at a time from the penultimate
        # character going backwards, searching for a newline character
        # If we find a new line, exit the search
        while pos > 0 and file.read(1) != "\n":
            pos -= 1
            file.seek(pos, os.SEEK_SET)

        # So long as we're not at the start of the file, delete all the characters ahead
        # of this position
        if pos > 0:
            file.seek(pos, os.SEEK_SET)
            file.truncate()
    
    #return os.path.abspath(file)

def find_id():
    with default_storage.open(os.path.join('files_static', 'test.json')) as f:
        result = []
        for line in f:
            content = json.loads(line)
            result.append(content['id'])
    return result

def to_html(var1):    
    soup = BeautifulSoup(open('elk/templates/elk/dashboards.html'), 'html.parser')
    alphabet = list(string.ascii_lowercase)

    for div in soup.find_all("script",{'class':'thesis'}):
        div.decompose()
    
    for i,j in zip(var1,alphabet):
        p_tag = soup.new_tag("script",**{'class':'thesis'})
        p_tag.string ='function'+ ' ' + j+ '() {' + '\n'+'\t'+ 'document.getElementById(\"iframeDisplay\").innerHTML = \"<iframe src=\\\"https://localhost:5601/app/dashboards#/view/' + i +  '?embed=true&_g=(filters%3A!())&show-top-menu=true&show-query-input=true&show-time-filter=true\\\" style=\\\"position:fixed; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; margin:0; padding-top:70px; overflow:hidden;\\\"></iframe>\";' + '\n'+'\t' +'document.getElementById(\"hide-div\").style.display = \"none\"; window.location = loc; }' + '\n'
        soup.body.append(p_tag)

        with open("elk/templates/elk/dashboards.html", "w") as file:
            file.write(str(soup))

    for div in soup.find_all("a",{"class":"my-thesis"}):
        div.decompose()

        with open("elk/templates/elk/dashboards.html", "w") as file:
            file.write(str(soup))

    for i in range(len(var1)):

        new_tag = soup.new_tag("a",**{'style':'cursor:pointer; color:#fff', 'class':'my-thesis'}, onclick=alphabet[i]+"()")
        new_tag.string ='Dashboard ' + alphabet[i] +'\n'
        soup.body.main.nav.div.append(new_tag)

        with open("elk/templates/elk/dashboards.html", "w") as file:
            file.write(str(soup))



def create_data_view(index_name):  # WORKS

    headers = {
        'kbn-xsrf': 'true',
        # Already added when you pass json= but not when you pass data=
        'Content-Type': 'application/json',
    }

    json_data = {
        'data_view': {
            'title': index_name,
            "timeFieldName": "Timestamp"
        },
    }

    response = requests.post('https://localhost:5601/api/data_views/data_view', headers=headers, json=json_data, verify=False, auth=('elastic', 'elastic'))
    print(response)


def bokeh_upload_file(file):
    if len(os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh"))) == 0:
        default_storage.open(os.path.join('files_bokeh', file),'w')
        shutil.copy(default_storage.path(os.path.join('files', file)),default_storage.path(os.path.join('files_bokeh', file)))
    else:
        #folder = '/path/to/folder'
        for filename in os.listdir(os.path.join(MEDIA_ROOT, "files_bokeh")):
            file_path = os.path.join(os.path.join(MEDIA_ROOT, "files_bokeh"), filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        
        default_storage.open(os.path.join('files_bokeh', file),'w')
        shutil.copy(default_storage.path(os.path.join('files', file)),default_storage.path(os.path.join('files_bokeh', file)))
    