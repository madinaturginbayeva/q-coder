from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(null=True)
    faculty = models.CharField(max_length=4096, null=True)
    major = models.CharField(max_length=4096, null=True)
    graduation_year = models.IntegerField(null=True)
    enrollment_year = models.IntegerField(null=True)
    phone = models.CharField(max_length=11, null=True)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty =  models.CharField(max_length=4096, null=True)
    degree =  models.CharField(max_length=4096, null=True) 
    position =  models.CharField(max_length=4096, default='Teacher', null=True)



