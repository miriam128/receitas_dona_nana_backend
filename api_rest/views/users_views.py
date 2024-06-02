from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from ..serializers.users_serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers.token_serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['POST'])
def login(request):
    serializer = CustomTokenObtainPairSerializer(data=request.data)
    if serializer.is_valid():
        token_pair = serializer.validated_data
        access_token = str(token_pair['access'])
        refresh_token = str(token_pair['refresh'])
        return Response({
            'access_token': 'Bearer ' + access_token,
            'refresh_token': refresh_token,
        })
    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
