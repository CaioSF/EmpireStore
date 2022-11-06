from django.urls import path
from .views import index, SuporteView, PedidosView, entrar, cadastro, cart_home

urlpatterns = [
    path('', index, name='index'),
    path('suporte/', SuporteView.as_view(), name='suporte'),
    path('pedidos/', PedidosView.as_view(), name='pedidos'),
    path('entrar/', entrar, name='entrar'),
    path('cadastro/', cadastro, name='cadastro'),
    path('cart/', cart_home, name='cart'),
]

