from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from english.forms import DriverCreationForm, GroupCreateForm
from english.models import Lesson, Teacher, Groups, Student


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "dashboard/index.html")


class DashboardListView(LoginRequiredMixin, generic.ListView):
    model = Lesson
    template_name = "dashboard/dashboard.html"
    ordering = ("-created_time",)
    paginate_by = 5


class CreateTeacherView(generic.CreateView):
    model = Teacher
    template_name = "registration/sign_in.html"
    form_class = DriverCreationForm
    success_url = "/dashboard/"


class GroupListView(LoginRequiredMixin, generic.ListView):
    model = Groups
    template_name = "dashboard/group_list.html"
    paginate_by = 8


class GroupDetailView(LoginRequiredMixin, generic.DetailView):
    model = Groups
    template_name = "dashboard/group_detail.html"

class GroupCreateView(LoginRequiredMixin, generic.CreateView):
    model = Groups
    form_class = GroupCreateForm
    template_name = "dashboard/group_create_form.html"
    success_url = reverse_lazy("english:dashboard")


class StudentsListView(LoginRequiredMixin, generic.ListView):
    model = Student
    template_name = "dashboard/students_list.html"
    paginate_by = 8


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Student
    template_name = "dashboard/student_detail.html"
