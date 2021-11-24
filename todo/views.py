from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Task


class Home(TemplateView):
    template_name = "home.html"


class TaskList(ListView):
    model = Task
    template_name = "todo/todo_list.html"


class TaskDetail(DetailView):
    model = Task
    template_name = "todo/todo_detail.html"
