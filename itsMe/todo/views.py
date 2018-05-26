from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Todo, Task
from django.utils.timezone import now, timedelta


def todoList(request):
    user = request.user
    task = Task.objects.filter(author=user).last()
    today = now().date() + timedelta(days=0)
    todoList_Today = Todo.objects.filter(author=user, is_do=False, create_date__gte=today).all()
    doList_Today = Todo.objects.filter(author=user, is_do=True, create_date__gte=today).all()
    todoList = Todo.objects.filter(author=user, is_do=False, create_date__lt=today).all()
    doList_page = Todo.objects.filter(author=user, is_do=True, create_date__lt=today).all()

    paginator = Paginator(doList_page, 8)
    page = request.GET.get('page')
    try:
        doList = paginator.page(page)
    except PageNotAnInteger:
        doList = paginator.page(1)
    except EmptyPage:
        doList = paginator.page(paginator.num_pages)
    return render(request,'todo/todo.html', {'todoList_Today': todoList_Today, 'doList_Today': doList_Today,
                                             'todoList': todoList, 'doList': doList, 'task': task})


def todoAdd(request):
    user = request.user
    if request.method == 'POST':
        todo = request.POST.get('todo')
        Todo.objects.create(author=user, content=todo)

    return redirect('/todo/')

def todoUpdate(request, id):
    todo = Todo.objects.get(pk=id)
    if request.method == 'POST':
        content = request.POST.get('todo')
        todo.content = content
        todo.save()

    return redirect('/todo/edit/')


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

def todoDelete(request):
    todo_id = request.GET.get('todo-id')
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()

    return HttpResponse()

def todoTask(request):
    user = request.user
    task_pre = Task.objects.filter(author=user).last()
    if request.method == 'POST':
        task = request.POST.get('task')
        Task.objects.create(author=user, content=task)
        return redirect('/todo/')

    todoList_all = Todo.objects.filter(author=user).all()
    paginator = Paginator(todoList_all, 10)
    page = request.GET.get('page')
    try:
        todoList = paginator.page(page)
    except PageNotAnInteger:
        todoList = paginator.page(1)
    except EmptyPage:
        todoList = paginator.page(paginator.num_pages)
    return render(request, 'todo/task.html', {'task': task_pre, 'todoList': todoList})