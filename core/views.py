from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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



def add_task(request):
    if request.method == "POST":
        task =  Task(task=request.POST.get("task"), owner_id=request.user.id)
        if task:
            task.save()
            return redirect("home")

@login_required
def show_tasks(request):
    tasks = Task.objects.values_list("task", flat=True).filter(owner_id=request.user.id)
    context = {
        "tasks": tasks
    }
    return render(request, "core/index.html", context)
    # надо что был типо SELECT task FROM core_task WHERE owner_id == request.user.id
    #HttpResponse (context['tasks'])