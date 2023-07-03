from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Property, Favourite
from .serializers import PropertySerializer, FavouriteSerializer, GetFavouriteSerializer, SimilarPropertySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

class ApiProprtyHomePage(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def perform_create(self, serializer):
        serializer.save(agent=self.request.user)




# class ApiPropertyDetailPage(APIView):
#     def get(self, request, slug, id):
#         property = Property.objects.get(slug=slug, id=id)
#         serializer = PropertySerializer(property)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, slug, id):
#         property = Property.objects.get(slug=slug, id=id)
#         print(property.agent)
#         print(request.user)
#         if request.user != property.agent:
#             return Response({"Access Denied": "You do not have the right to edit this property"})
#         elif request.user.is_agent == False:
#             return Response({"Error": "Only agents can edit properties"})
        
#         serializer = PropertySerializer(property, data=request.data, partial=True)
#         serializer.is_valid()
#         serializer.save()
#         return Response({
#             "Message": "House details updated ",
#             "view_update": f"https://127.0.0.1:800/property/{slug}/{id}/"
#         }, status=status.HTTP_201_CREATED)
    
#     def delete(self, request, slug, id):
#         property = Property.objects.get(slug=slug, id=id)
#         property.delete()
#         return Response(
#             {"Success": "House deleted successfuly!"},
#             status=status.HTTP_NO_CONTENT
#         )


class ApiPropertyDetailPage(APIView):
    def get(self, request, **kwargs):
        slug = kwargs.get("slug")
        id = kwargs.get("id")
        print(slug)

        if slug and not id:
            print("yes")
            property = Property.objects.get(slug=slug)
        elif id and not slug:
            print("no")
            property = Property.objects.get(id=id)
        elif id and slug:
            property = Property.objects.get(slug=slug, id=id)
        serializer = PropertySerializer(property)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    

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

class NewAddFavouriteProperty(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, slug, id, format=None):
        try:
            property = Property.objects.get(slug=slug, id=id)
        except Property.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user = request.user
        if property in Favourite.objects.get(user=user).property.all():
            return Response({"Message": "Property already exists in your collection"})
        user_favourite = Favourite.objects.get(user=request.user)
        user_favourite.property.add(property)
        user_favourite.save()
        return Response({"Message": "Propety has been added successfully!!"})
        

    

class GetFavouriteProperty(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = request.user
        all_favourites = Favourite.objects.filter(user=user)
        serializer = GetFavouriteSerializer(all_favourites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class SimilarProperty(APIView):

    def get(self, request, **kwargs):
        id = kwargs["id"]
        slug = kwargs["slug"]
        print(id, slug)
        current_property = Property.objects.get(id=id, slug=slug)
        city_id = current_property.city
        similar_properties = Property.objects.filter(bedrooms=current_property.bedrooms) | Property.objects.filter(agent=current_property.agent.id) | Property.objects.filter(city=current_property.city)
        serializer = SimilarPropertySerializer(similar_properties, many=True)
        return Response({"Message":"Similar properties you may like",
                         "Property details": serializer.data}, status=status.HTTP_200_OK)