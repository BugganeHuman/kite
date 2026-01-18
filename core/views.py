from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Task

def signup(request):
    print("start signup")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("2------------")
            login(request, form.save())
            print(form)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def add_task(request):
    if request.method == "POST":
        task =  Task(task=request.POST.get("task"), owner_id=request.user.id)
        if task:
            task.save()
            return redirect("home")

@login_required
def show_tasks(request):
    tasks = Task.objects.all().filter(owner_id=request.user.id)
    context = {
        "tasks": tasks
    }
    return render(request, "core/index.html", context)
    # типо SELECT task FROM core_task WHERE owner_id == request.user.id

@login_required
def delete_task(request, task_id):
    print("executed delete_task")
    if request.method == "POST":
        deleted_task = Task.objects.filter(id = task_id)
        print(deleted_task)
        deleted_task.delete()
        return redirect("home")