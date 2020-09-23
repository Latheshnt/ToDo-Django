from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import TodoApp



def home(request):
    all_todo_items = TodoApp.objects.all()
    return render(request, "todo.html",  {'all_items': all_todo_items})


def addTodo(request):
    new_item = TodoApp(content = request.POST['content'])
    new_item.save()
    return redirect('/')


def deleteTodo(request, Todo_id):
    delete_item = TodoApp.objects.get(id = Todo_id)
    delete_item.delete()
    return redirect('/')