from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('restrito/', admin.site.urls),
    path('', include('aplic.urls')),
]
