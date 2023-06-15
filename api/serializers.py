from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):

    city = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    type = serializers.StringRelatedField()
    agent = serializers.SerializerMethodField("agent_username")
    class Meta:
        model = Property
        fields = ["id", "title", "slug", "address", "city", "state", "sale_type", "picture", "type", "price", "agent"]

    
    def agent_username(self, obj):
        return obj.agent.username