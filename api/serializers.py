from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):

    city = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    type = serializers.StringRelatedField()
    agent = serializers.SerializerMethodField("agent_username")
    price = serializers.SerializerMethodField("add_commas_to_price")
    class Meta:
        model = Property
        fields = ["id", "title", "slug", "address", "city", "state", "sale_type", "picture", "type", "price", "agent"]

    
    def agent_username(self, obj):
        return obj.agent.username
    
    def add_commas_to_price(self, obj):
        price_str = str(obj.price)[::-1]
        price_str_with_commas = ",".join(price_str[i:i+3] for i in range(0, len(price_str), 3))
        return price_str_with_commas[::-1]