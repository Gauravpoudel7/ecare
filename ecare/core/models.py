from datetime import datetime
from django.db import models
from django.urls import reverse


class registerp(models.Model):
    hospital = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    dob = models.DateField(default=None)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    sex = models.CharField(max_length=30)


# Create your models here.
