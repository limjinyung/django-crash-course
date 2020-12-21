from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Student(models.Model):
    RACE_CHOICES = (
        ('C', 'Chinese'),
        ('M', 'Malay'),
        ('I', 'Indian')
    )
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registrationDate = models.DateField("Date of Registration")
    race = models.CharField(max_length=20, choices=RACE_CHOICES)