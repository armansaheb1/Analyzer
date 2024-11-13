from django.contrib import admin
from .models import CustomUser, Service, Category, ImageService, NewsSite, NewsIntrest, NewsReport, NewsService, SocialIntrest, Tone, Format, StaticEntry, IdeaStaticEntry, File

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(NewsSite)
admin.site.register(NewsIntrest)
admin.site.register(NewsReport)
admin.site.register(NewsService)
admin.site.register(SocialIntrest)
admin.site.register(Tone)
admin.site.register(Format)
admin.site.register(StaticEntry)
admin.site.register(IdeaStaticEntry)
admin.site.register(ImageService)
admin.site.register(File)
