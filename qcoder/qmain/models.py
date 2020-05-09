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
    term = models.CharField(max_length=32, choices=SEMESTERS, null=True)
    year = models.IntegerField(null=True)
    entry_code = models.CharField(max_length=16, null=True)
    lector = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    students = models.ManyToManyField(Student)
    
    def __str__(self):
        return self.name

class TaskType(models.Model):
    type_name = models.CharField(max_length=256)    

class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    deadline = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, null=True)

class TaskLinks(models.Model):
    link = models.CharField(max_length=4096) 
    task_file = models.ForeignKey(Task, on_delete=models.CASCADE) 

class Assignments(models.Model):
    grade = models.FloatField(default=0.0, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)

class AssignmentLinks(models.Model):
    link = models.CharField(max_length=4096) 
    task_file = models.ForeignKey(Assignments, on_delete=models.CASCADE) 
    
    
