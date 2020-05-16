from django.db import models
from django.contrib.auth.models import User

"""
    Student model, created after User register as Student
"""
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(null=True)
    faculty = models.CharField(max_length=4096, null=True)
    major = models.CharField(max_length=4096, null=True)
    graduation_year = models.IntegerField(null=True)
    enrollment_year = models.IntegerField(null=True)
    phone = models.CharField(max_length=11, null=True)

"""
    Teacher model, created after User register as Teacher
"""
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty =  models.CharField(max_length=4096, null=True)
    degree =  models.CharField(max_length=4096, null=True) 
    position =  models.CharField(max_length=4096, default='Teacher', null=True)



