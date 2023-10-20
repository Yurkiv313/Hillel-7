# Generated by Django 4.2.6 on 2023-10-15 15:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0006_alter_student_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="RequestLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("path", models.CharField(max_length=255)),
                ("method", models.CharField(max_length=10)),
                ("ex_time", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
