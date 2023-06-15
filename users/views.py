from django.shortcuts import render
from .serializers import UserRegistrationSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

class ApiUserRegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"Success": "User account creation successful",
                         "name": user.username,
                         "email": user.email}, status=status.HTTP_201_CREATED)
    
        
