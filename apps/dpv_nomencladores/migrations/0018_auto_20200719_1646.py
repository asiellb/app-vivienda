# Generated by Django 2.2.2 on 2020-07-19 16:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_nomencladores', '0017_auto_20200610_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clasificacionrespuesta',
            name='codigo',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[a-zA-ZñáéíóúÁÉÍÓÚÑ ]*[a-zA-ZñáéíóúÁÉÍÓÚÑ ]$', message='Este campo solo puede contener letras')], verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='conclusioncaso',
            name='codigo',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[a-zA-ZñáéíóúÁÉÍÓÚÑ ]*[a-zA-ZñáéíóúÁÉÍÓÚÑ ]$', message='Este campo solo puede contener letras')], verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='genero',
            name='nombre',
            field=models.CharField(max_length=11, validators=[django.core.validators.MaxLengthValidator(11), django.core.validators.RegexValidator('^[a-zA-ZñáéíóúÁÉÍÓÚÑ ]*[a-zA-ZñáéíóúÁÉÍÓÚÑ ]$', message='Este campo solo puede contener letras')], verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='genero',
            name='sigla',
            field=models.CharField(max_length=1, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(1), django.core.validators.RegexValidator('^[a-zA-ZñáéíóúÁÉÍÓÚÑ ]*[a-zA-ZñáéíóúÁÉÍÓÚÑ ]$', message='Este campo solo puede contener letras')], verbose_name='Inicial'),
        ),
        migrations.AlterField(
            model_name='tipoqueja',
            name='numero',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[a-zA-ZñáéíóúÁÉÍÓÚÑ ]*[a-zA-ZñáéíóúÁÉÍÓÚÑ ]$', message='Este campo solo puede contener letras')], verbose_name='Código'),
        ),
    ]
