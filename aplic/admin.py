from django.contrib import admin

from .models import Produto, Compra, Cliente, Funcionario

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('cod_produto', 'descricao', 'lote')


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('valor', 'quantidade', 'cod_produto')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nascimento', 'id_cliente', 'email', 'end_logradouro', 'end_numero', 'end_cep',
                    'end_bairro', 'end_uf', 'end_cidade', 'end_complemento')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nascimento', 'id_funcionario', 'cargo', 'end_logradouro', 'end_numero', 'end_cep',
                    'end_bairro', 'end_uf', 'end_cidade', 'end_complemento')

