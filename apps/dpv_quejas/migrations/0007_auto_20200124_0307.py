# Generated by Django 2.2 on 2020-01-24 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('dpv_nomencladores', '0008_auto_20200124_0307'),
        ('dpv_quejas', '0006_auto_20200119_0452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='damnificadonatural',
            name='damnificado_ptr',
        ),
        migrations.RemoveField(
            model_name='damnificadonatural',
            name='persona_natural',
        ),
        migrations.AddField(
            model_name='damnificado',
            name='id_objecto',
            field=models.PositiveIntegerField(null=True, verbose_name='related object'),
        ),
        migrations.AddField(
            model_name='damnificado',
            name='tipo_contenido',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(models.Q(('app_label', 'dpv_persona'), ('model', 'personanatural')), models.Q(('app_label', 'dpv_persona'), ('model', 'personajuridica')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Damnificado de la queja'),
        ),
        migrations.AddField(
            model_name='queja',
            name='codigo_numero',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='queja',
            name='fecha_termino',
            field=models.DateTimeField(default=None, null=True, verbose_name='Fecha Término'),
        ),
        migrations.AddField(
            model_name='queja',
            name='tipo',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='tipo_queja', to='dpv_nomencladores.TipoQueja', verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='queja',
            name='clasificacion',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='queja_respuesta_clase', to='dpv_nomencladores.ClasificacionRespuesta', verbose_name='Tipo de Queja'),
        ),
        migrations.DeleteModel(
            name='DamnificadoJuridico',
        ),
        migrations.DeleteModel(
            name='DamnificadoNatural',
        ),
    ]
