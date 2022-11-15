from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView 
from django.urls import path
from django.views.generic import TemplateView
from carts.views import cart_home
from accounts.views import login_page, register_page, logout_page
from .views import (home_page, 
                    contact_page
)

urlpatterns = [
	path('', home_page, name='home'),
	path('contact/', contact_page, name='contact'),
    path('cart/', cart_home, name='cart'),
    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_page, name='register'),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
