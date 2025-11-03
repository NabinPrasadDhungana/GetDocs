from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    # slug = serializers.SerializerMethodField()
    class Meta:
        model = models.Category
        fields = '__all__'

    # def get_slug(self, obj):
    #     ref = obj.name
    #     return ref.lower().replace(' ', '-')

class NoteSerializer(serializers.ModelSerializer):
    # download_count = serializers.IntegerField(read_only=True)
    # uploader = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = models.Note
        fields = [
            'id',
            'title',
            'description',
            'category',
            'file',
            'thumbnail',
            'uploader',
            'created_at',
            'updated_at',
            'is_public',
            'download_count'
        ]
        read_only_fields = ['id', 'download_count','created_at', 'updated_at', 'uploader']
    