from django.db.models import Q
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse


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


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active = True)

    def featured(self):
        return self.filter(featured = True, active=True)
    
    def search(self, query):
        lookups = (
            Q(title__contains = query) | 
            Q(descricao__contains = query) | 
            Q(valor__contains = query)
        )
        return self.filter(lookups).distinct()


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def all(self):
        return self.get_queryset().active()

    def featured(self):
        #self.getqueryset().filter(featured = True)
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Product(models.Model):
    OPCOES = (
        ('Mouse', 'Mouse'),
        ('Teclado', 'Teclado'),
        ('Headset', 'Headset'),
        ('Controle', 'Controle'),
        ('Caixa de Som', 'Caixa de Som'),
    )
    tipo = models.CharField('Tipo', blank=True, max_length=20, choices=OPCOES)
    slug = models.SlugField(blank=True, unique=True)
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=30)
    descricao = models.TextField('Descricao', max_length=10000)
    valor = models.DecimalField('Valor', max_digits=6, decimal_places=2)
    title = models.CharField('title', max_length=250, default='Product')
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    featured = models.BooleanField(default = False)
    active = models.BooleanField(default = True)

    class Meta: 
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    objects = ProductManager()

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug = self.slug)
        #return reverse("detail", kwargs={"slug": self.slug})
        

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    pre_save.connect(product_pre_save_receiver, sender = Product)



class Pedido(models.Model):
    data = models.DateField('Data de Nascimento', blank=True, null=True, help_text='Formato DD/MM/AAAA')
    status = models.CharField('Status', max_length=50)
    prazo_entrega = models.DateField('Data de Nascimento', blank=True, null=True, help_text='Formato DD/MM/AAAA')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    valor = models.DecimalField('Valor', max_digits=6, decimal_places=2)
    quantidade = models.IntegerField('Quantidade')


    

class Item_pedido(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade')

    def __str__(self):
        return f"{self.product} {self.quantidade}"
    

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
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


