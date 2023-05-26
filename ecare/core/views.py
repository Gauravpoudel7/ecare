from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST.get("usernamep")
        password = request.POST.get("passp")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("patient")
        else:
            return redirect("home")
    else:
        return render(request, "home.html")


def patient(request):
    return render(request, "patient.html")
