from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:id>/', views.blog, name='blog'),
    path('write/', views.blogWrite, name='blogWrite'),

]