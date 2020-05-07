from django.db import models
from django.contrib.auth.models import User
from users.models import Student, Teacher

class Course(models.Model):
    SEMESTERS = [
        ('SPRING', 'Spring'),
        ('FALL', 'Fall'),
    ]
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=128)
    description = models.TextField()
    term = models.CharField(max_length=32, choices=SEMESTERS)
    year = models.IntegerField()
    entry_code = models.CharField(max_length=16)
    lector = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    deadline = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class TaskLinks(models.Model):
    link = models.CharField(max_length=4096) 
    task_file = models.ForeignKey(Task, on_delete=models.CASCADE) 

class Assignments(models.Model):
    grade = models.FloatField(default=0.0, null=True)

class AssignmentLinks(models.Model):
    link = models.CharField(max_length=4096) 
    task_file = models.ForeignKey(Assignments, on_delete=models.CASCADE) 
    
    
