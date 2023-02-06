from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=150)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female')
    ])
    emergency_contact_name = models.CharField(max_length=150)
    emergency_contact_phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name
