from django.db import models

class Executor(models.Model):
    ACTIVATE = (
        ('1', 'activate'),
        ('2', 'inactive')
    )
    name = models.CharField(max_length=50)
    activated = models.CharField(max_length=1, choices=ACTIVATE, blank=False, null=False, default='1')

class MaintenanceReport(models.Model):
    STATUS = (
        ('1', 'Open'),
        ('2', 'Check'),
        ('3', 'Closed')
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
    line = models.CharField(max_length=100, default='auto_complete')
    machine = models.CharField(max_length=100, default='auto_complete')
    code = models.CharField(max_length=1, choices=CODE, blank=False, null=False, default='1')
    description = models.CharField(max_length=200)
    time_spend = models.CharField(max_length=2)
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='1')
    executors = models.ManyToManyField(Executor, through='ExecutorReport')

class ExecutorReport(models.Model):
    idExecutor = models.ForeignKey(Executor, on_delete=models.DO_NOTHING)
    idReport = models.ForeignKey(MaintenanceReport, on_delete=models.CASCADE)

class Line(models.Model):
    ACTIVATE = (
        ('1', 'activate'),
        ('2', 'inactive')
    )
    name = models.CharField(max_length=50)
    activate = models.CharField(max_length=1, choices=ACTIVATE, blank=False, null=False, default='1')

class Machine(models.Model):
    ACTIVATE = (
        ('1', 'activate'),
        ('2', 'inactive')
    )
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    activate = models.CharField(max_length=1, choices=ACTIVATE, blank=False, null=False, default='1')