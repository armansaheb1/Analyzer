from django.contrib import admin
from django.urls import path, include
from Analyzer import settings
from django.conf.urls.static import static

urlpatterns = [
    path("api/v1/admin/", admin.site.urls),
    path("api/v1/", include("main.urls")),
    path("api/v1/adminpanel/", include("admin.urls")),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.authtoken")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
