from django.urls import path
from english.views import index, DashboardListView


urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", DashboardListView.as_view(), name="dashboard")
]

app_name = "english"
