from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoList, name='todo'),
    path('add/', views.todoAdd, name='todoAdd'),
    path('<int:id>/del/', views.todoDelete, name='todoDel'),
    path('<int:id>/do/', views.todoFinish, name='todoFinish'),
    path('<int:id>/undo/', views.todoUnfinish, name='todoUnfinish'),
    path('edit/', views.todoTask, name='todoTask'),
]