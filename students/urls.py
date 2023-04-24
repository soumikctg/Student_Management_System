from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('', views.index, name='index'),
    path('faculty/', views.view_faculty, name='faculty'),
    path('<int:student_id>',views.view_students, name='view_student'),
    path('<int:student_id>/guardians',views.view_guardians, name='view_guardian'),
    path('add/', views.add, name='add'),
    path('addfaculty/', views.add_faculty, name='addfaculty'),
    path('addguardian/', views.add_guardian, name='addguardian'),
    path('editstudent/<int:student_id>/', views.edit_student, name='editstudent'),
    path('editguardian/<int:guardian_id>/', views.edit_guardian, name='editguardian'),
    path('delete/<int:student_id>/', views.delete_student, name='deletestudent'),
    path('deleteguardian/<int:guardian_id>/', views.delete_guardian, name='deleteguardian'),
    path('deletefaculty/<int:id>/', views.delete_faculty, name='deletefaculty'),
    path('editfaculty/<int:id>/', views.edit_faculty, name='editfaculty'),
    path('uploadmark/', views.import_csv, name='uploadmark'),
    path('uploadfaculty/', views.import_faculty, name='uploadfaculty'),
]