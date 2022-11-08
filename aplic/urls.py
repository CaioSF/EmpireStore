from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import index, entrar, cadastro, cart_home
from .views import (SuporteView,
                    PedidosView,
                    ProductListView,
                    ProductDetailView,
                    ProductFeaturedListView,
                    ProductFeaturedDetailView,
                    ProductDetailSlugView,)



urlpatterns = [
    path('', index, name='index'),
    path('suporte/', SuporteView.as_view(), name='suporte'),
    path('pedidos/', PedidosView.as_view(), name='pedidos'),
    path('entrar/', entrar, name='entrar'),
    path('cadastro/', cadastro, name='cadastro'),  
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view()),
    path('products/<slug:slug>/', ProductDetailSlugView.as_view()),
    path('<slug:slug>/', ProductDetailSlugView.as_view()),
    path('cart/', cart_home, name='cart'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
