# Generated by Django 3.2.5 on 2022-09-02 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, null=True)),
                ('abreviado', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('autorizar_sol', models.BooleanField(default=False, null=True)),
                ('autorizar_req', models.BooleanField(default=False, null=True)),
                ('ver_sol', models.BooleanField(default=False, null=True)),
                ('ver_req', models.BooleanField(default=False, null=True)),
                ('crear_sol', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(blank=True, upload_to='profile_images')),
                ('distrito', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.distrito')),
                ('staff', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.tipo_perfil')),
            ],
        ),
    ]