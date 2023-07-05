from rest_framework import serializers
from .models import Property, Favourite, Review
from users.models import User


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["user", "property", "rating", "comments"]

class FavouriteSerializer(serializers.Serializer):
    property_title = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)

    def validate(self, attrs):
        username = attrs.get("username")
        property = attrs.get("property_title")
        if not Property.objects.filter(title=property):
            raise ValueError({"Error": "That property title doesn't exist"})
        
        if not User.objects.get(username=username):
            raise ValueError({"Message": "User not found"})
        
        return attrs


    def create(self, validated_data):
        property = validated_data["property_title"]
        username = validated_data["username"]
        get_property = Property.objects.get(title=property).id
        user = User.objects.get(username=username)
        new_favourite = Favourite.objects.create(user=user)
        new_favourite.property.add(get_property)
        payload = {
            "property": property,
            "username": username
        }
        return payload
    

class GetFavouriteSerializer(serializers.ModelSerializer):
    property = serializers.SerializerMethodField("get_full_property_display")
    class Meta:
        model = Favourite

        fields = ["property"]

    
    def get_full_property_display(self, obj):
        return PropertySerializer(obj.property.all(), many=True).data

    
    
    


class PropertySerializer(serializers.ModelSerializer):

    city = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    type = serializers.StringRelatedField()
    agent = serializers.SerializerMethodField("agent_username")
    price = serializers.SerializerMethodField("add_commas_to_price")
    class Meta:
        model = Property
        fields = ["id", "title", "slug", "address", "city", "state", "sale_type", "bedrooms", "picture", "type", "price", "agent"]

    
    def agent_username(self, obj):
        return obj.agent.username
    
    def add_commas_to_price(self, obj):
        price_str = str(obj.price)[::-1]
        price_str_with_commas = ",".join(price_str[i:i+3] for i in range(0, len(price_str), 3))
        return price_str_with_commas[::-1]
    


class SimilarPropertySerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField("add_commas_to_price")
    city = serializers.StringRelatedField()
    view_details = serializers.SerializerMethodField("full_details")
    class Meta:
        model = Property

        fields = ["title", "city", "price", "picture", "view_details"]

    
    def full_details(self, obj):
        return f"http://127.0.0.1:8000/api/property/{obj.slug}/{obj.id}"

    
    def add_commas_to_price(self, obj):
        price_str = str(obj.price)[::-1]
        price_str_with_commas = ",".join(price_str[i:i+3] for i in range(0, len(price_str), 3))
        return price_str_with_commas[::-1]