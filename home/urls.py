from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('tasks', views.tasks, name='tasks'),
     path('update/<str:taskTitle>/', views.update_task, name='update_task'),
     path('delete/<str:taskTitle>/', views.delete_task, name='delete_task')
]
