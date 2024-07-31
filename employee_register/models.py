from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)
class Employee(models.Model):
    fullName = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    position = models.CharField(max_length=100)