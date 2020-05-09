from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('courses', views.courses, name='courses'),
    path('assignments', views.assignments, name='assignments'),
    path('students', views.students, name='students'),
    re_path(r'course/(?P<id>[0-9]+)/$', views.course, name='course'),
    path('exams', views.check_exam, name='exams'),
]