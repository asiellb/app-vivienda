# Generated by Django 2.2.2 on 2020-01-27 16:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_nomencladores', '0009_auto_20200124_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConclusionCaso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Eliminado')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.RegexValidator('[a-zA-Z0-9 ]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Conclusión del Caso')),
                ('codigo', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*[a-zA-Z ]$', message='Este campo solo puede contener letras')], verbose_name='Código')),
            ],
            options={
                'verbose_name': 'Conclusión del Caso',
                'verbose_name_plural': 'Conclusiones del Casos',
                'ordering': ['nombre'],
                'unique_together': {('nombre', 'deleted_at'), ('codigo', 'deleted_at')},
            },
        ),
    ]
