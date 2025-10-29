from rest_framework import serializers
from . import models

class CustomUserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    class Meta:
        model = models.CustomUser
        fields = [
            'id',
            'last_login',
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'is_buyer',
            'is_seller',
        ]
        

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'