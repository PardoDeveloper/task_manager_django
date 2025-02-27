from django.urls import path, include
from .views import contact, ContactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact', ContactViewSet, basename='contact')

urlpatterns = [
    path('', contact, name='contact'),
    path('api', include(router.urls)),
]