# Generated by Django 2.1 on 2019-04-10 22:34

import apps.email_sender.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfigurate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puerto', models.PositiveSmallIntegerField(blank=True, help_text='Puerto de conección al servidor.', null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Puerto')),
                ('servidor', models.CharField(blank=True, help_text='Servidor SMTP por donde se enviarán los correos.', max_length=255, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(255), apps.email_sender.validators.validate_ip46_fqdn_address], verbose_name='Servidor')),
                ('use_tls', models.BooleanField(default=False, help_text='Marque si el servidor usa seguridad TLS', verbose_name='Seguridad con TLS')),
                ('use_ssl', models.BooleanField(default=False, help_text='Marque si el servidor usa seguridad SSL', verbose_name='Seguridad con SSL')),
                ('usuario', models.CharField(blank=True, help_text='Usuario para autenticarse en el servidor', max_length=255, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(255)], verbose_name='Usuario')),
                ('password', models.CharField(blank=True, help_text='Contraseña del usuario para authenticarse en el servidor.', max_length=50, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(50)], verbose_name='Contraseña')),
            ],
            options={
                'verbose_name': 'COnfiguración de Correo',
                'verbose_name_plural': 'Configuraciones de Correo',
                'ordering': ['servidor'],
            },
        ),
    ]
