from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets

# Create your views here.
class UserProfileViewset(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer