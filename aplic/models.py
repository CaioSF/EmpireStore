from django.db import models

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

    class Meta:
        abstract = True
        verbose_name = 'Usuário'
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.nome

class Cliente(Usuario):
    email = models.EmailField('email', max_length=200)
    endereco = models.ForeignKey(Endereco, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

class Funcionario(Usuario):
    OPCOES = (
        ('Gerente', 'Gerente'),
        ('Atendente', 'Atendente'),
    )
    cargo = models.CharField('Cargo', blank=True, max_length=100, choices=OPCOES)
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
        ('Impressora', 'Impressora'),
        ('Caixa de Som', 'Caixa de Som'),
    )
    tipo = models.CharField('Tipo', blank=True, max_length=20, choices=OPCOES)
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=30)
    descricao = models.TextField('Descricao', max_length=500)
    lote = models.CharField('Lote', max_length=30)


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


    def __str__(self):
        return f"{self.tipo} {self.marca} {self.modelo}"

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

class Compra(models.Model):
    valor = models.DecimalField('Preco', max_digits=5, decimal_places=2)
    quantidade = models.IntegerField('Quantidade')

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"



