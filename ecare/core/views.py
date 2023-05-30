from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import registerp
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "home.html")


def patient(request):
    return render(request, "patient.html")


def register(request):
    if request.method == "POST":
        fullname = request.POST.get("fullnamereg")
        address = request.POST.get("addreg")
        bloodgroup = request.POST.get("bgreg")
        sex = request.POST.get("sexreg")
        hospital = request.POST.get("hospitalreg")
        email = request.POST.get("emailreg")
        dob = request.POST.get("dobreg")

        if registerp.objects.filter(email=email).exists():
            messages.error(request, "email exists")

        else:
            new_user = registerp(
                full_name=fullname,
                address=address,
                blood_group=bloodgroup,
                email=email,
                hospital=hospital,
                dob=dob,
                sex=sex,
            )
            new_user.save()
            return redirect("home")
    else:
        return render(request, "register.html")


def doctor(request):
    return render(request, "doctor.html")


def patientlogin(request):
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
        return render(request, "patientlogin.html")


def doctorlogin(request):
    if request.method == "POST":
        username = request.POST.get("usernamed")
        password = request.POST.get("passd")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("doctor")
        else:
            return redirect("home")
    else:
        return render(request, "doctorlogin.html")
