from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("list/", TaskList.as_view(), name="todo_list"),
    path("<int:pk>/", TaskDetail.as_view(), name="todo_detail")
]
