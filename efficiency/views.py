from datetime import datetime

from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from efficiency.models import Machine, ProductionLog
from efficiency.serializers import MachineSerializer, ProductionLogSerializer
from efficiency.utils import calculate_oee


class MachineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows machines to be viewed or edited.

    Provides CRUD (Create, Retrieve, Update, Delete) operations for machines.

    Attributes:
    queryset (QuerySet): Queryset containing all Machine instances.
    serializer_class (Serializer): Serializer class to serialize Machine instances.
    """
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class ProductionLogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows production logs to be viewed or edited.

    Provides CRUD (Create, Retrieve, Update, Delete) operations for production logs.

    Attributes:
    queryset (QuerySet): Queryset containing all ProductionLog instances.
    serializer_class (Serializer): Serializer class to serialize ProductionLog instances.
    """
    queryset = ProductionLog.objects.all()
    serializer_class = ProductionLogSerializer

    
class OEEView(generics.ListAPIView):
    """
    API endpoint to calculate Overall Equipment Effectiveness (OEE) for machines based on production logs.

    Query Parameters:
    - machine_id: Filter logs by machine ID (optional)
    - start_date: Filter logs by start date (optional, format: YYYY-MM-DD)
    - end_date: Filter logs by end date (optional, format: YYYY-MM-DD)

    Returns:
    - JSON response containing OEE metrics for each machine based on filtered production logs.
    """

    def get(self, request, *args, **kwargs):
        machine_id = request.query_params.get('machine_id')
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        logs = ProductionLog.objects.all()

        # Filter logs based on query parameters
        if machine_id:
            logs = logs.filter(machine_id=machine_id)

        try:
            # Apply date filters if provided
            if start_date_str:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
                logs = logs.filter(start_time__date__gte=start_date)

            if end_date_str:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
                logs = logs.filter(end_time__date__lte=end_date)

        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        oee_results = []

        # Calculate OEE metrics for each machine based on filtered logs
        for log in logs:  # Iterate over individual ProductionLog instances
            oee, availability, performance, quality = calculate_oee([log])  # Pass each log as a list

            oee_results.append({
                'machine_id': log.machine.id,
                'machine_name': log.machine.machine_name,
                'OEE': oee,
                'Availability': availability,
                'Performance': performance,
                'Quality': quality
            })

        return Response(oee_results)