from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.PositiveBigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
    
class Guardians(models.Model):
    guardian_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    relation = models.CharField(max_length=20)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    
class Faculty(models.Model):
    name = models.CharField(max_length=50)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=20)
    address = models.CharField(max_length=150)