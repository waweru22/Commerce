from django.shortcuts import render
from .models import Cart, CartItem
from Products.models import Product
from .serializers import CartSerializer, CartItemSerializer
from django.contrib.auth.decorators import login_required
#REST FRAMEWORK
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

@api_view(['GET'])
def getCartData(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCartItemData(request):
    items = CartItem.objects.all()
    serializer = CartItemSerializer(items, many=True)
    return Response(serializer.data)

class CartItemView(APIView):
    permission_classes = ( IsAuthenticated, )
    authentication_classes = ( TokenAuthentication, SessionAuthentication )

    def post(self, request, format=None, *args, **kwargs):
        data = request.data
        prod_id = data.pop('product_id', '')
        quantity = data.pop('quantity', '')
        product = Product.objects.get(id=prod_id)

        if product:
            cart, created = Cart.objects.get_or_create(owner=request.user, **kwargs)
        
            if cart:
                cart_item = CartItem(product_id=product, quantity=quantity)
                cart.num_of_items += quantity
                price_of_cart_item = product.price * quantity
                cart.total += price_of_cart_item
                cart_item.save()
                cart.save()
                cart_item.cart.add(cart) #Issue here with the cart name

        cart_serializer = CartSerializer(cart)
        cart_item_serializer = CartItemSerializer(cart_item)
        return Response({"Message": "Cart Item added successfully", "cart": cart_serializer.data, "cart_item": cart_item_serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request):
        pass

