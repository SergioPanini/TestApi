from rest_framework import serializers
from .models import Apps

class AppSer(serializers.Serializer):
    Name = serializers.CharField()
    Des = serializers.CharField()
    KeyApi = serializers.CharField()

    def create(self, validated_date):
        return Apps.objects.create(**validated_date)
