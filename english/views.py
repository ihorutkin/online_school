from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import generic

from english.models import Lesson


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "dashboard/index.html")


class DashboardListView(generic.ListView):
    model = Lesson
    template_name = "dashboard/dashboard.html"
    ordering = ("-created_time",)
    paginate_by = 5
