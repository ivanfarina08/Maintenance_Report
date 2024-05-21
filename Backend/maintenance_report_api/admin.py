from django.contrib import admin
from maintenance_report_api.models import MaintenanceReport, Executor, ExecutorReport


class MaintenanceReports(admin.ModelAdmin):
    list_display = ('id','date', 'shift', 'line_machine', 'code', 'description', 'time_spend', 'status')
    list_display_links = ('id',)

admin.site.register(MaintenanceReport,MaintenanceReports)

class Executors(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id',)

admin.site.register(Executor,Executors)

class ExecutorReports(admin.ModelAdmin):
    list_display = ('id','idExecutor', 'idReport')
    list_display_links = ('id',)

admin.site.register(ExecutorReport,ExecutorReports)