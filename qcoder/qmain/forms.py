from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, DateTimeField
from .models import Course, Task

# Create the form class.
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description','year']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control validate', 'placeholder':'Title'}),
            'code': TextInput(attrs={'class':'form-control validate',  'placeholder':'Code'}),
            'description': Textarea(attrs={'class':'form-control validate',  'placeholder':'Description'}),
            'year': TextInput(attrs={'class': 'form-control validate',  'placeholder':'Year'}),
        }

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control validate', 'id':'orangeForm-name','placeholder':'Title'}),
            'description': Textarea(attrs={'class':'md-textarea form-control','placeholder':'Description','rows':'3'}),
            'deadline' : DateTimeInput(attrs={'type':'date'}, format="%d-%m-%Y %H:%M:%S")
        }