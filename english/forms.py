from django.contrib.auth.forms import UserCreationForm
from django import forms
from english.models import Teacher, Groups


class TeacherCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Teacher
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
        )


class StudentSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "first name"
            }
        )
    )


class LessonSearchForm(forms.Form):
    topic = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "lesson topic"
            }
        )
    )


class GroupSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "group name"
            }
        )
    )
