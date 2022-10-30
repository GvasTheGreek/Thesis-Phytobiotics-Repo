from django.urls import path
from . import views
from . import dash_example
from . import prwto_grafima_dash
from . import dash_example2
from . import dash_example3
from . import deutero_grafima_dash
from . import trito_grafima_dash
from . import tetarto_grafima_dash
from . import pempto_grafima_dash


urlpatterns = [
    
    path('graphs_interactive/',views.graphs_interactive, name='interactive-graphs'),
]