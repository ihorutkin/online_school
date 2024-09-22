from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from english.models import Teacher, Groups


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Teacher
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
        )


class GroupCreateForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Groups
        fields = "__all__"
