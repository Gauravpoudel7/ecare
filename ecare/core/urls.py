from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("patient", views.patient, name="patient"),
    path("register", views.register, name="register"),
    path("doctor", views.doctor, name="doctor"),
    path("patientlogin", views.patientlogin, name="patientlogin"),
    path("doctorlogin", views.doctorlogin, name="doctorlogin"),
]
