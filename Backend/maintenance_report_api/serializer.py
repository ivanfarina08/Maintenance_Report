from rest_framework import serializers
from maintenance_report_api.models import MaintenanceReport, Executor, ExecutorReport

class MaintenanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceReport
        fields = '__all__'

class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'

class ExecutorReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutorReport
        fields = '__all__'