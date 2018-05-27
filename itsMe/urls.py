"""itsMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .blog import views as blog_view
from .authentication import views as authentication_views


urlpatterns = [
    path('itswcg/', admin.site.urls),

    path('', blog_view.blog, name='blog'),
    path('login/', auth_views.login, {'template_name': 'authentication/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('signup/', authentication_views.signup, name='signup'),
    path('captcha/', include('captcha.urls')),
    path('setting/', include('itsMe.authentication.urls')),
    path('todo/', include('itsMe.todo.urls'))
]
