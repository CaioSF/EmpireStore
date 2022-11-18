
from django.contrib import admin
from django.urls import path, include
from addresses.views import checkout_address_create_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplic.urls')),
    path('products/', include("products.urls", namespace="products")),
    path('search/', include("search.urls", namespace="search")),
    path('cart/', include("carts.urls", namespace="cart")),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
]