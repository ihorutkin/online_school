from django.urls import path
from english.views import (
    index,
    DashboardListView,
    CreateTeacherView,
    GroupCreateView,
    GroupDetailView,
    StudentsListView,
    GroupListView,
    StudentDetailView
)


urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", DashboardListView.as_view(), name="dashboard"),
    path("group/", GroupListView.as_view(), name="group-list"),
    path("group/<int:pk>/", GroupDetailView.as_view(), name="group-detail"),
    path("group/create/", GroupCreateView.as_view(), name="group-create"),
    path("students/", StudentsListView.as_view(), name="students-list"),
    path("students/<int:pk>", StudentDetailView.as_view(), name="student-detail"),
    path("signup/", CreateTeacherView.as_view(), name="create_teacher")
]

app_name = "english"
