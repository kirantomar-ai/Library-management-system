from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "phone", "email", "password","address","college")

    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data["name"],
            phone=validated_data["phone"],
            email=validated_data["email"],
            password=validated_data["password"],
            address=validated_data["address"],
            college=validated_data["college"],

        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "phone", "email","address","college")

    
       