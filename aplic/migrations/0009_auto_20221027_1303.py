# Generated by Django 2.2.19 on 2022-10-27 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0008_auto_20221027_1255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compra_fornecedor',
            options={'verbose_name': 'Compra Fornecedor', 'verbose_name_plural': 'Compra Fornecedores'},
        ),
        migrations.RenameField(
            model_name='compra_fornecedor',
            old_name='xmnl',
            new_name='xml',
        ),
    ]