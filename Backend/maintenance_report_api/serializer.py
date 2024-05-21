from rest_framework import serializers
from maintenance_report_api.models import MaintenanceReport

class MaintenanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceReport
        fields = '__all__'