from django.urls import path

from .views import index

app_name = 'newyear'
urlpatterns = [
    path("", index, name='index')
]