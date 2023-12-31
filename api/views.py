from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Property, Favourite, Review, Contact
from .serializers import PropertySerializer, FavouriteSerializer, GetFavouriteSerializer, SimilarPropertySerializer, ReviewSerializer, PropertyContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from .permissions import CanCreatePropertyPermission
from rest_framework import serializers
from django.contrib.auth.models import AnonymousUser
from rest_framework.filters import SearchFilter, OrderingFilter


class ApiProprtyHomePage(ListCreateAPIView):
    ''' This view allows unauthenticated users to
    view a list of vailable properties,and allows authenticated
    users who are agents to upload properties.'''
    
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    search_fields = ["bedrooms", "city__name", "state__name", "sale_type"]
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly, CanCreatePropertyPermission]

    def perform_create(self, serializer):
        serializer.save(agent=self.request.user)


    
# class ApiProprtyHomePage(APIView):
#     search_fields = ["bedrooms", "city__name", "state__name", "sale_type"]
#     filter_backends = [SearchFilter, OrderingFilter]
#     def get(self, request, format=None):
#         queryset = Property.objects.all()
#         serializer = PropertySerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, format=None):
#         user = request.user
#         if user.is_agent == False:
#             return Response({"Error": "Only agents can post properties",
#                              "Agent sign up link": "http:127.0.0.1:8000/users/register/agent/"})
#         print(user)
#         property = Property(agent=request.user)
#         serializer = PropertySerializer(property, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    




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
    '''This returns a single property at a time;
    Alos allows users who are the owners of the property
    to edit and delete their properties.'''
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
    
    def put(self, request, **kwargs):
        slug = kwargs.get("slug")
        id = kwargs.get("id")
        current_user = request.user
        print(current_user)
        if slug and not id:
            property = Property.objects.get(slug=slug)
        elif id and not slug:
            property = Property.objects.get(id=id)
        elif id and slug:
            property = Property.objects.get(slug=slug, id=id)
        if current_user == AnonymousUser:
            raise serializers.ValidationError({"Error": "You are not logged in"})
        elif current_user != property.agent:
            raise serializers.ValidationError({"Error": "You are not the agent of this property!!"})
        
        serializer = PropertySerializer(property, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {"Message": "House details has been updated"}
        data2 = dict(serializer.data)
        data.update(data2)
        return Response(data, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, **kwargs):
        slug = kwargs.get("slug")
        id = kwargs.get("id")
        current_user = request.user
        print(current_user)
        if slug and not id:
            property = Property.objects.get(slug=slug)
        elif id and not slug:
            property = Property.objects.get(id=id)
        elif id and slug:
            property = Property.objects.get(slug=slug, id=id)
        if current_user == AnonymousUser:
            raise serializers.ValidationError({"Error": "You are not logged in"})
        elif current_user != property.agent:
            raise serializers.ValidationError({"Error": "You are not the agent of this property!!"})
        
        property.delete()
        return Response({"Success": "House has been deleted"}, status=status.HTTP_204_NO_CONTENT)
    


class AddPropertyReview(ListCreateAPIView):
    '''This view allows authenticated users to leave their
    reviews about a property.'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        property_id = self.kwargs['id']
        property = Property.objects.get(id=property_id)
        serializer.save(user=self.request.user, property=property)
        return super().perform_create(serializer)

    
    def get_queryset(self):
        property_id = self.kwargs['id']
        queryset = Review.objects.filter(property=property_id)
        return queryset
    

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
    '''
    Returns a list of properties that a user has registered as his/
    her favourites.'''
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = request.user
        all_favourites = Favourite.objects.filter(user=user)
        serializer = GetFavouriteSerializer(all_favourites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class SimilarProperty(APIView):
    '''
        Returns a list of similar properties related
        to the one the use is checking out.
    '''
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
    



class PropertyContactView(ListCreateAPIView):
    # queryset = Contact.objects.all()
    serializer_class = PropertyContactSerializer

    def get_queryset(self):
        property_id = self.kwargs["id"]
        messages = Contact.objects.filter(property=property_id)
        return messages
    
    def perform_create(self, serializer):
        property_id = self.kwargs["id"]
        current_property = Property.objects.get(id=property_id)
        agent = current_property.agent
        serializer.save(property=current_property, agent=agent)
        return super().perform_create(serializer)
    
