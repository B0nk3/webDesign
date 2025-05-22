from django.shortcuts import render, HttpResponse
from .models import Post
from .models import TodoItem
# Create your views here.
def home(request):
    return render(request, "main.html")

def todos(request):
    items = todoitem.object.all()
    return render (request, "todos.html", {"todos: items"})

def aout(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'formular.html')

