from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main import models

import google.generativeai as genai
import os
import urllib.request
import json
import time

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

from django.core.management.base import BaseCommand, CommandError


def get_news():
    past = ""
    today = ""
    for itemm in models.NewsSite.objects.all().order_by("-id"):
        fp = urllib.request.urlopen(itemm.url)
        mybytes = fp.read()

        mystr = mybytes.decode("utf8")
        print(itemm.url)
        fp.close()
        prompt = f"give me only a json dict with pic,description and title from news in {mystr} "
        response = model.generate_content(prompt).text
        response = response.replace("```json", "").replace("```", "")
        today = today + response + "\n\n\n"
    for item in models.NewsIntrest.objects.all():

        prompt = f"give me only a json dict with pic,description and title from json related to {item.subject} or it's subject if it's subject is not in the {past} based on this json {today} "
        response = model.generate_content(prompt).text
        response = response.replace("```json", "").replace("```", "")
        response = json.loads(response)
        for itemm in response:
            if "title" in itemm:
                if not len(models.NewsReport.objects.filter(pic=itemm["pic"])):
                    models.NewsReport.objects.create(
                        title=itemm["title"],
                        text=itemm["description"],
                        pic=itemm["pic"],
                        subject=item.subject,
                    )
        time.sleep(3)


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_news()
