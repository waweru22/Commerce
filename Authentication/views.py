from rest_framework import status
from rest_framework.views import APIView
from .serializers import LoginSerializer
from rest_framework.response import Response

class LoginView(APIView):
    def post(self, request, format=None):

        if request.user.is_authenticated:
            return Response({"message": "User Already Signed In"}, status=status.HTTP_200_OK)

        data = request.data

        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return Response({"message": "Positive Test"}, status=status.HTTP_200_OK)
        # user = serializer.validated_data["user"]
