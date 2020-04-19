from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    GROUPS = (('Teacher', 'Teacher'),('Student', 'Student'),)
    email = forms.EmailField()
    groups = forms.ChoiceField(choices=GROUPS)

    class Meta:
        model = User
        fields = ['username','email','groups','password1','password2']