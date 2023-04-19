from django.db import models
from django.utils import timezone


class Position(models.Model):
    position = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.position


class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    birth_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return self.fullname
