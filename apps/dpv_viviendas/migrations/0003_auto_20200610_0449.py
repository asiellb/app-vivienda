# Generated by Django 2.2.2 on 2020-06-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_viviendas', '0002_auto_20200117_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='vivienda',
            name='cantidad_aclifim',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='Cantidad de impedidos físicos que conviven en la vivienda', verbose_name='Cantidad de Impedidos Físicos'),
        ),
        migrations.AddField(
            model_name='vivienda',
            name='cantidad_anciano',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='Cantidad de personas de la 3ra edad que conviven en la vivienda', verbose_name='Cantidad de Personas de 3ra Edad'),
        ),
        migrations.AddField(
            model_name='vivienda',
            name='cantidad_menores',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='Cantidad de menores de edad que conviven en la vivienda', verbose_name='Cantidad de Menores de Edad'),
        ),
        migrations.AddField(
            model_name='vivienda',
            name='cantidad_mujeres',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='Cantidad de mujeres que conviven en la vivienda', verbose_name='Cantidad de Mujeres'),
        ),
    ]