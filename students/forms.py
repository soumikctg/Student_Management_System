from django import forms
from .models import Student,Guardians



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
        labels = {
            'student_id' : 'Student ID',
            'first_name' : 'First Name', 
            'last_name' : 'Last Name', 
            'email' : 'Email', 
            'field_of_study' : 'Field of Study', 
            'gpa' : 'GPA'
        }
        widgets = {
            'student_id' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}), 
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}), 
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}), 
            'field_of_study' : forms.TextInput(attrs={'class' : 'form-control'}), 
            'gpa' : forms.NumberInput(attrs={'class' : 'form-control'})
        }
        
class GuardianForm(forms.ModelForm):
    class Meta:
        model = Guardians
        fields = ['guardian_id', 'name', 'phone', 'relation', 'student']
        labels = {
            'guardian_id' : 'Guardian ID',
            'name' : 'Name', 
            'phone' : 'Phone', 
            'relation' : 'Relationship with student',
            'student' : 'Students ID'
        }
        widgets = {
            'guardian_id' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control'}), 
            'phone' : forms.NumberInput(attrs={'class' : 'form-control'}), 
            'relation' : forms.TextInput(attrs={'class' : 'form-control'}),
            'student' : forms.NumberInput(attrs={'class' : 'form-control'}),
            
        }
