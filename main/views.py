from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers
import urllib.request
import json
import time
import google.generativeai as genai
import os
import json
from rest_framework.authentication import (
    
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
import sys
import threading
import time

from openai import OpenAI
# from langchain_community.document_loaders import AsyncHtmlLoader, RSSFeedLoader
# from llama_index.core import SimpleDirectoryReader, GPTVectorStoreIndex, StorageContext, load_index_from_storage
# from llama_index.core import Settings
# from llama_index.embeddings.openai import OpenAIEmbedding
# from llama_index.core.node_parser import SentenceSplitter
# from llama_index.llms.openai import OpenAI
# from llama_index.core import Settings
from Analyzer import settings

genai.configure(api_key = settings.GEMINI_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def get_social(subject):
    pass

# def get_news_gpt(subject, user):
#     Settings.llm = OpenAI(model="gpt-4o")
#     Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
#     Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
#     Settings.num_output = 512
#     Settings.context_window = 3900
#     Settings.chunk_size = 2048
#     for itemmm in models.NewsSite.objects.all().order_by("id"):
        
#         documents = str(RSSFeedLoader(urls=[itemmm.url]).load(
            
#         ))
#         with open("/Analyzer/input/copy.txt", 'r+') as f:
#             f.write(documents)
#             f.truncate()     
#         documents = SimpleDirectoryReader('/Analyzer/input').load_data()
#         index = GPTVectorStoreIndex.from_documents(
#             documents
#         )
        
#         index.storage_context.persist(persist_dir='/Analyzer/done')

#         try:
#             prompt = f"full news related to {subject} from context with pic,description and title  as only a json with data field with a list of dics"
#             storage_context = StorageContext.from_defaults(persist_dir='/Analyzer/done')
#             index = load_index_from_storage(storage_context)
#             response = index.as_query_engine().query(prompt)

#             response = response.response
            

            
#             response = response.replace("```json", "").replace("```", "")
#             # print(response)
#             response = json.loads(response)
#             response = response['data']
#             for itemm in response:
#                 if "title" in itemm and "description" in itemm :
#                     if len(itemm["description"]) > 80:
                
#                         models.NewsReport.objects.create(
#                             user= user,
#                             title=itemm["title"],
#                             text=itemm["description"],
#                             subject=subject,
#                             resource=itemmm.name
#                     )
                                
#         except:
#             pass




def get_news(subject):
    today = ""
    for itemm in models.NewsSite.objects.all().order_by("-id"):
        fp = urllib.request.urlopen(itemm.url)
        mybytes = fp.read()

        mystr = mybytes.decode("utf8")
        print(itemm.url)
        fp.close()
        today = today + mystr + "\n\n\n"

        prompt = f"content related to {subject} as only a json with pic,description and title based on {today} "
    response = model.generate_content(prompt).text
    
    response = response.replace("```json", "").replace("```", "")
    print(response)
    response = json.loads(response)
    for itemm in response:
        if "title" in itemm and "pic" in itemm and "description" in itemm:
            if not len(models.NewsReport.objects.filter(pic=itemm["pic"])):
                models.NewsReport.objects.create(
                    title=itemm["title"],
                    text=itemm["description"],
                    pic=itemm["pic"],
                    subject=subject,
                )

class Categories(APIView):
    def get(self, request):
        query = models.Category.objects.all()
        serializer = serializers.CategorySerializer(query, many=True)
        return Response(serializer.data)


class ServicesOne(APIView):
    def get(self, request, slug):
        query = models.Service.objects.get(slug=slug)
        serializer = serializers.UserServiceSerializer(query)
        return Response(serializer.data)


class Services(APIView):
    def get(self, request):
        query = models.Service.objects.all()
        serializer = serializers.UserServiceSerializer(query, many=True)
        return Response(serializer.data)


class NewsServices(APIView):
    def get(self, request):
        query = models.NewsService.objects.all().order_by('-id')
        serializer = serializers.NewsServiceSerializer(query, many=True)
        return Response(serializer.data)
    

class ImageServices(APIView):
    def get(self, request):
        query = models.ImageService.objects.all().order_by('-id')
        serializer = serializers.ImageServiceSerializer(query, many=True)
        return Response(serializer.data)

class NewsIntrests(APIView):
    def get(self, request):
        query = models.NewsIntrest.objects.filter(user=request.user).order_by('-id')
        serializer = serializers.NewsIntrestSerializer(query, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = serializers.NewsIntrestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
        query = models.NewsIntrest.objects.filter(user=request.user).order_by('-id')
        serializer = serializers.NewsIntrestSerializer(query, many=True)
        x = threading.Thread(target=get_news_gpt, args=(request.data['subject'],request.user))
        x.start()
        return Response(serializer.data)
    
    def delete(self, request, id):
        query = models.NewsIntrest.objects.get(id=id).delete()
        query = models.NewsIntrest.objects.filter(user=request.user).order_by('-id')
        serializer = serializers.NewsIntrestSerializer(query, many=True)
        return Response(serializer.data)


class Tones(APIView):
    def get(self, request):
        query = models.Tone.objects.all().order_by('-id')
        serializer = serializers.ToneSerializer(query, many=True)
        return Response(serializer.data)
    
class IdeaEntries(APIView):
    def get(self, request):
        query = models.IdeaStaticEntry.objects.all().order_by('-id')
        serializer = serializers.IdeaStaticEntrySerializer(query, many=True)
        return Response(serializer.data)

class StaticEntries(APIView):
    def get(self, request):
        query = models.StaticEntry.objects.all().order_by('-id')
        serializer = serializers.StaticEntrySerializer(query, many=True)
        return Response(serializer.data)


class Formats(APIView):
    def get(self, request):
        query = models.Format.objects.all().order_by('-id')
        serializer = serializers.FormatSerializer(query, many=True)
        return Response(serializer.data)

class SocialIntrests(APIView):
    def get(self, request):
        query = models.SocialIntrest.objects.all().order_by('-id')
        serializer = serializers.SocialIntrestSerializer(query, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = serializers.SocialIntrestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
        query = models.SocialIntrest.objects.all().order_by('-id')
        serializer = serializers.SocialIntrestSerializer(query, many=True)
        x = threading.Thread(target=get_social, args=(request.data['subject'],))
        x.start()
        return Response(serializer.data)
    
    def delete(self, request, id):
        query = models.SocialIntrest.objects.get(id=id).delete()
        query = models.SocialIntrest.objects.all().order_by('-id')
        serializer = serializers.SocialIntrestSerializer(query, many=True)
        return Response(serializer.data)


class Reports(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if len(models.NewsIntrest.objects.filter(user= request.user)) < 1:
            return Response(1)
        else:
            query = models.NewsReport.objects.filter(user= request.user).order_by('-id')
            serializer = serializers.NewsReportSerializer(query, many=True)
            return Response(serializer.data)

class SocialReports(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if len(models.SocialIntrest.objects.filter(user= request.user)) < 1:
            return Response(1)
        else:
            query = models.NewsReport.objects.all().order_by('-id')
            serializer = serializers.NewsReportSerializer(query, many=True)
            return Response(serializer.data)

class GPTBuilder(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        import logging
        logger = logging.getLogger('django')

        query = models.Service.objects.get(slug=slug)
        prompt = query.prompt
        prompt = prompt + '\n پاسخ باید به شکل html باشد'
        for item in query.static_variables.all():
            if request.data["data2"]['n' + str(item.id)]:
                prompt = prompt + '\n' + item.prompt.replace('$entry', request.data["data2"]['n' + str(item.id)])
        prompt = prompt + '\n متن اصلی : \n' + request.data["maintext"]
        
        logger.info(prompt)
        response = model.generate_content(prompt)
        return Response(response.text)



class GBuilder(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        import logging
        logger = logging.getLogger('django')

        query = models.Service.objects.get(slug=slug)
        prompt = query.prompt
        prompt = prompt + '\n پاسخ باید به شکل html باشد'
        for item in query.static_variables.all():
            if request.data["data2"]['n' + str(item.id)]:
                prompt = prompt + '\n' + item.prompt.replace('$entry', request.data["data2"]['n' + str(item.id)])
        prompt = prompt + '\n متن اصلی : \n' + request.data["maintext"]
        
        logger.info(prompt)
        response = model.generate_content(prompt)
        return Response(response.text)


class GBuilderWrite(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        prompt = f'{request.data["text"]}'
        if request.data["tone"] or request.data["format"] or request.data["prompt"]:
            prompt = prompt + 'را با'
        if request.data["tone"]:
            prompt = prompt + 'لحن' + request.data["tone"] + ','
        if request.data["format"]:
            prompt = prompt + 'فرمت' + request.data["tone"] + ','
        if request.data["prompt"]:
            prompt = prompt + '' + request.data["tone"] + ','
        prompt = prompt + ' با حالت فقط یک اچ تی ام ال و بدون توضیح کد بنویس '
        response = model.generate_content(prompt)
        return Response(response.text)



class GBuilderNews(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id, service):
        query = models.NewsReport.objects.get(id=id)
        service = models.NewsService.objects.get(id=service)
        prompt = 'a brief' + service.prompt
        prompt = prompt + '\n پاسخ باید به شکل html باشد'
        prompt = prompt.replace(
            "$text", f"{query.title} \n {query.text}"
        )
        prompt = prompt + 'return result as only a html without pictures'
        response = model.generate_content(prompt)
        return Response(response.text.replace('```html', '').replace('```', ''))

class GBuilderFile(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        service= models.ImageService.objects.get(id= request.data['id'])
        client = OpenAI(api_key= settings.OPEN_AI_KEY)
        # file = client.files.create( file=open(request.data["file"], "rb"), purpose="fine-tune" ) 
        completion = client.chat.completions.create( model="gpt-4o",
        messages=[ {"role": "system", "content": "You are a helpful assistant that can read Files."}, 
                    { "role": "user", "content": [
                        {
                        "type": "image_url",
                        "image_url": {
                            "url": request.data['file']
                        }
                        }
                    ] 
                    },
                   {"role": "user", "content": service.prompt} ] ) 
        print(completion.choices[0].message) 
        return Response(completion.choices[0].message)

class GBuilderFileManual(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        client = OpenAI(api_key= settings.OPEN_AI_KEY)
        # file = client.files.create( file=open(request.data["file"], "rb"), purpose="fine-tune" ) 
        completion = client.chat.completions.create( model="gpt-4o",
        messages=[ {"role": "system", "content": "You are a helpful assistant that can read Files."}, 
                    { "role": "user", "content": [
                        {
                        "type": "image_url",
                        "image_url": {
                            "url": request.data['file']
                        }
                        }
                    ] 
                    },
                   {"role": "user", "content": request.data['maintext']} ] ) 
        print(completion.choices[0].message) 
        return Response(completion.choices[0].message)



class GBuilderIdea(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        import logging
        logger = logging.getLogger('django')
        prompt = f'\n return only a json list with title and description with article ideas for {request.data["maintext"]}'
        logger.info(prompt + '\n')

        for item in models.IdeaStaticEntry.objects.all():
            if request.data["data"]['n' + str(item.id)]:
                prompt = prompt + '\n' + item.prompt.replace('$entry', str(request.data["data"]['n' + str(item.id)]))

        
        response = model.generate_content(prompt)
        return Response(json.loads(response.text.replace('```json', '').replace('```', '')))


class Uploader(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = serializers.FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)