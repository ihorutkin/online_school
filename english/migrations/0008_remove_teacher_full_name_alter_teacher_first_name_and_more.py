# Generated by Django 5.1.1 on 2024-09-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("english", "0007_alter_teacher_lesson"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="teacher",
            name="full_name",
        ),
        migrations.AlterField(
            model_name="teacher",
            name="first_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="last_name",
            field=models.CharField(max_length=255),
        ),
    ]
