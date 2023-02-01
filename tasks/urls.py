from django.urls import path
from .views import index, add_task

app_name = "tasks"
urlpatterns = [
    path("", index, name='index'),
    path("add_task", add_task, name="add_task")
]