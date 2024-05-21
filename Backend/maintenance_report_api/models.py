from django.db import models

class MaintenanceReport(models.Model):
    STATUS = (
        ('1', 'Create'),
        ('2', 'Atribuída'),
        ('3', 'Executada'),
        ('4', 'Feedback'),
        ('5', 'Concluída')
    )
    SHIFT = (
        ('M','Morning Shift'),
        ('A','Afternoon Shift'),
        ('N','Night Shift')
    )
    CODE = (
        ('1', 'Code 1'),
        ('2', 'Code 2')
    )
    title = models.CharField(max_length=50, blank=False, null=False, default='teste')
    date = models.DateField()
    shift = models.CharField(max_length=1, choices=SHIFT, blank=False, null=False, default='M')
    line_machine = models.CharField(max_length=50)
    code = models.CharField(max_length=1, choices=CODE, blank=False, null=False, default='1')
    description = models.CharField(max_length=100)
    number_people = models.CharField(max_length=15)
    time_spend = models.CharField(max_length=2)
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='1')