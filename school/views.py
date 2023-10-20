import time

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import TeacherForm, GroupForm, StudentForm, StudentsGroupForm
from .models import Teacher, Group, Student, StudentsGroup


def teacher_form(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "teacher/teacher_form.html", {"form": form})
    form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("teacher_edit", args=[form.instance.pk]))

    return render(request, "teacher/teacher_form.html", {"form": form})


def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(request, "teacher/teacher_edit.html", {"form": form})
    form = TeacherForm(request.POST, instance=teacher)
    if "delete" in request.POST:
        groups = teacher.group_set.all()
        if groups.exists():
            error_message = f"Неможливо видалити вчителя, оскільки є прив'язані групи."
            return render(
                request, "teacher/teacher_error.html", {"error_message": error_message}
            )
        teacher.delete()
        return redirect("teacher_list")
    if form.is_valid():
        form.save()
        return redirect("teacher_list")

    return render(request, "teacher/teacher_edit.html", {"form": form})


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
        return redirect(reverse("group_edit", args=[form.instance.pk]))

    return render(request, "group/group_form.html", {"form": form})


def group_edit(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == "GET":
        form = GroupForm(instance=group)
        return render(request, "group/group_edit.html", {"form": form})
    form = GroupForm(request.POST, instance=group)
    if "delete" in request.POST:
        group.delete()
        return redirect("group_list")
    if form.is_valid():
        form.save()
        return redirect("group_list")

    return render(request, "group/group_edit.html", {"form": form})


def group_list(request):
    groups = Group.objects.all()
    return render(request, "group/group_list.html", {"groups": groups})


def student_form(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request, "student/student_form.html", {"form": form})
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("student_list")

    return render(request, "student/student_form.html", {"form": form})


def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "GET":
        form = StudentForm(instance=student)
        return render(request, "student/student_edit.html", {"form": form})
    form = StudentForm(request.POST, instance=student)
    if "delete" in request.POST:
        student.delete()
        return redirect("student_list")
    if form.is_valid():
        form.save()
        return redirect("student_list")

    return render(request, "student/student_edit.html", {"form": form})


def student_list(request):
    students = Student.objects.all()
    return render(request, "student/student_list.html", {"students": students})


def student_group_form(request):
    if request.method == "GET":
        form = StudentsGroupForm()
        return render(request, "student_group/student_group_form.html", {"form": form})
    form = StudentsGroupForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("student_group_list")

    return render(request, "student_group/student_group_form.html", {"form": form})


def student_group_edit(request, pk):
    student_group = get_object_or_404(StudentsGroup, pk=pk)
    if request.method == "GET":
        form = StudentsGroupForm(instance=student_group)
        return render(request, "student_group/student_group_edit.html", {"form": form})
    form = StudentsGroupForm(request.POST, instance=student_group)
    if "delete" in request.POST:
        student_group.delete()
        return redirect("student_group_list")
    if form.is_valid():
        form.save()
        return redirect("student_group_list")

    return render(request, "student_group/student_group_edit.html", {"form": form})


def student_group_list(request):
    students_group = StudentsGroup.objects.all()
    return render(
        request,
        "student_group/student_group_list.html",
        {"students_groups": students_group},
    )
