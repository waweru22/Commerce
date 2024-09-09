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
    authentication_classes = ( SessionAuthentication, TokenAuthentication, )

    def post(self, request, format=None):

        if request.user.is_authenticated:
            return Response({"message": f"User {request.user} Already Signed In"}, status=status.HTTP_200_OK)

        data = request.data

        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        if token:
            return Response({"message": "Logged In Successfully", "token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"Message": "Error Creating Token"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = ( IsAuthenticated, )
    authentication_classes = ( SessionAuthentication, TokenAuthentication, )
    def get(self, request):
        if request.user.auth_token:
            request.user.auth_token.delete()
            logout(request)
            return Response({"message": "User Successfully Logged Out"}, status=status.HTTP_200_OK)
        return Response({"message": "User Does Not Have An Auth Token"}, status=status.HTTP_401_UNAUTHORIZED)
