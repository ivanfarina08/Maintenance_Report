from rest_framework import serializers
from maintenance_report_api.models import MaintenanceReport, Executor, ExecutorReport

class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'

class MaintenanceReportSerializer(serializers.ModelSerializer):
    executors = ExecutorSerializer(many=True, read_only=True)
    class Meta:
        model = MaintenanceReport
        fields = '__all__'

class ExecutorReportSerializer(serializers.ModelSerializer):
    idExecutor = ExecutorSerializer()
    idReport = MaintenanceReportSerializer()

    class Meta:
        model = ExecutorReport
        fields = '__all__'

class ExecutorReportCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutorReport
        fields = '__all__'
