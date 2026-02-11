from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Task, CompletedTask

def signup(request):
    print("start signup")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("form.is_valid")
            login(request, form.save())
            return redirect("home")
        else:
            print("NOT VALID - ", form.errors.as_data())
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def add_task(request, category):
    print("executing add_task")
    print(request.path)
    if request.method == "POST":
        task =  Task(task=request.POST.get("task"),
                    owner_id=request.user.id, category=category)
        if len(task.task.strip()) > 0  :
            task.save()

            tasks = Task.objects.filter(owner_id=request.user.id, category=category)
            if category:
                return render(request, f"core/{category}.html", {"tasks" : tasks} )

            return HttpResponse("I don't now where redirect")
        else:
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return redirect("home")

@login_required
def show_tasks_main(request):
    tasks = Task.objects.all().filter(owner_id=request.user.id,
                category="main").order_by("-position")
    context = {
        "tasks": tasks
    }
    return render(request, "core/main.html", context)
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
            return HttpResponse("")
        else:
            return HttpResponse("GET OUT")
    else:
        return redirect("home")

@login_required
def update_task(request, task_id, tasks_list):
    print(f"task_id= {task_id}")
    if request.method == "POST":
        updating_task = Task.objects.get(id=task_id)
        if request.user.id == updating_task.owner_id:
            updating_task.task = request.POST.get("new_task")
            updating_task.save()
            if tasks_list == "tasks_list_main":
                tasks = Task.objects.filter(owner_id=request.user.id,
                            category="main").order_by("-position")
                return render(request, "core/main.html",
                              {"tasks" : tasks})

            elif tasks_list == "tasks_list_work":
                tasks = Task.objects.filter(owner_id=request.user.id,
                            category="work").order_by("-position")
                return render(request, "core/work.html",
                    {"tasks" : tasks})\

            elif tasks_list == "tasks_list_notes":
                tasks = Task.objects.filter(owner_id=request.user.id,
                            category="notes").order_by("-position")
                return render(request, "core/notes.html",
                    {"tasks" : tasks})

            return HttpResponse("")
        else:
            return HttpResponse("GET OUT")
    else:
        return redirect("home")

def show_update(request, updated_task_id, tasks_list):
    print(f"executing show_update.  updated_task_id={updated_task_id}")
    task = Task.objects.get(id=updated_task_id)
    if request.user.id == task.owner_id:
        context = {
            "task": task,
            "tasks_list" : tasks_list,
        }
        return render(request, "core/partials/update_form.html", context)
    return redirect("home")

@login_required
def show_completed_tasks(request):
    completed_tasks = CompletedTask.objects.all().filter(
                        owner_id=request.user.id).order_by("-id")
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
def delete_completed_task(request, completed_task_id):
    print(f"executing deleted_completed_task")
    if request.method == "POST":
        deleting_completed_task = CompletedTask.objects.get(id=completed_task_id,
        owner_id=request.user.id)
        if deleting_completed_task:
            deleting_completed_task.delete()
            return HttpResponse("")
        else:
            return HttpResponse("This record is not exist")
    else:
        return redirect("show_completed_tasks")

@login_required
def show_tasks_work(request):
    print("executing show_tasks_work")
    if request.method == "GET":
        tasks = Task.objects.all().filter(owner_id=request.user.id,
                        category="work").order_by("-position")
        context = {
            "tasks": tasks
        }
        return render(request, "core/work.html", context)
    else:
        return redirect("home")

@login_required
def show_notes(request):
    if request.method == "GET":
        notes = Task.objects.all().filter(owner_id=request.user.id,
                    category="notes").order_by("-position")
        context = {
            "tasks" : notes,
        }
        return render(request, "core/notes.html", context)
    else:
        return redirect("home")

@login_required
def move_task(request, task_id, direction):
    task = get_object_or_404(Task, id=task_id)

    if direction == "up":
        task.position += 1
        task.save()
    elif direction == "down":
        task.position -= 1
        task.save()

    tasks = Task.objects.filter(category=task.category, owner_id= request.user.id)

    if task.category == "notes":
        return render(request, "core/notes.html", {"tasks" : tasks})
    elif task.category == "work":
        return render(request, "core/work.html", {"tasks": tasks})
    elif task.category == "main":
        return render(request, "core/main.html", {"tasks": tasks})

    return redirect(request.META.get("HTTP_REFERER", "/"))