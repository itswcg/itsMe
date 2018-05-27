from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm

# @login_required
def blog(request):
    user = request.user
    blogs = Blog.objects.all()
    if request.method != 'POST':
        return render(request, 'blog/blogs.html', {'form': BlogForm, 'blogs': blogs})

    form = BlogForm(request.POST)
    if form.is_valid():
        content = form.cleaned_data.get('content')
        Blog.objects.create(author=user, content=content)

    return redirect('')

