# Generated by Django 2.2.19 on 2022-09-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_auto_20220926_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registo',
            name='senha',
            field=models.TextField(help_text='A senha deve conter letras maiusculas', max_length=16, verbose_name='Senha'),
        ),
    ]
