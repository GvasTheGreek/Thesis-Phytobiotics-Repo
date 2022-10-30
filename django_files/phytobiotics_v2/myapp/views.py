from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from . temp import fi,fc, fks, fg, fr, pie_chart_max, pie_chart_min

# Create your views here.


def welcome(request):
    if request.user.is_authenticated:
        return render(request,'myapp/home.html')
    else:
        return render(request,'myapp/welcome.html')

def about(request):
    return render(request,'myapp/about.html')

@login_required
def home_page(request):
    content = {
        'sample1': fi(),
        'sample2': fc(),
        'sample3': fks(),
        'sample4': fg(),
        'sample5': fr(),
        'sample6': pie_chart_max(),
        'sample7': pie_chart_min(),
    }
    return render(request,'myapp/home.html',content)
