from django.urls import path
from . import views

urlpatterns = [
    path("teacher/", views.teacher_form, name="teacher_form"),
    path("teachers/", views.teacher_list, name="teacher_list"),
    path("teacher/<int:pk>", views.teacher_edit, name="teacher_edit"),
    path("group/", views.group_form, name="group_form"),
    path("groups/", views.group_list, name="group_list"),
    path("group/<int:pk>", views.group_edit, name="group_edit"),
    path("student/", views.student_form, name="student_form"),
    path("students/", views.student_list, name="student_list"),
    path("student/<int:pk>", views.student_edit, name="student_edit"),
    path("studentgroup/", views.student_group_form, name="student_group_form"),
    path("studentgroups/", views.student_group_list, name="student_group_list"),
    path("studentgroup/<int:pk>", views.student_group_edit, name="student_group_edit"),
]
