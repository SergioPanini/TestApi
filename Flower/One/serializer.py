from rest_framework import serializers
from .models import Apps

class AppSer(serializers.Serializer):
    Name = serializers.CharField()
    Des = serializers.CharField()
    KeyApi = serializers.CharField()

    def create(self, validated_date):
        return Apps.objects.create(**validated_date)

    def update(self, instance, validated_date):
        instance.Name = validated_date.get('Name', instance.Name)
        instance.Des = validated_date.get('Des', instance.Des)
        instance.save()

        return instance

class testser(serializers.Serializer):
    Name = serializers.CharField()
    def create(self, validated_data):
        return Apps.objects.create(**validated_data)