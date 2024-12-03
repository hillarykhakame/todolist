from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('add_task', views.add_task, name='add_task'),
     path('manage_task', views.manage_task, name='tasks'),
     path('update/<str:taskTitle>/', views.update_task, name='update_task'),
     path('delete/<str:taskTitle>/', views.delete_task, name='delete_task'),
     path('register', views.register_page, name='register'),
     path('login', views.login_page, name='login'),
     path('logout/', views.logout_user, name='logout'),
]
