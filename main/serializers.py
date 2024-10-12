from rest_framework import serializers
from . import models


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Service
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Category
        fields = ("id", "name", "icon", "services")


class NewsReportSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.NewsReport
        fields = "__all__"
