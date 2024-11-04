from django.shortcuts import render

from main import models
from main import serializers
from rest_framework.response import Response
from rest_framework.views import APIView


class ServicesOne(APIView):
    def get(self, request, slug):
        query = models.Service.objects.get(slug=slug)
        serializer = serializers.ServiceSerializer(query)
        return Response(serializer.data)
    
    def put(self, request, slug):
        query = models.Service.objects.get(slug = slug)
        serializer = serializers.ServiceSerializer(query, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(
                category=models.Category.objects.get(id=request.data["category"])
            )
        
        return Response(serializer.data)



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
    
    def put(self, request, slug):
        query = models.Service.objects.get(slug = slug)
        serializer = serializers.ServiceSerializer(query, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(
                category=models.Category.objects.get(id=request.data["category"])
            )
        
        return Response(serializer.data)

    
    def delete(self, request, id):
        query = models.Service.objects.get(id = id)
        query.delete()
        query = models.Service.objects.all()
        serializer = serializers.ServiceSerializer(query, many=True)
        return Response(serializer.data)

class Formats(APIView):
    def get(self, request):
        query = models.Format.objects.all()
        serializer = serializers.FormatSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.FormatSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        query = models.Format.objects.all()
        serializer = serializers.FormatSerializer(query, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        query = models.Format.objects.get(id = id)
        query.delete()
        query = models.Format.objects.all()
        serializer = serializers.FormatSerializer(query, many=True)
        return Response(serializer.data)

class Tones(APIView):
    def get(self, request):
        query = models.Tone.objects.all()
        serializer = serializers.ToneSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ToneSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        query = models.Tone.objects.all()
        serializer = serializers.ToneSerializer(query, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        query = models.Tone.objects.get(id = id)
        query.delete()
        query = models.Tone.objects.all()
        serializer = serializers.ToneSerializer(query, many=True)
        return Response(serializer.data)


class Categories(APIView):
    def get(self, request):
        query = models.Category.objects.all()
        serializer = serializers.CategorySerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        query = models.Category.objects.all()
        serializer = serializers.CategorySerializer(query, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        query = models.Category.objects.get(id = id)
        query.delete()
        query = models.Category.objects.all()
        serializer = serializers.CategorySerializer(query, many=True)
        return Response(serializer.data)


class NewsServices(APIView):
    def get(self, request):
        query = models.NewsService.objects.all()
        serializer = serializers.NewsServiceSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.NewsServiceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save( )
        query = models.NewsService.objects.all()
        serializer = serializers.NewsServiceSerializer(query, many=True)
        return Response(serializer.data)
