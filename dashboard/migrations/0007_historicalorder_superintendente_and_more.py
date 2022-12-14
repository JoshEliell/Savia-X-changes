# Generated by Django 4.1.1 on 2022-10-27 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('dashboard', '0006_inventario_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorder',
            name='superintendente',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.profile'),
        ),
        migrations.AddField(
            model_name='historicalorder',
            name='supervisor',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.profile'),
        ),
        migrations.AddField(
            model_name='order',
            name='superintendente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intendente', to='user.profile'),
        ),
        migrations.AddField(
            model_name='order',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisor', to='user.profile'),
        ),
    ]
