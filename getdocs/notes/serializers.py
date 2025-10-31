from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    class Meta:
        model = models.Category
        fields = '__all__'

    def get_slug(self, obj):
        ref = obj.name
        slug = list(ref)
        return ref.lower().replace(' ', '-')

class NoteSerializer(serializers.ModelSerializer):
    download_count = serializers.IntegerField(read_only=True)
    uploader = serializers.SerializerMethodField()
    class Meta:
        model = models.Note
        fields = '__all__'
    
    def get_uploader(self, obj):
        request = self.context.get('request')
        user = request.user if request else None
        return user.username if user else None
    