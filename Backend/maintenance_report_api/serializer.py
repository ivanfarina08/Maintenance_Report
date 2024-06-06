from rest_framework import serializers
from maintenance_report_api.models import MaintenanceReport, Executor, ExecutorReport, Line, Machine

class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'

class MaintenanceReportSerializer(serializers.ModelSerializer):
    line_name = serializers.CharField(source='line.name', read_only=True)
    machine_name = serializers.CharField(source='machine.name', read_only=True)
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

class LineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Line
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    line_name = serializers.CharField(source='line.name', read_only=True)

    class Meta:
        model = Machine
        fields = ['id', 'name', 'activate', 'line', 'line_name']
