from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/v1/admin/", admin.site.urls),
    path("api/v1/", include("main.urls")),
    path("api/v1/adminpanel/", include("admin.urls")),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.authtoken")),
]
