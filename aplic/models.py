from django.db import models
from django.db.models import Model







class Produto(models.Model):
    cod_produto = models.CharField('Codigo', max_length=100)
    descricao = models.TextField('Descrição', max_length=500)
    lote = models.CharField('Lote', max_length=30)


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.cod_produto


class Teste(Model):
    valor = models.DecimalField('Valor', max_digits=5, decimal_places=2)
    nome = models.CharField('Nome', max_length=100)


    def __str__(self):
        return self.nome



