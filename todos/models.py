from django.db import models
from django.contrib import admin


class TodoItem(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    description = models.CharField(max_length=255)


class TodoItemView(admin.ModelAdmin):
    list_display = ('title', 'author', 'description')
