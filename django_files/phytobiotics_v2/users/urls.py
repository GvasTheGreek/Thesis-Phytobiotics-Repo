from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register-page'),
    path('profile/', views.profile, name='profile-page'),
    path('new_profile/',views.new_profile, name='new-profile'),
]