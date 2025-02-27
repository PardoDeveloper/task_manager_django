from django.shortcuts import render
from .models import Task

# Create your views here.
def tasks_list(request):
    tasks = Task.objects.all()
    context = {
        "tasks" : tasks
    }
    return render(request, 'tasks/tasks_list.html', context)