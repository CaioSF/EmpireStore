from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, entrar, cadastro, cart_home
from .views import (SuporteView,
                    PedidosView,
                    ProdutoListView,
                    ProdutoDetailView,
                    ProdutoFeaturedListView,
                    ProdutoFeaturedDetailView,
                    ProdutoDetailSlugView)

urlpatterns = [
    path('', index, name='index'),
    path('suporte/', SuporteView.as_view(), name='suporte'),
    path('pedidos/', PedidosView.as_view(), name='pedidos'),
    path('entrar/', entrar, name='entrar'),
    path('cadastro/', cadastro, name='cadastro'),  
    path('featured/', ProdutoFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProdutoFeaturedDetailView.as_view()),
    path('produtos/', ProdutoListView.as_view(), name='produtos'),
    path('produtos/<int:pk>', ProdutoDetailView.as_view()),
    path('produtos/<slug:slug>/', ProdutoDetailSlugView.as_view()),
    path('cart/', cart_home, name='cart'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
