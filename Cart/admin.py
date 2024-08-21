from django.contrib import admin
from .models import Cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart
        fields = '__all__'


