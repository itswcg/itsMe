from django.shortcuts import render
from .models import Todo

def todoList(request):
    render(request,'todo/todo.html')