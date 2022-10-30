from django.urls import path
from . import views


urlpatterns = [
    path('search/',views.search_index, name='search-page'),
    path('upload/',views.BookUploadView, name='upload_file'),
    path('dashboards/',views.test, name='test-page'),
]