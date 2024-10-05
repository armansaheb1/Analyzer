from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main import models

import google.generativeai as genai
import os
import urllib.request
import json

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        past = ""
        today = ""
        for itemm in models.NewsSite.objects.all():
            fp = urllib.request.urlopen(itemm.url)
            mybytes = fp.read()

            mystr = mybytes.decode("utf8")
            fp.close()
            prompt = f"give me only a dict with pic,description and title from news in {mystr} "
            response = model.generate_content(prompt).text
            response = response.replace("```json", "").replace("```", "")
            today = today + response + "\n\n\n"
        for item in models.NewsReport.objects.all():
            past = past + item.title + "\n"
        for item in models.NewsIntrest.objects.all():

            prompt = f"give me only a dict with pic,description and title from news related to {item.subject} or it's subject if it's subject is not in the {past} based on {today} "
            response = model.generate_content(prompt).text
            response = response.replace("```json", "").replace("```", "")
            response = json.loads(response)
            print(response)
            for item in response:
                models.NewsReport.objects.create(
                    title=item.title, text=item.description, pic=item.pic
                )
            print("Done")
