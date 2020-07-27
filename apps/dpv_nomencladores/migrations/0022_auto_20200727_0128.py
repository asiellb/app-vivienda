# Generated by Django 2.2.2 on 2020-07-27 01:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_nomencladores', '0021_auto_20200726_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='organismo',
            name='email',
            field=models.EmailField(blank=True, default='', help_text='Correo eletrónico de contacto del organismo', max_length=254, verbose_name='Correo Electrónico'),
        ),
        migrations.AddField(
            model_name='organismo',
            name='nombre_contacto',
            field=models.CharField(blank=True, default='', help_text='Nombre de la persona de contacto del organismo', max_length=200, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(200), django.core.validators.RegexValidator('^[a-zA-ZñáéíóúÁÉÍÓÚÑ ]*[a-zA-ZñáéíóúÁÉÍÓÚÑ ]$', message='Este campo solo puede contener letras')], verbose_name='Nombre de contacto'),
        ),
        migrations.AddField(
            model_name='organismo',
            name='telefono',
            field=models.CharField(blank=True, default='', help_text='Teléfono de contacto del organismo', max_length=8, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8), django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Teléfono'),
        ),
        migrations.AddField(
            model_name='prensaescrita',
            name='email',
            field=models.EmailField(blank=True, default='', help_text='Correo eletrónico de contacto de la prensa', max_length=254, verbose_name='Correo Electrónico'),
        ),
        migrations.AddField(
            model_name='prensaescrita',
            name='nombre_contacto',
            field=models.CharField(blank=True, default='', help_text='Nombre de la persona de contacto de la prensa', max_length=200, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(200), django.core.validators.RegexValidator('^[a-zA-ZñáéíóúÁÉÍÓÚÑ ]*[a-zA-ZñáéíóúÁÉÍÓÚÑ ]$', message='Este campo solo puede contener letras')], verbose_name='Nombre de contacto'),
        ),
        migrations.AddField(
            model_name='prensaescrita',
            name='telefono',
            field=models.CharField(blank=True, default='', help_text='Teléfono de contacto de la prensa', max_length=8, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8), django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='organismo',
            name='nombre',
            field=models.CharField(help_text='Nombre del organismo.', max_length=90, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9 ]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', "), django.core.validators.MaxLengthValidator(90)], verbose_name='Organismo'),
        ),
        migrations.AlterField(
            model_name='organismo',
            name='siglas',
            field=models.CharField(help_text='Siglas representativas del organismo', max_length=15, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9 ]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Siglas'),
        ),
        migrations.AlterUniqueTogether(
            name='organismo',
            unique_together={('telefono', 'deleted_at'), ('nombre', 'deleted_at'), ('email', 'deleted_at')},
        ),
    ]