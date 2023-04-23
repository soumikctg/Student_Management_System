from django.contrib import admin
from .models import Student,Guardians,Faculty
# Register your models here.
admin.site.register(Student)
admin.site.register(Guardians)
admin.site.register(Faculty)