from django.db import models


class registerp(models.Model):
    hospital = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    blood_group = models.CharField(max_length=10)
    phone_num = models.IntegerField()
    dob = models.IntegerField()
    sex = models.CharField(max_length=30)


# Create your models here.
