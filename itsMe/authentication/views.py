from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def signup(request):
    if request.method != 'POST':
        return render(request, 'authentication/signup.html', {'form': SignUpForm()})

    form = SignUpForm(request.POST)

    if not form.is_valid():
        return render(request, 'authentication/signup.html', {'form': form})

    username = form.cleaned_data.get('username')
    email = form.cleaned_data.get('email')
    password = form.cleaned_data.get('password')

    User.objects.create_user(username=username, password=password, email=email)

    user = authenticate(username=username, password=password)
    login(request, user)

    return redirect('/')