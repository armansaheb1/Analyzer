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
        for item in models.Occasion.objects.all():
            item.delete()
        date = str(ShamsiDateTime()).split('-')
        print(date)
        import requests

        url = f'https://holidayapi.ir/jalali/{date[0]}/{date[1]}/{date[2]}'

        res = requests.get(url).content
        res = json.loads(res)
        print(res)
        for item in res['events']:
            prompt = 'مناسبت پایین را بررسی کن و اگر برای ایران ملی و مذهبی نبود یک false جواب بده در غیر این صورت فقط مناسبت را در ۴ کلمه بنویس'+ '\n' +'مناسبت :' + item['description']
            description = response = model.generate_content(prompt).text
            if not 'false' in description and not 'False' in description :
                models.Occasion.objects.create(name = description)