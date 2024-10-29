from django.contrib import admin
from .models import CustomUser, Service, Category, NewsSite, NewsIntrest, NewsReport, NewsService, SocialIntrest, Tone, Format, StaticEntry

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

