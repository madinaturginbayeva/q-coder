from django.shortcuts import render
from .models import Course

def courses(request):
    context = {
        'courses' : Course.objects.all(),
        'title' : 'Courses'
    }
    return render(request, 'qmain/courses.html', context)

def assignments(request):
    return render(request, 'qmain/assignments.html', {'title':'Assignments'})

def students(request):
    return render(request, 'qmain/students.html', {'title':'Student'})

def course(request):
    return render(request, 'qmain/course.html', {'title':'Course'})