from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


def index(request):
    allTodos = TodoItem.objects.all()
    return render(request, 'index.html', {'todos': allTodos})


def new(request):
    newItem = TodoItem(title=request.POST['title'],
                       author=request.POST['author'],
                       description=request.POST['description'])

    newItem.save()

    return HttpResponseRedirect('/todos/')


def delete(request, id):
    item = TodoItem.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect('/todos/')
