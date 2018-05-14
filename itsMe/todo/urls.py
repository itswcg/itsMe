from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoList, name='todo'),
    path('add/', views.todoAdd, name='todoAdd'),
    path('<int:id>/do/', views.todoFinish, name='todoFinish'),
    path('<int:id>/undo/', views.todoUnfinish, name='todoUnfinish'),
]