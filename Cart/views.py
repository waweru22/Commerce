from django.shortcuts import render
from .models import Cart
from .serializers import CartSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class CartItems(APIView):
    # permission_classes = ( IsAuthenticated, )
    # authentication_classes = ( TokenAuthentication, SessionAuthentication )

    def post(self, request, product_id):
        if request.method == "POST":
            try:
                cart_item = Cart.objects.filter(user=request.user, product=product_id)[0]
            except:
                return Response("No product found")
            try:
                if cart_item:
                    cart_item.quantity += 1
                    cart_item.save()
                else:
                    cart_item = Cart.objects.create(user=request.user, product=product_id)
                cartserializer = CartSerializer(cart_item)
                return Response({"message": "Item added to cart successfully", "cart_item": cartserializer.data}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"message": "Failed to add item", "Error": e}, status=status.HTTP_400_BAD_REQUEST)


        pass
        # return Response({"message": "This is the Cart"}, status=status.HTTP_200_OK)
