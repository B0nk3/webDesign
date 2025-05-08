from django.shortcuts import render, HttpResponse
# Create your views here.
def home(request):
    return render(request, "home.html")
from .models import TodoItem
def todos(request):
    items = todoitem.object.all()
    return render (request, "todos.html", {"todos: items"})