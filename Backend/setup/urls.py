from django.contrib import admin
from django.urls import path,include
from maintenance_report_api.views import MaintenanceReportViewSet, ExecutorViewSet, ExecutorReportViewSet, MaintenanceReportListAPIView, ExecutorReportListAPIView, LineViewSet, MachineViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('api/executor', ExecutorViewSet,basename='ExecutorViewSets')
router.register('api/maintenancereport', MaintenanceReportViewSet,basename='MaintenanceReportViewSets')
router.register('api/executorreport', ExecutorReportViewSet,basename='ExecutorReportViewSets')
router.register('api/line', LineViewSet,basename='LineViewSets')
router.register('api/machine', MachineViewSet,basename='MachineViewSets')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/executorreports/', ExecutorReportListAPIView.as_view(), name='executor-report-list'),
    path('api/maintenancereports/', MaintenanceReportListAPIView.as_view(), name='maintenance-report-list'),
    path('', include(router.urls))
]
