from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    download_count = serializers.IntegerField(read_only=True)
    uploader = serializers.SerializerMethodField()
    class Meta:
        model = models.Note
        fields = '__all__'
    
    def get_uploader(self, obj):
        request = self.context.get('request')
        return request.user if request else None
    