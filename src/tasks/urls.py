from django.urls import path, include
from .views import tasks_list
from .views import taskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', taskViewSet, basename='task')

urlpatterns = [
    path('', tasks_list, name='tasks_list'),
    path('api', include(router.urls)),
]