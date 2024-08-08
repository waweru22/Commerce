from rest_framework import status
from django.contrib.auth import logout
from .serializers import LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


class LoginView(APIView):
    permission_classes = ( AllowAny, )
    def post(self, request, format=None):

        if request.user.is_authenticated:
            return Response({"message": "User Already Signed In"}, status=status.HTTP_200_OK)

        data = request.data

        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response({"message": "Logged In Successfully", "token": token.key}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = ( IsAuthenticated, )
    authentication_classes = ( SessionAuthentication, TokenAuthentication, )
    def get(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response({"message": "User Successfully Logged Out"}, status=status.HTTP_200_OK)


class TokenTestView(APIView):
    permission_classes = ( IsAuthenticated, )
    authentication_classes = ( SessionAuthentication, TokenAuthentication, )
    def get(self, request):
        return Response({"message": f"Shit worked for {request.user}"})