from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import AppUser, Vendor, Customer
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.formfields import PhoneNumberField

# Register your models here.

# admin.site.register(Customer)
# admin.site.register(Vendor)

@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    model = AppUser
    fieldsets=(
        (None, {'fields': ('email', 'username', 'password', 'user_type')}),
        (_('Personal info'), {'fields': ('address', 'phone_no') }),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('date_joined',),})
         
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('firstname', 'lastname'),
        })
    )

    list_display = ["id", "email", "username", "is_staff", "is_active"]
    readonly_fields = ["date_joined", "user_type"]

    search_fields = ("email",)
    ordering = ("id",)

# class PhoneForm(forms.ModelForm):
#     widgets = {
#         'phone_no': PhoneNumberPrefixWidget()
#     }

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    model = Vendor
    # form = PhoneForm

    list_display = ["business_name"]
    search_fields = ("business_name",)
    ordering = ("business_name",)

# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ["phone_no"]
#         widgets = {
#             "phone_no": PhoneNumberPrefixWidget()
#         }

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    # form = CustomerForm

    list_display = ["id", "lastname", "firstname"]
    search_fields = ("firstname", "lastname")
    ordering = ("id",)
