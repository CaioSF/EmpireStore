from django.db import models
from django import forms


class Produto(models.Model):
    cod_produto = models.CharField('Codigo', max_length=100)
    descricao = models.TextField('Descrição', max_length=500)
    lote = models.CharField('Lote', max_length=30)



    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.cod_produto