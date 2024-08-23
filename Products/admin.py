from django.contrib import admin
from .models import Category, Product, Image

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

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    model = Image

    list_display = ("id", "image")
    