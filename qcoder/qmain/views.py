from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

def main(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'qmain/landing.html', {'form': form})

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