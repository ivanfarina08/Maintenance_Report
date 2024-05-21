from rest_framework import viewsets
from maintenance_report_api.models import MaintenanceReport, Executor, ExecutorReport
from maintenance_report_api.serializer import MaintenanceReportSerializer, ExecutorSerializer, ExecutorReportSerializer

class MaintenanceReportViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = MaintenanceReport.objects.all()
    serializer_class = MaintenanceReportSerializer

class ExecutorViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer

class ExecutorReportViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = ExecutorReport.objects.all()
    serializer_class = ExecutorReportSerializer