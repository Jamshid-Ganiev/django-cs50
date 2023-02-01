from django.urls import path
from .views import index, greet

app_name = 'hello'
urlpatterns = [
    path("", index, name="index"),
    path("<str:name>", greet, name="greet")
]