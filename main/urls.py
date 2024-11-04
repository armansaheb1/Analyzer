"""
URL configuration for Analyzer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("services", views.Services.as_view()),
    path("idea-entries", views.IdeaEntries.as_view()),
    path("static-entries", views.StaticEntries.as_view()),
    path("tones", views.Tones.as_view()),
    path("formats", views.Formats.as_view()),
    path("intrests", views.NewsIntrests.as_view()),
    path("intrests/<id>", views.NewsIntrests.as_view()),
    path("intrests-social/<id>", views.SocialIntrests.as_view()),
    path("intrests-social", views.SocialIntrests.as_view()),
    path("news-services", views.NewsServices.as_view()),
    path("image-services", views.ImageServices.as_view()),
    path("reports", views.Reports.as_view()),
    path("social-reports", views.SocialReports.as_view()),
    path("categories", views.Categories.as_view()),
    path("services/<slug>", views.ServicesOne.as_view()),
    path("gbuilder/<slug>", views.GBuilder.as_view()),
    path("gbuilderwrite", views.GBuilderWrite.as_view()),
    path("gideabuilder", views.GBuilderIdea.as_view()),
    path("gbuilderfile", views.GBuilderFile.as_view()),
    path("gbuilderfilemanual", views.GBuilderFileManual.as_view()),
    path("uploader", views.Uploader.as_view()),
    path("news-services/<id>/<service>/", views.GBuilderNews.as_view()),
]
