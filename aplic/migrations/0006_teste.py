# Generated by Django 2.2.19 on 2022-09-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0005_auto_20220926_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
    ]
