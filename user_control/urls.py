from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from django.urls import path, include

myrouter = DefaultRouter()

myrouter.register('users', UserViewSet, 'user_control')



urlpatterns = [
    path('', include(myrouter.urls)),
]