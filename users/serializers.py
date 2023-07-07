from rest_framework import status
from rest_framework.response import Response
from .models import User
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True}
        }


    def save(self):
        user = User(
            email = self.validated_data["email"],
            username = self.validated_data["username"]
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"Response": "Both passwords must match"})
        
        user.set_password(password)
        # user.is_active = True
        user.save()
        return user
    


class AgentRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True}
        }


    def save(self):
        user = User(
            email = self.validated_data["email"],
            username = self.validated_data["username"]
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"Response": "Both passwords must match"})
        
        user.set_password(password)
        user.is_agent = True
        user.is_active = True
        user.save()
        return user