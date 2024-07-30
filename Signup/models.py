from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

class AppUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email: 
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        user = self.model(
             email = self.normalize_email(email=email),
            username=username,
        )
        user.set_password(password)
        user.save()
        return user
         
    def create_superuser(self, email, username, password):
            user = self.create_user( 
                email = self.normalize_email(email=email), 
                username=username, 
                password=password
                )
            #user.is_admin = True
            user.is_staff = True
            user.is_superuser = True
            user.save()
            return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    user_type = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    #is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    # user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=150)
 
    username = models.CharField(max_length=50)
    # phone_number = models.

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # def save(self, *args, **kwargs):
    #     if not self.type or self.type == None:
    #         self.type = AppUser.Types.CUSTOMER
    #     return super().save(*args, **kwargs)

# class Vendor(models.Model):
#     ven_id = models.OneToOneField(AppUser, on_delete=models.CASCADE)
#     business_name = models.CharField(max_length=100)
#     overview = models.TextField()
#     contact_firstname = models.CharField(max_length=30)
#     contact_lastname = models.CharField(max_length=30)
#     bank_name = models.CharField(max_length=100)
#     beneficiary_name = models.CharField(max_length=100)
#     account_number = models.CharField(max_length=9)


# class Customer(models.Model):
    # cust_id = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    # firstname = models.CharField(max_length=30)
    # lastname = models.CharField(max_length=30)



    

    
