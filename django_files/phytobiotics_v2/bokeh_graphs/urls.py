from django.urls import path
from . import views


urlpatterns = [
    path('visualize/',views.visualization, name='visualization'),
]