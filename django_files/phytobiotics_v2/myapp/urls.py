from django.urls import path
from . import views

urlpatterns = [
    path('welcome', views.welcome, name='welcome'),
    path('about/',views.about, name='about-page'),
    path('',views.home_page, name='home_page'),
]
