from django.db import models
from django.utils.translation import gettext_lazy as _

    
class Machine(models.Model):
    """
    Machine model represents a manufacturing machine.

    Attributes:
    machine_name (str): Name of the machine.
    machine_serial_no (str): Serial number of the machine.
    time (datetime): Last updated time of the machine information.
    """

    machine_name = models.CharField(max_length=255, help_text="Name of the machine")
    machine_serial_no = models.CharField(max_length=255, help_text="Serial number of the machine")
    time = models.DateTimeField(auto_now=True, help_text="Last updated time")

    def __str__(self):
        return self.machine_name

    
class ProductionLog(models.Model):
    """
    ProductionLog model represents the log of production cycles for a machine.

    Attributes:
    cycle_no (str): Cycle number of the production log.
    unique_id (str): Unique identifier of the production log.
    material_name (str): Name of the material being processed.
    machine (Machine): ForeignKey relationship to Machine model.
    start_time (datetime): Start time of the production cycle.
    end_time (datetime): End time of the production cycle.
    duration (DurationField): Duration of the production cycle.
    """

    cycle_no = models.CharField(max_length=255, help_text="Cycle number of the production log")
    unique_id = models.CharField(max_length=255, help_text="Unique identifier of the production log")
    material_name = models.CharField(max_length=255, help_text="Name of the material being processed")
    machine = models.ForeignKey('Machine', on_delete=models.CASCADE, help_text="Machine associated with the production log")
    start_time = models.DateTimeField(help_text="Start time of the production cycle")
    end_time = models.DateTimeField(help_text="End time of the production cycle")
    duration = models.DurationField(blank=True, null=True, help_text="Duration of the production cycle")

    class Meta:
        verbose_name = _("Production Log")
        verbose_name_plural = _("Production Logs")

    def __str__(self):
        return self.cycle_no
