from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from english.models import Teacher, Lesson, Groups, Student


@admin.register(Teacher)
class TeacherAdmin(UserAdmin):
    ordering = ("full_name",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["topic", "group", "teacher", "created_time"]
    search_fields = ("topic", "teacher", "group",)


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "progress"]
    ordering = ("level",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ("full name", {
           'fields': ("name", "surname",)
        }),
    )
    ordering = ("surname",)
    search_fields = ("name", "surname", "email",)

admin.site.unregister(Group)
