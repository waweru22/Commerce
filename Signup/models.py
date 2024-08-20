from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import AppUserManager
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class AppUser(AbstractBaseUser, PermissionsMixin):
    # user_id = models.AutoField(primary_key=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=150)
    username = models.CharField(max_length=50, unique=True)
    phone_no = PhoneNumberField(unique=True) 

    # is_admin = models.BooleanField(default=False)
    # is_customer = models.BooleanField(default=False)
    # is_vendor = models.BooleanField(default=False)

    objects = AppUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    

class Vendor(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name="vendor")
    
    business_name = models.CharField(max_length=100)
    overview = models.TextField()
    contact_firstname = models.CharField(max_length=30)
    contact_lastname = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=100)
    beneficiary_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=15)

    # user = models.OneToOneField(AppUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name

    def get_user(self):
        return self.user

class Customer(models.Model):  
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name="customer")
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    def __str__(self):
        fn_upper = self.firstname.title()
        ln_upper = self.lastname.title()
        return f"{ln_upper}, {fn_upper}"

# {
# "user_type": "customer",
# "username": "customer1",
# "email": "customer1@gmail.com",
# "password": "1111",
# "address": "No 9, Nunya Business Crescent",
# "firstname": "Nunya",
# "lastname": "Business"
# }





# {
#     "user_type": "vendor",
#     "email": "first@gmail.com",
#     "address": "10, x street, lagos",
#     "username": "First",
#     "business_name": "business1",
#     "contact_firstname": "contactfn1",
#     "contact_lastname": "contactln1",
#     "bank_name": "GTB",
#     "beneficiary_name": "beneficiary1",
#     "account_number": "09128722496",
#     "firstname": "first",
#     "lastname": "user",
#     "password": "1111"
# }

    
