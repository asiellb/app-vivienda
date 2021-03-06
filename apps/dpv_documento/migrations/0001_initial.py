# Generated by Django 2.2.2 on 2020-03-29 14:55

import apps.dpv_documento.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dpv_persona', '0006_auto_20200310_1917'),
        ('dpv_nomencladores', '0015_auto_20200211_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDPVDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Eliminado')),
                ('nombre', models.CharField(blank=True, default='', max_length=20, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de Documento',
                'verbose_name_plural': 'Tipos de Documentos',
                'ordering': ('nombre',),
                'unique_together': {('nombre', 'deleted_at')},
            },
        ),
        migrations.CreateModel(
            name='DPVDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Eliminado')),
                ('no_registro', models.CharField(blank=True, max_length=10, verbose_name='No. Registro')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')),
                ('no_refer', models.CharField(default='', max_length=20, verbose_name='No. Referencia')),
                ('asunto', models.CharField(blank=True, default='', max_length=400, verbose_name='Asunto')),
                ('fecha_entrega', models.DateTimeField(default=None, null=True, verbose_name='Fecha de Entrega al Destino')),
                ('fecha_termino', models.DateTimeField(default=None, null=True, verbose_name='Fecha de Termino')),
                ('dias', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Dias')),
                ('archivo_digital', models.FileField(blank=True, upload_to=apps.dpv_documento.models.scramble_upload_doc, verbose_name='Copia en Digital')),
                ('clasificacion', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dpv_documento.TipoDPVDocumento', verbose_name='Clasificacion')),
                ('destino', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dpv_nomencladores.AreaTrabajo', verbose_name='Destino')),
                ('municipio', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dpv_nomencladores.Municipio', verbose_name='Destino')),
                ('procedencia', models.ForeignKey(blank=True, help_text='De donde proviene el documento', on_delete=django.db.models.deletion.CASCADE, to='dpv_nomencladores.Procedencia', verbose_name='Procedencia')),
                ('promovente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dpv_persona.PersonaNatural', verbose_name='Promovente')),
                ('registrado_por', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Registrado por')),
            ],
            options={
                'verbose_name': 'Tipo de Documento',
                'verbose_name_plural': 'Tipos de Documentos',
                'ordering': ('-fecha_registro', 'no_registro'),
                'unique_together': {('no_registro', 'deleted_at')},
            },
        ),
    ]
