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
            login(request, form.save())
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def add_task(request, category):
    if request.method == "POST":
        task =  Task(task=request.POST.get("task"), owner_id=request.user.id, category=category)
        if len(task.task.strip()) > 0  :
            task.save()
            if category == "main":
                return redirect("home")
            elif category == "work":
                return redirect("show_tasks_work")
            return HttpResponse("I don't now where redirect")
        else:
            return redirect("home")

@login_required
def show_tasks_main(request):
    tasks = Task.objects.all().filter(owner_id=request.user.id, category="main")
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
                            owner_id=deleted_task.owner_id,
                            category=deleted_task.category).save()
            deleted_task.delete()
            if deleted_task.category == "main":
                return redirect("home")
            elif deleted_task.category == "work":
                return redirect("show_tasks_work")
            return HttpResponse("I don't now where redirect")
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
            if updating_task.category == "main":
                return redirect("home")
            elif updating_task.category == "work":
                return redirect("show_tasks_work")
            return HttpResponse("I don't now where redirect")
        else:
            return HttpResponse("GET OUT")
    else:
        return redirect("home") # надо сделать интерфейс

@login_required
def show_completed_tasks(request):
    completed_tasks = CompletedTask.objects.all().filter(owner_id=request.user.id)
    context = {
        'completed_tasks': completed_tasks
    }
    return render(request, 'core/completed_tasks.html', context)

@login_required
def delete_all_completed_tasks(request):
    if request.method == "POST":
        deleted_tasks = CompletedTask.objects.filter(owner_id=request.user.id)
        deleted_tasks.delete()
        return redirect("show_completed_tasks")
    else:
        return redirect("show_completed_tasks")

@login_required
def deleted_completed_task(request, completed_task_id):
    if request.method == "POST":
        deleting_completed_task = CompletedTask.objects.get(id=completed_task_id,
        owner_id=request.user.id)
        if deleting_completed_task:
            deleting_completed_task.delete()
            return redirect("show_completed_tasks")
        else:
            return HttpResponse("This record is not exist")
    else:
        return redirect("show_completed_tasks")

@login_required
def show_tasks_work(request):
    if request.method == "GET":
        tasks = Task.objects.all().filter(owner_id=request.user.id, category="work")
        context = {
            "tasks": tasks
        }
        return render(request, "core/work.html", context)
    else:
        return redirect("home")