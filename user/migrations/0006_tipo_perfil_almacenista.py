# Generated by Django 4.1.1 on 2022-11-16 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_tipo_perfil_superintendente_tipo_perfil_supervisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_perfil',
            name='almacenista',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
