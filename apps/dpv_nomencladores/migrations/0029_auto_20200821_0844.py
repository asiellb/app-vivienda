# Generated by Django 2.2.2 on 2020-08-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_nomencladores', '0028_auto_20200821_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='email',
            field=models.EmailField(blank=True, default='', help_text='Correo eletrónico de contacto de la organización', max_length=254, verbose_name='Correo Electrónico'),
        ),
    ]
