from django.urls import path
from english.views import (
    index,
    DashboardListView,
    CreateTeacherView,
    GroupCreateView,
    GroupDetailView,
    StudentsListView,
    GroupListView
)


urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", DashboardListView.as_view(), name="dashboard"),
    path("group/", GroupListView.as_view(), name="group-list"),
    path("group/<int:pk>/", GroupDetailView.as_view(), name="group-detail"),
    path("group/create/", GroupCreateView.as_view(), name="group-create"),
    path("students/", StudentsListView.as_view(), name="students-list"),
    path("signup/", CreateTeacherView.as_view(), name="create_teacher")
]

app_name = "english"
