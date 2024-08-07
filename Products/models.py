from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from Signup.models import AppUser


class Product(AbstractBaseUser):
    vendor = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name

