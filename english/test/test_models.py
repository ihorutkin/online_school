from django.test import TestCase
from django.utils import timezone
from english.models import Groups, Student, Lesson, Teacher
import datetime

class GroupsModelTest(TestCase):
    def test_groups_str_method(self):
        group = Groups.objects.create(
            name="Beginner",
            level="A1",
            progress=20,
            starting_time="2023-09-01"
        )
        self.assertEqual(str(group), "Beginner A1 20%")


class StudentModelTest(TestCase):
    def test_student_creation(self):
        group = Groups.objects.create(
            name="Beginner",
            level="A1",
            progress=20,
            starting_time="2023-09-01"
        )
        student = Student.objects.create(
            name="John",
            surname="Doe",
            email="john.doe@example.com",
            group=group
        )
        self.assertEqual(student.name, "John")
        self.assertEqual(student.surname, "Doe")


class LessonModelTest(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create_user(
            username="teacher1",
            email="teacher1@example.com",
            password="password123"
        )
        self.group = Groups.objects.create(
            name="Intermediate",
            level="B1",
            progress=50,
            starting_time="2023-09-01"
        )

    def test_lesson_creation(self):
        lesson = Lesson.objects.create(
            topic="Vocabulary",
            group=self.group,
            teacher=self.teacher,
            start_time=timezone.now() + datetime.timedelta(hours=1),
            end_time=timezone.now() + datetime.timedelta(hours=2)
        )
        self.assertEqual(lesson.topic, "Vocabulary")

    def test_lesson_time_validation(self):
        lesson = Lesson(
            topic="Grammar",
            group=self.group,
            teacher=self.teacher,
            start_time=timezone.now() + datetime.timedelta(hours=2),
            end_time=timezone.now() + datetime.timedelta(hours=1)
        )
        with self.assertRaises(Exception):
            lesson.full_clean()
