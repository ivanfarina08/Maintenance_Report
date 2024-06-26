# Generated by Django 5.0.6 on 2024-05-22 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_report_api', '0008_alter_maintenancereport_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenancereport',
            name='number_people',
        ),
        migrations.AlterField(
            model_name='executorreport',
            name='idExecutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='maintenance_report_api.executor'),
        ),
        migrations.AlterField(
            model_name='executorreport',
            name='idReport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance_report_api.maintenancereport'),
        ),
    ]
