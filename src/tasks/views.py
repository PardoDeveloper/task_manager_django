from django.shortcuts import render
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer

# Create your views here.
def tasks_list(request):
    tasks = Task.objects.all()
    context = {
        "tasks" : tasks
    }
    return render(request, 'tasks/tasks_list.html', context)

class taskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer