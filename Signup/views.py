import requests

from rest_framework.views import APIView
from .serializers import AppUserSerializer

from rest_framework import status
from Signup.models import AppUser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
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

class UserRegistration(APIView):
    permission_classes = ( AllowAny, )
    queryset = AppUser.objects.all()

    # def get(self, request, format=None):
    #     users = AppUser.objects.all()
    #     serializer = AppUserSerializer(users, many=True)
    #     return Response(serializer.data) 
    
    def post(self, request):
        serializer = AppUserSerializer(data=request.data)
        password = request.data['password']

        if serializer.is_valid(raise_exception = True):
            user = serializer.save()

            data = serializer.data

            token = self.signupauth({'username': data['username'], 'password': password})

            # print(request.user)

            return Response({"message": "User Created and Logged In Successfully", "token": token}, status=status.HTTP_200_OK)

    def signupauth(self, user):
        # print(user)
        username = user.get('username', None)
        password = user.get('password', None)

        res = requests.post('http://127.0.0.1:8000/auth/', data={
            'username': username,
            'password': password
        })

        if res.status_code==200:
            data = res.json()
            return data['token']
            

# TODO: Create endpoints to display vendors and customers

        
       