from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
#
@login_required
def setting(request):
    user = request.user
    username = user.username
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()

            message = '修改成功'
            messages.add_message(request, messages.SUCCESS, message)

            new_user = authenticate(username=username, password=new_password)
            login(request, new_user)
    else:
        form = ProfileForm(instance=user)

    return render(request, 'authentication/setting.html', {'form': form})
