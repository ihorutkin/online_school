from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Groups(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    teacher = models.ManyToManyField(
        "Teacher",
        related_name="teacher_groups"
    )
    progress = models.DecimalField(max_digits=100, decimal_places=0)

    def __str__(self):
        return f"{self.name} {self.level} {self.progress}%"


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    group = models.ForeignKey(
        Groups,
        on_delete=models.CASCADE,
        related_name="students"
    )


class Lesson(models.Model):
    topic = models.CharField(max_length=255)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name="lessons")
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="lessons"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.topic} {self.group} {self.teacher} {self.created_time}"


class Teacher(AbstractUser):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="lesson_teachers"
    )
    groups = models.ManyToManyField(Groups, related_name="group_teachers")
