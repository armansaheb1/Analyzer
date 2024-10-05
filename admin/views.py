from django.shortcuts import render

from main import models
from main import serializers
from rest_framework.response import Response
from rest_framework.views import APIView


class Services(APIView):
    def get(self, request):
        query = models.Service.objects.all()
        serializer = serializers.ServiceSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ServiceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                category=models.Category.objects.get(id=request.data["category"])
            )
        query = models.Service.objects.all()
        serializer = serializers.ServiceSerializer(query, many=True)
        return Response(serializer.data)
