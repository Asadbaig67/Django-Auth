from rest_framework import serializers
from Authentication.models import Custom_User
from django.contrib.auth.models import User


class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            'password',
        ]  # Include the fields you want to serialize


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = "__all__"
