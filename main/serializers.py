from rest_framework import serializers
from . import models


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Service
        fields = "__all__"

class NewsServiceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.NewsService
        fields = "__all__"

class NewsIntrestSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.NewsIntrest
        fields = "__all__"

class SocialIntrestSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.SocialIntrest
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Category
        fields = ("id", "name", "services")


class NewsReportSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.NewsReport
        fields = "__all__"

class ToneSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Tone
        fields = "__all__"


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Format
        fields = "__all__"
