# Generated by Django 2.2.2 on 2021-01-17 18:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_nomencladores', '0033_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='redsocial',
            name='url',
            field=models.URLField(blank=True, default='', help_text='URL del url de la red social', max_length=254, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(254), django.core.validators.URLValidator], verbose_name='URL'),
        ),
    ]
