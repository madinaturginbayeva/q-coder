from django.shortcuts import render
from .forms import UserRegisterForm

def register(request):
    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

def login(request):
    form = UserCreationForm()
    return render(request, 'users/login.html', {'form' : form})
