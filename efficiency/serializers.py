from rest_framework import serializers

from efficiency.models import Machine, ProductionLog


class MachineSerializer(serializers.ModelSerializer):
    """
    Serializer for Machine model.

    Serializes Machine instances into JSON format for API responses.

    Attributes:
    model (Model): Machine model class.
    fields (list): List of fields to include in serialization.
    read_only_fields (list): List of read-only fields that cannot be modified during object creation or update.
    """
    class Meta:
        model = Machine
        fields = ['id', 'machine_name', 'machine_serial_no', 'time']
        read_only_fields = ['time']


class ProductionLogSerializer(serializers.ModelSerializer):
    """
    Serializer for ProductionLog model.

    Serializes ProductionLog instances into JSON format for API responses.

    Attributes:
    model (Model): ProductionLog model class.
    fields (list): List of fields to include in serialization.
    read_only_fields (list): List of read-only fields that cannot be modified during object creation or update.
    """

    class Meta:
        model = ProductionLog
        fields = ['id', 'cycle_no', 'unique_id', 'material_name', 'machine', 'start_time', 'end_time', 'duration']
        read_only_fields = ['duration']

    def create(self, validated_data):
        """
        Create a new ProductionLog instance.

        Calculates the duration from start_time and end_time before creating the object.

        Args:
        validated_data (dict): Validated data from the serializer.

        Returns:
        ProductionLog: Newly created ProductionLog instance.
        """
        start_time = validated_data['start_time']
        end_time = validated_data['end_time']
        duration = end_time - start_time
        validated_data['duration'] = duration

        return super().create(validated_data)