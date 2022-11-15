from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from .views import home_page, contact_page, login_page, register_page
from products.views import (ProductListView, 
                            ProductDetailView, 
                            ProductDetailSlugView,
                            ProductFeaturedListView,
                            ProductFeaturedDetailView)

urlpatterns = [
	path('', home_page),
	path('contact/', contact_page),
    path('login/', login_page),
    path('register/', register_page),
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view()),
    path('products/<slug:slug>/', ProductDetailSlugView.as_view()),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
