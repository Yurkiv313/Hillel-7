from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Teacher, Group, Student, StudentsGroup


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "birth_date", "subject"]

    def clean_birthdate(self):
        birthdate = self.cleaned_data["birth_date"]
        if birthdate > timezone.now().date():
            raise ValidationError("Дата народження не може бути в майбутньому.")
        return birthdate

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 3:
            raise forms.ValidationError("Ім'я повинно містити принаймні 3 символи")
        return name


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "curator"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if Group.objects.filter(name=name).exists():
            raise ValidationError("Група з таким ім'ям вже існує.")
        return name


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "entry_year"]

    def clean_entry_year(self):
        entry_year = self.cleaned_data.get("entry_year")
        current_year = 2023
        if entry_year < current_year - 5 or entry_year > current_year:
            raise forms.ValidationError(
                "Рік вступу має бути в діапазоні від {} до {}".format(
                    current_year - 5, current_year
                )
            )
        return entry_year


class StudentsGroupForm(forms.ModelForm):
    class Meta:
        model = StudentsGroup
        fields = ["group", "student"]
