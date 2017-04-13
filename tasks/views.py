from django.shortcuts import render, render_to_response
from .models import *

def index(request):
    tasks = Task.objects.all()
    impotant_tasks = tasks.order_by('-rate')[:3]
    fresh_tasks = tasks.order_by('-create_date')[:3]

    return render_to_response('tasks/index.html', 
        {'impotant_tasks':impotant_tasks, 'fresh_tasks':fresh_tasks})


def task(request, task_id):
    task = Task.objects.get(id=task_id)
    more_tasks = Task.objects.exclude(id=task_id)[:3]
    return render_to_response('tasks/task.html', 
        {'task':task, 'more_tasks':more_tasks})

def tasks(request):
    tasks = Task.objects.all()
    return render_to_response('tasks/tasks.html', 
        {'tasks':tasks})

def people(request):
    return render_to_response('tasks/people.html')

def profile(request, user_id):
    return render_to_response('tasks/profile.html')
