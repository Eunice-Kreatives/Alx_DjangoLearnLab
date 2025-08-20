from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "profile_picture"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()  # ✅ CharField included

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        # ✅ uses get_user_model().objects.create_user
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        Token.objects.create(user=user)  # auto-generate token
        return user

