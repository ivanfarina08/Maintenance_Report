from django.contrib import admin
from maintenance_report_api.models import MaintenanceReport


class MaintenanceReports(admin.ModelAdmin):
    list_display = ('id','date', 'shift', 'line_machine', 'code', 'description', 'time_spend', 'status')
    list_display_links = ('id',)

admin.site.register(MaintenanceReport,MaintenanceReports)