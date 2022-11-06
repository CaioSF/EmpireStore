# Generated by Django 2.2.19 on 2022-11-06 07:08

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_remove_produto_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='', variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Foto'),
        ),
    ]
