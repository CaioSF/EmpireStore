from re import A
from django.contrib import admin

from .models import Produto, Cliente, Funcionario, Endereco, Cargo, Estoque, Forma_pagamento, Compra_fornecedor, Fornecedor



@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nascimento')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo',)

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nascimento', 'salario')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'marca', 'modelo', 'descricao')

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('end_logradouro', 'end_numero', 'end_cep', 'end_bairro', 'end_uf', 'end_cidade', 'end_complemento')

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('quantidade',)

@admin.register(Forma_pagamento)
class Forma_pagamentoAdmin(admin.ModelAdmin):
    list_display = ('forma_pagamento',)

@admin.register(Compra_fornecedor)
class Compra_fornecedorAdmin(admin.ModelAdmin):
    list_display = ('quantidade', 'tipo', 'marca', 'modelo', 'xml',)

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'inscricao_estadual', 'razao_social', 'contato',)
