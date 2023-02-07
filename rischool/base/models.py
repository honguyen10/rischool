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

class Level(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    subject_id = models.ForeignKey(Subject, on_delete=models.PROTECT)
    level_id = models.ForeignKey(Level, on_delete=models.PROTECT)
    duration = models.CharField(max_length=100)
    max_unit_load = models.IntegerField()
    min_unit_load = models.IntegerField()

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=200)
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    schedule = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
