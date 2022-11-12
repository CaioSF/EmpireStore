from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('restrito/', admin.site.urls),
    path('', include('aplic.urls')),
    path('search', include("search.urls", namespace="search")),
    path('email', include('envia_email.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
