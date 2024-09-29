from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic

import plotly.graph_objects as go
from plotly.offline import plot

from english.forms import (
    TeacherCreationForm,
    StudentSearchForm,
    LessonSearchForm,
    GroupSearchForm
)
from english.models import Lesson, Teacher, Groups, Student


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "dashboard/index.html")


def dashboard_view(request: HttpRequest) -> HttpResponse:
    amount_students = Student.objects.all().count()
    amount_groups = Groups.objects.all().count()
    amount_lessons = Lesson.objects.all().count()

    groups = Groups.objects.all()

    x_data = ['2024-01-01', '2024-02-01', '2024-03-01',
         '2024-04-01', '2024-05-01', '2024-06-01',
         '2024-07-01', '2024-08-01', '2024-09-01',
         '2024-10-01', '2024-11-01', '2024-12-01']

    group_values = {}

    x_value = []
    y_value = []

    for date in x_data:
        count = 0
        for group in groups:
            if group.starting_time.strftime("%Y-%m-%d") == date:
                count += 1
        group_values[date] = count

    for key, value in group_values.items():
        x_value.append(key)
        y_value.append(value)



    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=x_value,
        y=y_value,
        marker=dict(
            color='skyblue',
            line=dict(
                color='blue',
                width=2
            )
        ),
        hoverinfo='x+y',
        name='Values'
    ))

    fig.update_layout(
        title=dict(
            text='Amount groups every month',
            font=dict(size=24),
            x=0.5,
            xanchor='center',
        ),
        xaxis_title='Date',
        yaxis_title='Value',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            size=14,
            color='black'
        ),
        hovermode='x',
        xaxis=dict(
            showgrid=True,
            gridcolor='lightgray',
            tickangle=-45,
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='lightgray',
            rangemode='tozero'
        ),
        height=500,
        width=900,
    )


    plot_div = plot(fig, output_type="div")

    context = {
        "amount_students": amount_students,
        "amount_groups": amount_groups,
        "amount_lessons": amount_lessons,
        "plot_div": plot_div,
    }
    return render(
        request,
        "dashboard/dashboard.html",
        context=context
    )


class TeacherDetailView(LoginRequiredMixin, generic.DetailView):
    model = Teacher
    template_name = "dashboard/admin_page.html"


class CreateTeacherView(generic.CreateView):
    model = Teacher
    form_class = TeacherCreationForm
    template_name = "registration/create_teacher.html"
    success_url = reverse_lazy("english:dashboard")


class GroupListView(LoginRequiredMixin, generic.ListView):
    model = Groups
    template_name = "dashboard/group_list.html"
    paginate_by = 8
    queryset = Groups.objects.prefetch_related("teacher")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = GroupSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        form = GroupSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return self.queryset


class GroupDetailView(LoginRequiredMixin, generic.DetailView):
    model = Groups
    template_name = "dashboard/group_detail.html"

    def get_queryset(self):
        return super().get_queryset().prefetch_related('teacher')


class GroupCreateView(LoginRequiredMixin, generic.CreateView):
    model = Groups
    fields = "__all__"
    template_name = "forms/group_form.html"
    success_url = reverse_lazy("english:group-list")


class GroupUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Groups
    fields = "__all__"
    success_url = reverse_lazy("english:group-list")
    template_name = "forms/group_form.html"


class GroupDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Groups
    template_name = "forms/group_delete_confirm.html"
    success_url = reverse_lazy("english:group-list")


class StudentsListView(LoginRequiredMixin, generic.ListView):
    model = Student
    template_name = "dashboard/students_list.html"
    queryset = Student.objects.select_related("group")
    paginate_by = 8
    ordering = ("surname",)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StudentsListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = StudentSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        form = StudentSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return self.queryset



class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Student
    template_name = "dashboard/student_detail.html"


class StudentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Student
    fields = "__all__"
    template_name = "forms/student_form.html"
    success_url = reverse_lazy("english:students-list")


class StudentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Student
    template_name = "forms/student_delete_conformation.html"
    success_url = reverse_lazy("english:students-list")


class StudentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Student
    fields = "__all__"
    template_name = "forms/student_form.html"
    success_url = reverse_lazy("english:students-list")

class LessonListView(LoginRequiredMixin, generic.ListView):
    model = Lesson
    template_name = "dashboard/lesson_list.html"
    queryset = Lesson.objects.select_related('teacher', 'group')
    paginate_by = 8
    ordering = ("start_time",)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LessonListView, self).get_context_data(**kwargs)
        topic = self.request.GET.get("topic", "")
        context["search_form"] = LessonSearchForm(
            initial={
                "topic": topic
            }
        )
        return context

    def get_queryset(self):
        form = LessonSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                topic__icontains=form.cleaned_data["topic"]
            )
        return self.queryset


class LessonUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Lesson
    fields = "__all__"
    template_name = "forms/lesson_form.html"
    success_url = reverse_lazy("english:lesson-list")


class LessonDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Lesson
    template_name = "forms/lesson_delete_confirm.html"
    success_url = reverse_lazy("english:lesson-list")


class LessonCreateView(LoginRequiredMixin, generic.CreateView):
    model = Lesson
    fields = "__all__"
    success_url = reverse_lazy("english:lesson-list")
    template_name = "forms/lesson_form.html"
