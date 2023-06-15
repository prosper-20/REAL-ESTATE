from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Property
from .serializers import PropertySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ApiProprtyHomePage(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer



class ApiPropertyDetailPage(APIView):
    def get(self, request, slug, id):
        property = Property.objects.get(slug=slug, id=id)
        serializer = PropertySerializer(property)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug, id):
        property = Property.objects.get(slug=slug, id=id)
        serializer = PropertySerializer(property, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response({
            "Message": "House details updated ",
            "view_update": f"https://127.0.0.1:800/property/{slug}/{id}/"
        }, status=status.HTTP_201_CREATED)
    
    def delete(self, request, slug, id):
        property = Property.objects.get(slug=slug, id=id)
        property.delete()
        return Response(
            {"Success": "House deleted successfuly!"},
            status=status.HTTP_204_NCO
        )