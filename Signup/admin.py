from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser
# from Signup.models import Vendor, Customer

# Register your models here.

# admin.site.register(Customer)
# admin.site.register(Vendor)

@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    model = AppUser
    list_display = ["email", "username", "is_staff", "is_active"]

    search_fields = ("email",)
    ordering = ("email",)
