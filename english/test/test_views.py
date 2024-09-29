from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import datetime
from english.models import Teacher, Groups, Student, Lesson

class DashboardViewTest(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(
            username="new_teacher",
            first_name="Name1",
            last_name="Surname1",
            email="jane.doe@example.com",
            password="password123"
        )
        self.group = Groups.objects.create(
            name="Intermediate",
            level="B1",
            progress=50,
            starting_time="2023-09-01"
        )
        self.student = Student.objects.create(
            name="John",
            surname="Doe",
            email="john.doe@example.com",
            group=self.group
        )
        self.lesson = Lesson.objects.create(
            topic="Vocabulary",
            group=self.group,
            teacher=self.teacher,
            start_time=timezone.now() + datetime.timedelta(hours=1),
            end_time=timezone.now() + datetime.timedelta(hours=2)
        )

    def test_dashboard_view(self):
        response = self.client.get(reverse("english:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/dashboard.html")
        self.assertIn("amount_students", response.context)
        self.assertIn("amount_groups", response.context)
        self.assertIn("amount_lessons", response.context)
        self.assertEqual(response.context["amount_students"], 1)
        self.assertEqual(response.context["amount_groups"], 1)
        self.assertEqual(response.context["amount_lessons"], 1)
