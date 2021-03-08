from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    age = models.IntegerField()
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    percentage = models.IntegerField()
    def __str__(self) -> str:
        return self.name
