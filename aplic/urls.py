from django.urls import path
from .views import index, SuporteView, PedidosView, entrar, cadastro, cart_home, ProdutoListView, ProdutoDetailView

urlpatterns = [
    path('', index, name='index'),
    path('suporte/', SuporteView.as_view(), name='suporte'),
    path('pedidos/', PedidosView.as_view(), name='pedidos'),
    path('entrar/', entrar, name='entrar'),
    path('cadastro/', cadastro, name='cadastro'),
    path('produtos/', ProdutoListView.as_view(), name='produttos'),
    path('produtos/<int:pk>', ProdutoDetailView.as_view()),
    path('cart/', cart_home, name='cart'),
]

