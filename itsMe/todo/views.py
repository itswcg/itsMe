from django.shortcuts import render, redirect
from .models import Todo


def todoList(request):
    user = request.user
    todoList = Todo.objects.filter(author=user, is_do=False).all()
    doList = Todo.objects.filter(author=user, is_do=True).all
    return render(request,'todo/todo.html', {'todoList': todoList, 'doList': doList})


def todoAdd(request):
    user = request.user
    if request.method == 'POST':
        todo = request.POST.get('todo')
        Todo.objects.create(author=user, content=todo)

    return redirect('/todo/')


def todoFinish(request, id):
    todo = Todo.objects.get(pk=id)
    todo.is_do = True
    todo.save()

    return redirect('/todo/')




def todoUnfinish(request, id):
    todo = Todo.objects.get(pk=id)
    todo.is_do = False
    todo.save()

    return redirect('/todo/')