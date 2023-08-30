from django.db import models

# Create your models here.

class Student(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f'Roll : {self.roll} - {self.name}'