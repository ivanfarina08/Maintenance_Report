from django.contrib import admin
from django.urls import path,include
from maintenance_report_api.views import MaintenanceReportViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('api/maintenancereport', MaintenanceReportViewSet,basename='MaintenanceReportViewSets')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
