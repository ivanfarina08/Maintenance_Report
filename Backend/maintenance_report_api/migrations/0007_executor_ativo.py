# Generated by Django 5.0.6 on 2024-05-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_report_api', '0006_alter_maintenancereport_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='executor',
            name='ativo',
            field=models.CharField(choices=[('1', 'Ativo'), ('2', 'Inativo')], default='1', max_length=1),
        ),
    ]
