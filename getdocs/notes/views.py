from rest_framework import viewsets
from . import serializers
from . import models
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .permissions import AllowAnyForGet

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [AllowAnyForGet]

    # def get_permissions(self):
    #     self.permission_classes = [AllowAny]
    #     if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
    #         self.permission_classes = [IsAdminUser]
    #     return super().get_permissions()

class NoteViewSet(viewsets.ModelViewSet):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes = [AllowAnyForGet]

    def perform_create(self, serializer):
        serializer.save(uploader=self.request.user)