from django.shortcuts import render_to_response, redirect
from tasks.models import *          
from .forms import *
from django.template import RequestContext
from django.http import HttpResponseBadRequest


def index(request):
    tasks = Task.objects.all()
    important_tasks = tasks.order_by('-rate')[:3]
    fresh_tasks = tasks.order_by('-create_date')[:3]
    form = CreateTaskForm()
    return render_to_response('tasks/index.html',
        {'important_tasks':important_tasks,
        'fresh_tasks':fresh_tasks, 
        'form':form}, 
        context_instance=RequestContext(request))


def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, request.FILES, )
        if form.is_valid():
            task = form.save(commit=False)
            # task.user = request.user
            task.save()
            return redirect('/task/'+str(task.id))
    return HttpResponseBadRequest()


def task(request, task_id):
    task = Task.objects.get(id=task_id)
    more_tasks = Task.objects.exclude(id=task_id)[:3]
    return render_to_response('tasks/task.html',
                              {'task': task, 'more_tasks': more_tasks})


def tasks(request):
    tasks = Task.objects.all()
    return render_to_response('tasks/tasks.html',
                              {'tasks': tasks})


def people(request):
    return render_to_response('tasks/people.html')


def profile(request, user_id):
    return render_to_response('tasks/profile.html')
