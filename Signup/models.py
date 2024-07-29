from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

class AppUserManager(BaseUserManager):
    def create_user(self, email, user_type, username, password=None):
        if user_type == 'Customer':
            if not email: 
                raise ValueError('An email is required.')
            if not password:
                raise ValueError('A password is required.')
            email = self.normalize_email(email=email)
            user = self.model(
                email=email,
                user_type=user_type,
                username=username,
            )
            user.set_password(password)
            user.save()
        elif user_type == 'Customer': 
            if not email:
                raise ValueError('An email is required.')
            if not password:
                raise ValueError('A password is required')
            user = self.create_user(email, user_type, username, password)
            user.save()
        #Create new variables for vendor


#Specifying Choices

USER_TYPE_CHOICES = (
    ("vendor", "Vendor"),
    ("Customer", "Customer")
)

class AppUser(AbstractBaseUser):
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='')
    user_id = models.AutoField(primary_key=True)
    # username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=150)
    # phone_number = models.

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type', 'username']

class Vendor(models.Model):
    business_name = models.CharField(max_length=100)
    overview = models.TextField()
    contact_firstname = models.CharField(max_length=30)
    contact_lastname = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=100)
    beneficiary_name = models.CharField(max_length=100)
    account_number = models.IntegerField()


class Customer(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)