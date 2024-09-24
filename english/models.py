from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Groups(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    teacher = models.ManyToManyField(
        "Teacher",
        related_name="teacher_groups"
    )
    progress = models.DecimalField(
        max_digits=100,
        decimal_places=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    starting_time = models.DateField()
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
    group = models.ForeignKey(
        Groups,
        on_delete=models.CASCADE,
        related_name="lessons"
    )
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

    def clean(self):
        super().clean()

        if self.start_time > self.end_time:
            raise ValidationError('The time difference between '
                                  'start_time and end_time '
                                  'cannot exceed 24 hours.')

        if (self.end_time - self.start_time).total_seconds() > 24 * 3600:
            raise ValidationError('The time difference between '
                                  'start_time and end_time '
                                  'cannot exceed 24 hours.')

        if self.start_time < timezone.now():
            raise ValidationError('Start time cannot be in the past.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Lesson, self).save(*args, **kwargs)


class Teacher(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="lesson_teachers",
        null=True,
        blank=True
    )
    groups = models.ManyToManyField(
        Groups,
        related_name="group_teachers"
    )

    class Meta:
        verbose_name = "Teacher"
