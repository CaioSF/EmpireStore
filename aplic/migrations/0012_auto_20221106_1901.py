# Generated by Django 2.2.19 on 2022-11-06 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0011_auto_20221106_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='produtos/'),
        ),
    ]
