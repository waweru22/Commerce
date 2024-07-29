from rest_framework.response import Response
from rest_framework.decorators import api_view
from Signup.models import AppUser
from .serializers import AppUserSerializer

@api_view(['GET'])
def getData(request):
    users = AppUser.objects.all()
    serializer = AppUserSerializer(users, many=True)
    return Response(serializer.data)