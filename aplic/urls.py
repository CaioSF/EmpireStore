from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


from carts.views import cart_home
from .views import index, entrar, cadastro, suporte, pedidos, logout_page
from .views import (ProductListView,
                    ProductDetailView,
                    ProductFeaturedListView,
                    ProductFeaturedDetailView,
                    ProductDetailSlugView,)


urlpatterns = [
    path('', index, name='index'),
    path('suporte/', suporte, name='suporte'),
    path('pedidos/', pedidos, name='pedidos'),
    path('entrar/', entrar, name='entrar'),
    path('logout/', logout_page, name='logout'),
    path('cadastro/', cadastro, name='cadastro'),  
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view()),
    path('products/<slug:slug>/', ProductDetailSlugView.as_view()),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
    path('cart/', cart_home, name='cart'),
]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
