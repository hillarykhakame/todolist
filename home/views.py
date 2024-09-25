from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from home.models import Task
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def home(request):
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
            return render(request, 'index.html', context)

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

    return render(request, 'index.html', context)


def tasks(request):
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

def delete_task(request, taskTitle):
    taskTitle = taskTitle.replace('%20', ' ')  # Replace encoded spaces if necessary
    task = get_object_or_404(Task, taskTitle=taskTitle)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')  # Replace 'task_list' with your actual view name
    return render(request, 'confirm_delete.html', {'task': task})