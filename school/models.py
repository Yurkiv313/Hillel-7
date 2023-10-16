from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    birth_date = models.DateField()
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    curator = models.ForeignKey(Teacher, on_delete=models.PROTECT, to_field="name")

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=16, null=True)
    entry_year = models.IntegerField()

    def __str__(self):
        return self.name


class StudentsGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT, to_field="id")
    student = models.ForeignKey(Student, on_delete=models.PROTECT, to_field="id")


class RequestLog(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    ex_time = models.FloatField()

    def __str__(self):
        return f"Path: {self.path}, Method: {self.method}, Execution Time: {self.ex_time:} seconds"
