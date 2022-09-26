from django.contrib import admin

from .models import Produto, Teste

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('cod_produto', 'descricao', 'lote')

@admin.register(Teste)
class TesteAdmin(admin.ModelAdmin):
    list_display = ('valor', 'nome')

