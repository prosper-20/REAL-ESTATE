from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Property, Favourite
from .serializers import PropertySerializer, FavouriteSerializer, GetFavouriteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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
        print(property.agent)
        print(request.user)
        if request.user != property.agent:
            return Response({"Access Denied": "You do not have the right to edit this property"})
        elif request.user.is_agent == False:
            return Response({"Error": "Only agents can edit properties"})
        
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
            status=status.HTTP_NO_CONTENT
        )
    

class AddFavouriteProperty(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = FavouriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new = serializer.save()
        return Response({
            "Success": "Property has been successfully added",
            "username": new["username"],
            "title": new["property"]
        }, status=status.HTTP_201_CREATED)
    

class GetFavouriteProperty(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = request.user
        all_favourites = Favourite.objects.filter(user=user)
        serializer = GetFavouriteSerializer(all_favourites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class SimilarPropert(APIView):
    def get(self, request, **kwargs):
        id = kwargs["id"]
        slug = kwargs["slug"]
        current_property = Property.objects.get(id=id, slug=slug)
        serializer = PropertySerializer(current_property)
        return Response(serializer.data, status=status.HTTP_200_OK)