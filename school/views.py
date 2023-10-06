from django.shortcuts import render, redirect

from .forms import TeacherForm, GroupForm
from .models import Teacher, Group


def teacher_form(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "teacher/teacher_form.html", {"form": form})
    form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("teacher_list")
    return render(request, "teacher/teacher_form.html", {"form": form})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher/teacher_list.html", {"teachers": teachers})


def group_form(request):
    if request.method == "GET":
        form = GroupForm()
        return render(request, "group/group_form.html", {"form": form})
    form = GroupForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("group_list")
    return render(request, "group/group_form.html", {"form": form})


def group_list(request):
    groups = Group.objects.all()
    return render(request, "group/group_list.html", {"groups": groups})
