# Generated by Django 2.2.19 on 2022-11-08 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0021_auto_20221107_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
