from rest_framework import serializers
from maintenance_report_api.models import MaintenanceReport, Executor, ExecutorReport, Line, Machine
from maintenance_report_api.validators import *

class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'
    def validate(self, data):
        if not executor_name(data['name']):
            raise serializers.ValidationError({'Name': "The name must be more than 3 characters and less than 45 characters"})
        return data

class MaintenanceReportSerializer(serializers.ModelSerializer):
    line_name = serializers.CharField(source='line.name', read_only=True)
    machine_name = serializers.CharField(source='machine.name', read_only=True)
    executors = ExecutorSerializer(many=True, read_only=True)
    class Meta:
        model = MaintenanceReport
        fields = '__all__'
    def validate(self, data):
        if not report_title(data['title']):
            raise serializers.ValidationError({'Title': "The title must be more than 3 characters and less than 45 characters"})
        if not report_description(data['description']):
            raise serializers.ValidationError({'Description' : "The description must be less than 200 characters"})
        if not report_time_spend(data['time_spend']):
            raise serializers.ValidationError({'Time Spend': 'The time spend must be less than 2 characters'})
        return data

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
    def validate(self, data):
        if not line_name(data['name']):
            raise serializers.ValidationError({'Name': "The name must be more than 3 characters and less than 45 characters"})
        return data

class MachineSerializer(serializers.ModelSerializer):
    line_name = serializers.CharField(source='line.name', read_only=True)

    class Meta:
        model = Machine
        fields = ['id', 'name', 'activate', 'line', 'line_name']
    def validate(self, data):
        if not machine_name(data['name']):
            raise serializers.ValidationError({'Name': "The name must be more than 3 characters and less than 45 characters"})
        return data
    
