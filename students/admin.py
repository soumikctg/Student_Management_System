from django.contrib import admin
from .models import Student,Person,Guardians
# Register your models here.
admin.site.register(Student)
admin.site.register(Person)
admin.site.register(Guardians)