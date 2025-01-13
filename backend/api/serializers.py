from django.contrib.auth.models import User # importing user model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} # password is not read only so it cannot be accessed by anyone

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user