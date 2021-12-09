from django.core import serializers
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Task, Category

from datetime import date


class Home(TemplateView):
    template_name = "home.html"


class TaskList(ListView):
    model = Task
    template_name = "todo/todo_list.html"

    def post(self, request):
        if request.method == "POST" and request.is_ajax():
            text = request.POST.get("text")
            if text == "EXPIRED":
                expired_tasks = Task.objects.filter(dead_line__lt=date.today())
                tasks = expired_tasks

            elif text == "IN PROGRESS":
                in_progress = Task.objects.filter(dead_line__gte=date.today())
                tasks = in_progress

            elif text == "LAST 3 TASKS":
                last_tasks = Task.objects.all().order_by("-create_time")[:3]
                tasks = last_tasks

            if tasks:
                return JsonResponse({
                    'tasks': list(tasks.values_list('title', flat=True))
                })
            else:
                return JsonResponse({
                    'tasks': [],
                    'msg': "doesn't match any files",
                })

        return render(request, 'todo/todo_list.html')


class TaskDetail(DetailView):
    model = Task
    template_name = "todo/todo_detail.html"


def add_task(request):
    categories = list(Category.objects.values_list("category_name", flat=True))

    if request.method == "POST" and request.is_ajax():
        title = request.POST.get("title")
        category = request.POST.get("category")
        priority = request.POST.get("priority")
        dead_line = request.POST.get("deadLine")
        description = request.POST.get("description")

        category1 = Category.objects.filter(category_name=category).last()

        task = Task.objects.create(title=title, description=description,
                                   priority=priority, dead_line=dead_line)

        task.category.add(category1)

        return JsonResponse({})

    else:
        return render(request, "todo/add_task.html", {"categories": categories})


class CategoryList(ListView):
    model = Category
    template_name = "todo/category_list.html"

    def post(self, request):
        if request.method == "POST" and request.is_ajax():
            text = request.POST.get("text")
            if text == "EMPTY CATEGORY":
                empty_categories = []
                categories = Category.objects.all()
                for category in categories:
                    tasks = category.cat_rel.all().values()
                    if not (tasks.exists()):
                        empty_categories.append(category.category_name)
                cats = empty_categories

            elif text == "MOST":
                popular = Category.objects.annotate(Count('cat_rel')).order_by('-cat_rel__count')[:3]
                popular_categories = list(popular.values_list('category_name', flat=True))
                cats = popular_categories

            if cats:
                return JsonResponse({
                    # 'tasks': list(cats.values_list('category_name', flat=True))
                    'tasks': cats,
                })
            else:
                return JsonResponse({
                    'tasks': [],
                    'msg': "doesn't match any files",
                })

        return render(request, 'todo/category_list.html')


class CategoryDetail(DetailView):
    model = Category
    template_name = 'todo/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = list(Task.objects.all().filter(category=context["category"]))
        return context

