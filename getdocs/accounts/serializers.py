from rest_framework import serializers
from . import models
from django.core.validators import RegexValidator

class CustomUserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    username = serializers.CharField(
        required=True,
        validators=[RegexValidator(
        regex=r'^([a-z_][a-z0-9_]{2,9})$',
        message='Please enter a valid username between 3 and 10 characters long. It must start with a lowercase letter (a-z) or an underscore (_), and can only contain lowercase letters, numbers, or underscores.'
    )]
    )
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
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