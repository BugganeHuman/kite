from django.urls import path, include
from .views import (signup, show_tasks_main, add_task, delete_task,
                    update_task, show_completed_tasks, deleted_completed_task,
                    delete_all_completed_tasks, show_tasks_work, show_update)
urlpatterns = [
    path("", show_tasks_main, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", signup, name="signup"),
    path("add_task/<str:category>/", add_task, name="add_task"),
    path("delete_task/<int:task_id>/", delete_task, name="delete_task"),
    path("update_task/<int:task_id>/", update_task, name="update_task"),
    path("completed_tasks/", show_completed_tasks, name="show_completed_tasks"),
    path("deleted_completed_task/<int:completed_task_id>/", deleted_completed_task,
            name="deleted_completed_task"),
    path("delete_all_completed_tasks/", delete_all_completed_tasks,
            name="delete_all_completed_tasks"),
    path("work/", show_tasks_work, name="show_tasks_work"),
    path("show_update/", show_update, name="show_update")
]