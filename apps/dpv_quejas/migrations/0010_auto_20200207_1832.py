# Generated by Django 2.2 on 2020-02-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_quejas', '0009_queja_responder_a'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queja',
            name='no_radicacion',
            field=models.CharField(blank=True, default='', max_length=7, verbose_name='No. Radicación Antiguo'),
        ),
    ]
