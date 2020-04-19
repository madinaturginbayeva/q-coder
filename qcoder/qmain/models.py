from django.db import models
from django.contrib.auth.models import User

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
    lector = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

# class Assignment(models.Model):
#     title = models.CharField(max_length=256)
#     description = models.TextField()
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    
