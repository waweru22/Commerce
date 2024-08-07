from django.shortcuts import render

from rest_framework import generics
from .serializers import AppUserSerializer, VendorSerializer, CustomerSerializer

# Create your views here.

#Create view for user details

from rest_framework.response import Response
from rest_framework.decorators import api_view
from Signup.models import AppUser
from .serializers import AppUserSerializer

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

class Users(generics.ListCreateAPIView):
    serializer_class = AppUserSerializer
    queryset = AppUser.objects.all()
    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception = True):
            user = serializer.save()
            print('from post request: ', user)
            serialized_user = AppUserSerializer(user, context=self.get_serializer_context()).data
            print('serialized user data: ', serialized_user)
            return Response(serialized_user)
        
       