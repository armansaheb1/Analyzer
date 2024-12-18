from main import models
import google.generativeai as genai
import json
from langchain_community.document_loaders import WebBaseLoader
from Analyzer import settings
from django.core.management.base import BaseCommand
genai.configure(api_key = settings.GEMINI_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def newser():
    print('start')
    for site in models.NewsSite.objects.all():
        for service in models.NewsService.objects.all():
            link = models.NewsLink.objects.get(site= site, service=service)
            loader = WebBaseLoader(
                        web_path = link.url
                    )
            jsons = {}
            jsons[service.id] = {}
            for subservice in models.NewsSubService.objects.all():
                try:
                    prompt = service.prompt
                    prompt = prompt + subservice.prompt
                    
                    prompt = prompt + '\n اخبار به دست آمده را به صورت فقط یک لیست جیسون بدون اضافات و توضیحات ارایه کن . هر آیتم لیست باید دارای دو فیلد title , text  باشد . دقت کن که تیتر کوتاه و متن بلند باشد ولی از ۲۰۰ کاراکتر بیشتر نشود\n'

                    prompt = prompt + f"متن اصلی : {str(loader.load())}"
                    response = model.generate_content(prompt).text.replace('json', '').replace('```', '').replace('```', '')
                    response = json.loads(response)
                    jsons[service.id][subservice.id] = response
                except:
                    jsons[service.id][subservice.id] = None 
        print('Done')
        site.json = jsons
        site.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
            # get_news()
            newser()
