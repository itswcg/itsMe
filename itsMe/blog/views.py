from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm

# @login_required
def blogs(request):
    user = request.user
    blogs = Blog.objects.filter(author=user)

    return render(request, 'blog/blogs.html', {'blogs': blogs})

def blog(request, id):
    blog = Blog.objects.get(pk=id)
    return render(request, 'blog/blog.html', {'blog': blog})


def blogWrite(request):
    pass

def blogEdit(request):
    pass

def blogDelete(request):
    pass