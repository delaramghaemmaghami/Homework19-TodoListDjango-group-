from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100,
                                     blank=False)

    description = models.TextField(max_length=500)

    def __str__(self):
        return self.category_name


class Task(models.Model):
    title = models.CharField(max_length=100,
                             blank=False)

    description = models.TextField(max_length=500,
                                   blank=False)

    category = models.ManyToManyField(Category,
                                      related_name="cat_rel")  # views.py ->class CategoryList ->Most, Empty

    PRIORITY_CHOICES = [
        ('high', 'high'),
        ('medium', 'medium'),
        ('low', 'low')
    ]
    priority = models.CharField(max_length=6,
                                choices=PRIORITY_CHOICES,
                                default="low")

    create_time = models.DateField(auto_now_add=True)
    dead_line = models.DateField()

    def __str__(self):
        return self.title

