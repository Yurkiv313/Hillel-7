from django.urls import path
from . import views

urlpatterns = [
    path("teacher/", views.teacher_form, name="teacher_form"),
    path("teachers/", views.teacher_list, name="teacher_list"),
    path("group/", views.group_form, name="group_form"),
    path("groups/", views.group_list, name="group_list"),
]
