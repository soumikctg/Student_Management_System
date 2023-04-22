from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>',views.view_students, name='view_student'),
    path('<int:student_id>/guardians',views.view_guardians, name='view_guardian'),
    path('add/', views.add, name='add'),
    path('addguardian/', views.add_guardian, name='addguardian'),
    path('editstudent/<int:student_id>/', views.edit_student, name='editstudent'),
    path('editguardian/<int:guardian_id>/', views.edit_guardian, name='editguardian'),
    path('delete/<int:student_id>/', views.delete_student, name='deletestudent'),
    path('deleteguardian/<int:guardian_id>/', views.delete_guardian, name='deleteguardian'),
]