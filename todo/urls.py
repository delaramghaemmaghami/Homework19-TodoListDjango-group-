from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("list/", TaskList.as_view(), name="todo_list"),
    path("<int:pk>/", TaskDetail.as_view(), name="todo_detail"),
    path("addTask/", add_task, name="add_task"),
    path("categorylist/", CategoryList.as_view(), name="category_list"),
    path("category/<int:pk>/", CategoryDetail.as_view(), name="category_detail"),
]
