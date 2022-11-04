from django.urls import path
from .views import IndexView, SuporteView, PedidosView, EntrarView, CadastroView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('suporte/', SuporteView.as_view(), name='suporte'),
    path('pedidos/', PedidosView.as_view(), name='pedidos'),
    path('entrar/', EntrarView.as_view(), name='entrar'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
]

