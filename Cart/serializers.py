from .models import Cart, CartItem
from rest_framework import serializers 

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["owner", "num_of_items", "total", "updated_at", "created_at"]

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["cart", "product_id", "quantity", "added"]
