from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Task, CompletedTask

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
        if len(task.task) > 0  :
            task.save()
            return redirect("home")
        else:
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
    print("executing delete_task")
    if request.method == "POST":
        deleted_task = Task.objects.get(id = task_id)
        if request.user.id == deleted_task.owner_id:
            CompletedTask(completed_task=deleted_task.task,
                owner_id=deleted_task.owner_id).save()
            deleted_task.delete()
            return redirect("home")
        else:
            return HttpResponse("GET OUT")
    else:
        return redirect("home")

@login_required
def update_task(request, task_id, new_task):
    if request.method == "POST":
        updating_task = Task.objects.get(id=task_id)
        if request.user.id == updating_task.owner_id:
            updating_task.task = new_task
            updating_task.save()
            #return redirect("home")
        else:
            HttpResponse("GET OUT")
    else:
        redirect("home") # надо сделать интерфейс

@login_required
def delete_all_completed_tasks(request):
    if request.method == "POST":
        deleted_tasks = CompletedTask.objects.filter(owner_id=request.user.id)
        deleted_tasks.delete()
        return redirect("show_completed_tasks")
    else:
        return redirect("show_completed_tasks")

def show_completed_tasks(request):
    completed_tasks = CompletedTask.objects.all()
    context = {
        'completed_tasks': completed_tasks
    }
    return render(request, 'core/completed_tasks.html', context)