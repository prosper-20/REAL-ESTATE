from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Property
from .serializers import PropertySerializer

class ApiProprtyHomePage(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
