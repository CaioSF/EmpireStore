# Generated by Django 2.2.19 on 2022-11-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0015_auto_20221107_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(),
        ),
    ]
