# Generated by Django 2.2.19 on 2022-11-07 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0020_auto_20221107_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
