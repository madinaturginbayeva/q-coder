from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms

class UserRegisterForm(UserCreationForm):
    GROUPS = (('Teacher', 'Teacher'),('Student', 'Student'),)
    email = forms.EmailField()
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['username','email','group','password1','password2']