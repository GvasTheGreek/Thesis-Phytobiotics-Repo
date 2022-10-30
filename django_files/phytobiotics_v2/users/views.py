from django.shortcuts import render , redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm  #On 25/10
from django.contrib import messages #25/10
from .forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm

from django.contrib.auth.decorators import login_required #29/10


# START For Create Kibana User
import requests
import time
from requests.auth import HTTPBasicAuth
from requests.structures import CaseInsensitiveDict
# END For Create Kibana User

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            #return HttpResponse(password)
            register_kibana_user(username,password,email)
            #messages.success(request, f'Your account has been created! You may now login')
            return redirect('Login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})


@login_required
def profile(request):
    if request.method =='POST':
        us_form= UserUpdateForm(request.POST, instance=request.user)
        pr_form= ProfileUpdateForm(request.POST,
                                   request.FILES, 
                                   instance=request.user.profile)

        if us_form.is_valid() and pr_form.is_valid():
            us_form.save()
            pr_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile-page')
    else:
        us_form= UserUpdateForm(instance=request.user)
        pr_form= ProfileUpdateForm(instance=request.user.profile)

    context ={
        'us_form' : us_form,
        'pr_form' : pr_form
    }
    return render(request, 'users/profile.html', context)


def register_kibana_user(username,password,email):
    response = requests.get('https://host.docker.internal:9200',
                            verify=False,
                            auth=HTTPBasicAuth('elastic', 'elastic'))
    # print(response)
    
    data = {
        "password": password,
        "enabled": True,
        "roles": ["superuser", "kibana_admin"],
        "full_name": username,
        "email": email,
        "metadata": {
            "intelligence": 7
        }
    }
    
    headers = {
        'content-type': 'application/json'
    }
    
    name = username
    r = requests.post('https://host.docker.internal:9200/_security/user/' + name, json=data, headers=headers, verify=False, auth=('elastic', 'elastic'))
    #print(r)


@login_required
def new_profile(request):
    return render(request, 'users/new_profile.html')