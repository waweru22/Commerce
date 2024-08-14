from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import generics
from .serializers import AppUserSerializer, VendorSerializer, CustomerSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from Signup.models import AppUser
from .serializers import AppUserSerializer

from rest_framework.permissions import AllowAny

@api_view(['GET'])
def getData(request):
    users = AppUser.objects.all()
    serializer = AppUserSerializer(users, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def addUser(request):
#     serializer = AppUserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

class Users(APIView):
    permission_classes = ( AllowAny, )
    queryset = AppUser.objects.all()

    # def get(self, request, format=None):
    #     users = AppUser.objects.all()
    #     serializer = AppUserSerializer(users, many=True)
    #     return Response(serializer.data)
    
    def post(self, request):
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            user = serializer.save()
            print(serializer.data)
            print(user)

            
            return Response(serializer.data)
        
# TODO: Create endpoints to display vendors and customers

        
       