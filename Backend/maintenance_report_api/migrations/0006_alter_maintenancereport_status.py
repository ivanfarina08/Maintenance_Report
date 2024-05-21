# Generated by Django 5.0.6 on 2024-05-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_report_api', '0005_executor_executorreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancereport',
            name='status',
            field=models.CharField(choices=[('1', 'Created'), ('2', 'Assigned'), ('3', 'Completed')], default='1', max_length=1),
        ),
    ]