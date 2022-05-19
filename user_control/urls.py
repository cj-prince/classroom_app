from rest_framework.routers import DefaultRouter
from .views import (UserViewSet,UserProfileViewSet,StudentViewSet,TeacherViewSet,FileuploadViewSet)
from django.urls import path, include

myrouter = DefaultRouter()

myrouter.register('users', UserViewSet, 'user_control')
myrouter.register('user_profile', UserProfileViewSet, 'user_profile_control')
myrouter.register('student', StudentViewSet, 'student_control')
myrouter.register('teacher', TeacherViewSet, 'teacher_control')
myrouter.register('file-upload', FileuploadViewSet, 'file_control')



urlpatterns = [
    path('', include(myrouter.urls)),
]