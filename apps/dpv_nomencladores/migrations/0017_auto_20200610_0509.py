# Generated by Django 2.2.2 on 2020-06-10 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_nomencladores', '0016_anonimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consejopopular',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consejos', to='dpv_nomencladores.Municipio'),
        ),
    ]