from rest_framework import serializers
from photos.models.photo import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'favorite', 'signature', 'photo', 'author', 'created_at', 'updated_at', 'deleted_at', 'is_deleted')
        read_only_fields = ('created_at', 'updated_at', 'deleted_at', 'is_deleted')
