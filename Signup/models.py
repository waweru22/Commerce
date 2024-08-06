from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import AppUserManager
import uuid

# Create your models here.

class AppUser(AbstractBaseUser, PermissionsMixin):
    # user_id = models.AutoField(primary_key=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    email = models.EmailField()
    date_joined = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=150)
    username = models.CharField(max_length=50, unique=True, default=uuid.uuid1)

    # is_admin = models.BooleanField(default=False)
    # is_customer = models.BooleanField(default=False)
    # is_vendor = models.BooleanField(default=False)
    # type = models.CharField(max_length=10, choices=Types.choices, default=Types.CUSTOMER)
    # phone_number = models.

    objects = AppUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # def save(self, *args, **kwargs):
    #     if not self.type or self.type == None:
    #         self.type = AppUser.Types.CUSTOMER
    #     return super().save(*args, **kwargs)

    
    

class Vendor(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="vendor")
    email = models.EmailField()
    username = models.CharField(max_length=50, unique=True, default=uuid.uuid1)
    date_joined = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=150)
    business_name = models.CharField(max_length=100)
    overview = models.TextField()
    contact_firstname = models.CharField(max_length=30)
    contact_lastname = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=100)
    beneficiary_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=9)

    # user = models.OneToOneField(AppUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name


class Customer(models.Model):  
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="customer")
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    # user = models.OneToOneField(AppUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname}, {self.lastname}"



    

    
