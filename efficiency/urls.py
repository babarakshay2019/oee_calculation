from django.urls import path
from rest_framework.routers import DefaultRouter

from efficiency.views import MachineViewSet, OEEView, ProductionLogViewSet

router = DefaultRouter()
router.register('machines', MachineViewSet)
router.register('production_logs', ProductionLogViewSet)

urlpatterns = [
    path('oee/', OEEView.as_view(), name='oee'),
] + router.urls
