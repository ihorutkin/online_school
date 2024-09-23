from django.urls import path
from english.views import (
    index,
    dashboard_view,
    CreateTeacherView,
    TeacherDetailView,
    GroupCreateView,
    GroupDetailView,
    GroupListView,
    GroupUpdateView,
    GroupDeleteView,
    StudentsListView,
    StudentDetailView,
    StudentUpdateView,
    StudentDeleteView,
    StudentCreateView,
    LessonCreateView,
    LessonListView,
    LessonUpdateView,
    LessonDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path("teacher/<int:pk>", TeacherDetailView.as_view(), name="teacher_admin"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("teacher/create/", CreateTeacherView.as_view(), name="create-teacher"),
    path("group/", GroupListView.as_view(), name="group-list"),
    path("group/<int:pk>/", GroupDetailView.as_view(), name="group-detail"),
    path("group/create/", GroupCreateView.as_view(), name="group-create"),
    path("group/update/<int:pk>", GroupUpdateView.as_view(), name="group-update"),
    path("group/delete/<int:pk>", GroupDeleteView.as_view(), name="group-delete"),
    path("students/", StudentsListView.as_view(), name="students-list"),
    path("students/<int:pk>", StudentDetailView.as_view(), name="student-detail"),
    path("students/update/<int:pk>", StudentUpdateView.as_view(), name="student-update"),
    path("students/delete/<int:pk>", StudentDeleteView.as_view(), name="student-delete"),
    path("students/create/", StudentCreateView.as_view(), name="student-create"),
    path("lesson/", LessonListView.as_view(), name="lesson-list"),
    path("lesson/create/", LessonCreateView.as_view(), name="lesson-create"),
    path("lesson/update/<int:pk>", LessonUpdateView.as_view(), name="lesson-update"),
    path("lesson/delete/<int:pk>", LessonDeleteView.as_view(), name="lesson-delete"),
]

app_name = "english"
