from django.db import models
from typing import ClassVar
from django.db import models
import datetime
from products.models import Product

class Produto(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=50)


    def __str__(self) -> str:
        return self.nome

class Vendas(models.Model):
    produto = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    total = models.FloatField()
    data = models.DateTimeField(default=datetime.datetime.now())


    def __str__(self):
        return self.nome_produto.nome