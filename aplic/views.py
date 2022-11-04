from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class SuporteView(TemplateView):
    template_name = 'suporte.html'

class PedidosView(TemplateView):
    template_name = 'pedidos.html'

class EntrarView(TemplateView):
    template_name = 'entrar.html'

class CadastroView(TemplateView):
    template_name = 'cadastro.html'
    