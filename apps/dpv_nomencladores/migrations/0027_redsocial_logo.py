# Generated by Django 2.2.2 on 2020-07-27 06:05

import apps.dpv_nomencladores.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_nomencladores', '0026_auto_20200727_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='redsocial',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.dpv_nomencladores.models.scramble_upload_logo, verbose_name='Logo'),
        ),
    ]
