from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from home.models import Task
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def add_task(request):
    context = {'success': False}
    
    if request.method == "POST":
        title = request.POST.get('title', '').strip()  # Trim any extra whitespace
        desc = request.POST.get('desc', '')

        if not title:
            # If title is empty, return an error message
            context = {
                'success': False,
                'error': 'Task title cannot be empty.',
                'name': 'Hillary'
            }
            return render(request, 'add_task.html', context)

        # Create and save the Task only if title is valid
        details = Task(taskTitle=title, taskDesc=desc)
        try:
            details.save()
            print('The data has been saved to the db')
            context = {'success': True, 'name': 'Hillary'}
        except ValidationError as e:
            context = {
                'success': False,
                'error': str(e),
                'name': 'Hillary'
            }

    return render(request, 'add_task.html', context)

@login_required(login_url='login')
def manage_task(request):
    tasks = Task.objects.all()
    for task in tasks:
        if not task.taskTitle:
            print(f"Task with ID {task.id} has an empty taskTitle")
    return render(request, 'tasks.html', {'tasks': tasks})



def update_task(request, taskTitle):
    taskTitle = taskTitle.replace('%20', ' ')  # Replace encoded spaces if necessary
    task = get_object_or_404(Task, taskTitle=taskTitle)

    if request.method == 'POST':
        task.taskTitle = request.POST.get('taskTitle')
        task.taskDesc = request.POST.get('taskDesc')
        task.save()
        return redirect('tasks')  # Ensure 'task_list' is a valid URL name

    return render(request, 'update_task.html', {'task': task})

@login_required(login_url='login')
def delete_task(request, taskTitle):
    taskTitle = taskTitle.replace('%20', ' ')  # Replace encoded spaces if necessary
    task = get_object_or_404(Task, taskTitle=taskTitle)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')  # Replace 'task_list' with your actual view name
    return render(request, 'confirm_delete.html', {'task': task})

def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ user)
                return redirect('login')
    
        context = {'form':form }
        return render(request, 'register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password=password)

            if user is not None:
                login(request, user)
                return redirect('add_task')
            else:
                messages.info(request, 'Invalid Username or Password !')
                


        context = {}
        return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('/')
 