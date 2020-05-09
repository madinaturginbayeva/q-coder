from django.forms import ModelForm, TextInput, Textarea
from .models import Course

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