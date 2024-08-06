from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import AppUser, Vendor
# from Signup.models import Vendor, Customer

# Register your models here.

# admin.site.register(Customer)
# admin.site.register(Vendor)

@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    model = AppUser
    fieldsets=(
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': ('address',) }),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('date_joined',),})
         
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('firstname', 'lastname'),
        })
    )

    list_display = ["email", "username", "is_staff", "is_active"]
    readonly_fields = ["date_joined"]

    search_fields = ("email",)
    ordering = ("email",)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    model = Vendor

    list_display = ["business_name"]
    search_fields = ("business_name",)
    ordering = ("business_name",)
