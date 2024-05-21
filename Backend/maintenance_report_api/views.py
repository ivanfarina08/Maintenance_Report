from rest_framework import viewsets
from maintenance_report_api.models import MaintenanceReport
from maintenance_report_api.serializer import MaintenanceReportSerializer

class MaintenanceReportViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = MaintenanceReport.objects.all()
    serializer_class = MaintenanceReportSerializer