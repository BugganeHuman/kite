from django.urls import path, include
from .views import signup, show_tasks, add_task, delete_task
urlpatterns = [
    path("", show_tasks, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", signup, name="signup"),
    path("add_task/", add_task),
    path("delete_task/<int:task_id>/", delete_task, name="delete_task"),
]