from django.contrib import admin
from .models import Student,Guardians,Faculty,Marks
# Register your models here.
admin.site.register(Student)
admin.site.register(Guardians)
admin.site.register(Faculty)
admin.site.register(Marks)