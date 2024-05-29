from rest_framework import generics
from rest_framework import viewsets
from maintenance_report_api.models import MaintenanceReport, Executor, ExecutorReport, Line, Machine
from maintenance_report_api.serializer import MaintenanceReportSerializer, ExecutorSerializer, ExecutorReportSerializer, ExecutorReportCRUDSerializer, LineSerializer, MachineSerializer

class MaintenanceReportListAPIView(generics.ListAPIView):
    queryset = MaintenanceReport.objects.all()
    serializer_class = MaintenanceReportSerializer

class MaintenanceReportViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceReport.objects.all()
    serializer_class = MaintenanceReportSerializer

class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer

class ExecutorReportListAPIView(generics.ListAPIView):
    queryset = ExecutorReport.objects.all()
    serializer_class = ExecutorReportSerializer

class ExecutorReportViewSet(viewsets.ModelViewSet):
    queryset = ExecutorReport.objects.all()
    serializer_class = ExecutorReportCRUDSerializer

class LineViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LineSerializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
