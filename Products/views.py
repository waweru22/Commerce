from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ProductAPI(APIView):
    def get(self, request, format=None):
        return Response({"message": "Iniital Test Successful"}, status=status.HTTP_200_OK)
