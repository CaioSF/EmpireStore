from django.contrib import admin

from .models import Produto, Cliente, Funcionario, Endereco


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nascimento')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nascimento', 'cargo')



@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'marca', 'modelo', 'descricao')


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('end_logradouro', 'end_numero', 'end_cep', 'end_bairro', 'end_uf', 'end_cidade', 'end_complemento')