from django.shortcuts import render,redirect
from django.db import connection
from .models import Student,Faculty, Guardians
from django.urls import reverse
from .forms import StudentForm, GuardianForm, FacultyForm


# Create your views here.
def index(request):
    student = Student.objects.all()
    print(student)
    return render(request, 'index.html', {
        'students' : student
    })
    
def view_students(request, student_id):
    student = Student.objects.get(pk = student_id)
    return redirect(reverse('index'))

def view_guardians(request, student_id):
    student = Student.objects.get(student_id=student_id)
    guardians= student.guardians_set.all()
    print(guardians)
    return render(request, 'guardian.html', {
        'guardians' : guardians
    })
    
def view_faculty(request):
    faculty = Faculty.objects.all()
    return render(request, 'faculty.html', {
        'faculties' : faculty
    })
    
# guardian
def add_guardian(request):
    if request.method == 'POST':
        form = GuardianForm(request.POST)
        if form.is_valid():
            new_guardian_id = form.cleaned_data['guardian_id']
            new_name = form.cleaned_data['name']
            new_phone = form.cleaned_data['phone']
            new_relation = form.cleaned_data['relation']
            new_student = form.cleaned_data['student']
            
            
            new_guardian = Guardians(
                guardian_id = new_guardian_id,
                name = new_name,
                phone = new_phone,
                relation = new_relation,
                student = new_student
            )
            
            new_guardian.save()
            return render(request, 'addguardian.html', {
                'form' : GuardianForm(),
                'success' : True
            })
        else:
            return render(request, 'addguardian.html', {
                'form' : GuardianForm(),
            })
    else:
        form =GuardianForm()
        return render(request, 'addguardian.html', {
                'form' : GuardianForm(),
            })
        
def edit_guardian(request, guardian_id):
    if request.method == 'POST':
        guardian = Guardians.objects.get(pk=guardian_id)
        form = GuardianForm(request.POST, instance=guardian)
        if form.is_valid():
            form.save()
            return render( request, 'editguardian.html', {
                'form': form,
                'success' : True
            })
        else:
             render(request, 'editguardian.html', {
                'form' : form
            })
            
    else:
        guardian =Guardians.objects.get(pk=guardian_id)
        form= GuardianForm(instance=guardian)
    
        return render(request, 'editguardian.html', {
            'form' : form
        })

def delete_guardian(request, guardian_id):
    if request.method == 'POST':
        guardian = Guardians.objects.get(pk=guardian_id)
        guardian.delete()
    return redirect(reverse('index'))

# student  
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_id = form.cleaned_data['student_id']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']
            
            new_student = Student(
                student_id = new_student_id,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                gpa = new_gpa
            )
            
            new_student.save()
            return render(request, 'add.html', {
                'form' : StudentForm(),
                'success' : True
            })
        else:
            return render(request, 'add.html', {
                'form' : StudentForm(),
            })
    else:
        form =StudentForm()
        return render(request, 'add.html', {
                'form' : StudentForm(),
            })
        
        
def edit_student(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(pk=student_id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render( request, 'editstudent.html', {
                'form': form,
                'success' : True
            })
        else:
             render(request, 'editstudent.html', {
                'form' : form
            })
            
    else:
        student =Student.objects.get(pk=student_id)
        form= StudentForm(instance=student)
    
        return render(request, 'editstudent.html', {
            'form' : form
        })
        
        
def delete_student(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(pk=student_id)
        student.delete()
    return redirect(reverse('index'))




#faculty
def add_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_phone = form.cleaned_data['phone']
            new_email = form.cleaned_data['email']
            new_address =  form.cleaned_data['address']
            
            
            cursor=connection.cursor()
            query = f"INSERT INTO studentdb.students_faculty (name, phone, email, address) VALUES ('{new_name}', '{new_phone}', '{new_email}', '{new_address}')"
            cursor.execute(query)
        
            
            return render(request, 'addfaculty.html', {
                'form' :FacultyForm,
                'success' : True
            })
        else:
            return render(request, 'addfaculty.html', {
                'form' : FacultyForm
            })
    else:
        form = FacultyForm()
        return render(request, 'addfaculty.html', {
                'form' : form
            })
        
        
def delete_faculty(request, id):
    if request.method == 'POST':
        faculty = Faculty.objects.get(pk=id)
        cursor=connection.cursor()
        query = f"DELETE FROM studentdb.students_faculty WHERE id = '{id}'"
        cursor.execute(query)
    return redirect(reverse('faculty'))