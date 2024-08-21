from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import AppUser
# from django import forms
# from phonenumber_field.widgets import PhoneNumberPrefixWidget

# Register your models here.

# admin.site.register(Customer)
# admin.site.register(Vendor)

@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    model = AppUser
    fieldsets=(
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': ('address', 'phone_no') }),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
         
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('firstname', 'lastname'),
        })
    )

    list_display = ["id", "email", "username"]

    search_fields = ("username",)
    ordering = ("id",)

