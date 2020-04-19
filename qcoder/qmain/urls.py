from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('assignments', views.assignments, name='assignments'),
    path('students', views.students, name='students'),
    path('course', views.course, name='course')
]