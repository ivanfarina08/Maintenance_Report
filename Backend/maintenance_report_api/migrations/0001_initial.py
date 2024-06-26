# Generated by Django 5.0.6 on 2024-05-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('sift', models.CharField(choices=[('M', 'Morning Shift'), ('A', 'Afternoon Shift'), ('N', 'Night Shift')], default='M', max_length=1)),
                ('line_machine', models.CharField(max_length=50)),
                ('code', models.CharField(choices=[('1', 'Code 1'), ('2', 'Code 2')], default='1', max_length=1)),
                ('description', models.CharField(max_length=100)),
                ('number_people', models.CharField(max_length=15)),
                ('time_spend', models.CharField(max_length=2)),
                ('status', models.CharField(choices=[('1', 'Create'), ('2', 'Atribuída'), ('3', 'Executada'), ('4', 'Feedback'), ('5', 'Concluída')], default='1', max_length=1)),
            ],
        ),
    ]
