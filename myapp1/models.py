from django.db import models


# Create your models here.

class Student(models.Model):
    sId = models.CharField(max_length=30)
    sName = models.CharField(max_length=22)
    sEmail = models.EmailField()
    sGender = models.CharField(max_length=10)
