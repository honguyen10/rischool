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

class Subject(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=150)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female')
    ])
    subject_ids = models.ManyToManyField(Subject)

    def __str__(self):
        subjects = ", ".join(subject.name for subject in self.subject_ids.all())
        display = self.name + ' - ' + subjects
        return display
