# Generated by Django 2.2.19 on 2022-10-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0005_auto_20221027_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
            ],
        ),
        migrations.CreateModel(
            name='Forma_pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Forma_pagamento', models.CharField(blank=True, choices=[('Boleto', 'Boleto'), ('Cartão de crédito', 'Cartão de crédito'), ('Cartão de débito', 'Cartão de débito'), ('pix', 'pix')], max_length=30, verbose_name='Forma_pagamento')),
            ],
        ),
    ]