from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category

    list_display = ["name"]
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    model = Product

    list_display = ["name", "price", "size"]
    search_fields = ("name",)
    ordering = ("name",)
