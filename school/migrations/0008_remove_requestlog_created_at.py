# Generated by Django 4.2.6 on 2023-10-15 15:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0007_requestlog"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="requestlog",
            name="created_at",
        ),
    ]
