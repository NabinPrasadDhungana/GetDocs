from rest_framework import viewsets
from . import serializers
from . import models
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class NoteViewSet(viewsets.ModelViewSet):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes = [IsAuthenticated]