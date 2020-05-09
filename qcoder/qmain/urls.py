from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('courses', views.courses, name='courses'),
    path('assignments', views.assignments, name='assignments'),
    path('students', views.students, name='students'),
    path('course', views.course, name='course'),
    path('exams', views.check_exam, name='exams'),
]