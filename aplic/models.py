from django.db import models
from django.db.models import Model

class Endereco(models.Model):
    end_logradouro = models.CharField('Logradouro', max_length=200)
    end_numero = models.CharField('Número', blank=True, max_length=10)
    end_cep = models.CharField('CEP', max_length=10)
    end_bairro = models.CharField('Bairro', max_length=30)
    end_uf = models.CharField('UF', max_length=2)
    end_cidade = models.CharField('Cidade', max_length=40)
    end_complemento = models.CharField('Complemento', max_length=30)

    class Meta:
        abstract = False
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.end_logradouro


class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    data_nascimento = models.DateField('Data de Nascimento', blank=True, null=True, help_text='Formato DD/MM/AAAA')


    class Meta:
        abstract = True
        verbose_name = 'Usuário'
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.nome

class Cliente(Usuario, Endereco):
    id_cliente = models.CharField('ID', max_length=5)
    email = models.EmailField('email', max_length=200)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT, related_name="clientes")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Funcionario(Usuario, Endereco):
    id_funcionario = models.CharField('ID', max_length=5)
    OPCOES = (
        ('Gerente', 'Gerente'),
        ('Atendente', 'Atendente'),
    )
    cargo = models.CharField('Cargo', blank=True, max_length=100, choices=OPCOES)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT, related_name="funcionarios")

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Produto(models.Model):
    cod_produto = models.CharField('Código', max_length=100)
    descricao = models.TextField('Descrição', max_length=500)
    lote = models.CharField('Lote', max_length=30)


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.cod_produto


class Compra(Model):
    valor = models.DecimalField('Preço', max_digits=5, decimal_places=2)
    quantidade = models.IntegerField('Quantidade')
    cod_produto = models.CharField('Código', max_length=20)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"


