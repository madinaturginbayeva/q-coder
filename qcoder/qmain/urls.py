from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('courses', views.courses, name='courses'),
    path('assignments', views.assignments, name='assignments'),
    path('course/<int:id>/students', views.students, name='students'),
    path('course/<int:id>/tasks', views.course, name='course'),
    path('course/<int:course_id>/tasks/<int:task_id>', views.check_exam, name='exams'),
    path('course/<int:course_id>/tasks/<int:task_id>/list',views.task, name='task')
]