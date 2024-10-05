from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers

import google.generativeai as genai
import os
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated, AllowAny

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")


class Categories(APIView):
    def get(self, request):
        query = models.Category.objects.all()
        serializer = serializers.CategorySerializer(query, many=True)
        return Response(serializer.data)


class ServicesOne(APIView):
    def get(self, request, slug):
        query = models.Service.objects.get(slug=slug)
        serializer = serializers.ServiceSerializer(query)
        return Response(serializer.data)


class Services(APIView):
    def get(self, request):
        query = models.Service.objects.all()
        serializer = serializers.ServiceSerializer(query, many=True)
        return Response(serializer.data)


class GBuilder(APIView):
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        query = models.Service.objects.get(slug=slug)
        prompt = query.prompt
        for item in query.variables:
            prompt = prompt.replace(
                "$" + item["name"], request.data["data"][item["name"]]
            )
        response = model.generate_content(prompt)
        return Response(response.text)
