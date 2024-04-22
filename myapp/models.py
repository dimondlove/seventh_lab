from django.db import models


# Create your models here.
class Student(models.Model):
    lastname = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    patronymic = models.CharField(max_length=35)
    birth_year = models.IntegerField()
    group = models.CharField(max_length=20)
