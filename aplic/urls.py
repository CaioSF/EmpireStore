from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from .views import home_page, contact_page, login_page, register_page

urlpatterns = [
	path('', home_page),
	path('contact/', contact_page),
    path('login/', login_page),
    path('register/', register_page),
	path('admin/', admin.site.urls),
]
