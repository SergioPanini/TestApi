from rest_framework import serializers
from .models import APPModels
class AppGetSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=255)
    KeyApi = serializers.CharField(max_length=255)

class AppPostSerializer(serializers.Serializer):
    Name = serializers.CharField()

    def create(self, validated_data):
        return APPModels.objects.create(**validated_data)