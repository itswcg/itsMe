from django.shortcuts import render, redirect
from .models import Todo, Task
from django.utils.timezone import now, timedelta


def todoList(request):
    user = request.user
    task = Task.objects.filter(author=user).last()
    today = now().date() + timedelta(days=0)
    todoList_Today = Todo.objects.filter(author=user, is_do=False, create_date__gte=today).all()
    doList_Today = Todo.objects.filter(author=user, is_do=True, create_date__gte=today).all()
    todoList = Todo.objects.filter(author=user, is_do=False, create_date__lt=today).all()
    doList = Todo.objects.filter(author=user, is_do=True, create_date__lt=today).all
    return render(request,'todo/todo.html', {'todoList_Today': todoList_Today, 'doList_Today': doList_Today,
                                             'todoList': todoList, 'doList': doList, 'task': task})


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

def todoTask(request):
    user = request.user
    task1 = Task.objects.filter(author=user).last()
    if request.method == 'POST':
        task = request.POST.get('task')
        Task.objects.create(author=user, content=task)
        return redirect('/todo/')

    return render(request, 'todo/task.html', {'task': task1})