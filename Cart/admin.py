from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart
        fields = '__all__'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    class Meta:
        model = CartItem
        fields = '__all__'



