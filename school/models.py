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
