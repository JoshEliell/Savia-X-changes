# Generated by Django 4.1.1 on 2022-11-16 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_tipo_perfil_almacen_tipo_perfil_autorizacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_perfil',
            name='inicio_estadisticas',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
