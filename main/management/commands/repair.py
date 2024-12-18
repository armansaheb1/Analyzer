from main import models

import os
import json
import time
import requests
from openai import OpenAI
from langchain_community.document_loaders import AsyncHtmlLoader, RSSFeedLoader
from django.core.management.base import BaseCommand
from Analyzer import settings
import google.generativeai as genai
import datetime 
from shamsi_datetime import ShamsiDateTime
genai.configure(api_key = settings.GEMINI_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
import openai
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=settings.OPEN_AI_KEY,
)
openai.my_api_key = settings.OPEN_AI_KEY

class Command(BaseCommand):
    def handle(self, *args, **options):
        for site in models.NewsSite.objects.all():
            for service in models.NewsService.objects.all():
                models.NewsLink.objects.create(site = site, service = service)
            
        