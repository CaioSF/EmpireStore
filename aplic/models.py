from statistics import quantiles
from django.db import models
from django.forms import IntegerField
from django.conf import settings


class Endereco(models.Model):
    end_logradouro = models.CharField('Logradouro', max_length=200)
    end_numero = models.CharField('Numero', blank=True, max_length=10)
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
    email = models.EmailField('email', max_length=200)
    senha = models.CharField('Senha', max_length=20)

    class Meta:
        abstract = True
        verbose_name = 'Usuário'
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.nome

class Cliente(Usuario):
    contato = models.CharField('Contato:', null=True, max_length=11, help_text='DDD + Número de telefone')
    endereco = models.ForeignKey(Endereco, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class Cargo(models.Model):
    OPCOES = (        
        ('Gerente', 'Gerente'),
        ('Atendente', 'Atendente'),
        ('Faturista', 'Faturista'),
    )
    cargo = models.CharField('Cargo', blank=True, max_length=20, choices=OPCOES)
    

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo



class Funcionario(Usuario):
    cargo = models.ForeignKey(Cargo, blank=True, on_delete=models.DO_NOTHING)
    salario = models.DecimalField('Salário', max_digits=6, decimal_places=2)
    endereco = models.ForeignKey(Endereco, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return self.nome

class Produto(models.Model):
    OPCOES = (
        ('Mouse', 'Mouse'),
        ('Teclado', 'Teclado'),
        ('Headset', 'Headset'),
        ('Controle', 'Controle'),
        ('Caixa de Som', 'Caixa de Som'),
    )
    tipo = models.CharField('Tipo', blank=True, max_length=20, choices=OPCOES)
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=30)
    descricao = models.TextField('Descricao', max_length=500)
    valor = models.DecimalField('Valor', max_digits=6, decimal_places=2)
    image = models.FileField(upload_to='produtos/')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


    def __str__(self):
        return f"{self.tipo} {self.marca} {self.modelo}"



class Pedido(models.Model):
    data = models.DateField('Data de Nascimento', blank=True, null=True, help_text='Formato DD/MM/AAAA')
    status = models.CharField('Status', max_length=50)
    prazo_entrega = models.DateField('Data de Nascimento', blank=True, null=True, help_text='Formato DD/MM/AAAA')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField('Valor', max_digits=6, decimal_places=2)
    quantidade = models.IntegerField('Quantidade')

    

class Item_pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade')

    def __str__(self):
        return f"{self.produto} {self.quantidade}"
    

class Pagamento_nfe(models.Model):
    valor = models.DecimalField('Valor', max_digits=6, decimal_places=2)
    data = models.DateField('Data de Nascimento', blank=True, null=True, help_text='Formato DD/MM/AAAA')

    def __str__(self):
        return self.valor


class Compra_fornecedor(models.Model):
    quantidade = models.IntegerField('Quantidade')
    OPCOES = (
        ('Mouse', 'Mouse'),
        ('Teclado', 'Teclado'),
        ('Headset', 'Headset'),
        ('Controle', 'Controle'),
        ('Impressora', 'Impressora'),
        ('Caixa de Som', 'Caixa de Som'),
    )
    tipo = models.CharField('Tipo', blank=True, max_length=20, choices=OPCOES)
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=30)
    xml = models.CharField('XML', max_length=99999)

    class Meta:
        verbose_name = 'Compra Fornecedor'
        verbose_name_plural = 'Compra Fornecedores'

    def __str__(self):
        return self.quantidade
    
class Fornecedor(models.Model):
    cnpj = models.CharField('CNPJ', max_length=14)
    inscricao_estadual = models.CharField('Inscrição Estadual', max_length=9)
    razao_social = models.CharField('Razão Social', max_length=50)
    contato = models.EmailField('Contato', max_length=100, help_text='contato@exemplo.com')

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.razao_social

class Forma_pagamento(models.Model):
    OPCOES = (
        ('Boleto', 'Boleto'),
        ('Cartão de crédito', 'Cartão de crédito'),
        ('Cartão de débito', 'Cartão de débito'),
        ('pix', 'pix'),
    )
    forma_pagamento = models.CharField('Forma de pagamento', blank=True, max_length=30, choices=OPCOES)

    class Meta:
        verbose_name = 'Forma de pagamento'
        verbose_name_plural = 'Forma de pagamentos'
    
class Estoque(models.Model):
    quantidade = models.IntegerField('Quantidade')

    class Meta:
        verbose_name = 'Estoque'

    def __str__(self):
        return self.quantidade


User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
            else:
                cart_obj = Cart.objects.new(user=request.user)
                new_obj = True
                request.sessio['cart_id'] = cart_obj.id
            return cart_obj, new_obj

        def new(self, user=None):
            user_obj = None
            if user is not None:
                if user.is_authenticated:
                    user_obj = user
            return self.model.objects.create(user=user_obj)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Produto, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

