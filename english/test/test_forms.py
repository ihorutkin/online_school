from django.test import TestCase
from english.forms import (
    TeacherCreationForm,
    StudentSearchForm,
    LessonSearchForm,
    GroupSearchForm
)

class TeacherCreationFormTest(TestCase):
    def test_valid_teacher_creation_form(self):
        form_data = {
            'username': 'new_user',
            'password1': 'Password123!',
            'password2': 'Password123!',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
        }
        form = TeacherCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_teacher_creation_form(self):
        form_data = {
            'username': 'new_user',
            'password1': 'password123',
            'password2': 'different_password',
            'first_name': '',
            'last_name': '',
            'email': 'john.doeexample.com',
        }
        form = TeacherCreationForm(data=form_data)
        self.assertFalse(form.is_valid())


class StudentSearchFormTest(TestCase):
    def test_student_search_form(self):
        form_data = {'name': 'John'}
        form = StudentSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class LessonSearchFormTest(TestCase):
    def test_lesson_search_form(self):
        form_data = {'topic': 'Grammar'}
        form = LessonSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class GroupSearchFormTest(TestCase):
    def test_group_search_form(self):
        form_data = {'name': 'Intermediate'}
        form = GroupSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
